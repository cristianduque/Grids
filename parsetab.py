
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LP RP COMMA INT FLOAT STRING CREATE DESTROY WINDOW GRID SPRITE DRAW START ADD WINPOS\n    execute : create\n    | destroy\n    | draw\n    | start\n    | append\n    | empty\n    \n    object : WINDOW\n    | GRID\n    | SPRITE\n    \n    create : CREATE object parameters\n    \n    destroy : DESTROY object\n    \n    draw : DRAW parameters\n    \n    start : START\n    \n    append : ADD WINPOS parameters\n    \n    parameters : LP parameter RP\n    | LP parameter COMMA parameter RP\n    | LP parameter COMMA parameter COMMA parameter RP\n    | LP parameter COMMA parameter COMMA parameter COMMA parameter RP\n    | empty\n    \n    parameter : INT\n    | FLOAT\n    | STRING\n    | LP parameter COMMA parameter RP\n    \n    empty :\n    '
    
_lr_action_items = {'CREATE':([0,],[8,]),'DESTROY':([0,],[9,]),'DRAW':([0,],[10,]),'START':([0,],[11,]),'ADD':([0,],[12,]),'$end':([0,1,2,3,4,5,6,7,10,11,13,14,15,16,17,18,20,21,22,28,30,36,40,42,],[-24,0,-1,-2,-3,-4,-5,-6,-24,-13,-24,-7,-8,-9,-11,-12,-19,-24,-10,-14,-15,-16,-17,-18,]),'WINDOW':([8,9,],[14,14,]),'GRID':([8,9,],[15,15,]),'SPRITE':([8,9,],[16,16,]),'LP':([10,13,14,15,16,19,21,23,31,32,35,39,],[19,19,-7,-8,-9,23,19,23,23,23,23,23,]),'WINPOS':([12,],[21,]),'INT':([19,23,31,32,35,39,],[25,25,25,25,25,25,]),'FLOAT':([19,23,31,32,35,39,],[26,26,26,26,26,26,]),'STRING':([19,23,31,32,35,39,],[27,27,27,27,27,27,]),'RP':([24,25,26,27,33,34,37,38,41,],[30,-20,-21,-22,36,37,-23,40,42,]),'COMMA':([24,25,26,27,29,33,37,38,],[31,-20,-21,-22,32,35,-23,39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'execute':([0,],[1,]),'create':([0,],[2,]),'destroy':([0,],[3,]),'draw':([0,],[4,]),'start':([0,],[5,]),'append':([0,],[6,]),'empty':([0,10,13,21,],[7,20,20,20,]),'object':([8,9,],[13,17,]),'parameters':([10,13,21,],[18,22,28,]),'parameter':([19,23,31,32,35,39,],[24,29,33,34,38,41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> execute","S'",1,None,None,None),
  ('execute -> create','execute',1,'p_execute','grids.py',73),
  ('execute -> destroy','execute',1,'p_execute','grids.py',74),
  ('execute -> draw','execute',1,'p_execute','grids.py',75),
  ('execute -> start','execute',1,'p_execute','grids.py',76),
  ('execute -> append','execute',1,'p_execute','grids.py',77),
  ('execute -> empty','execute',1,'p_execute','grids.py',78),
  ('object -> WINDOW','object',1,'p_object','grids.py',84),
  ('object -> GRID','object',1,'p_object','grids.py',85),
  ('object -> SPRITE','object',1,'p_object','grids.py',86),
  ('create -> CREATE object parameters','create',3,'p_create','grids.py',92),
  ('destroy -> DESTROY object','destroy',2,'p_destroy','grids.py',98),
  ('draw -> DRAW parameters','draw',2,'p_draw','grids.py',104),
  ('start -> START','start',1,'p_start','grids.py',110),
  ('append -> ADD WINPOS parameters','append',3,'p_append','grids.py',116),
  ('parameters -> LP parameter RP','parameters',3,'p_parameters','grids.py',122),
  ('parameters -> LP parameter COMMA parameter RP','parameters',5,'p_parameters','grids.py',123),
  ('parameters -> LP parameter COMMA parameter COMMA parameter RP','parameters',7,'p_parameters','grids.py',124),
  ('parameters -> LP parameter COMMA parameter COMMA parameter COMMA parameter RP','parameters',9,'p_parameters','grids.py',125),
  ('parameters -> empty','parameters',1,'p_parameters','grids.py',126),
  ('parameter -> INT','parameter',1,'p_parameter','grids.py',141),
  ('parameter -> FLOAT','parameter',1,'p_parameter','grids.py',142),
  ('parameter -> STRING','parameter',1,'p_parameter','grids.py',143),
  ('parameter -> LP parameter COMMA parameter RP','parameter',5,'p_parameter','grids.py',144),
  ('empty -> <empty>','empty',0,'p_empty','grids.py',150),
]
