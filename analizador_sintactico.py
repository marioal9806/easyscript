'''
Language : ScriptGO
Author : Mario Alberto Ortega
Student ID : A01730557
'''
import ply.lex as lex
import ply.yacc as yacc
import sys

import parserules
from parserules import *

# PARSER
# -------------------------------------------------------------------------
parser = yacc.yacc(module=parserules)

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
