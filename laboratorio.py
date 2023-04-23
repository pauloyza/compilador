import ply.lex as lex
#import re

reserved = {
    
    'if'    : 'IF',
    'then'  : 'THEN',
    'while' : 'WHILE',
    'type'  : 'TIPO',
    'begin' : 'BEGIN',
    'end'   : 'END',
    'const' : 'CONSTANTE',
    'var'   : 'VARIAVEL',
    'integer': 'INTEGER',
    'real'  : 'REAL',
    'array' : 'ARRAY',
    'record': 'RECORD',
    'write' : 'WRITE',
    'read'  : 'READ',
    'else'  : 'ELSE',
    'of'    : 'OF',
    'function': 'FUNCAO'



}
tokens = [
   'NUMBER',
   'DECIMER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'LJACARE',
   'RJACARE',
   'EQUAL',
   'ATRIBUTION',
   'EXCLA',
   'DOT',
   'COMMA',
   'DOTCOMMA',
   'DOTDOT',
   'LCOL',
   'RCOL',
   'QUOTATION',
   'ID'
] + list(reserved.values())

literals = '+-*/><=!.,;:[]()"'



 
# Regular expression rules for simple tokens
#t_PLUS    = r'\+'
#t_MINUS   = r'-'
#t_TIMES   = r'\*'
#t_DIVIDE  = r'/'
#t_LPAREN  = r'\('
#t_RPAREN  = r'\)'

#programming the literals:
def t_PLUS(t):
    r'\+'
    t.type = '+'
    return t

def t_MINUS(t):
    r'-'
    t.type = '-'
    return t

def t_TIMES(t):
    r'\*'
    t.type = '*'
    return t

def t_DIVIDE(t):
    r'/'
    t.type = '/'
    return t

def t_LPAREN(t):
    r'\('
    t.type = '('
    return t

def t_RPAREN(t):
    r'\)'
    t.type = ')'
    return t

def t_LJACARE(t):
    r'\<'
    t.type = '<'
    return t

def t_RJACARE(t):
    r'\>'
    t.type = '>'
    return t

def t_EQUAL(t):
    r'\=='
    t.value = '=='
    return t

def t_ATRIBUTION(t):
    r'\='
    t.type = '='
    return t

def t_EXLA(t):
    r'\!'
    t.type = '!'
    return t



def t_COMMA(t):
    r'\,'
    t.type = ','
    return t

def t_DOTCOMMA(t):
    r'\;'
    t.type = ';'
    return t

def t_DOTDOT(t):
    r'\:'
    t.type = ':'
    return t

def t_LCOL(t):
    r'\['
    t.type = '['
    return t

def t_RCOL(t):
    r'\]'
    t.type = ']'
    return t

def t_QUOTATION(t):
    r'\"'
    t.type = '"'
    return t

#Ignore comments
def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# A regular expression rule with some action code

def t_DECIMER(t):
    r'([0-9]*\.)[0-9]+'
    t.value = float(t.value)    
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)    
    return t



def t_DOT(t):
    r'\.'
    t.type = '.'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
#comentário
(3.2 +4) * 10  if paulo = == 3.2.4
  + -20 *2
'''

#test literals
lit = '''
+-*/><=!.,;:[]()"
'''


def leiaArq(textao):
    arq = open(textao, "r", encoding="utf-8")
    linhas = arq.readlines()
    datareal = ""
    for linha in linhas:
        datareal += linha 
    return datareal   

# Give the lexer some input
#lexer.input(datareal)

#Leitura Principal
lexer.input(leiaArq("gram01.txt"))

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)



