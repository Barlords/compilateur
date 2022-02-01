# -----------------------------------------------------------------------------
# calc.py
#
# Expressions arithmétiques sans variables
# -----------------------------------------------------------------------------

from genereTreeGraphviz import printTreeGraph

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'IS_SUPP', 'IS_SUPP_0R_EQUALS', 'IS_INF', 'IS_INF_OR_EQUALS', 'IS_EQUALS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
    )

reserved = {
    'fonction' : 'FUNCTION',
    'print' : 'PRINT',
    'printString' : 'PRINT_STR',
    'empty' : 'EMPTY',
    'while' : 'WHILE',
    'for' : 'FOR',
    'if' : 'IF',
    'else' : 'ELSE',
    'void' : 'VOID',
    'null' : 'NULL',
    'return' : 'RETURN'
}

names = dict()
functions = dict()

tokens = [
    'NUMBER', 'NAME', 'STRING',
    'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'PLUS_PLUS', 'MINUS_MINUS',
    'LPAREN', 'RPAREN', 'LACO', 'RACO', 'QUOT', 'COMMA',
    'AND', 'OR', 'TRUE', 'FALSE',
    'SEMICOLON',
    'INCR', 'DECR',
    'MINUS_EQUALS', 'PLUS_EQUALS', 'TIMES_EQUALS', 'DIVIDE_EQUALS',
    'IS_SUPP', 'IS_SUPP_0R_EQUALS', 'IS_INF', 'IS_INF_OR_EQUALS', 'IS_EQUALS',

] + list(reserved.values())

# Tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_INCR = r'\+\+'
t_DECR = r'--'
t_MINUS_EQUALS = r'-='
t_PLUS_EQUALS = r'\+='
t_TIMES_EQUALS = r'\*='
t_DIVIDE_EQUALS = r'/='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LACO = r'\{'
t_RACO = r'\}'
t_QUOT = r'\"'
t_COMMA = r','
t_AND = r'&'
t_OR = r'\|'
t_TRUE = r'T'
t_FALSE = r'F'
t_SEMICOLON = r';'
t_IS_SUPP = r'>'
t_IS_SUPP_0R_EQUALS = r'>='
t_IS_INF = r'<'
t_IS_INF_OR_EQUALS = r'<='
t_IS_EQUALS = r'=='

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'STRING')
    return t

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lex.lex()

def p_start(p):
    '''START : bloc '''
    p[0] = ('START', p[1])
    print('Arbre de dérivation = ', p[0])
    printTreeGraph(p[0])
    evalInst(p[1])

def p_bloc(p):
    '''bloc : bloc statement SEMICOLON
            | statement SEMICOLON'''
    if len(p) == 4:
        p[0] = ('bloc', p[1], p[2])
    else:
        p[0] = ('bloc', p[1], 'empty')

def p_statement_print(p):
    '''statement : PRINT LPAREN expression RPAREN'''
    p[0] = ('print',p[3])

def p_statement_printString(p):
    '''statement : PRINT_STR LPAREN QUOT STRING QUOT RPAREN'''
    p[0] = ('print',p[4])

def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    p[0] = ('assign', p[1], p[3])


def p_statement_increment_var(p):
    '''statement : NAME INCR
                | NAME DECR'''
    p[0] = (p[2], p[1])

def p_statement_modif_var(p):
    '''statement : NAME PLUS_EQUALS expression
                | NAME MINUS_EQUALS expression
                | NAME TIMES_EQUALS expression
                | NAME DIVIDE_EQUALS expression'''
    p[0] = (p[2], p[1], p[3])


def p_expression_opperation(p):
    '''expression : expression MINUS expression
				| expression PLUS expression
				| expression TIMES expression
				| expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER
                | NAME'''
    p[0] = p[1]

def p_expression_bool(p):
    '''expression : TRUE
                | FALSE'''
    if p[1] == 'T':
        p[0] = True
    elif p[1] == 'F':
        p[0] = False

