# module: tokrules.py
# This module just contains the lexing rules
import ply.lex as lex

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
    'LESSTHANOREQUAL',
    'GREATERTHANOREQUAL',

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
t_LESSTHANOREQUAL = r'\<\='
t_GREATERTHANOREQUAL = r'\>\='
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

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SIZE(t):
    r'\[\d+\]'
    t.value = int(t.value.lstrip('\[').rstrip('\]'))
    return t

def t_SIZE_ID(t):
    r'\[[a-zA-Z_][a-zA-Z0-9_]*\]'
    t.type = 'SIZE_ID'
    t.value = t.value.lstrip('\[').rstrip('\]')
    return t

def t_STRING(t):
    r'\"[a-zA-Z 0-9:!@#$%^&*()-+=/?<>,\\]+\"'
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

def t_COMMENT(t):
    r'//.*'
    pass
    # No return value. Token discarded