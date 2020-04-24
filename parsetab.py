
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS CLOSEPAR COMMA DIM DIVIDE DO ELSE END EQUALS FLOAT FLOAT_TYPE FOR GOSUB GOTO GREATERTHAN IDENTIFIER IF INPUT INT INT_TYPE ISEQUALTO LABEL LABEL_SALTO LESSTHAN LET LOOP MINUS MULTIPLY NEXT OPENPAR OR PLUS PRINT PROGRAM RETURN SIZE SIZE_ID STRING STRING_TYPE THEN TO WHILE\n    programa : PROGRAM var procedure block END\n    \n    var : DIM repeated_identifier AS type repeated_size var\n        | DIM repeated_identifier AS STRING_TYPE var\n        | empty\n    \n    repeated_size : SIZE repeated_size\n                    | SIZE_ID repeated_size\n                    | empty\n    \n    repeated_identifier : IDENTIFIER COMMA repeated_identifier\n                        | IDENTIFIER\n    \n    type : INT_TYPE\n            | FLOAT_TYPE\n    \n    block : statement block\n            | empty\n    \n    statement : INPUT repeated_print\n        | PRINT repeated_print\n        | FOR IDENTIFIER EQUALS INT TO INT block NEXT IDENTIFIER\n        | WHILE expression block LOOP\n        | DO block LOOP WHILE expression\n        | IF expression THEN block ELSE block END IF\n        | GOSUB LABEL\n        | GOTO LABEL\n        | LABEL_SALTO\n    \n    statement : LET IDENTIFIER repeated_size EQUALS expression\n    \n    procedure : LABEL block RETURN procedure\n                | empty\n    \n    repeated_print : repeated_elem COMMA repeated_print\n                    | repeated_elem\n    \n    repeated_elem : STRING\n                    | elem\n    \n    expression : expression_s op_rel expression_s\n                | expression_s\n    \n    expression_s : term \n                | term PLUS expression_s\n                | term MINUS expression_s\n                | term OR expression_s\n    \n    term : factor\n        | factor MULTIPLY term\n        | factor DIVIDE term\n        | factor AND term\n    \n    factor : elem\n            | OPENPAR expression CLOSEPAR\n    \n    elem : INT\n        | FLOAT\n        | IDENTIFIER repeated_size\n    \n    op_rel : LESSTHAN\n            | GREATERTHAN\n            | ISEQUALTO\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,27,],[0,-1,]),'DIM':([2,50,51,52,53,57,58,59,77,80,81,],[4,-48,4,-10,-11,-48,-48,-7,4,-5,-6,]),'LABEL':([2,3,5,20,21,49,50,51,52,53,57,58,59,77,78,80,81,95,],[-48,7,-4,46,47,7,-48,-48,-10,-11,-48,-48,-7,-48,-3,-5,-6,-2,]),'INPUT':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,14,14,-25,14,14,-22,-14,-27,-28,-29,-42,-43,-48,-15,14,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,14,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,14,-23,14,-19,-16,]),'PRINT':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,15,15,-25,15,15,-22,-14,-27,-28,-29,-42,-43,-48,-15,15,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,15,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,15,-23,15,-19,-16,]),'FOR':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,16,16,-25,16,16,-22,-14,-27,-28,-29,-42,-43,-48,-15,16,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,16,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,16,-23,16,-19,-16,]),'WHILE':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,73,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,17,17,-25,17,17,-22,-14,-27,-28,-29,-42,-43,-48,-15,17,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,92,17,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,17,-23,17,-19,-16,]),'DO':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,18,18,-25,18,18,-22,-14,-27,-28,-29,-42,-43,-48,-15,18,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,18,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,18,-23,18,-19,-16,]),'IF':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,103,105,106,],[-48,-48,-4,19,19,-25,19,19,-22,-14,-27,-28,-29,-42,-43,-48,-15,19,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,19,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,19,-23,19,105,-19,-16,]),'GOSUB':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,20,20,-25,20,20,-22,-14,-27,-28,-29,-42,-43,-48,-15,20,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,20,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,20,-23,20,-19,-16,]),'GOTO':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,21,21,-25,21,21,-22,-14,-27,-28,-29,-42,-43,-48,-15,21,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,21,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,21,-23,21,-19,-16,]),'LABEL_SALTO':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,22,22,-25,22,22,-22,-14,-27,-28,-29,-42,-43,-48,-15,22,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,22,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,22,-23,22,-19,-16,]),'LET':([2,3,5,6,7,8,12,18,22,29,30,31,32,33,34,35,36,38,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,74,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,100,105,106,],[-48,-48,-4,23,23,-25,23,23,-22,-14,-27,-28,-29,-42,-43,-48,-15,23,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,23,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,23,-23,23,-19,-16,]),'END':([2,3,5,6,8,11,12,13,22,28,29,30,31,32,33,34,35,36,39,40,41,42,46,47,49,50,51,52,53,56,57,58,59,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,95,97,98,99,101,105,106,],[-48,-48,-4,-48,-25,27,-48,-13,-22,-12,-14,-27,-28,-29,-42,-43,-48,-15,-31,-32,-36,-40,-20,-21,-48,-48,-48,-10,-11,-44,-48,-48,-7,-24,-48,-3,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-2,-18,-48,-23,103,-19,-16,]),'IDENTIFIER':([4,14,15,16,17,19,23,26,43,55,62,63,64,65,66,67,68,69,70,71,92,94,104,],[10,35,35,37,35,35,48,10,35,35,35,-45,-46,-47,35,35,35,35,35,35,35,35,106,]),'RETURN':([7,12,13,22,24,28,29,30,31,32,33,34,35,36,39,40,41,42,46,47,56,57,58,59,79,80,81,83,84,85,86,87,88,89,90,91,97,99,105,106,],[-48,-48,-13,-22,49,-12,-14,-27,-28,-29,-42,-43,-48,-15,-31,-32,-36,-40,-20,-21,-44,-48,-48,-7,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-18,-23,-19,-16,]),'AS':([9,10,54,],[25,-9,-8,]),'COMMA':([10,30,31,32,33,34,35,56,57,58,59,80,81,],[26,55,-28,-29,-42,-43,-48,-44,-48,-48,-7,-5,-6,]),'LOOP':([12,13,18,22,28,29,30,31,32,33,34,35,36,38,39,40,41,42,44,46,47,56,57,58,59,61,79,80,81,83,84,85,86,87,88,89,90,91,97,99,105,106,],[-48,-13,-48,-22,-12,-14,-27,-28,-29,-42,-43,-48,-15,-48,-31,-32,-36,-40,73,-20,-21,-44,-48,-48,-7,83,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-18,-23,-19,-16,]),'ELSE':([12,13,22,28,29,30,31,32,33,34,35,36,39,40,41,42,46,47,56,57,58,59,74,79,80,81,83,84,85,86,87,88,89,90,91,93,97,99,105,106,],[-48,-13,-22,-12,-14,-27,-28,-29,-42,-43,-48,-15,-31,-32,-36,-40,-20,-21,-44,-48,-48,-7,-48,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,98,-18,-23,-19,-16,]),'NEXT':([12,13,22,28,29,30,31,32,33,34,35,36,39,40,41,42,46,47,56,57,58,59,79,80,81,83,84,85,86,87,88,89,90,91,97,99,100,102,105,106,],[-48,-13,-22,-12,-14,-27,-28,-29,-42,-43,-48,-15,-31,-32,-36,-40,-20,-21,-44,-48,-48,-7,-26,-5,-6,-17,-30,-33,-34,-35,-37,-38,-39,-41,-18,-23,-48,104,-19,-16,]),'STRING':([14,15,55,],[31,31,31,]),'INT':([14,15,17,19,43,55,60,62,63,64,65,66,67,68,69,70,71,92,94,96,],[33,33,33,33,33,33,82,33,-45,-46,-47,33,33,33,33,33,33,33,33,100,]),'FLOAT':([14,15,17,19,43,55,62,63,64,65,66,67,68,69,70,71,92,94,],[34,34,34,34,34,34,34,-45,-46,-47,34,34,34,34,34,34,34,34,]),'OPENPAR':([17,19,43,62,63,64,65,66,67,68,69,70,71,92,94,],[43,43,43,43,-45,-46,-47,43,43,43,43,43,43,43,43,]),'STRING_TYPE':([25,],[51,]),'INT_TYPE':([25,],[52,]),'FLOAT_TYPE':([25,],[53,]),'MULTIPLY':([33,34,35,41,42,56,57,58,59,80,81,91,],[-42,-43,-48,69,-40,-44,-48,-48,-7,-5,-6,-41,]),'DIVIDE':([33,34,35,41,42,56,57,58,59,80,81,91,],[-42,-43,-48,70,-40,-44,-48,-48,-7,-5,-6,-41,]),'AND':([33,34,35,41,42,56,57,58,59,80,81,91,],[-42,-43,-48,71,-40,-44,-48,-48,-7,-5,-6,-41,]),'PLUS':([33,34,35,40,41,42,56,57,58,59,80,81,88,89,90,91,],[-42,-43,-48,66,-36,-40,-44,-48,-48,-7,-5,-6,-37,-38,-39,-41,]),'MINUS':([33,34,35,40,41,42,56,57,58,59,80,81,88,89,90,91,],[-42,-43,-48,67,-36,-40,-44,-48,-48,-7,-5,-6,-37,-38,-39,-41,]),'OR':([33,34,35,40,41,42,56,57,58,59,80,81,88,89,90,91,],[-42,-43,-48,68,-36,-40,-44,-48,-48,-7,-5,-6,-37,-38,-39,-41,]),'LESSTHAN':([33,34,35,39,40,41,42,56,57,58,59,80,81,85,86,87,88,89,90,91,],[-42,-43,-48,63,-32,-36,-40,-44,-48,-48,-7,-5,-6,-33,-34,-35,-37,-38,-39,-41,]),'GREATERTHAN':([33,34,35,39,40,41,42,56,57,58,59,80,81,85,86,87,88,89,90,91,],[-42,-43,-48,64,-32,-36,-40,-44,-48,-48,-7,-5,-6,-33,-34,-35,-37,-38,-39,-41,]),'ISEQUALTO':([33,34,35,39,40,41,42,56,57,58,59,80,81,85,86,87,88,89,90,91,],[-42,-43,-48,65,-32,-36,-40,-44,-48,-48,-7,-5,-6,-33,-34,-35,-37,-38,-39,-41,]),'THEN':([33,34,35,39,40,41,42,45,56,57,58,59,80,81,84,85,86,87,88,89,90,91,],[-42,-43,-48,-31,-32,-36,-40,74,-44,-48,-48,-7,-5,-6,-30,-33,-34,-35,-37,-38,-39,-41,]),'CLOSEPAR':([33,34,35,39,40,41,42,56,57,58,59,72,80,81,84,85,86,87,88,89,90,91,],[-42,-43,-48,-31,-32,-36,-40,-44,-48,-48,-7,91,-5,-6,-30,-33,-34,-35,-37,-38,-39,-41,]),'SIZE':([35,48,50,52,53,57,58,],[57,57,57,-10,-11,57,57,]),'SIZE_ID':([35,48,50,52,53,57,58,],[58,58,58,-10,-11,58,58,]),'EQUALS':([37,48,57,58,59,75,80,81,],[60,-48,-48,-48,-7,94,-5,-6,]),'TO':([82,],[96,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'var':([2,51,77,],[3,78,95,]),'empty':([2,3,6,7,12,18,35,38,48,49,50,51,57,58,74,77,98,100,],[5,8,13,13,13,13,59,13,59,8,59,5,59,59,13,5,13,13,]),'procedure':([3,49,],[6,76,]),'repeated_identifier':([4,26,],[9,54,]),'block':([6,7,12,18,38,74,98,100,],[11,24,28,44,61,93,101,102,]),'statement':([6,7,12,18,38,74,98,100,],[12,12,12,12,12,12,12,12,]),'repeated_print':([14,15,55,],[29,36,79,]),'repeated_elem':([14,15,55,],[30,30,30,]),'elem':([14,15,17,19,43,55,62,66,67,68,69,70,71,92,94,],[32,32,42,42,42,32,42,42,42,42,42,42,42,42,42,]),'expression':([17,19,43,92,94,],[38,45,72,97,99,]),'expression_s':([17,19,43,62,66,67,68,92,94,],[39,39,39,84,85,86,87,39,39,]),'term':([17,19,43,62,66,67,68,69,70,71,92,94,],[40,40,40,40,40,40,40,88,89,90,40,40,]),'factor':([17,19,43,62,66,67,68,69,70,71,92,94,],[41,41,41,41,41,41,41,41,41,41,41,41,]),'type':([25,],[50,]),'repeated_size':([35,48,50,57,58,],[56,75,77,80,81,]),'op_rel':([39,],[62,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM var procedure block END','programa',5,'p_programa','analizador_sintactico.py',18),
  ('var -> DIM repeated_identifier AS type repeated_size var','var',6,'p_var','analizador_sintactico.py',24),
  ('var -> DIM repeated_identifier AS STRING_TYPE var','var',5,'p_var','analizador_sintactico.py',25),
  ('var -> empty','var',1,'p_var','analizador_sintactico.py',26),
  ('repeated_size -> SIZE repeated_size','repeated_size',2,'p_repeated_size','analizador_sintactico.py',32),
  ('repeated_size -> SIZE_ID repeated_size','repeated_size',2,'p_repeated_size','analizador_sintactico.py',33),
  ('repeated_size -> empty','repeated_size',1,'p_repeated_size','analizador_sintactico.py',34),
  ('repeated_identifier -> IDENTIFIER COMMA repeated_identifier','repeated_identifier',3,'p_repeated_identifier','analizador_sintactico.py',40),
  ('repeated_identifier -> IDENTIFIER','repeated_identifier',1,'p_repeated_identifier','analizador_sintactico.py',41),
  ('type -> INT_TYPE','type',1,'p_var_type','analizador_sintactico.py',48),
  ('type -> FLOAT_TYPE','type',1,'p_var_type','analizador_sintactico.py',49),
  ('block -> statement block','block',2,'p_block','analizador_sintactico.py',55),
  ('block -> empty','block',1,'p_block','analizador_sintactico.py',56),
  ('statement -> INPUT repeated_print','statement',2,'p_statement','analizador_sintactico.py',62),
  ('statement -> PRINT repeated_print','statement',2,'p_statement','analizador_sintactico.py',63),
  ('statement -> FOR IDENTIFIER EQUALS INT TO INT block NEXT IDENTIFIER','statement',9,'p_statement','analizador_sintactico.py',64),
  ('statement -> WHILE expression block LOOP','statement',4,'p_statement','analizador_sintactico.py',65),
  ('statement -> DO block LOOP WHILE expression','statement',5,'p_statement','analizador_sintactico.py',66),
  ('statement -> IF expression THEN block ELSE block END IF','statement',8,'p_statement','analizador_sintactico.py',67),
  ('statement -> GOSUB LABEL','statement',2,'p_statement','analizador_sintactico.py',68),
  ('statement -> GOTO LABEL','statement',2,'p_statement','analizador_sintactico.py',69),
  ('statement -> LABEL_SALTO','statement',1,'p_statement','analizador_sintactico.py',70),
  ('statement -> LET IDENTIFIER repeated_size EQUALS expression','statement',5,'p_statement_assignment','analizador_sintactico.py',76),
  ('procedure -> LABEL block RETURN procedure','procedure',4,'p_procedure','analizador_sintactico.py',84),
  ('procedure -> empty','procedure',1,'p_procedure','analizador_sintactico.py',85),
  ('repeated_print -> repeated_elem COMMA repeated_print','repeated_print',3,'p_repeated_print','analizador_sintactico.py',91),
  ('repeated_print -> repeated_elem','repeated_print',1,'p_repeated_print','analizador_sintactico.py',92),
  ('repeated_elem -> STRING','repeated_elem',1,'p_repeated_elem','analizador_sintactico.py',98),
  ('repeated_elem -> elem','repeated_elem',1,'p_repeated_elem','analizador_sintactico.py',99),
  ('expression -> expression_s op_rel expression_s','expression',3,'p_expression','analizador_sintactico.py',105),
  ('expression -> expression_s','expression',1,'p_expression','analizador_sintactico.py',106),
  ('expression_s -> term','expression_s',1,'p_expression_s','analizador_sintactico.py',116),
  ('expression_s -> term PLUS expression_s','expression_s',3,'p_expression_s','analizador_sintactico.py',117),
  ('expression_s -> term MINUS expression_s','expression_s',3,'p_expression_s','analizador_sintactico.py',118),
  ('expression_s -> term OR expression_s','expression_s',3,'p_expression_s','analizador_sintactico.py',119),
  ('term -> factor','term',1,'p_term','analizador_sintactico.py',129),
  ('term -> factor MULTIPLY term','term',3,'p_term','analizador_sintactico.py',130),
  ('term -> factor DIVIDE term','term',3,'p_term','analizador_sintactico.py',131),
  ('term -> factor AND term','term',3,'p_term','analizador_sintactico.py',132),
  ('factor -> elem','factor',1,'p_factor','analizador_sintactico.py',142),
  ('factor -> OPENPAR expression CLOSEPAR','factor',3,'p_factor','analizador_sintactico.py',143),
  ('elem -> INT','elem',1,'p_elem_num','analizador_sintactico.py',153),
  ('elem -> FLOAT','elem',1,'p_elem_num','analizador_sintactico.py',154),
  ('elem -> IDENTIFIER repeated_size','elem',2,'p_elem_num','analizador_sintactico.py',155),
  ('op_rel -> LESSTHAN','op_rel',1,'p_op_rel','analizador_sintactico.py',165),
  ('op_rel -> GREATERTHAN','op_rel',1,'p_op_rel','analizador_sintactico.py',166),
  ('op_rel -> ISEQUALTO','op_rel',1,'p_op_rel','analizador_sintactico.py',167),
  ('empty -> <empty>','empty',0,'p_empty','analizador_sintactico.py',177),
]
