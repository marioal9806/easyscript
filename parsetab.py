
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS CALL CLOSEPAR COMMA DIM DIVIDE DO ELSE END EQUALS FLOAT FLOAT_TYPE FOR GOTO GREATERTHAN GREATERTHANOREQUAL IDENTIFIER IF INPUT INT INT_TYPE ISEQUALTO LABEL LABEL_SALTO LBRACKET LESSTHAN LESSTHANOREQUAL LET LOOP MINUS MULTIPLY NEXT OPENPAR OR PLUS PRINT PROGRAM RBRACKET RETURN STRING STRING_TYPE THEN TO WHILE\n    programa : programa_aux var procedure block END\n    \n    programa_aux : PROGRAM\n    \n    var : DIM repeated_identifier AS type repeated_size aux_size var\n        | DIM repeated_identifier AS STRING_TYPE var\n        | empty\n    \n    repeated_size : LBRACKET INT RBRACKET repeated_size\n                    | empty\n    \n    aux_size : empty\n    \n    repeated_identifier : IDENTIFIER COMMA repeated_identifier\n                        | IDENTIFIER\n    \n    type : INT_TYPE\n            | FLOAT_TYPE\n    \n    block : statement block\n            | empty\n    \n    statement : GOTO LABEL\n        | LABEL_SALTO\n    \n    statement : FOR aux1 TO aux2 block NEXT aux3\n    \n    aux1 : IDENTIFIER EQUALS expression\n    \n    aux2 : expression\n    \n    aux3 : IDENTIFIER\n    \n    statement : DO do_while_inicio block LOOP WHILE aux_do_while\n    \n    do_while_inicio : empty\n    \n    aux_do_while : expression\n    \n    statement : WHILE aux_while DO block LOOP fin_while\n    \n    aux_while : expression\n    \n    fin_while : empty\n    \n    statement : IF aux_if THEN block ELSE aux_else block END IF aux_fin\n    \n    aux_if : expression\n    \n    aux_else : empty\n    \n    aux_fin : empty\n    \n    statement : LET aux_array EQUALS expression\n    \n    statement : CALL LABEL\n    \n    procedure : aux_label block aux_return procedure\n                | empty\n    \n    aux_label : LABEL\n    \n    aux_return : RETURN\n    \n    statement : INPUT repeated_print\n    \n    statement : PRINT repeated_print\n    \n    repeated_print : repeated_elem COMMA repeated_print\n                    | repeated_elem\n    \n    repeated_elem : STRING\n                    | elem\n    \n    expression : expression_s op_rel expression_s\n                | expression_s\n    \n    expression_s : term \n                | term PLUS expression_s\n                | term MINUS expression_s\n                | term OR expression_s\n    \n    term : factor\n        | factor MULTIPLY term\n        | factor DIVIDE term\n        | factor AND term\n    \n    factor : elem\n            | OPENPAR expression CLOSEPAR\n    \n    elem : INT\n        | aux_array\n        | elem_else\n    \n    aux_array : size_identifier repeated_size_access end_array\n    \n    size_identifier : IDENTIFIER\n    \n    repeated_size_access : LBRACKET expression RBRACKET repeated_size_access\n                    | empty\n    \n    end_array : empty\n    \n    elem_else : FLOAT\n    \n    op_rel : LESSTHANOREQUAL\n            | GREATERTHANOREQUAL\n            | ISEQUALTO\n            | GREATERTHAN\n            | LESSTHAN\n\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[3,]),'$end':([1,29,],[0,-1,]),'DIM':([2,3,60,61,62,63,89,91,112,113,121,130,],[5,-2,-69,5,-11,-12,-69,-7,5,-8,-69,-6,]),'LABEL':([2,3,4,6,16,23,58,59,60,61,62,63,89,91,92,112,113,120,121,130,],[-69,-2,10,-5,31,52,10,-36,-69,-69,-11,-12,-69,-7,-4,-69,-8,-3,-69,-6,]),'GOTO':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,16,16,-34,-35,16,-16,-69,-15,16,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,16,-69,-61,16,-33,-69,-7,-4,16,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,16,-29,-6,-17,-20,-69,-27,-30,]),'LABEL_SALTO':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,17,17,-34,-35,17,-16,-69,-15,17,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,17,-69,-61,17,-33,-69,-7,-4,17,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,17,-29,-6,-17,-20,-69,-27,-30,]),'FOR':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,18,18,-34,-35,18,-16,-69,-15,18,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,18,-69,-61,18,-33,-69,-7,-4,18,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,18,-29,-6,-17,-20,-69,-27,-30,]),'DO':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,36,37,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,19,19,-34,-35,19,-16,-69,-15,19,-22,68,-25,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,19,-69,-61,19,-33,-69,-7,-4,19,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,19,-29,-6,-17,-20,-69,-27,-30,]),'WHILE':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,96,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,20,20,-34,-35,20,-16,-69,-15,20,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,20,-69,-61,20,-33,-69,-7,-4,20,-19,116,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,20,-29,-6,-17,-20,-69,-27,-30,]),'IF':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,134,135,136,137,],[-69,-2,-69,-5,21,21,-34,-35,21,-16,-69,-15,21,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,21,-69,-61,21,-33,-69,-7,-4,21,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,21,-29,-6,-17,-20,135,-69,-27,-30,]),'LET':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,22,22,-34,-35,22,-16,-69,-15,22,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,22,-69,-61,22,-33,-69,-7,-4,22,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,22,-29,-6,-17,-20,-69,-27,-30,]),'CALL':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,23,23,-34,-35,23,-16,-69,-15,23,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,23,-69,-61,23,-33,-69,-7,-4,23,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,23,-29,-6,-17,-20,-69,-27,-30,]),'INPUT':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,24,24,-34,-35,24,-16,-69,-15,24,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,24,-69,-61,24,-33,-69,-7,-4,24,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,24,-29,-6,-17,-20,-69,-27,-30,]),'PRINT':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,68,82,84,85,88,89,91,92,93,94,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,137,],[-69,-2,-69,-5,25,25,-34,-35,25,-16,-69,-15,25,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,25,-69,-61,25,-33,-69,-7,-4,25,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,25,-29,-6,-17,-20,-69,-27,-30,]),'END':([2,3,4,6,7,9,13,14,15,17,30,31,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,58,59,60,61,62,63,82,84,88,89,91,92,98,99,100,101,102,103,104,105,106,107,110,111,112,113,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,133,135,136,137,],[-69,-2,-69,-5,-69,-34,29,-69,-14,-16,-13,-15,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-36,-69,-69,-11,-12,-69,-61,-33,-69,-7,-4,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-8,-69,-69,-69,-3,-69,-21,-23,-24,-26,-60,-69,-29,-6,-17,-20,134,-69,-27,-30,]),'IDENTIFIER':([5,18,20,21,22,24,25,28,42,65,66,69,70,71,72,73,74,75,76,77,78,79,80,83,86,87,116,122,],[12,33,48,48,48,48,48,12,48,48,48,48,-64,-65,-66,-67,-68,48,48,48,48,48,48,48,48,48,48,132,]),'RETURN':([8,10,14,15,17,26,30,31,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,82,84,98,99,100,101,102,103,104,105,106,107,110,111,117,118,123,124,125,126,127,131,132,135,136,137,],[-69,-35,-69,-14,-16,59,-13,-15,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-61,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-69,-21,-23,-24,-26,-60,-17,-20,-69,-27,-30,]),'AS':([11,12,64,],[27,-10,-9,]),'COMMA':([12,43,44,45,46,47,48,54,55,56,82,84,106,107,118,127,],[28,-55,-56,-57,-69,-63,-59,87,-41,-42,-69,-61,-58,-62,-69,-60,]),'LOOP':([14,15,17,19,30,31,34,35,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,67,68,82,84,97,98,99,100,101,102,103,104,105,106,107,110,111,117,118,123,124,125,126,127,131,132,135,136,137,],[-69,-14,-16,-69,-13,-15,-69,-22,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,96,-69,-69,-61,117,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,-69,-69,-21,-23,-24,-26,-60,-17,-20,-69,-27,-30,]),'ELSE':([14,15,17,30,31,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,82,84,85,98,99,100,101,102,103,104,105,106,107,109,110,111,117,118,123,124,125,126,127,131,132,135,136,137,],[-69,-14,-16,-13,-15,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-61,-69,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,119,-31,-39,-69,-69,-21,-23,-24,-26,-60,-17,-20,-69,-27,-30,]),'NEXT':([14,15,17,30,31,38,39,40,41,43,44,45,46,47,48,52,53,54,55,56,57,82,84,93,94,98,99,100,101,102,103,104,105,106,107,110,111,115,117,118,123,124,125,126,127,131,132,135,136,137,],[-69,-14,-16,-13,-15,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-32,-37,-40,-41,-42,-38,-69,-61,-69,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-31,-39,122,-69,-69,-21,-23,-24,-26,-60,-17,-20,-69,-27,-30,]),'OPENPAR':([20,21,42,65,66,69,70,71,72,73,74,75,76,77,78,79,80,83,86,116,],[42,42,42,42,42,42,-64,-65,-66,-67,-68,42,42,42,42,42,42,42,42,42,]),'INT':([20,21,24,25,42,65,66,69,70,71,72,73,74,75,76,77,78,79,80,83,86,87,90,116,],[43,43,43,43,43,43,43,43,-64,-65,-66,-67,-68,43,43,43,43,43,43,43,43,43,114,43,]),'FLOAT':([20,21,24,25,42,65,66,69,70,71,72,73,74,75,76,77,78,79,80,83,86,87,116,],[47,47,47,47,47,47,47,47,-64,-65,-66,-67,-68,47,47,47,47,47,47,47,47,47,47,]),'STRING':([24,25,87,],[55,55,55,]),'STRING_TYPE':([27,],[61,]),'INT_TYPE':([27,],[62,]),'FLOAT_TYPE':([27,],[63,]),'TO':([32,38,39,40,41,43,44,45,46,47,48,82,84,95,98,99,100,101,102,103,104,105,106,107,118,127,],[65,-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-18,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-69,-60,]),'EQUALS':([33,46,48,51,82,84,106,107,118,127,],[66,-69,-59,86,-69,-61,-58,-62,-69,-60,]),'THEN':([38,39,40,41,43,44,45,46,47,48,49,50,82,84,98,99,100,101,102,103,104,105,106,107,118,127,],[-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,85,-28,-69,-61,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-69,-60,]),'CLOSEPAR':([38,39,40,41,43,44,45,46,47,48,81,82,84,98,99,100,101,102,103,104,105,106,107,118,127,],[-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,105,-69,-61,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,-69,-60,]),'RBRACKET':([38,39,40,41,43,44,45,46,47,48,82,84,98,99,100,101,102,103,104,105,106,107,108,114,118,127,],[-44,-45,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-43,-46,-47,-48,-50,-51,-52,-54,-58,-62,118,121,-69,-60,]),'LESSTHANOREQUAL':([38,39,40,41,43,44,45,46,47,48,82,84,99,100,101,102,103,104,105,106,107,118,127,],[70,-45,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-46,-47,-48,-50,-51,-52,-54,-58,-62,-69,-60,]),'GREATERTHANOREQUAL':([38,39,40,41,43,44,45,46,47,48,82,84,99,100,101,102,103,104,105,106,107,118,127,],[71,-45,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-46,-47,-48,-50,-51,-52,-54,-58,-62,-69,-60,]),'ISEQUALTO':([38,39,40,41,43,44,45,46,47,48,82,84,99,100,101,102,103,104,105,106,107,118,127,],[72,-45,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-46,-47,-48,-50,-51,-52,-54,-58,-62,-69,-60,]),'GREATERTHAN':([38,39,40,41,43,44,45,46,47,48,82,84,99,100,101,102,103,104,105,106,107,118,127,],[73,-45,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-46,-47,-48,-50,-51,-52,-54,-58,-62,-69,-60,]),'LESSTHAN':([38,39,40,41,43,44,45,46,47,48,82,84,99,100,101,102,103,104,105,106,107,118,127,],[74,-45,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-46,-47,-48,-50,-51,-52,-54,-58,-62,-69,-60,]),'PLUS':([39,40,41,43,44,45,46,47,48,82,84,102,103,104,105,106,107,118,127,],[75,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-50,-51,-52,-54,-58,-62,-69,-60,]),'MINUS':([39,40,41,43,44,45,46,47,48,82,84,102,103,104,105,106,107,118,127,],[76,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-50,-51,-52,-54,-58,-62,-69,-60,]),'OR':([39,40,41,43,44,45,46,47,48,82,84,102,103,104,105,106,107,118,127,],[77,-49,-53,-55,-56,-57,-69,-63,-59,-69,-61,-50,-51,-52,-54,-58,-62,-69,-60,]),'MULTIPLY':([40,41,43,44,45,46,47,48,82,84,105,106,107,118,127,],[78,-53,-55,-56,-57,-69,-63,-59,-69,-61,-54,-58,-62,-69,-60,]),'DIVIDE':([40,41,43,44,45,46,47,48,82,84,105,106,107,118,127,],[79,-53,-55,-56,-57,-69,-63,-59,-69,-61,-54,-58,-62,-69,-60,]),'AND':([40,41,43,44,45,46,47,48,82,84,105,106,107,118,127,],[80,-53,-55,-56,-57,-69,-63,-59,-69,-61,-54,-58,-62,-69,-60,]),'LBRACKET':([46,48,60,62,63,118,121,],[83,-59,90,-11,-12,83,90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'programa_aux':([0,],[2,]),'var':([2,61,112,],[4,92,120,]),'empty':([2,4,7,8,14,19,34,46,58,60,61,68,82,85,89,93,112,117,118,119,121,128,135,],[6,9,15,15,15,35,15,84,9,91,6,15,107,15,113,15,6,126,84,129,91,15,137,]),'procedure':([4,58,],[7,88,]),'aux_label':([4,58,],[8,8,]),'repeated_identifier':([5,28,],[11,64,]),'block':([7,8,14,34,68,85,93,128,],[13,26,30,67,97,109,115,133,]),'statement':([7,8,14,34,68,85,93,128,],[14,14,14,14,14,14,14,14,]),'aux1':([18,],[32,]),'do_while_inicio':([19,],[34,]),'aux_while':([20,],[36,]),'expression':([20,21,42,65,66,83,86,116,],[37,50,81,94,95,108,110,124,]),'expression_s':([20,21,42,65,66,69,75,76,77,83,86,116,],[38,38,38,38,38,98,99,100,101,38,38,38,]),'term':([20,21,42,65,66,69,75,76,77,78,79,80,83,86,116,],[39,39,39,39,39,39,39,39,39,102,103,104,39,39,39,]),'factor':([20,21,42,65,66,69,75,76,77,78,79,80,83,86,116,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'elem':([20,21,24,25,42,65,66,69,75,76,77,78,79,80,83,86,87,116,],[41,41,56,56,41,41,41,41,41,41,41,41,41,41,41,41,56,41,]),'aux_array':([20,21,22,24,25,42,65,66,69,75,76,77,78,79,80,83,86,87,116,],[44,44,51,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'elem_else':([20,21,24,25,42,65,66,69,75,76,77,78,79,80,83,86,87,116,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'size_identifier':([20,21,22,24,25,42,65,66,69,75,76,77,78,79,80,83,86,87,116,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'aux_if':([21,],[49,]),'repeated_print':([24,25,87,],[53,57,111,]),'repeated_elem':([24,25,87,],[54,54,54,]),'aux_return':([26,],[58,]),'type':([27,],[60,]),'op_rel':([38,],[69,]),'repeated_size_access':([46,118,],[82,127,]),'repeated_size':([60,121,],[89,130,]),'aux2':([65,],[93,]),'end_array':([82,],[106,]),'aux_size':([89,],[112,]),'aux_do_while':([116,],[123,]),'fin_while':([117,],[125,]),'aux_else':([119,],[128,]),'aux3':([122,],[131,]),'aux_fin':([135,],[136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> programa_aux var procedure block END','programa',5,'p_programa','parserules.py',57),
  ('programa_aux -> PROGRAM','programa_aux',1,'p_programa_aux','parserules.py',63),
  ('var -> DIM repeated_identifier AS type repeated_size aux_size var','var',7,'p_var','parserules.py',73),
  ('var -> DIM repeated_identifier AS STRING_TYPE var','var',5,'p_var','parserules.py',74),
  ('var -> empty','var',1,'p_var','parserules.py',75),
  ('repeated_size -> LBRACKET INT RBRACKET repeated_size','repeated_size',4,'p_repeated_size','parserules.py',84),
  ('repeated_size -> empty','repeated_size',1,'p_repeated_size','parserules.py',85),
  ('aux_size -> empty','aux_size',1,'p_aux_size','parserules.py',97),
  ('repeated_identifier -> IDENTIFIER COMMA repeated_identifier','repeated_identifier',3,'p_repeated_identifier','parserules.py',140),
  ('repeated_identifier -> IDENTIFIER','repeated_identifier',1,'p_repeated_identifier','parserules.py',141),
  ('type -> INT_TYPE','type',1,'p_var_type','parserules.py',157),
  ('type -> FLOAT_TYPE','type',1,'p_var_type','parserules.py',158),
  ('block -> statement block','block',2,'p_block','parserules.py',164),
  ('block -> empty','block',1,'p_block','parserules.py',165),
  ('statement -> GOTO LABEL','statement',2,'p_statement','parserules.py',171),
  ('statement -> LABEL_SALTO','statement',1,'p_statement','parserules.py',172),
  ('statement -> FOR aux1 TO aux2 block NEXT aux3','statement',7,'p_statement_for','parserules.py',180),
  ('aux1 -> IDENTIFIER EQUALS expression','aux1',3,'p_for_aux1','parserules.py',186),
  ('aux2 -> expression','aux2',1,'p_for_aux2','parserules.py',200),
  ('aux3 -> IDENTIFIER','aux3',1,'p_for_aux3','parserules.py',223),
  ('statement -> DO do_while_inicio block LOOP WHILE aux_do_while','statement',6,'p_statement_do_while','parserules.py',243),
  ('do_while_inicio -> empty','do_while_inicio',1,'p_do_while_inicio','parserules.py',249),
  ('aux_do_while -> expression','aux_do_while',1,'p_aux_do_while','parserules.py',259),
  ('statement -> WHILE aux_while DO block LOOP fin_while','statement',6,'p_statement_while','parserules.py',275),
  ('aux_while -> expression','aux_while',1,'p_aux_while','parserules.py',281),
  ('fin_while -> empty','fin_while',1,'p_aux_fin_while','parserules.py',296),
  ('statement -> IF aux_if THEN block ELSE aux_else block END IF aux_fin','statement',10,'p_statement_if','parserules.py',314),
  ('aux_if -> expression','aux_if',1,'p_aux_if','parserules.py',320),
  ('aux_else -> empty','aux_else',1,'p_aux_else','parserules.py',331),
  ('aux_fin -> empty','aux_fin',1,'p_aux_if_fin','parserules.py',347),
  ('statement -> LET aux_array EQUALS expression','statement',4,'p_statement_assignment','parserules.py',355),
  ('statement -> CALL LABEL','statement',2,'p_statement_procedure','parserules.py',367),
  ('procedure -> aux_label block aux_return procedure','procedure',4,'p_procedure','parserules.py',378),
  ('procedure -> empty','procedure',1,'p_procedure','parserules.py',379),
  ('aux_label -> LABEL','aux_label',1,'p_procedure_label','parserules.py',385),
  ('aux_return -> RETURN','aux_return',1,'p_procedure_return','parserules.py',393),
  ('statement -> INPUT repeated_print','statement',2,'p_statement_input','parserules.py',408),
  ('statement -> PRINT repeated_print','statement',2,'p_statement_print','parserules.py',419),
  ('repeated_print -> repeated_elem COMMA repeated_print','repeated_print',3,'p_repeated_print','parserules.py',431),
  ('repeated_print -> repeated_elem','repeated_print',1,'p_repeated_print','parserules.py',432),
  ('repeated_elem -> STRING','repeated_elem',1,'p_repeated_elem','parserules.py',441),
  ('repeated_elem -> elem','repeated_elem',1,'p_repeated_elem','parserules.py',442),
  ('expression -> expression_s op_rel expression_s','expression',3,'p_expression','parserules.py',450),
  ('expression -> expression_s','expression',1,'p_expression','parserules.py',451),
  ('expression_s -> term','expression_s',1,'p_expression_s','parserules.py',460),
  ('expression_s -> term PLUS expression_s','expression_s',3,'p_expression_s','parserules.py',461),
  ('expression_s -> term MINUS expression_s','expression_s',3,'p_expression_s','parserules.py',462),
  ('expression_s -> term OR expression_s','expression_s',3,'p_expression_s','parserules.py',463),
  ('term -> factor','term',1,'p_term','parserules.py',472),
  ('term -> factor MULTIPLY term','term',3,'p_term','parserules.py',473),
  ('term -> factor DIVIDE term','term',3,'p_term','parserules.py',474),
  ('term -> factor AND term','term',3,'p_term','parserules.py',475),
  ('factor -> elem','factor',1,'p_factor','parserules.py',484),
  ('factor -> OPENPAR expression CLOSEPAR','factor',3,'p_factor','parserules.py',485),
  ('elem -> INT','elem',1,'p_elem','parserules.py',494),
  ('elem -> aux_array','elem',1,'p_elem','parserules.py',495),
  ('elem -> elem_else','elem',1,'p_elem','parserules.py',496),
  ('aux_array -> size_identifier repeated_size_access end_array','aux_array',3,'p_aux_array','parserules.py',502),
  ('size_identifier -> IDENTIFIER','size_identifier',1,'p_size_identifier','parserules.py',508),
  ('repeated_size_access -> LBRACKET expression RBRACKET repeated_size_access','repeated_size_access',4,'p_repeated_size_access','parserules.py',563),
  ('repeated_size_access -> empty','repeated_size_access',1,'p_repeated_size_access','parserules.py',564),
  ('end_array -> empty','end_array',1,'p_end_array','parserules.py',581),
  ('elem_else -> FLOAT','elem_else',1,'p_elem_float','parserules.py',587),
  ('op_rel -> LESSTHANOREQUAL','op_rel',1,'p_op_rel','parserules.py',593),
  ('op_rel -> GREATERTHANOREQUAL','op_rel',1,'p_op_rel','parserules.py',594),
  ('op_rel -> ISEQUALTO','op_rel',1,'p_op_rel','parserules.py',595),
  ('op_rel -> GREATERTHAN','op_rel',1,'p_op_rel','parserules.py',596),
  ('op_rel -> LESSTHAN','op_rel',1,'p_op_rel','parserules.py',597),
  ('empty -> <empty>','empty',0,'p_empty','parserules.py',608),
]
