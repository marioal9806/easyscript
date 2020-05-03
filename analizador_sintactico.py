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

type_rules = {

    'INT':{
        'INT':{'+':'INT', '-':'INT', '*': 'INT', '/':'INT', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'FLOAT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'STRING':{'+':'X', '-':'X', '*': 'X', '/':'X', '>':'X', '<':'X', '==':'X'}
        },

    'FLOAT':{
        'INT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'FLOAT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'STRING':{'+':'X', '-':'X', '*': 'X', '/':'X', '>':'X', '<':'X', '==':'X'}
        },
    
    'STRING':{
        'INT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'FLOAT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'STRING':{'+':'X', '-':'X', '*': 'X', '/':'X', '>':'X', '<':'X', '==':'BOOL'}
    }
}

def getType(type1, type2, type3):
    op_type = type_rules[type1][type2][type3]
    if op_type == 'X':
        print(f"TYPE ERROR: CANNOT PERFORM {type2} {type1} {type3} OPERATION")
        quit()
    else:
        return op_type

def formatResult(result, op_type):
    if op_type == 'INT':
        return int(result)
    elif op_type == 'FLOAT':
        return float(result)

def run(p):
    global triplos_queue
    global symbol_table
    if type(p) == list:
        
        # Assignment operation
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
            
        # Arithmetic operations
        op1 = run(p[1])
        op2 = run(p[2])
        op_type = getType(p[0], p[1], p[2])

        if p[0] == '+':
            result = op1 + op2
            return formatResult(result, op_type)
        elif p[0] == '-':
            result = op1 - op2
            return formatResult(result, op_type)
        elif p[0] == '*':
            result = op1 * op2
            return formatResult(result, op_type)
        elif p[0] == '/':
            result = op1 / op2
            return formatResult(result, op_type)
        
        # Logic operations
        elif p[0] == '>':
            if op1 > op2:
                return 1
            else:
                return 0
        elif p[0] == '<':
            if op1 < op2:
                return 1
            else:
                return 0
        elif p[0] == '==':
            if op1 == op2:
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

# Begin parsing process
parser.parse(s)

print('\nTabla de Simbolos:')
print(symbol_table, end='\n\n')

print('Triplos queue:')
print(triplos_queue, end='\n\n')

# Process all the actions in the intermediate code
for instruction in triplos_queue:
    run(instruction)

print('Tabla de Simbolos:')
print(symbol_table, end='\n\n')
