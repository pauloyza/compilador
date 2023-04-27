from laboratorio2 import tokens
import ply.yacc as yacc

def p_expression_begin(p):
    'expression : BEGIN'

def p_expression_plus(p):
    'expression : expression "+" term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression "-" term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term "*" factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term "/" factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : "(" expression ")"'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

data2 = '''
3 + 4
'''

while True:
   try:
       s = input('calc >m ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

print(yacc.parse(data2))