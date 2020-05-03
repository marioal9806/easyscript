'''
Language : ScriptGO
Author : Mario Alberto Ortega
Student ID : A01730557
'''
import ply.lex as lex
import ply.yacc as yacc
import sys

# LEXER
# -----------------------------------------------------------------------------
import tokrules
from tokrules import *
lexer = lex.lex(module=tokrules)

def p_programa(p):
    '''
    programa : PROGRAM var procedure block END
    '''
    pass

def p_var(p):
    '''
    var : DIM repeated_identifier AS type repeated_size var
        | DIM repeated_identifier AS STRING_TYPE var
        | empty
    '''
    global aux_dim
    if(len(p) != 2):
        for variable in aux_dim:
            symbol_table[variable] = [p[4],None]

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
    global aux_dim
    aux_dim.append(p[1])

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
    statement : INPUT repeated_print
        | PRINT repeated_print
        | FOR IDENTIFIER EQUALS INT TO INT block NEXT IDENTIFIER
        | WHILE expression block LOOP
        | DO block LOOP WHILE expression
        | IF expression THEN block ELSE block END IF
        | GOSUB LABEL
        | GOTO LABEL
        | LABEL_SALTO
    '''
    pass

def p_statement_assignment(p):
    '''
    statement : LET IDENTIFIER repeated_size EQUALS expression
    '''
    global triplos_queue
    if(p[3] == None):
        p[0] = ['=', p[2], p[5]]
        triplos_queue.append(p[0])
        print(p[0])

def p_procedure(p):
    '''
    procedure : LABEL block RETURN procedure
                | empty
    '''
    pass

def p_repeated_print(p):
    '''
    repeated_print : repeated_elem COMMA repeated_print
                    | repeated_elem
    '''
    pass

def p_repeated_elem(p):
    '''
    repeated_elem : STRING
                    | elem
    '''
    pass

def p_expression(p):
    '''
    expression : expression_s op_rel expression_s
                | expression_s
    '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = [p[2], p[1], p[3]]
        print(p[0])

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
        print(p[0])

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
        print(p[0])

def p_factor(p):
    '''
    factor : elem
            | OPENPAR expression CLOSEPAR
    '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_elem_num(p):
    '''
    elem : INT
        | FLOAT
        | IDENTIFIER repeated_size
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(p[2] == None):
        p[0] = p[1]

def p_op_rel(p):
    '''
    op_rel : LESSTHAN
            | GREATERTHAN
            | ISEQUALTO
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error found!")
    pass

def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None

# PARSER
# -------------------------------------------------------------------------
parser = yacc.yacc()

symbol_table = {}
aux_dim = []
triplos_queue = []

def run(p):
    global triplos_queue
    global symbol_table
    if type(p) == list:

        if(p[0] == '='):
            try:
                symbol_table[p[1]][1] = run(p[2])
            except:
                print(f"ERROR: UNDECLARED VARIABLE \"{p[1]}\"")
                quit()
        if(type(p[1]) == str):
            p[1] = symbol_table[p[1]][1]
        if(type(p[2]) == str):
            p[2] = symbol_table[p[2]][1]
            

        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '>':
            if run(p[1]) > run(p[2]):
                return 1
            else:
                return 0
        elif p[0] == '<':
            if run(p[1]) < run(p[2]):
                return 1
            else:
                return 0
        elif p[0] == '==':
            if run(p[1]) == run(p[2]):
                return 1
            else:
                return 0
    else:
        return p

try:
    # s = input('>> ')
    with open('ejemplo_expresiones.txt','r', encoding='utf8') as file:
        s = file.read()
except EOFError:
    quit()
parser.parse(s)

print('\nTabla de Simbolos:')
print(symbol_table, end='\n\n')

print('Triplos queue:')
print(triplos_queue, end='\n\n')

for instruction in triplos_queue:
    run(instruction)

print('Tabla de Simbolos:')
print(symbol_table, end='\n\n')
