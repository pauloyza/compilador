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
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'ID'
] + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

#others expressions


# A regular expression rule with some action code
def t_NUMBER(t):
    r'([0-9]*\.)*[0-9]+'
    t.value = float(t.value)    
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
3.2 +4 * 10 paulo
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
