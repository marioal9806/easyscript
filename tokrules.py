# module: tokrules.py
# This module just contains the lexing rules
import ply.lex as lex

class MyLexer(object):

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
        'CALL' : 'CALL',
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
        'CLOSEPAR',
        'LBRACKET',
        'RBRACKET'
    ] + list(reserved.values())

    t_ISEQUALTO = r'\=\='
    t_EQUALS = r'\='
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_MULTIPLY = r'\*'
    t_DIVIDE = r'\/'
    t_OPENPAR = r'\('
    t_CLOSEPAR = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LESSTHANOREQUAL = r'\<\='
    t_GREATERTHANOREQUAL = r'\>\='
    t_LESSTHAN = r'\<'
    t_GREATERTHAN = r'\>'
    t_ignore = r' \t'
    t_COMMA = r','

    def t_LABEL(self, t):
        r'\#[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = 'LABEL'
        return t

    def t_LABEL_SALTO(self, t):
        r'\#\#[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = 'LABEL_SALTO'
        return t

    def t_FLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r'\"[a-zA-Z 0-9:!@#$%^&*()-+=/?<>,\\]+\"'
        t.value = str(t.value)
        return t

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'IDENTIFIER')
        return t

    def t_error(self, t):
        print(f"Illegal character {t.value[0]} at line {t.lineno}")
        t.lexer.skip(1)

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_COMMENT(self, t):
        r'//.*'
        pass
        # No return value. Token discarded

    def __init__(self):
        self.lexer = lex.lex(module=self)