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
    print(p)

def p_var(p):
    '''
    var : DIM repeated_identifier AS type repeated_size var
        | DIM repeated_identifier AS STRING_TYPE var
        | 
    '''
    print(p)

def p_repeated_size(p):
    '''
    repeated_size : SIZE repeated_size
                    | SIZE_ID repeated_size
                    | 
    '''
    print(p)

def p_repeated_identifier(p):
    '''
    repeated_identifier : IDENTIFIER COMMA repeated_identifier
                        | IDENTIFIER
    '''
    print(p)

def p_var_type(p):
    '''
    type : INT_TYPE
            | FLOAT_TYPE
    '''
    print(p)
    
def p_block(p):
    '''
    block : statement block
            | 
    '''
    print(p)

def p_statement(p):
    '''
    statement : INPUT repeated_print
        | PRINT repeated_print
        | FOR IDENTIFIER EQUALS INT TO INT block NEXT IDENTIFIER
        | WHILE expression block LOOP
        | DO block LOOP WHILE expression
        | LET IDENTIFIER repeated_size EQUALS expression
        | IF expression THEN block ELSE block END IF
        | GOSUB LABEL
        | GOTO LABEL
        | LABEL_SALTO
    '''
    print(p)

def p_procedure(p):
    '''
    procedure : LABEL block RETURN procedure
                | 
    '''
    print(p)

def p_repeated_print(p):
    '''
    repeated_print : repeated_elem COMMA repeated_print
                    | repeated_elem
    '''
    print(p)

def p_repeated_elem(p):
    '''
    repeated_elem : STRING
                    | elem
    '''
    print(p)

def p_expression(p):
    '''
    expression : expression_s op_rel expression_s
                | expression_s
    '''
    print(p)

def p_expression_s(p):
    '''
    expression_s : expression_t 
                | expression_t PLUS expression_s
                | expression_t MINUS expression_s
                | expression_t OR expression_s
    '''
    print(p)

def p_expression_t(p):
    '''
    expression_t : expression_f
                | expression_f MULTIPLY expression_t
                | expression_f DIVIDE expression_t
                | expression_f AND expression_t
    '''
    print(p)

def p_expression_f(p):
    '''
    expression_f : elem
                | OPENPAR expression CLOSEPAR
    '''
    print(p)

def p_elem_num(p):
    '''
    elem : INT
        | FLOAT
        | IDENTIFIER repeated_size
        | IDENTIFIER 
    '''
    print(p)

def p_op_rel(p):
    '''
    op_rel : LESSTHAN
            | GREATERTHAN
            | ISEQUALTO
    '''
    print(p)

def p_error(p):
    print("Syntax error found!")
    print(p)

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