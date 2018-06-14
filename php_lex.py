import ply.lex as lex

# tokens
tokens = [
    'ESPACIO',
    'COMILLA_DOBLE',
    'MULTIPLICACION',
    'SUMA',
    'RESTA',
    'DIVISION',
    'IGUAL',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MENOR_IGUAL_QUE',
    'MAYOR_IGUAL_QUE',
    'OP_AND',
    'OP_OR',
    'IGUAL',
    'IDENTICO',
    'DIFERENTE',
    'DIFERENT',
    'NO_IDENTICO',
    'NAVE_ESPACIAL',
    'FUSION_NULL',
    'INCREMENTO',
    'DECREMENTO',
    'NOT',
    'ID'
]

reserved = {
    '__halt_compiler':"__HALT_COMPILER",
    'abstract': "ABSTRACT",
    'and': "AND",
	'array': "ARRAY",
	'as': "AS",
	'break': "BREAK", 
	'callable': "CALLABLE", 
	'case': "CASE", 
	'catch' : "CATCH", 
	'class' : "CLASS", 
	'clone' : "CLONE", 
	'const' : "CONST", 
	'continue' : "CONTINUE", 
	'declare' : "DECLARE", 
	'default' : "DEFAULT", 
	'die' : "DIE", 
	'do' : "DO", 
	'echo' : "ECHO", 
	'else' : "ELSE", 
	'elseif' : "ELSEIF", 
	'empty' : "EMPTY", 
	'enddeclare' : "ENDDECLARE", 
	'endfor' : "ENDFOR", 
	'endforeach' : "ENDFOREACH", 
	'endif' : "ENDIF", 
	'endswitch' : "ENDSWITCH", 
	'endwhile' : "ENDWHILE", 
	'eval' : "EVAL", 
	'exit' : "EXIT", 
	'extends' : "EXTENDS", 
	'final' : "FINAL", 
	'for' : "FOR", 
	'foreach' : "FOREACH", 
	'function' : "FUNCTION", 
	'global' : "GLOBAL", 
	'goto' : "GOTO", 
	'if' : "IF", 
	'implements' : "IMPLEMENTS", 
	'include' : "INCLUDE", 
	'include_once' : "INCLUDE ONCE", 
	'instanceof' : "INSTANCEOF",
	'insteadof' : "INSTEADOF",
	'interface' : "INTERFACE",
	'isset' : "ISSET",
	'list' : "LIST",
	'namespace' : "NAMESPACE",
	'new' : "NEW",
	'or' : "OR",
	'print' : "PRINT",
	'private' : "PRIVATE",
	'protected' : "PROTECTED",
	'public' : "PUBLIC",
	'require' : "REQUIRE",
	'require_once' : "REQUIRE ONCE",
	'return' : "RETURN", 
	'static' : "STATIC", 
	'switch' : "SWITCH", 
	'throw' : "THROW", 
	'trait' : "TRAIT", 
	'try' : "TRY", 
	'unset' : "UNSET", 
	'use' : "USE", 
	'var' : "VAR", 
	'while' : "WHILE", 
	'xor' : "XOR"
}

def t_ID(t):
    r'[a-zA-Z]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t___HALT_COMPILER(t):
    r'__halt_compiler'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_AND(t):
    r'and|AND|\&\&'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_AS(t):
    r'as'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CALLABLE(t):
    r'callable'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t