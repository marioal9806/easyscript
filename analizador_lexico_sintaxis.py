import ply.lex as lex
import ply.yacc as yacc
import sys

reserved = {
    'PROGRAM' : 'PROGRAM',
    'DIM' : 'DIM',
    'AS' : 'AS',
    'INPUT' : 'INPUT',
    'PRINT' : 'PRINT',
    'END' : 'END',
    'LET' : 'LET',
    'IF' : 'IF',
    'THEN' : 'THEN',
    'ELSE' : 'ELSE',
    'WHILE' : 'WHILE',
    'LOOP' : 'LOOP',
    'DO' : 'DO',
    'FOR' : 'FOR',
    'NEXT' : 'NEXT',
    'GOTO' : 'GOTO',
    'GOSUB' : 'GOSUB',
    'RETURN' : 'RETURN',
    'TO' : 'TO',
    'INT' : 'INT_TYPE',
    'FLOAT' : 'FLOAT_TYPE',
    'STRING' : 'STRING_TYPE',
    'OR' : 'OR',
    'AND' : 'AND'
}

tokens = [
    'LABEL',
    'LABEL_SALTO',
    'COMMA',

    'INT',
    'FLOAT',
    'STRING',
    'SIZE',
    'SIZE_ID',
    
    'IDENTIFIER',

    'EQUALS',
    'ISEQUALTO',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LESSTHAN',
    'GREATERTHAN',

    'OPENPAR',
    'CLOSEPAR'
] + list(reserved.values())

t_ISEQUALTO = r'\=\='
t_EQUALS = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_ignore = r' \t'
t_COMMA = r','

def t_LABEL(t):
    r'\#[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'LABEL'
    return t

def t_LABEL_SALTO(t):
    r'\#\#[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'LABEL_SALTO'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d'
    t.value = float(t.value)
    return t

def t_SIZE(t):
    r'\[\d+\]'
    t.value = int(t.value.lstrip('\[').rstrip('\]'))
    return t

def t_SIZE_ID(t):
    r'\[[a-zA-Z_][a-zA-Z0-9_]*\]'
    t.type = 'SIZE_ID'
    return t

def t_STRING(t):
    r'["][a-zA-Z 0-9:!@#$%^&*()-+=/?<>,]+["]'
    t.value = str(t.value.lstrip("\"").rstrip("\""))
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_error(t):
    print(f"Illegal character {t.value[0]} at line {t.lineno}")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

lexer = lex.lex()
# LEXER
# -----------------------------------------------------------------------------

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