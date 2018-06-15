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
    'ASIGNACION',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MENOR_IGUAL_QUE',
    'MAYOR_IGUAL_QUE',
    'OP_AND',
    'OP_OR',
    'IDENTICO',
    'DIFERENTE',
    'DIFERENT',
    'NO_IDENTICO',
    'NAVE_ESPACIAL',
    'FUSION_NULL',
    'INCREMENTO',
    'DECREMENTO',
    'NOT',
    'ID',
    'PARENTESIS_DER',
    'PARENTESIS_IZQ',
    'LLAVE_DER',
    'LLAVE_IZQ',
    'COMENTARIO',
    'CORCHETE_DER',
    'CORCHETE_IZQ',
    'NUMERO',
    'PUNTO_COMA',
    'DOS_PUNTOS',
    'PUNTO'
]

reserved = {
    'abstract': 'ABSTRACT',
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

def Milexer():
	
	t_SUMA    = r'\+'
	t_RESTA   = r'-'
	t_DIVISION  = r'/'
	t_MULTIPLICACION = r'\*'
	t_PARENTESIS_IZQ  = r'\('
	t_PARENTESIS_DER  = r'\)'
	t_LLAVE_DER = r'\}'
    t_LLAVE_IZQ = r'\{'
    t_COMENTARIO = r'\\\\'
    t_CORCHETE_DER = r'\]'
    t_CORCHETE_IZQ = r'\['
    t_ASIGNACION = r'='
    t_COMILLA_DOBLE = r'"'
    t_MAYOR_QUE = r'>'
    t_MENOR_QUE = r'<'
    t_MENOR_IGUAL_QUE = r'<='
    t_MAYOR_IGUAL_QUE = r'>='
    t_OP_AND = r'&&'
    t_OP_OR = r'\|\|'
    t_IGUAL = r'=='
    t_IDENTICO = r'==='
    t_DIFERENTE = r'!='
    t_DIFERENT = r'<>'
    t_NO_IDENTICO = r'!=='
    t_NAVE_ESPACIAL = r'<=>'
    t_FUSION_NULL = r'\?\?'
    t_INCREMENTO = r'\+\+'
    t_DECREMENTO = r'--'
    t_NOT = r'!'
    t_PUNTO_COMA = r';'
    t_DOS_PUNTOS = r':'
    t_PUNTO = r'\.'
    t_ignore  = ' \t'
	def t_ID(t):
	    r'^\$[a-zA-Z]*'
	    t.type = reserved.get(t.value, 'ID')
	    return t
	def t_NUMERO(t):
		r'\d+'
		t.value = int(t.value)    
    	return t
