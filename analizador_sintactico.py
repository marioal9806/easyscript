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

# ------------------------------------------------------------------------------
# AUXILIARY FUNCTIONS
def processVariableDeclaration():
    global queue_var
    global stack_type
    print(queue_var)
    print(stack_type)
    while len(queue_var) != 1:
        end_parse = False
        curr_type = stack_type.pop()
        curr_ID = queue_var.pop().rstrip('$')
        symbol_table[curr_ID] = [curr_type, None]
        next_ID = queue_var.pop()

        while next_ID[-1] != '$':
            curr_ID = next_ID
            symbol_table[curr_ID] = [curr_type, None]
            if len(queue_var) == 0:
                end_parse = True
                break
            else:
                next_ID = queue_var.pop()
        if end_parse:
            break
        else:
            queue_var.append(next_ID)

    curr_type = stack_type.pop()
    curr_ID = queue_var.pop().rstrip('$')
    symbol_table[curr_ID] = [curr_type, None]

def convertStandardType(temp_type):
    if temp_type == int:
        return 'INT'
    elif temp_type == float:
        return 'FLOAT'

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
            # try:
                symbol_table[p[1]][1] = run(p[2])
                return
            # except KeyError:
                # print(f"ERROR: UNDECLARED VARIABLE \'{p[1]}\'")
                # quit()
        type1 = ""
        type2 = ""
        print(symbol_table)
        print(p[0])
        print(p[1])
        print(type(p[1]))
        print(p[2])
        print(type(p[2]))
        
        op1 = p[1]
        op2 = p[2]

        

        if(type(op1) == str):
            type1 = symbol_table[op1][0]
            op1 = symbol_table[op1][1]
        elif(type(op1) == list):
            op1 = run(op1)
            type1 = convertStandardType(type(op1))
        else:
            type1 = convertStandardType(type(op1))


        if(type(op2) == str):
            type2 = symbol_table[op2][0]
            op2 = symbol_table[op2][1]
        elif(type(op2) == list):
            op2 = run(op2)
            type2 = convertStandardType(type(op2))
        else:
            type2 = convertStandardType(type(op2))


        # Arithmetic operations
        op_type = getType(type1, type2, p[0])

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

# ------------------------------------------------------------------------------
# PROGRAM EXECUTION

try:
    # s = input('>> ')
    with open('ejemplo_expresiones.txt','r', encoding='utf8') as file:
        s = file.read()
except EOFError:
    quit()

global symbol_table

# Begin parsing process
parser.parse(s)

print('Triplos queue:')
print(triplos_queue, end='\n\n')

# Process all the variable declarations
processVariableDeclaration()

print('\nTabla de Simbolos:')
print(symbol_table, end='\n\n')

# Process all the actions in the intermediate code
for instruction in triplos_queue:
    run(instruction)

print('Tabla de Simbolos:')
print(symbol_table, end='\n\n')
