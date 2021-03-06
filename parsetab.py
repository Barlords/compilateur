
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocIS_SUPPIS_SUPP_0R_EQUALSIS_INFIS_INF_OR_EQUALSIS_EQUALSleftPLUSMINUSleftTIMESDIVIDEAND COMMA DECR DIVIDE DIVIDE_EQUALS ELSE EMPTY EQUALS FALSE FOR FUNCTION IF INCR IS_EQUALS IS_INF IS_INF_OR_EQUALS IS_SUPP IS_SUPP_0R_EQUALS LACO LCOMMENT LPAREN MINUS MINUS_EQUALS MINUS_MINUS NAME NULL NUMBER OR PLUS PLUS_EQUALS PLUS_PLUS PRINT QUOT RACO RCOMMENT RETURN RPAREN SEMICOLON SPACE TIMES TIMES_EQUALS TRUE VOID WHILESTART : bloc bloc : bloc statement SEMICOLON\n            | statement SEMICOLON\n            | bloc LCOMMENT comment RCOMMENT\n            | LCOMMENT comment RCOMMENTstatement    : PRINT LPAREN expression RPAREN\n                    | PRINT LPAREN QUOT expression QUOT RPARENcomment  : NAME\n                | NAME SPACE commentstatement : NAME EQUALS expressionstatement    : NAME INCR\n                    | NAME DECRstatement    : NAME PLUS_EQUALS expression\n                    | NAME MINUS_EQUALS expression\n                    | NAME TIMES_EQUALS expression\n                    | NAME DIVIDE_EQUALS expressionexpression   : expression MINUS expression\n\t\t\t        | expression PLUS expression\n\t\t\t\t    | expression TIMES expression\n\t\t\t\t    | expression DIVIDE expressionexpression     : LPAREN expression RPARENexpression   : NUMBER\n                    | NAMEexpression   : TRUE\n                    | FALSEexpression   : expression IS_SUPP expression\n                    | expression IS_SUPP_0R_EQUALS expression\n                    | expression IS_INF expression\n                    | expression IS_INF_OR_EQUALS expression\n                    | expression IS_EQUALS expression\n                    | expression AND expression\n                    | expression OR expressionstatement    : IF LPAREN expression RPAREN LACO bloc RACO\n                    | IF LPAREN expression RPAREN LACO bloc RACO ELSE LACO bloc RACO statement    : WHILE LPAREN expression RPAREN LACO bloc RACOstatement    : FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACO bloc RACOargs     : expression\n                | expression COMMA argsstatement    : FUNCTION NAME LPAREN RPAREN LACO bloc RACO\n                    | FUNCTION NAME LPAREN args RPAREN LACO bloc RACOstatement    : NAME LPAREN RPAREN\n                    | NAME LPAREN args RPAREN'
    
