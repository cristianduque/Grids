
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LP RP COMMA INT FLOAT STRING CREATE WINDOW GRID SPRITE DRAW START ADD WINPOS CONTROLLER\n    execute : create\n    | start\n    | append\n    | empty\n    \n    object : WINDOW\n    | GRID\n    | SPRITE\n    | CONTROLLER\n    | DRAW\n    \n    create : CREATE object parameters\n    \n    start : START\n    \n    append : ADD WINPOS parameters\n    \n    parameters : LP parameter RP\n    | LP parameter COMMA parameter RP\n    | LP parameter COMMA parameter COMMA parameter RP\n    | LP parameter COMMA parameter COMMA parameter COMMA parameter RP\n    | empty\n    \n    parameter : INT\n    | FLOAT\n    | STRING\n    | LP parameter COMMA parameter RP\n    \n    empty :\n    '
    
_lr_action_items = {'CREATE':([0,],[6,]),'START':([0,],[7,]),'ADD':([0,],[8,]),'$end':([0,1,2,3,4,5,7,9,10,11,12,13,14,15,16,18,19,26,32,36,38,],[-22,0,-1,-2,-3,-4,-11,-22,-5,-6,-7,-8,-9,-22,-10,-17,-12,-13,-14,-15,-16,]),'WINDOW':([6,],[10,]),'GRID':([6,],[11,]),'SPRITE':([6,],[12,]),'CONTROLLER':([6,],[13,]),'DRAW':([6,],[14,]),'WINPOS':([8,],[15,]),'LP':([9,10,11,12,13,14,15,17,20,27,28,31,35,],[17,-5,-6,-7,-8,-9,17,20,20,20,20,20,20,]),'INT':([17,20,27,28,31,35,],[22,22,22,22,22,22,]),'FLOAT':([17,20,27,28,31,35,],[23,23,23,23,23,23,]),'STRING':([17,20,27,28,31,35,],[24,24,24,24,24,24,]),'RP':([21,22,23,24,29,30,33,34,37,],[26,-18,-19,-20,32,33,-21,36,38,]),'COMMA':([21,22,23,24,25,29,33,34,],[27,-18,-19,-20,28,31,-21,35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'execute':([0,],[1,]),'create':([0,],[2,]),'start':([0,],[3,]),'append':([0,],[4,]),'empty':([0,9,15,],[5,18,18,]),'object':([6,],[9,]),'parameters':([9,15,],[16,19,]),'parameter':([17,20,27,28,31,35,],[21,25,29,30,34,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> execute","S'",1,None,None,None),
  ('execute -> create','execute',1,'p_execute','grids.py',76),
  ('execute -> start','execute',1,'p_execute','grids.py',77),
  ('execute -> append','execute',1,'p_execute','grids.py',78),
  ('execute -> empty','execute',1,'p_execute','grids.py',79),
  ('object -> WINDOW','object',1,'p_object','grids.py',85),
  ('object -> GRID','object',1,'p_object','grids.py',86),
  ('object -> SPRITE','object',1,'p_object','grids.py',87),
  ('object -> CONTROLLER','object',1,'p_object','grids.py',88),
  ('object -> DRAW','object',1,'p_object','grids.py',89),
  ('create -> CREATE object parameters','create',3,'p_create','grids.py',95),
  ('start -> START','start',1,'p_start','grids.py',101),
  ('append -> ADD WINPOS parameters','append',3,'p_append','grids.py',107),
  ('parameters -> LP parameter RP','parameters',3,'p_parameters','grids.py',113),
  ('parameters -> LP parameter COMMA parameter RP','parameters',5,'p_parameters','grids.py',114),
  ('parameters -> LP parameter COMMA parameter COMMA parameter RP','parameters',7,'p_parameters','grids.py',115),
  ('parameters -> LP parameter COMMA parameter COMMA parameter COMMA parameter RP','parameters',9,'p_parameters','grids.py',116),
  ('parameters -> empty','parameters',1,'p_parameters','grids.py',117),
  ('parameter -> INT','parameter',1,'p_parameter','grids.py',132),
  ('parameter -> FLOAT','parameter',1,'p_parameter','grids.py',133),
  ('parameter -> STRING','parameter',1,'p_parameter','grids.py',134),
  ('parameter -> LP parameter COMMA parameter RP','parameter',5,'p_parameter','grids.py',135),
  ('empty -> <empty>','empty',0,'p_empty','grids.py',144),
]
