import ply.lex as lex
import ply.yacc as yacc
import sys
from collections import deque

# LEXER
# -----------------------------------------------------------------------------
import tokrules
from tokrules import *
lexer = lex.lex(module=tokrules)

triplos_queue = []
symbol_table = {}
procedure_table = {}
cont = 0
stack_saltos = deque()

# FOR
cont_var = 0            # Contador variables temporales
stack_id_for = deque()  # Almacena la variable de control del ciclo actual

# Variable Declaration Processing
queue_var = deque()
stack_type = deque()

def rellenar(dir, val):
    global triplos_queue
    if(triplos_queue[dir][0] == 'goto'):
        triplos_queue[dir][1] = val
    else:
        triplos_queue[dir][2] = val

def getTemp():
    global symbol_table
    global cont_var
    new_var = f"_{cont_var}"
    symbol_table[new_var] = ['INT', None]

    cont_var += 1
    return new_var

def p_programa(p):
    '''
    programa : programa_aux var procedure block END
    '''
    pass

def p_programa_aux(p):
    '''
    programa_aux : PROGRAM
    '''
    global triplos_queue
    global cont
    goto_inicial = ['goto', 1]
    triplos_queue.append(goto_inicial)
    cont += 1

def p_var(p):
    '''
    var : DIM repeated_identifier AS type repeated_size var
        | DIM repeated_identifier AS STRING_TYPE var
        | empty
    '''
    global queue_var
    global stack_type
    if(len(p) > 2):
        stack_type.append(p[4])

def p_repeated_size(p):
    '''
    repeated_size : SIZE repeated_size
                    | SIZE_ID repeated_size
                    | empty
    '''
    pass

def p_repeated_identifier(p):
    '''
    repeated_identifier : IDENTIFIER COMMA repeated_identifier
                        | IDENTIFIER
    '''
    global queue_var
    if len(p) == 2:
        queue_var.appendleft(p[1]+"$")
        p[0] = None
    else:
        if p[3] == None:
            queue_var.appendleft(p[1])
        else:
            queue_var.appendleft(p[3])
            queue_var.appendleft(p[1])
            p[0] = None

def p_var_type(p):
    '''
    type : INT_TYPE
            | FLOAT_TYPE
    '''
    p[0] = p[1]
    
def p_block(p):
    '''
    block : statement block
            | empty
    '''
    pass

def p_statement(p):
    '''
    statement : GOTO LABEL
        | LABEL_SALTO
    '''
    pass

# Traduccion FOR

def p_statement_for(p):
    '''
    statement : FOR aux1 TO aux2 block NEXT aux3
    '''
    pass

def p_for_aux1(p):
    '''
    aux1 : IDENTIFIER EQUALS expression
    '''
    global triplos_queue
    global cont
    global stack_id_for

    stack_id_for.appendleft(p[1])

    init = ['=', p[1], p[3]]
    triplos_queue.append(init)
    cont += 1

def p_for_aux2(p):
    '''
    aux2 : expression
    '''
    global triplos_queue
    global cont
    global stack_id_for
    global stack_saltos

    temp = getTemp()
    assign = ['=', temp, p[1]]
    triplos_queue.append(assign)
    cont += 1

    identifier =  stack_id_for.popleft()

    cond = ['<=', identifier, temp]
    gotof = ['gotofalso', cond, None]
    triplos_queue.append(gotof)
    cont += 1

    stack_saltos.appendleft(cont - 2)

def p_for_aux3(p):
    '''
    aux3 : IDENTIFIER
    '''
    global triplos_queue
    global cont
    global stack_saltos
    increment = ['=', p[1], ['+', p[1], 1]]
    triplos_queue.append(increment)
    cont += 1

    retorno = stack_saltos.popleft()
    salto = ['goto', retorno]
    triplos_queue.append(salto)
    cont += 1

    rellenar(retorno + 1, cont)

# Traduccion DO WHILE

def p_statement_do_while(p):
    '''
    statement : DO do_while_inicio block LOOP WHILE aux_do_while
    '''
    pass

def p_do_while_inicio(p):
    '''
    do_while_inicio : empty
    '''
    global stack_saltos
    global triplos_queue
    global cont

    stack_saltos.appendleft(cont)

def p_aux_do_while(p):
    '''
    aux_do_while : expression
    '''
    global stack_saltos
    global triplos_queue
    global cont

    inicio = stack_saltos.popleft()
    gotoverdadero = ['gotoverdadero', p[1], inicio]
    cont += 1

    triplos_queue.append(gotoverdadero)

