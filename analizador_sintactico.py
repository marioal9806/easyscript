'''
Language : EasyScript
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
        'INT':{'+':'INT', '-':'INT', '*': 'INT', '/':'INT', '>=':'BOOL', '<=':'BOOL', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'FLOAT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>=':'BOOL', '<=':'BOOL', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'STRING':{'+':'X', '-':'X', '*': 'X', '/':'X', '>=':'X', '<=':'X', '>':'X', '<':'X', '==':'X'}
        },

    'FLOAT':{
        'INT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>=':'BOOL', '<=':'BOOL', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'FLOAT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>=':'BOOL', '<=':'BOOL', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'STRING':{'+':'X', '-':'X', '*': 'X', '/':'X', '>=':'X', '<=':'X', '>':'X', '<':'X', '==':'X'}
        },
    
    'STRING':{
        'INT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>=':'BOOL', '<=':'BOOL', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'FLOAT':{'+':'FLOAT', '-':'FLOAT', '*': 'FLOAT', '/':'FLOAT', '>=':'BOOL', '<=':'BOOL', '>':'BOOL', '<':'BOOL', '==':'BOOL'},
        'STRING':{'+':'X', '-':'X', '*': 'X', '/':'X', '>=':'X', '<=':'X', '>':'X', '<':'X', '==':'BOOL'}
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

    # print(curr_type)
    # print(stack_type)
    # curr_type = stack_type.pop()
    # curr_ID = queue_var.pop().rstrip('$')
    symbol_table[curr_ID] = [curr_type, None]

def convertStandardType(temp_type):
    if temp_type == int:
        return 'INT'
    elif temp_type == float:
        return 'FLOAT'

def getOperatorType(op):
    if(type(op) == str):
        type_op = symbol_table[op][0]
        op = symbol_table[op][1]
    elif(type(op) == list):
        op = run(op)
        type_op = convertStandardType(type(op))
    else:
        type_op = convertStandardType(type(op))
    return (type_op, op)

def getResultType(type1, type2, type3):
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
    else:
        return str(result)

def print_elem(elem):
    global symbol_table
    if type(elem) == str:
        if(elem[0] == "\"" and elem[-1] == "\""):
            print(elem.rstrip("\"").lstrip("\""))
        else:
            try:
                print(symbol_table[elem][1])
            except KeyError as err:
                print(f"ERROR: UNDECLARED VARIABLE {err}")
                quit()
    else:
        print(elem)

def recursive_print(list_elem):
    if type(list_elem) == list:
        if len(list_elem) == 1:
            print_elem(list_elem[0])
        else:
            for elem in list_elem:
                recursive_print(elem)
    else:
        print_elem(list_elem)

def write_elem(elem):
    if(len(elem) > 1):
        print(f"ERROR: YOU CAN ONLY WRITE ONE VARIABLE")
        quit()
    else:
        global symbol_table
        var = elem[0]
        # Comprobar que la variable se encuentra en la tabla
        if var in symbol_table:
            valor = input()
            # Revisar si el valor corresponde con la variable
            type_var = symbol_table[var][0]
            try:   
                valor = formatResult(valor, type_var)
            except ValueError as err:
                print(f"ERROR: INPUT FOR VARIABLE: \'{var}\' MUST BE OF TYPE: \'{type_var}\'")
                quit()
            
            # Actualizar valor en la tabla de símbolos
            symbol_table[var][1] = valor
        else:
            print(f"ERROR: UNDECLARED VARIABLE {var}")
            quit()
        

def run(p):
    global triplos_queue
    global symbol_table
    global pc
    if type(p) == list:
        # Print
        if p[0] == 'print':
            recursive_print(p[1])
            return
        # Input
        if p[0] == 'input':
            write_elem(p[1])
            return

        # Goto falso
        if p[0] == 'gotofalso' :
            if run(p[1]) == 0:
                pc = p[2] - 1
            return
        # Goto verdadero
        elif p[0] == 'gotoverdadero':
            if run(p[1]) == 1:
                pc = p[2] - 1
            return
        # Goto
        elif p[0] == 'goto':
            pc = p[1] - 1
            return
        
        # Assignment operation
        if(p[0] == '='):
            try:
                symbol_table[p[1]][1] = run(p[2])
                return
            except KeyError as err:
                print(f"ERROR: UNDECLARED VARIABLE {err}")
                quit()
        type1 = ""
        type2 = ""
        
        op1 = p[1]
        op2 = p[2]

        type1, op1 = getOperatorType(op1)
        type2, op2 = getOperatorType(op2)

        # Arithmetic operations
        op_type = getResultType(type1, type2, p[0])

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
        elif p[0] == '>=':
            if op1 >= op2:
                return 1
            else:
                return 0
        elif p[0] == '<=':
            if op1 <= op2:
                return 1
            else:
                return 0
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
        if(type(p) == str):
            return symbol_table[p][1]
        return p

# ------------------------------------------------------------------------------
# PROGRAM EXECUTION

try:
    # s = input('>> ')
    with open('programa_prueba2.txt','r', encoding='utf8') as file:
        s = file.read()
except EOFError:
    quit()

global symbol_table
global stack_saltos
# global cont

# Begin parsing process
parser.parse(s)

print('Triplos queue:')
for triplo in triplos_queue:
    print(triplo)


# Process all the variable declarations
processVariableDeclaration()

print('\n')
pc = 0
# Process all the actions in the intermediate code
while(pc != len(triplos_queue)):
    run(triplos_queue[pc])
    pc += 1

print(f'\nContador: ', end='')
print(parserules.cont, end='\n')
print('\nStack Saltos: ', end='')
print(stack_saltos, end='\n\n')

print('Tabla de Simbolos:')
print(symbol_table, end='\n\n')
