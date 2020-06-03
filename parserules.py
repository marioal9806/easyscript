import ply.lex as lex
import ply.yacc as yacc
import sys
import copy
from collections import deque

# LEXER
# -----------------------------------------------------------------------------
from tokrules import MyLexer


class MyParser(object):
    tokens = MyLexer.tokens
    reserved = MyLexer.reserved

    triplos_queue = []
    symbol_table = {}
    procedure_table = {}
    cont = 0
    stack_saltos = deque()

    # FOR
    cont_var = 0            # self.contador variables temporales
    stack_id = deque()  # Almacena la variable de self.control del ciclo actual

    # Variable Declaration Processing
    queue_var = deque()
    stack_type = deque()

    # Dimensioned variable declaration process
    M = 1
    i = 0
    description_list = [[None,0],] 
        # [0] -> size, M 
        # [1:] -> dim, m
    base = 0
    array_table = {}

    # Array Variable Access Parsing
    dim_list = deque()
    is_array = False

    def rellenar(self, dir, val):
        if(self.triplos_queue[dir][0] == 'goto'):
            self.triplos_queue[dir][1] = val
        else:
            self.triplos_queue[dir][2] = val

    def getTemp(self):
        new_var = f"_{self.cont_var}"
        self.symbol_table[new_var] = ['INT', None]

        self.cont_var += 1
        return new_var

    def p_programa(self, p):
        '''
        programa : programa_aux var procedure block END
        '''
        pass

    def p_programa_aux(self, p):
        '''
        programa_aux : PROGRAM
        '''
        goto_inicial = ['goto', 1]
        self.triplos_queue.append(goto_inicial)
        self.cont += 1

    def p_var(self, p):
        '''
        var : DIM repeated_identifier AS type repeated_size aux_size var
            | DIM repeated_identifier AS STRING_TYPE var
            | empty
        '''
        if(len(p) > 2):
            self.stack_type.append(p[4])

    def p_repeated_size(self, p):
        '''
        repeated_size : LBRACKET INT RBRACKET repeated_size
                        | empty
        '''
        if(len(p) != 2):
            self.description_list.insert(1, [p[2], None])
            self.M = self.M * p[2]
            self.i += 1

    def p_aux_size(self, p):
        '''
        aux_size : empty
        '''
        if len(self.description_list) > 1:
            self.description_list[0][0] = self.i
            self.description_list[0][1] = self.M
            j = 1
            while(j < len(self.description_list) - 1):
                self.description_list[j][1] = self.description_list[j - 1][1] // self.description_list[j][0]
                j += 1
            self.description_list[j][1] = copy.deepcopy(self.base)
            # self.base += self.M

            self.M = 1
            self.i = 0

            aux_var_list = []
            curr_var = self.queue_var.popleft()
            if(curr_var[-1] == '$'):
                aux_var_list.append(curr_var.rstrip('$'))
            else:
                aux_var_list.append(curr_var)
                while(len(self.queue_var) != 0):
                    next_var = self.queue_var.popleft()
                    if(next_var[-1] == '$'):
                        aux_var_list.append(next_var.rstrip('$'))
                        break
                    else:
                        aux_var_list.append(next_var)

            for idx in range(0, len(aux_var_list)):
                size = self.description_list[0][1]
                copy_description_list = copy.deepcopy(self.description_list)
                self.array_table[aux_var_list[idx]] = copy_description_list
                self.base += size
                self.description_list[-1][1] += size

            aux_var_list[0] = aux_var_list[0] + '$'
            for var in aux_var_list:
                self.queue_var.appendleft(var)

            self.description_list = [[None,0],]

    def p_repeated_identifier(self, p):
        '''
        repeated_identifier : IDENTIFIER COMMA repeated_identifier
                            | IDENTIFIER
        '''
        if len(p) == 2:
            self.queue_var.appendleft(p[1]+"$")
            p[0] = None
        else:
            if p[3] == None:
                self.queue_var.appendleft(p[1])
            else:
                self.queue_var.appendleft(p[3])
                self.queue_var.appendleft(p[1])
                p[0] = None

    def p_var_type(self, p):
        '''
        type : INT_TYPE
                | FLOAT_TYPE
        '''
        p[0] = p[1]
        
    def p_block(self, p):
        '''
        block : statement block
                | empty
        '''
        pass

    def p_statement(self, p):
        '''
        statement : GOTO LABEL
            | LABEL_SALTO
        '''
        pass

    # Traduccion FOR

    def p_statement_for(self, p):
        '''
        statement : FOR aux1 TO aux2 block NEXT aux3
        '''
        pass

    def p_for_aux1(self, p):
        '''
        aux1 : IDENTIFIER EQUALS expression
        '''
        self.stack_id.appendleft(p[1])

        init = ['=', p[1], p[3]]
        self.triplos_queue.append(init)
        self.cont += 1

    def p_for_aux2(self, p):
        '''
        aux2 : expression
        '''
        temp = getTemp()
        assign = ['=', temp, p[1]]
        self.triplos_queue.append(assign)
        self.cont += 1

        identifier =  self.stack_id.popleft()

        cond = ['<=', identifier, temp]
        gotof = ['gotofalso', cond, None]
        self.triplos_queue.append(gotof)
        self.cont += 1

        self.stack_saltos.appendleft(self.cont - 2)

    def p_for_aux3(self, p):
        '''
        aux3 : IDENTIFIER
        '''
        increment = ['=', p[1], ['+', p[1], 1]]
        self.triplos_queue.append(increment)
        self.cont += 1

        retorno = self.stack_saltos.popleft()
        salto = ['goto', retorno]
        self.triplos_queue.append(salto)
        self.cont += 1

        self.rellenar(retorno + 1, self.cont)

    # Traduccion DO WHILE

    def p_statement_do_while(self, p):
        '''
        statement : DO do_while_inicio block LOOP WHILE aux_do_while
        '''
        pass

    def p_do_while_inicio(self, p):
        '''
        do_while_inicio : empty
        '''
        self.stack_saltos.appendleft(self.cont)

    def p_aux_do_while(self, p):
        '''
        aux_do_while : expression
        '''
        inicio = self.stack_saltos.popleft()
        gotoverdadero = ['gotoverdadero', p[1], inicio]
        self.cont += 1

        self.triplos_queue.append(gotoverdadero)

    # Traduccion WHILE

    def p_statement_while(self, p):
        '''
        statement : WHILE aux_while DO block LOOP fin_while
        '''
        pass

    def p_aux_while(self, p):
        '''
        aux_while : expression
        '''
        self.stack_saltos.appendleft(self.cont)

        gotofalso = ['gotofalso', p[1], None]
        self.triplos_queue.append(gotofalso)
        self.cont += 1
        self.stack_saltos.appendleft(self.cont - 1)

    def p_aux_fin_while(self, p):
        '''
        fin_while : empty
        '''
        falso = self.stack_saltos.popleft()
        retorno = self.stack_saltos.popleft()

        goto = ['goto', retorno]
        self.triplos_queue.append(goto)
        self.cont += 1
        
        self.rellenar(falso, self.cont)

    # Traduccion IF

    def p_statement_if(self, p):
        '''
        statement : IF aux_if THEN block ELSE aux_else block END IF aux_fin
        '''
        pass

    def p_aux_if(self, p):
        '''
        aux_if : expression
        '''
        gotofalso = ['gotofalso', p[1], None]
        self.triplos_queue.append(gotofalso)
        self.cont += 1
        self.stack_saltos.appendleft(self.cont - 1)

    def p_aux_else(self, p):
        '''
        aux_else : empty
        '''
        goto = ['goto', None]
        self.triplos_queue.append(goto)
        self.cont += 1

        falso = self.stack_saltos.popleft()
        self.rellenar(falso, self.cont)

        self.stack_saltos.appendleft(self.cont - 1)

    def p_aux_if_fin(self, p):
        '''
        aux_fin : empty
        '''
        fin = self.stack_saltos.popleft()
        self.rellenar(fin, self.cont)

    def p_statement_assignment(self, p):
        '''
        statement : LET aux_array EQUALS expression
        '''
        p[0] = ['=', p[2], p[4]]
        self.triplos_queue.append(p[0])
        self.cont += 1

    # Traducción Subrutinas (Procedures)

    def p_statement_procedure(self, p):
        '''
        statement : CALL LABEL
        '''
        call_statement = ['call', p[2]]
        self.triplos_queue.append(call_statement)
        self.cont += 1

    def p_procedure(self, p):
        '''
        procedure : aux_label block aux_return procedure
                    | empty
        '''
        pass

    def p_procedure_label(self, p):
        '''
        aux_label : LABEL
        '''
        self.procedure_table[p[1]] = self.cont

    def p_procedure_return(self, p):
        '''
        aux_return : RETURN
        '''
        return_statement = ['return']
        self.triplos_queue.append(return_statement)
        self.cont += 1

        self.rellenar(0, self.cont)

    # Traducción PRINT, INPUT

    def p_statement_input(self, p):
        '''
        statement : INPUT repeated_print
        '''
        input_statement = ['input', p[2]]
        self.cont += 1
        self.triplos_queue.append(input_statement)

    def p_statement_print(self, p):
        '''
        statement : PRINT repeated_print
        '''
        print_statement = ['print', p[2]]
        self.cont += 1

        self.triplos_queue.append(print_statement)

    def p_repeated_print(self, p):
        '''
        repeated_print : repeated_elem COMMA repeated_print
                        | repeated_elem
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1], p[3]]

    def p_repeated_elem(self, p):
        '''
        repeated_elem : STRING
                        | elem
        '''
        p[0] = p[1]

    # Traducción de Expresiones Aritmeticológicas

    def p_expression(self, p):
        '''
        expression : expression_s op_rel expression_s
                    | expression_s
        '''
        if(len(p) == 2):
            p[0] = p[1]
        else:
            p[0] = [p[2], p[1], p[3]]

    def p_expression_s(self, p):
        '''
        expression_s : term 
                    | term PLUS expression_s
                    | term MINUS expression_s
                    | term OR expression_s
        '''
        if(len(p) == 2):
            p[0] = p[1]
        else:
            p[0] = [p[2], p[1], p[3]]

    def p_term(self, p):
        '''
        term : factor
            | factor MULTIPLY term
            | factor DIVIDE term
            | factor AND term
        '''
        if(len(p) == 2):
            p[0] = p[1]
        else:
            p[0] = [p[2], p[1], p[3]]

    def p_factor(self, p):
        '''
        factor : elem
                | OPENPAR expression CLOSEPAR
        '''
        if(len(p) == 2):
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_elem(self, p):
        '''
        elem : INT
            | aux_array
            | elem_else
        '''
        p[0] = p[1]

    def p_aux_array(self, p):
        '''
        aux_array : size_identifier repeated_size_access end_array
        '''
        if p[3] == None:
            p[0] = p[1]
        else:
            p[0] = p[3]

    def p_size_identifier(self, p):
        '''
        size_identifier : IDENTIFIER
        '''
        self.stack_id.append(p[1])
        p[0] = p[1]

    def p_repeated_size_access(self, p):
        '''
        repeated_size_access : LBRACKET expression RBRACKET repeated_size_access
                        | empty
        '''
        if(len(p) > 2):
            self.is_array = True
            self.dim_list.appendleft(p[2])
        else:
            p[0] = None

    def p_end_array(self, p):
        '''
        end_array : empty
        '''
        if self.is_array:
            array_id = self.stack_id.pop()
            try:
                # Verificar que exista dicho array
                if array_id not in self.array_table:
                    raise Exception(array_id)
                else:
                    idx = 0
                    k = 1
                    size = self.array_table[array_id][0][0]
                    
                    # Verificar que el num de dimensiones coincida
                    try:
                        if size != len(self.dim_list):
                            raise Exception(size)
                    
                        while(k <= size):
                            current_dim = self.dim_list[k-1]
                            
                            # Verificar si dk está dentro de las dimensiones permitidas
                            verifica = ['verify', array_id, current_dim, k]
                            self.triplos_queue.append(verifica)
                            self.cont += 1

                            if k == size:
                                break

                            else:
                                m = self.array_table[array_id][k][1]
                                idx += current_dim*m
                                k = k + 1
                        
                        
                        idx += self.dim_list[k - 1] + self.array_table[array_id][k][1]

                        self.is_array = False
                        self.dim_list.clear()
                        p[0] = (idx,)
                    except Exception as err:
                        print(f"ERROR: Vector {array_id} expected {size} dimensions")
                        quit()

            except Exception as err:
                print(f"ERROR: Undeclared Dimensioned Variable \'{err.args}\'")
                quit()

    def p_elem_float(self, p):
        '''
        elem_else : FLOAT
        '''
        p[0] = p[1]

    def p_op_rel(self, p):
        '''
        op_rel : LESSTHANOREQUAL
                | GREATERTHANOREQUAL
                | ISEQUALTO
                | GREATERTHAN
                | LESSTHAN
        '''
        p[0] = p[1]

    def p_error(self, p):
        print(f"Syntax error found: {p}")
        quit()

    def p_empty(self, p):
        '''
        empty : 
        '''
        p[0] = None

    def __init__(self):
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self)