# Traduccion WHILE

def p_statement_while(p):
    '''
    statement : WHILE aux_while DO block LOOP fin_while
    '''
    pass

def p_aux_while(p):
    '''
    aux_while : expression
    '''
    global stack_saltos
    global triplos_queue
    global cont

    stack_saltos.appendleft(cont)

    gotofalso = ['gotofalso', p[1], None]
    triplos_queue.append(gotofalso)
    cont += 1
    stack_saltos.appendleft(cont - 1)

def p_aux_fin_while(p):
    '''
    fin_while : empty
    '''
    global stack_saltos
    global triplos_queue
    global cont
    falso = stack_saltos.popleft()
    retorno = stack_saltos.popleft()

    goto = ['goto', retorno]
    triplos_queue.append(goto)
    cont += 1
    
    rellenar(falso, cont)

# Traduccion IF

def p_statement_if(p):
    '''
    statement : IF aux_if THEN block ELSE aux_else block END IF aux_fin
    '''
    pass

def p_aux_if(p):
    '''
    aux_if : expression
    '''
    global triplos_queue
    global cont
    gotofalso = ['gotofalso', p[1], None]
    triplos_queue.append(gotofalso)
    cont += 1
    stack_saltos.appendleft(cont - 1)

def p_aux_else(p):
    '''
    aux_else : empty
    '''
    global triplos_queue
    global stack_saltos
    global cont
    goto = ['goto', None]
    triplos_queue.append(goto)
    cont += 1

    falso = stack_saltos.popleft()
    rellenar(falso, cont - 1)

    stack_saltos.appendleft(cont - 1)

def p_aux_if_fin(p):
    '''
    aux_fin : empty
    '''
    global stack_saltos
    fin = stack_saltos.popleft()
    rellenar(fin, cont)

def p_statement_assignment(p):
    '''
    statement : LET IDENTIFIER repeated_size EQUALS expression
    '''
    global triplos_queue
    global cont
    if(p[3] == None):
        p[0] = ['=', p[2], p[5]]
        triplos_queue.append(p[0])
        cont += 1

# Traducción Subrutinas (Procedures)

def p_statement_procedure(p):
    '''
    statement : CALL LABEL
    '''
    global cont
    global triplos_queue

    call_statement = ['call', p[2]]
    triplos_queue.append(call_statement)
    cont += 1

def p_procedure(p):
    '''
    procedure : aux_label block aux_return procedure
                | empty
    '''
    pass

def p_procedure_label(p):
    '''
    aux_label : LABEL
    '''
    global procedure_table
    global cont
    procedure_table[p[1]] = cont

def p_procedure_return(p):
    '''
    aux_return : RETURN
    '''
    global triplos_queue
    global cont

    return_statement = ['return']
    triplos_queue.append(return_statement)
    cont += 1

    rellenar(0, cont)

# Traducción PRINT, INPUT

def p_statement_input(p):
    '''
    statement : INPUT repeated_print
    '''
    global cont
    global triplos_queue

    input_statement = ['input', p[2]]
    cont += 1
    triplos_queue.append(input_statement)

def p_statement_print(p):
    '''
    statement : PRINT repeated_print
    '''
    global cont
    global triplos_queue

    print_statement = ['print', p[2]]
    cont += 1

    triplos_queue.append(print_statement)

def p_repeated_print(p):
    '''
    repeated_print : repeated_elem COMMA repeated_print
                    | repeated_elem
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1], p[3]]

def p_repeated_elem(p):
    '''
    repeated_elem : STRING
                    | elem
    '''
    p[0] = p[1]

# Traducción de Expresiones Aritmeticológicas

def p_expression(p):
    '''
    expression : expression_s op_rel expression_s
                | expression_s
    '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = [p[2], p[1], p[3]]

def p_expression_s(p):
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

def p_term(p):
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

def p_factor(p):
    '''
    factor : elem
            | OPENPAR expression CLOSEPAR
    '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_elem(p):
    '''
    elem : INT
        | IDENTIFIER repeated_size
        | elem_else
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(p[2] == None):
        p[0] = p[1]

def p_elem_float(p):
    '''
    elem_else : FLOAT
    '''
    p[0] = p[1]

def p_op_rel(p):
    '''
    op_rel : LESSTHANOREQUAL
            | GREATERTHANOREQUAL
            | ISEQUALTO
            | GREATERTHAN
            | LESSTHAN

    '''
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error found: {p}")
    pass

def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None