def p_expression_bool_compare(p):
    '''expression : expression IS_SUPP expression
                | expression IS_SUPP_0R_EQUALS expression
                | expression IS_INF expression
                | expression IS_INF_OR_EQUALS expression
                | expression IS_EQUALS expression
                | expression AND expression
                | expression OR expression'''
    p[0] = (p[2], p[1], p[3])

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN LACO bloc RACO
            | IF LPAREN expression RPAREN LACO bloc RACO ELSE LACO bloc RACO '''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if', p[3], p[6], ('else', p[10]))

def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN LACO bloc RACO'''
    p[0] = ('while', p[3], p[6])

def p_statement_for(p):
    '''statement : FOR LPAREN statement SEMICOLON expression SEMICOLON statement RPAREN LACO bloc RACO'''
    p[0] = ('for', p[3], p[5], p[7], p[10])

def p_args(p):
    '''args : expression
            | expression COMMA args'''
    if len(p) == 2:
        p[0] = ('param', p[1])
    else:
        p[0] = ('param', p[3], p[1])

def p_statement_declare_func(p):
    '''statement : FUNCTION NAME LPAREN RPAREN LACO bloc RACO
                | FUNCTION NAME LPAREN args RPAREN LACO bloc RACO'''
    if len(p) == 8:
        p[0] = ('function', (p[2], ('param', 'empty'), p[6]))
    else:
        p[0] = ('function', (p[2], p[4], p[7]))



def p_error(p):
    print("Syntax error at '%s'" % p.value)


import ply.yacc as yacc

yacc.yacc()


def evalExpr(t):
    #print('evalExpr')

    if type(t) is int : return t
    if type(t) is str : return names[t]
    if t[0] == '+':
        return evalExpr(t[1]) + evalExpr(t[2])
    if t[0] == '-':
        return evalExpr(t[1]) - evalExpr(t[2])
    if t[0] == '*':
        return evalExpr(t[1]) * evalExpr(t[2])
    if t[0] == '/':
        return evalExpr(t[1]) / evalExpr(t[2])


    if t[0] == '>':
        return evalExpr(t[1]) > evalExpr(t[2])
    if t[0] == '>=':
        return evalExpr(t[1]) >= evalExpr(t[2])
    if t[0] == '<':
        return evalExpr(t[1]) < evalExpr(t[2])
    if t[0] == '<=':
        return evalExpr(t[1]) <= evalExpr(t[2])
    if t[0] == '==':
        return evalExpr(t[1]) == evalExpr(t[2])

    if t[0] == '&':
        return evalExpr(t[1]) and evalExpr(t[2])
    if t[0] == '|':
        return evalExpr(t[1]) or evalExpr(t[2])



    return 'UNK'

def evalInst(t):
    #print('evalInst')
    if t == 'empty':
        return
    if t[0] == 'print':
        print(evalExpr(t[1]))
    if t[0] == 'bloc':
        evalInst(t[1])
        evalInst(t[2])

    if t[0] == 'if':
        if evalExpr(t[1]):
            evalInst(t[2])
        elif len(t) == 4:
            evalInst(t[3])
    if t[0] == 'while':
        while evalExpr(t[1]):
            evalInst(t[2])
    if t[0] == 'for':
        evalInst(t[1])
        while evalExpr(t[2]):
            evalInst(t[4])
            evalInst(t[3])

    if t[0] == 'assign':
        names[t[1]] = evalExpr(t[2])
    if t[0] == '++':
        names[t[1]] += 1
    if t[0] == '--':
        names[t[1]] -= 1
    if t[0] == '+=':
        names[t[1]] += evalExpr(t[2])
    if t[0] == '-=':
        names[t[1]] -= evalExpr(t[2])
    if t[0] == '*=':
        names[t[1]] *= evalExpr(t[2])
    if t[0] == '/=':
        names[t[1]] /= evalExpr(t[2])

    return t

s = 'print(7+3*4/(10-8)*3);' \
    'test=5;' \
    'while(test>0){' \
    '   test-=2;' \
    '   print(test);' \
    '};' \
    'for(i=0;i<10;i++){' \
    '   print(i);' \
    '};'
yacc.parse(s)