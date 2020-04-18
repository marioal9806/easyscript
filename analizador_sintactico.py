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
        | 
    '''
    pass

def p_repeated_size(p):
    '''
    repeated_size : SIZE repeated_size
                    | SIZE_ID repeated_size
                    | 
    '''
    pass

def p_repeated_identifier(p):
    '''
    repeated_identifier : IDENTIFIER COMMA repeated_identifier
                        | IDENTIFIER
    '''
    global env
    env[p[1]] = None

def p_var_type(p):
    '''
    type : INT_TYPE
            | FLOAT_TYPE
    '''
    pass
    
def p_block(p):
    '''
    block : statement block
            | 
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
    pass

def p_procedure(p):
    '''
    procedure : LABEL block RETURN procedure
                | 
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
    pass

def p_expression_s(p):
    '''
    expression_s : term 
                | term PLUS expression_s
                | term MINUS expression_s
                | term OR expression_s
    '''
    pass

def p_term(p):
    '''
    term : factor
                | factor MULTIPLY term
                | factor DIVIDE term
                | factor AND term
    '''
    pass

def p_factor(p):
    '''
    factor : elem
            | OPENPAR expression CLOSEPAR
    '''
    pass

def p_elem_num(p):
    '''
    elem : INT
        | FLOAT
        | IDENTIFIER repeated_size
    '''
    pass

def p_op_rel(p):
    '''
    op_rel : LESSTHAN
            | GREATERTHAN
            | ISEQUALTO
    '''
    pass

def p_error(p):
    print("Syntax error found!")
    pass

# PARSER
# -------------------------------------------------------------------------
parser = yacc.yacc()
env = {}

try:
    # s = input('>> ')
    with open('programa_ejemplo.txt','r', encoding='utf8') as file:
        s = file.read()
except EOFError:
    quit()
parser.parse(s)
print(env)