_lr_action_items = {'LCOMMENT':([0,2,13,29,31,52,89,90,92,95,96,98,99,104,108,109,110,111,],[4,12,-3,-2,-5,-4,4,4,4,12,12,12,4,12,4,4,12,12,]),'PRINT':([0,2,13,27,29,31,52,89,90,92,95,96,97,98,99,104,108,109,110,111,],[5,5,-3,5,-2,-5,-4,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'NAME':([0,2,4,10,12,13,16,17,20,21,22,23,24,25,26,27,29,31,32,33,35,51,52,56,57,58,59,60,61,62,63,64,65,66,69,72,89,90,92,95,96,97,98,99,104,108,109,110,111,],[6,6,15,28,15,-3,37,37,37,37,37,37,37,37,37,6,-2,-5,15,37,37,37,-4,37,37,37,37,37,37,37,37,37,37,37,37,37,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'IF':([0,2,13,27,29,31,52,89,90,92,95,96,97,98,99,104,108,109,110,111,],[7,7,-3,7,-2,-5,-4,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'WHILE':([0,2,13,27,29,31,52,89,90,92,95,96,97,98,99,104,108,109,110,111,],[8,8,-3,8,-2,-5,-4,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'FOR':([0,2,13,27,29,31,52,89,90,92,95,96,97,98,99,104,108,109,110,111,],[9,9,-3,9,-2,-5,-4,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'FUNCTION':([0,2,13,27,29,31,52,89,90,92,95,96,97,98,99,104,108,109,110,111,],[10,10,-3,10,-2,-5,-4,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,2,13,29,31,52,],[0,-1,-3,-2,-5,-4,]),'SEMICOLON':([3,11,18,19,36,37,38,39,40,41,42,43,44,45,50,55,68,75,76,77,78,79,80,81,82,83,84,85,86,91,94,100,101,103,107,112,113,],[13,29,-11,-12,-22,-23,-24,-25,-10,-13,-14,-15,-16,-41,72,-6,-42,-21,-17,-18,-19,-20,-26,-27,-28,-29,-30,-31,-32,97,-7,-33,-35,-39,-40,-34,-36,]),'LPAREN':([5,6,7,8,9,16,17,20,21,22,23,24,25,26,28,33,35,51,56,57,58,59,60,61,62,63,64,65,66,69,72,],[16,24,25,26,27,33,33,33,33,33,33,33,33,33,51,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'EQUALS':([6,],[17,]),'INCR':([6,],[18,]),'DECR':([6,],[19,]),'PLUS_EQUALS':([6,],[20,]),'MINUS_EQUALS':([6,],[21,]),'TIMES_EQUALS':([6,],[22,]),'DIVIDE_EQUALS':([6,],[23,]),'RACO':([13,29,31,52,95,96,98,104,110,111,],[-3,-2,-5,-4,100,101,103,107,112,113,]),'RCOMMENT':([14,15,30,53,],[31,-8,52,-9,]),'SPACE':([15,],[32,]),'QUOT':([16,36,37,38,39,67,75,76,77,78,79,80,81,82,83,84,85,86,],[35,-22,-23,-24,-25,87,-21,-17,-18,-19,-20,-26,-27,-28,-29,-30,-31,-32,]),'NUMBER':([16,17,20,21,22,23,24,25,26,33,35,51,56,57,58,59,60,61,62,63,64,65,66,69,72,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'TRUE':([16,17,20,21,22,23,24,25,26,33,35,51,56,57,58,59,60,61,62,63,64,65,66,69,72,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'FALSE':([16,17,20,21,22,23,24,25,26,33,35,51,56,57,58,59,60,61,62,63,64,65,66,69,72,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'RPAREN':([18,19,24,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,51,54,55,68,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,100,101,102,103,107,112,113,],[-11,-12,45,55,-22,-23,-24,-25,-10,-13,-14,-15,-16,-41,68,-37,70,71,73,75,-6,-42,93,-21,-17,-18,-19,-20,-26,-27,-28,-29,-30,-31,-32,94,-38,-7,-33,-35,106,-39,-40,-34,-36,]),'MINUS':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[56,-22,-23,-24,-25,56,56,56,56,56,56,56,56,56,56,-21,-17,-18,-19,-20,56,56,56,56,56,56,56,56,]),'PLUS':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[57,-22,-23,-24,-25,57,57,57,57,57,57,57,57,57,57,-21,-17,-18,-19,-20,57,57,57,57,57,57,57,57,]),'TIMES':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[58,-22,-23,-24,-25,58,58,58,58,58,58,58,58,58,58,-21,58,58,-19,-20,58,58,58,58,58,58,58,58,]),'DIVIDE':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[59,-22,-23,-24,-25,59,59,59,59,59,59,59,59,59,59,-21,59,59,-19,-20,59,59,59,59,59,59,59,59,]),'IS_SUPP':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[60,-22,-23,-24,-25,60,60,60,60,60,60,60,60,60,60,-21,-17,-18,-19,-20,None,None,None,None,None,60,60,60,]),'IS_SUPP_0R_EQUALS':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[61,-22,-23,-24,-25,61,61,61,61,61,61,61,61,61,61,-21,-17,-18,-19,-20,None,None,None,None,None,61,61,61,]),'IS_INF':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[62,-22,-23,-24,-25,62,62,62,62,62,62,62,62,62,62,-21,-17,-18,-19,-20,None,None,None,None,None,62,62,62,]),'IS_INF_OR_EQUALS':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[63,-22,-23,-24,-25,63,63,63,63,63,63,63,63,63,63,-21,-17,-18,-19,-20,None,None,None,None,None,63,63,63,]),'IS_EQUALS':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[64,-22,-23,-24,-25,64,64,64,64,64,64,64,64,64,64,-21,-17,-18,-19,-20,None,None,None,None,None,64,64,64,]),'AND':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[65,-22,-23,-24,-25,65,65,65,65,65,65,65,65,65,65,-21,-17,-18,-19,-20,-26,-27,-28,-29,-30,-31,65,65,]),'OR':([34,36,37,38,39,40,41,42,43,44,47,48,49,54,67,75,76,77,78,79,80,81,82,83,84,85,86,91,],[66,-22,-23,-24,-25,66,66,66,66,66,66,66,66,66,66,-21,-17,-18,-19,-20,-26,-27,-28,-29,-30,-31,-32,66,]),'COMMA':([36,37,38,39,47,75,76,77,78,79,80,81,82,83,84,85,86,],[-22,-23,-24,-25,69,-21,-17,-18,-19,-20,-26,-27,-28,-29,-30,-31,-32,]),'LACO':([70,71,73,93,105,106,],[89,90,92,99,108,109,]),'ELSE':([100,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'START':([0,],[1,]),'bloc':([0,89,90,92,99,108,109,],[2,95,96,98,104,110,111,]),'statement':([0,2,27,89,90,92,95,96,97,98,99,104,108,109,110,111,],[3,11,50,3,3,3,11,11,102,11,3,11,3,3,11,11,]),'comment':([4,12,32,],[14,30,53,]),'expression':([16,17,20,21,22,23,24,25,26,33,35,51,56,57,58,59,60,61,62,63,64,65,66,69,72,],[34,40,41,42,43,44,47,48,49,54,67,47,76,77,78,79,80,81,82,83,84,85,86,47,91,]),'args':([24,51,69,],[46,74,88,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> START","S'",1,None,None,None),
  ('START -> bloc','START',1,'p_start','calcBase.py',113),
  ('bloc -> bloc statement SEMICOLON','bloc',3,'p_bloc','calcBase.py',125),
  ('bloc -> statement SEMICOLON','bloc',2,'p_bloc','calcBase.py',126),
  ('bloc -> bloc LCOMMENT comment RCOMMENT','bloc',4,'p_bloc','calcBase.py',127),
  ('bloc -> LCOMMENT comment RCOMMENT','bloc',3,'p_bloc','calcBase.py',128),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_print','calcBase.py',140),
  ('statement -> PRINT LPAREN QUOT expression QUOT RPAREN','statement',6,'p_statement_print','calcBase.py',141),
  ('comment -> NAME','comment',1,'p_statement_comment','calcBase.py',149),
  ('comment -> NAME SPACE comment','comment',3,'p_statement_comment','calcBase.py',150),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','calcBase.py',154),
  ('statement -> NAME INCR','statement',2,'p_statement_increment_var','calcBase.py',159),
  ('statement -> NAME DECR','statement',2,'p_statement_increment_var','calcBase.py',160),
  ('statement -> NAME PLUS_EQUALS expression','statement',3,'p_statement_modif_var','calcBase.py',165),
  ('statement -> NAME MINUS_EQUALS expression','statement',3,'p_statement_modif_var','calcBase.py',166),
  ('statement -> NAME TIMES_EQUALS expression','statement',3,'p_statement_modif_var','calcBase.py',167),
  ('statement -> NAME DIVIDE_EQUALS expression','statement',3,'p_statement_modif_var','calcBase.py',168),
  ('expression -> expression MINUS expression','expression',3,'p_expression_opperation','calcBase.py',173),
  ('expression -> expression PLUS expression','expression',3,'p_expression_opperation','calcBase.py',174),
  ('expression -> expression TIMES expression','expression',3,'p_expression_opperation','calcBase.py',175),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_opperation','calcBase.py',176),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calcBase.py',181),
  ('expression -> NUMBER','expression',1,'p_expression_number','calcBase.py',186),
  ('expression -> NAME','expression',1,'p_expression_number','calcBase.py',187),
  ('expression -> TRUE','expression',1,'p_expression_bool','calcBase.py',192),
  ('expression -> FALSE','expression',1,'p_expression_bool','calcBase.py',193),
  ('expression -> expression IS_SUPP expression','expression',3,'p_expression_bool_compare','calcBase.py',201),
  ('expression -> expression IS_SUPP_0R_EQUALS expression','expression',3,'p_expression_bool_compare','calcBase.py',202),
  ('expression -> expression IS_INF expression','expression',3,'p_expression_bool_compare','calcBase.py',203),
  ('expression -> expression IS_INF_OR_EQUALS expression','expression',3,'p_expression_bool_compare','calcBase.py',204),
  ('expression -> expression IS_EQUALS expression','expression',3,'p_expression_bool_compare','calcBase.py',205),
  ('expression -> expression AND expression','expression',3,'p_expression_bool_compare','calcBase.py',206),
  ('expression -> expression OR expression','expression',3,'p_expression_bool_compare','calcBase.py',207),
  ('statement -> IF LPAREN expression RPAREN LACO bloc RACO','statement',7,'p_statement_if','calcBase.py',212),
  ('statement -> IF LPAREN expression RPAREN LACO bloc RACO ELSE LACO bloc RACO','statement',11,'p_statement_if','calcBase.py',213),
  ('statement -> WHILE LPAREN expression RPAREN LACO bloc RACO','statement',7,'p_statement_while','calcBase.py',221),
  ('statement -> FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACO bloc RACO','statement',11,'p_statement_for','calcBase.py',226),
  ('args -> expression','args',1,'p_args','calcBase.py',231),
  ('args -> expression COMMA args','args',3,'p_args','calcBase.py',232),
  ('statement -> FUNCTION NAME LPAREN RPAREN LACO bloc RACO','statement',7,'p_statement_declare_func','calcBase.py',240),
  ('statement -> FUNCTION NAME LPAREN args RPAREN LACO bloc RACO','statement',8,'p_statement_declare_func','calcBase.py',241),
  ('statement -> NAME LPAREN RPAREN','statement',3,'p_statement_call_func','calcBase.py',251),
  ('statement -> NAME LPAREN args RPAREN','statement',4,'p_statement_call_func','calcBase.py',252),
]
