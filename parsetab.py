
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS CALL CLOSEPAR COMMA DIM DIVIDE DO ELSE END EQUALS FLOAT FLOAT_TYPE FOR GOTO GREATERTHAN GREATERTHANOREQUAL IDENTIFIER IF INPUT INT INT_TYPE ISEQUALTO LABEL LABEL_SALTO LESSTHAN LESSTHANOREQUAL LET LOOP MINUS MULTIPLY NEXT OPENPAR OR PLUS PRINT PROGRAM RETURN SIZE SIZE_ID STRING STRING_TYPE THEN TO WHILE\n    programa : programa_aux var procedure block END\n    \n    programa_aux : PROGRAM\n    \n    var : DIM repeated_identifier AS type repeated_size aux_size var\n        | DIM repeated_identifier AS STRING_TYPE var\n        | empty\n    \n    repeated_size : SIZE repeated_size\n                    | empty\n    \n    aux_size : empty\n    \n    repeated_identifier : IDENTIFIER COMMA repeated_identifier\n                        | IDENTIFIER\n    \n    type : INT_TYPE\n            | FLOAT_TYPE\n    \n    block : statement block\n            | empty\n    \n    statement : GOTO LABEL\n        | LABEL_SALTO\n    \n    statement : FOR aux1 TO aux2 block NEXT aux3\n    \n    aux1 : IDENTIFIER EQUALS expression\n    \n    aux2 : expression\n    \n    aux3 : IDENTIFIER\n    \n    statement : DO do_while_inicio block LOOP WHILE aux_do_while\n    \n    do_while_inicio : empty\n    \n    aux_do_while : expression\n    \n    statement : WHILE aux_while DO block LOOP fin_while\n    \n    aux_while : expression\n    \n    fin_while : empty\n    \n    statement : IF aux_if THEN block ELSE aux_else block END IF aux_fin\n    \n    aux_if : expression\n    \n    aux_else : empty\n    \n    aux_fin : empty\n    \n    statement : LET IDENTIFIER repeated_size EQUALS expression\n    \n    statement : CALL LABEL\n    \n    procedure : aux_label block aux_return procedure\n                | empty\n    \n    aux_label : LABEL\n    \n    aux_return : RETURN\n    \n    statement : INPUT repeated_print\n    \n    statement : PRINT repeated_print\n    \n    repeated_print : repeated_elem COMMA repeated_print\n                    | repeated_elem\n    \n    repeated_elem : STRING\n                    | elem\n    \n    expression : expression_s op_rel expression_s\n                | expression_s\n    \n    expression_s : term \n                | term PLUS expression_s\n                | term MINUS expression_s\n                | term OR expression_s\n    \n    term : factor\n        | factor MULTIPLY term\n        | factor DIVIDE term\n        | factor AND term\n    \n    factor : elem\n            | OPENPAR expression CLOSEPAR\n    \n    elem : INT\n        | IDENTIFIER repeated_size_access\n        | elem_else\n    \n    repeated_size_access : SIZE repeated_size_access\n                    | SIZE_ID repeated_size_access\n                    | empty\n    \n    elem_else : FLOAT\n    \n    op_rel : LESSTHANOREQUAL\n            | GREATERTHANOREQUAL\n            | ISEQUALTO\n            | GREATERTHAN\n            | LESSTHAN\n\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[3,]),'$end':([1,29,],[0,-1,]),'DIM':([2,3,58,59,60,61,86,87,90,109,111,112,],[5,-2,-67,5,-11,-12,-67,-7,-67,-6,5,-8,]),'LABEL':([2,3,4,6,16,23,56,57,58,59,60,61,86,87,90,91,109,111,112,118,],[-67,-2,10,-5,31,50,10,-36,-67,-67,-11,-12,-67,-7,-67,-4,-6,-67,-8,-3,]),'GOTO':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,16,16,-34,-35,16,-16,-67,-15,16,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,16,-56,-67,-67,-60,16,-67,-7,-33,-67,-4,16,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,16,-29,-17,-20,-67,-27,-30,]),'LABEL_SALTO':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,17,17,-34,-35,17,-16,-67,-15,17,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,17,-56,-67,-67,-60,17,-67,-7,-33,-67,-4,17,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,17,-29,-17,-20,-67,-27,-30,]),'FOR':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,18,18,-34,-35,18,-16,-67,-15,18,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,18,-56,-67,-67,-60,18,-67,-7,-33,-67,-4,18,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,18,-29,-17,-20,-67,-27,-30,]),'DO':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,36,37,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,19,19,-34,-35,19,-16,-67,-15,19,-22,66,-25,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,19,-56,-67,-67,-60,19,-67,-7,-33,-67,-4,19,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,19,-29,-17,-20,-67,-27,-30,]),'WHILE':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,95,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,20,20,-34,-35,20,-16,-67,-15,20,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,20,-56,-67,-67,-60,20,-67,-7,-33,-67,-4,20,-19,114,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,20,-29,-17,-20,-67,-27,-30,]),'IF':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,129,130,131,132,],[-67,-2,-67,-5,21,21,-34,-35,21,-16,-67,-15,21,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,21,-56,-67,-67,-60,21,-67,-7,-33,-67,-4,21,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,21,-29,-17,-20,130,-67,-27,-30,]),'LET':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,22,22,-34,-35,22,-16,-67,-15,22,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,22,-56,-67,-67,-60,22,-67,-7,-33,-67,-4,22,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,22,-29,-17,-20,-67,-27,-30,]),'CALL':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,23,23,-34,-35,23,-16,-67,-15,23,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,23,-56,-67,-67,-60,23,-67,-7,-33,-67,-4,23,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,23,-29,-17,-20,-67,-27,-30,]),'INPUT':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,24,24,-34,-35,24,-16,-67,-15,24,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,24,-56,-67,-67,-60,24,-67,-7,-33,-67,-4,24,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,24,-29,-17,-20,-67,-27,-30,]),'PRINT':([2,3,4,6,7,8,9,10,14,17,19,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,66,80,81,82,83,84,86,87,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,130,131,132,],[-67,-2,-67,-5,25,25,-34,-35,25,-16,-67,-15,25,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,25,-56,-67,-67,-60,25,-67,-7,-33,-67,-4,25,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,25,-29,-17,-20,-67,-27,-30,]),'END':([2,3,4,6,7,9,13,14,15,17,30,31,38,39,40,41,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,80,81,82,83,86,87,89,90,91,97,98,99,100,101,102,103,104,105,106,109,110,111,112,115,116,117,118,120,121,122,123,124,125,126,127,128,130,131,132,],[-67,-2,-67,-5,-67,-34,29,-67,-14,-16,-13,-15,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-67,-36,-67,-67,-11,-12,-56,-67,-67,-60,-67,-7,-33,-67,-4,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-6,-39,-67,-8,-67,-67,-31,-3,-21,-23,-24,-26,-67,-29,-17,-20,129,-67,-27,-30,]),'IDENTIFIER':([5,18,20,21,22,24,25,28,42,63,64,67,68,69,70,71,72,73,74,75,76,77,78,88,108,114,119,],[12,33,44,44,49,44,44,12,44,44,44,44,-62,-63,-64,-65,-66,44,44,44,44,44,44,44,44,44,127,]),'RETURN':([8,10,14,15,17,26,30,31,38,39,40,41,43,44,45,46,50,51,52,53,54,55,80,81,82,83,97,98,99,100,101,102,103,104,105,106,110,115,117,120,121,122,123,126,127,130,131,132,],[-67,-35,-67,-14,-16,57,-13,-15,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-56,-67,-67,-60,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-39,-67,-31,-21,-23,-24,-26,-17,-20,-67,-27,-30,]),'AS':([11,12,62,],[27,-10,-9,]),'COMMA':([12,43,44,45,46,52,53,54,80,81,82,83,105,106,],[28,-55,-67,-57,-61,88,-41,-42,-56,-67,-67,-60,-58,-59,]),'LOOP':([14,15,17,19,30,31,34,35,38,39,40,41,43,44,45,46,50,51,52,53,54,55,65,66,80,81,82,83,96,97,98,99,100,101,102,103,104,105,106,110,115,117,120,121,122,123,126,127,130,131,132,],[-67,-14,-16,-67,-13,-15,-67,-22,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,95,-67,-56,-67,-67,-60,115,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-39,-67,-31,-21,-23,-24,-26,-17,-20,-67,-27,-30,]),'ELSE':([14,15,17,30,31,38,39,40,41,43,44,45,46,50,51,52,53,54,55,80,81,82,83,84,97,98,99,100,101,102,103,104,105,106,107,110,115,117,120,121,122,123,126,127,130,131,132,],[-67,-14,-16,-13,-15,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-56,-67,-67,-60,-67,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,116,-39,-67,-31,-21,-23,-24,-26,-17,-20,-67,-27,-30,]),'NEXT':([14,15,17,30,31,38,39,40,41,43,44,45,46,50,51,52,53,54,55,80,81,82,83,92,93,97,98,99,100,101,102,103,104,105,106,110,113,115,117,120,121,122,123,126,127,130,131,132,],[-67,-14,-16,-13,-15,-44,-45,-49,-53,-55,-67,-57,-61,-32,-37,-40,-41,-42,-38,-56,-67,-67,-60,-67,-19,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,-39,119,-67,-31,-21,-23,-24,-26,-17,-20,-67,-27,-30,]),'OPENPAR':([20,21,42,63,64,67,68,69,70,71,72,73,74,75,76,77,78,108,114,],[42,42,42,42,42,42,-62,-63,-64,-65,-66,42,42,42,42,42,42,42,42,]),'INT':([20,21,24,25,42,63,64,67,68,69,70,71,72,73,74,75,76,77,78,88,108,114,],[43,43,43,43,43,43,43,43,-62,-63,-64,-65,-66,43,43,43,43,43,43,43,43,43,]),'FLOAT':([20,21,24,25,42,63,64,67,68,69,70,71,72,73,74,75,76,77,78,88,108,114,],[46,46,46,46,46,46,46,46,-62,-63,-64,-65,-66,46,46,46,46,46,46,46,46,46,]),'STRING':([24,25,88,],[53,53,53,]),'STRING_TYPE':([27,],[59,]),'INT_TYPE':([27,],[60,]),'FLOAT_TYPE':([27,],[61,]),'TO':([32,38,39,40,41,43,44,45,46,80,81,82,83,94,97,98,99,100,101,102,103,104,105,106,],[63,-44,-45,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-18,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,]),'EQUALS':([33,49,85,86,87,109,],[64,-67,108,-67,-7,-6,]),'THEN':([38,39,40,41,43,44,45,46,47,48,80,81,82,83,97,98,99,100,101,102,103,104,105,106,],[-44,-45,-49,-53,-55,-67,-57,-61,84,-28,-56,-67,-67,-60,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,]),'CLOSEPAR':([38,39,40,41,43,44,45,46,79,80,81,82,83,97,98,99,100,101,102,103,104,105,106,],[-44,-45,-49,-53,-55,-67,-57,-61,104,-56,-67,-67,-60,-43,-46,-47,-48,-50,-51,-52,-54,-58,-59,]),'LESSTHANOREQUAL':([38,39,40,41,43,44,45,46,80,81,82,83,98,99,100,101,102,103,104,105,106,],[68,-45,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-46,-47,-48,-50,-51,-52,-54,-58,-59,]),'GREATERTHANOREQUAL':([38,39,40,41,43,44,45,46,80,81,82,83,98,99,100,101,102,103,104,105,106,],[69,-45,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-46,-47,-48,-50,-51,-52,-54,-58,-59,]),'ISEQUALTO':([38,39,40,41,43,44,45,46,80,81,82,83,98,99,100,101,102,103,104,105,106,],[70,-45,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-46,-47,-48,-50,-51,-52,-54,-58,-59,]),'GREATERTHAN':([38,39,40,41,43,44,45,46,80,81,82,83,98,99,100,101,102,103,104,105,106,],[71,-45,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-46,-47,-48,-50,-51,-52,-54,-58,-59,]),'LESSTHAN':([38,39,40,41,43,44,45,46,80,81,82,83,98,99,100,101,102,103,104,105,106,],[72,-45,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-46,-47,-48,-50,-51,-52,-54,-58,-59,]),'PLUS':([39,40,41,43,44,45,46,80,81,82,83,101,102,103,104,105,106,],[73,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-50,-51,-52,-54,-58,-59,]),'MINUS':([39,40,41,43,44,45,46,80,81,82,83,101,102,103,104,105,106,],[74,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-50,-51,-52,-54,-58,-59,]),'OR':([39,40,41,43,44,45,46,80,81,82,83,101,102,103,104,105,106,],[75,-49,-53,-55,-67,-57,-61,-56,-67,-67,-60,-50,-51,-52,-54,-58,-59,]),'MULTIPLY':([40,41,43,44,45,46,80,81,82,83,104,105,106,],[76,-53,-55,-67,-57,-61,-56,-67,-67,-60,-54,-58,-59,]),'DIVIDE':([40,41,43,44,45,46,80,81,82,83,104,105,106,],[77,-53,-55,-67,-57,-61,-56,-67,-67,-60,-54,-58,-59,]),'AND':([40,41,43,44,45,46,80,81,82,83,104,105,106,],[78,-53,-55,-67,-57,-61,-56,-67,-67,-60,-54,-58,-59,]),'SIZE':([44,49,58,60,61,81,82,86,],[81,86,86,-11,-12,81,81,86,]),'SIZE_ID':([44,81,82,],[82,82,82,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'programa_aux':([0,],[2,]),'var':([2,59,111,],[4,91,118,]),'empty':([2,4,7,8,14,19,34,44,49,56,58,59,66,81,82,84,86,90,92,111,115,116,124,130,],[6,9,15,15,15,35,15,83,87,9,87,6,15,83,83,15,87,112,15,6,123,125,15,132,]),'procedure':([4,56,],[7,89,]),'aux_label':([4,56,],[8,8,]),'repeated_identifier':([5,28,],[11,62,]),'block':([7,8,14,34,66,84,92,124,],[13,26,30,65,96,107,113,128,]),'statement':([7,8,14,34,66,84,92,124,],[14,14,14,14,14,14,14,14,]),'aux1':([18,],[32,]),'do_while_inicio':([19,],[34,]),'aux_while':([20,],[36,]),'expression':([20,21,42,63,64,108,114,],[37,48,79,93,94,117,121,]),'expression_s':([20,21,42,63,64,67,73,74,75,108,114,],[38,38,38,38,38,97,98,99,100,38,38,]),'term':([20,21,42,63,64,67,73,74,75,76,77,78,108,114,],[39,39,39,39,39,39,39,39,39,101,102,103,39,39,]),'factor':([20,21,42,63,64,67,73,74,75,76,77,78,108,114,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'elem':([20,21,24,25,42,63,64,67,73,74,75,76,77,78,88,108,114,],[41,41,54,54,41,41,41,41,41,41,41,41,41,41,54,41,41,]),'elem_else':([20,21,24,25,42,63,64,67,73,74,75,76,77,78,88,108,114,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'aux_if':([21,],[47,]),'repeated_print':([24,25,88,],[51,55,110,]),'repeated_elem':([24,25,88,],[52,52,52,]),'aux_return':([26,],[56,]),'type':([27,],[58,]),'op_rel':([38,],[67,]),'repeated_size_access':([44,81,82,],[80,105,106,]),'repeated_size':([49,58,86,],[85,90,109,]),'aux2':([63,],[92,]),'aux_size':([90,],[111,]),'aux_do_while':([114,],[120,]),'fin_while':([115,],[122,]),'aux_else':([116,],[124,]),'aux3':([119,],[126,]),'aux_fin':([130,],[131,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> programa_aux var procedure block END','programa',5,'p_programa','parserules.py',53),
  ('programa_aux -> PROGRAM','programa_aux',1,'p_programa_aux','parserules.py',59),
  ('var -> DIM repeated_identifier AS type repeated_size aux_size var','var',7,'p_var','parserules.py',69),
  ('var -> DIM repeated_identifier AS STRING_TYPE var','var',5,'p_var','parserules.py',70),
  ('var -> empty','var',1,'p_var','parserules.py',71),
  ('repeated_size -> SIZE repeated_size','repeated_size',2,'p_repeated_size','parserules.py',80),
  ('repeated_size -> empty','repeated_size',1,'p_repeated_size','parserules.py',81),
  ('aux_size -> empty','aux_size',1,'p_aux_size','parserules.py',93),
  ('repeated_identifier -> IDENTIFIER COMMA repeated_identifier','repeated_identifier',3,'p_repeated_identifier','parserules.py',121),
  ('repeated_identifier -> IDENTIFIER','repeated_identifier',1,'p_repeated_identifier','parserules.py',122),
  ('type -> INT_TYPE','type',1,'p_var_type','parserules.py',138),
  ('type -> FLOAT_TYPE','type',1,'p_var_type','parserules.py',139),
  ('block -> statement block','block',2,'p_block','parserules.py',145),
  ('block -> empty','block',1,'p_block','parserules.py',146),
  ('statement -> GOTO LABEL','statement',2,'p_statement','parserules.py',152),
  ('statement -> LABEL_SALTO','statement',1,'p_statement','parserules.py',153),
  ('statement -> FOR aux1 TO aux2 block NEXT aux3','statement',7,'p_statement_for','parserules.py',161),
  ('aux1 -> IDENTIFIER EQUALS expression','aux1',3,'p_for_aux1','parserules.py',167),
  ('aux2 -> expression','aux2',1,'p_for_aux2','parserules.py',181),
  ('aux3 -> IDENTIFIER','aux3',1,'p_for_aux3','parserules.py',204),
  ('statement -> DO do_while_inicio block LOOP WHILE aux_do_while','statement',6,'p_statement_do_while','parserules.py',224),
  ('do_while_inicio -> empty','do_while_inicio',1,'p_do_while_inicio','parserules.py',230),
  ('aux_do_while -> expression','aux_do_while',1,'p_aux_do_while','parserules.py',240),
  ('statement -> WHILE aux_while DO block LOOP fin_while','statement',6,'p_statement_while','parserules.py',256),
  ('aux_while -> expression','aux_while',1,'p_aux_while','parserules.py',262),
  ('fin_while -> empty','fin_while',1,'p_aux_fin_while','parserules.py',277),
  ('statement -> IF aux_if THEN block ELSE aux_else block END IF aux_fin','statement',10,'p_statement_if','parserules.py',295),
  ('aux_if -> expression','aux_if',1,'p_aux_if','parserules.py',301),
  ('aux_else -> empty','aux_else',1,'p_aux_else','parserules.py',312),
  ('aux_fin -> empty','aux_fin',1,'p_aux_if_fin','parserules.py',328),
  ('statement -> LET IDENTIFIER repeated_size EQUALS expression','statement',5,'p_statement_assignment','parserules.py',336),
  ('statement -> CALL LABEL','statement',2,'p_statement_procedure','parserules.py',349),
  ('procedure -> aux_label block aux_return procedure','procedure',4,'p_procedure','parserules.py',360),
  ('procedure -> empty','procedure',1,'p_procedure','parserules.py',361),
  ('aux_label -> LABEL','aux_label',1,'p_procedure_label','parserules.py',367),
  ('aux_return -> RETURN','aux_return',1,'p_procedure_return','parserules.py',375),
  ('statement -> INPUT repeated_print','statement',2,'p_statement_input','parserules.py',390),
  ('statement -> PRINT repeated_print','statement',2,'p_statement_print','parserules.py',401),
  ('repeated_print -> repeated_elem COMMA repeated_print','repeated_print',3,'p_repeated_print','parserules.py',413),
  ('repeated_print -> repeated_elem','repeated_print',1,'p_repeated_print','parserules.py',414),
  ('repeated_elem -> STRING','repeated_elem',1,'p_repeated_elem','parserules.py',423),
  ('repeated_elem -> elem','repeated_elem',1,'p_repeated_elem','parserules.py',424),
  ('expression -> expression_s op_rel expression_s','expression',3,'p_expression','parserules.py',432),
  ('expression -> expression_s','expression',1,'p_expression','parserules.py',433),
  ('expression_s -> term','expression_s',1,'p_expression_s','parserules.py',442),
  ('expression_s -> term PLUS expression_s','expression_s',3,'p_expression_s','parserules.py',443),
  ('expression_s -> term MINUS expression_s','expression_s',3,'p_expression_s','parserules.py',444),
  ('expression_s -> term OR expression_s','expression_s',3,'p_expression_s','parserules.py',445),
  ('term -> factor','term',1,'p_term','parserules.py',454),
  ('term -> factor MULTIPLY term','term',3,'p_term','parserules.py',455),
  ('term -> factor DIVIDE term','term',3,'p_term','parserules.py',456),
  ('term -> factor AND term','term',3,'p_term','parserules.py',457),
  ('factor -> elem','factor',1,'p_factor','parserules.py',466),
  ('factor -> OPENPAR expression CLOSEPAR','factor',3,'p_factor','parserules.py',467),
  ('elem -> INT','elem',1,'p_elem','parserules.py',476),
  ('elem -> IDENTIFIER repeated_size_access','elem',2,'p_elem','parserules.py',477),
  ('elem -> elem_else','elem',1,'p_elem','parserules.py',478),
  ('repeated_size_access -> SIZE repeated_size_access','repeated_size_access',2,'p_repeated_size_access','parserules.py',487),
  ('repeated_size_access -> SIZE_ID repeated_size_access','repeated_size_access',2,'p_repeated_size_access','parserules.py',488),
  ('repeated_size_access -> empty','repeated_size_access',1,'p_repeated_size_access','parserules.py',489),
  ('elem_else -> FLOAT','elem_else',1,'p_elem_float','parserules.py',495),
  ('op_rel -> LESSTHANOREQUAL','op_rel',1,'p_op_rel','parserules.py',501),
  ('op_rel -> GREATERTHANOREQUAL','op_rel',1,'p_op_rel','parserules.py',502),
  ('op_rel -> ISEQUALTO','op_rel',1,'p_op_rel','parserules.py',503),
  ('op_rel -> GREATERTHAN','op_rel',1,'p_op_rel','parserules.py',504),
  ('op_rel -> LESSTHAN','op_rel',1,'p_op_rel','parserules.py',505),
  ('empty -> <empty>','empty',0,'p_empty','parserules.py',516),
]
