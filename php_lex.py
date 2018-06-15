import ply.lex as lex

# tokens
tokens = [
    'ESPACIO',
    'COMILLA_DOBLE',
    'SUMA',
    'RESTA',
    'DIVISION',
    'IGUAL',
    'VECES',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MENOR_IGUAL_QUE',
    'MAYOR_IGUAL_QUE',
    'PARENTESI_ABIERTO',
    'PARENTESI_CERRADO',
    'LLAVE_ABIERTA',
    'LLAVE CERRADA',
    'CORCHETE_ABIERTO',
    'CORCHETE CERRADO',
    'NOT',
    'ID'
]


t_SUMA = r'\+'
t_RESTA = r'-'
t_VECES = r'\*'
t_DIVISION  = r'/'
t_IGUAL = r'='
t_DIFERENTE = r'!'
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_COMILLA_DOBLE = r'\"'
t_PARENTESI_ABIERTO = r'\('
t_PARENTESI_CERRADO = r'\)'
t_CORCHETE_ABIERTO  = r'\['
t_CORCHETE_CERRADO = r'\]'
t_LLAVE_CERRADA = r'{'
t_LLAVE_ABIERTA = r'}'







def t_MENOR_IGUAL_QUE(t):
    r'<='
    return t

def t_MAYOR_IGUAL_QUE(t):
    r'>='
    return t



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


