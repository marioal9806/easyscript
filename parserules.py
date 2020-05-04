import ply.lex as lex
import ply.yacc as yacc
import sys
from collections import deque

# LEXER
# -----------------------------------------------------------------------------
import tokrules
from tokrules import *
lexer = lex.lex(module=tokrules)

symbol_table = {}
triplos_queue = []

queue_var = deque()
stack_type = deque()

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