
import ply.yacc as yacc
import php_lex
tokens = php_lex.tokens

def p_assign(p):
    '''assign : NOMBRE ASIGNACION expr'''

def p_expr(p):
    '''expr : expr SUMA term
            | expr RESTA term
            | term '''

def p_term(p):
    '''term : term MULTIPLICACION factor
            | term DIVISION factor
            | factor '''

def p_factor(p):
    ''' factor : NUMERO '''

parser = yacc.yacc()