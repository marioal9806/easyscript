'''
Language : EasyScript
Author : Mario Alberto Ortega
Student ID : A01730557
'''
import ply.lex as lex
import ply.yacc as yacc
import sys
from collections import deque


from parserules import MyParser

from rlist import rlist

# PARSER
# -------------------------------------------------------------------------
p_mod = MyParser()
parser = p_mod.parser

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

pc = 0
array_space = rlist(0)

# ------------------------------------------------------------------------------
# AUXILIARY FUNCTIONS
def processVariableDeclaration():
    print(p_mod.queue_var)
    print(p_mod.stack_type)
    while len(p_mod.queue_var) != 1:
        end_parse = False
        curr_type = p_mod.stack_type.pop()
        curr_ID = p_mod.queue_var.pop().rstrip('$')
        if(curr_ID in p_mod.array_table):
            descr_list = p_mod.array_table[curr_ID]
            p_mod.symbol_table[curr_ID] = [curr_type, descr_list]
        else:
            p_mod.symbol_table[curr_ID] = [curr_type, None]
        next_ID = p_mod.queue_var.pop()

        while next_ID[-1] != '$':
            curr_ID = next_ID
            if(curr_ID in p_mod.array_table):
                descr_list = p_mod.array_table[curr_ID]
                p_mod.symbol_table[curr_ID] = [curr_type, descr_list]
            else:
                p_mod.symbol_table[curr_ID] = [curr_type, None]
            if len(p_mod.queue_var) == 0:
                end_parse = True
                break
            else:
                next_ID = p_mod.queue_var.pop()
        if end_parse:
            break
        else:
            p_mod.queue_var.append(next_ID)

    # print(curr_type)
    # print(p_mod.stack_type)
    # curr_type = p_mod.stack_type.pop()
    # curr_ID = p_mod.queue_var.pop().rstrip('$')
    p_mod.symbol_table[curr_ID] = [curr_type, None]

def convertStandardType(temp_type):
    if temp_type == int:
        return 'INT'
    elif temp_type == float:
        return 'FLOAT'

def getOperatorType(op):
    if(type(op) == str):
        type_op = p_mod.symbol_table[op][0]
        op = p_mod.symbol_table[op][1]
    elif(type(op) == list):
        op = run(op)
        type_op = convertStandardType(type(op))
    elif(type(op) == tuple):
        op = array_space[op[0]]
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
    if type(elem) == str:
        if(elem[0] == "\"" and elem[-1] == "\""):
            print(elem.rstrip("\"").lstrip("\""))
        else:
            try:
                print(p_mod.symbol_table[elem][1])
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
        var = elem[0]
        # Comprobar que la variable se encuentra en la tabla
        if var in p_mod.symbol_table:
            valor = input()
            # Revisar si el valor corresponde con la variable
            type_var = p_mod.symbol_table[var][0]
            try:   
                valor = formatResult(valor, type_var)
            except ValueError as err:
                print(f"ERROR: INPUT FOR VARIABLE: \'{var}\' MUST BE OF TYPE: \'{type_var}\'")
                quit()
            
            # Actualizar valor en la tabla de símbolos
            p_mod.symbol_table[var][1] = valor
        else:
            print(f"ERROR: UNDECLARED VARIABLE {var}")
            quit()

def run(p):
    global array_space
    global stack_return_address
    global pc
    if type(p) == list:
        # Verify
        if p[0] == 'verify':
            try:
                variable = p[1]
                offset = p[2]
                dim = p[3]
                if (offset < p_mod.symbol_table[variable][1][dim][0] and 
                    offset >= 0):
                    pc += 1
                    return
                else:
                    raise Exception(variable, offset)
            except Exception as err:
                x, y = err.args
                print(f"ERROR: Index {y} out of bounds on Vector \'{x}\''")
                quit()
        # Call
        if p[0] == 'call':
            try:
                dir_inicio = p_mod.procedure_table[p[1]]
                stack_return_address.appendleft(pc + 1)
                pc = dir_inicio
                return
            except KeyError as err:
                print(f"ERROR: UNDECLARED PROCEDURE {err}")
                quit()
        # Return
        if p[0] == 'return':
            pc = stack_return_address.popleft()
            return
        # Print
        if p[0] == 'print':
            recursive_print(p[1])
            pc += 1
            return
        # Input
        if p[0] == 'input':
            write_elem(p[1])
            pc += 1
            return

        # Goto falso
        if p[0] == 'gotofalso' :
            if run(p[1]) == 0:
                pc = p[2]
            else:
                pc += 1
            return
        # Goto verdadero
        elif p[0] == 'gotoverdadero':
            if run(p[1]) == 1:
                pc = p[2]
            else:
                pc += 1
            return
        # Goto
        elif p[0] == 'goto':
            pc = p[1]
            return
        
        # Assignment operation
        if(p[0] == '='):
            if(type(p[1]) == tuple and type(p[2]) == tuple):
                array_space[p[1][0]] = array_space[p[2][0]]
                pc += 1
                return
            elif(type(p[1]) == tuple):
                array_space[p[1][0]] = run(p[2])
                pc += 1
                return
            elif(type(p[2]) == tuple):
                try:
                    p_mod.symbol_table[p[1]][1] = array_space[p[2][0]]
                    pc += 1
                    return
                except KeyError as err:
                    print(f"ERROR: UNDECLARED VARIABLE {err}")
                    quit()
            else:
                try:
                    p_mod.symbol_table[p[1]][1] = run(p[2])
                    pc += 1
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
            return p_mod.symbol_table[p][1]
        return p

# ------------------------------------------------------------------------------
# PROGRAM EXECUTION

program = sys.argv[1]
try:
    with open(program,'r', encoding='utf8') as file:
        s = file.read()
except EOFError:
    quit()

stack_return_address = deque()

# Begin parsing process
parser.parse(s)

print('Triplos queue:')
for triplo in p_mod.triplos_queue:
    print(triplo)
print(end='\n')

# Process all the variable declarations
processVariableDeclaration()

print('Tabla de Simbolos:')
for var, value in p_mod.symbol_table.items():
    print(var, ": ", value)
print(end='\n')

print('Tabla de Procedimientos:')
print(p_mod.procedure_table, end='\n\n')

print('Array Table:')
for var, value in p_mod.array_table.items():
    print(var, ": ", value)
print(end='\n')

# Process all the actions in the intermediate code
while(pc != len(p_mod.triplos_queue)):
    run(p_mod.triplos_queue[pc])

print(f'\nContador: ', end='')
print(p_mod.cont, end='\n')
print('\nStack Saltos: ', end='')
print(p_mod.stack_saltos, end='\n\n')

print('Tabla de Simbolos:')
for var, value in p_mod.symbol_table.items():
    print(var, ": ", value)
print(end='\n')

print('Array Space:')
print(array_space, end='\n\n')
