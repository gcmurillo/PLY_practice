import ply.lex as lex

# tokens
tokens = [ 
    'COMILLA_DOBLE',
    'MULTIPLICACION',
    'SUMA',
    'RESTA',
    'DIVISION',
    'IDENTICO',
	'IGUAL',
    'ASIGNACION',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MENOR_IGUAL_QUE',
    'MAYOR_IGUAL_QUE',
    'OP_AND',
    'OP_OR',
    'DIFERENTE',
    'DIFERENT',
    'NO_IDENTICO',
    'NAVE_ESPACIAL',
    'FUSION_NULL',
    'INCREMENTO',
    'DECREMENTO',
    'NOT',
    'PARENTESIS_DER',
    'PARENTESIS_IZQ',
    'LLAVE_DER',
    'LLAVE_IZQ',
    'COMENTARIO',
    'CORCHETE_DER',
    'CORCHETE_IZQ',
    'NUMERO',
    'COMA',
    'PUNTO_COMA',
    'DOS_PUNTOS',
    'PUNTO',
	'NOMBRE'
]

reserved = {
	'and': "AND",
	'break': "BREAK", 
	'case': "CASE", 
	'catch' : "CATCH", 
	'clone' : "CLONE", 
	'const' : "CONST", 
	'continue' : "CONTINUE", 
	'default' : "DEFAULT",
	'do' : "DO", 
	'if' : "IF",
	'echo' : "ECHO", 
	'else' : "ELSE", 
	'elseif' : "ELSEIF", 
	'empty' : "EMPTY", 
	'enddeclare' : "ENDDECLARE", 
	'endfor' : "ENDFOR", 
	'endforeach' : "ENDFOREACH",
	'endif' : "ENDIF", 
	'endswitch' : "ENDSWITCH", 
	'while' : "WHILE",
	'endwhile' : "ENDWHILE",
	'exit' : "EXIT",  
	'final' : "FINAL", 
	'for' : "FOR", 
	'foreach' : "FOREACH",  
	'global' : "GLOBAL", 
	'goto' : "GOTO", 
	'list':"LIST",
	'new' : "NEW",
	'or' : "OR",
	'print' : "PRINT",
	'return' : "RETURN",
	'switch' : "SWITCH",
	'try' : "TRY",
	'xor' : "XOR",
	'list': 'LIST'
}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
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
t_ignore  = r' '
t_NOMBRE = r'\$[a-z]\w*'
t_COMA = r','


def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)    
	return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Caracter incorrecto '%s'" % t.value[0])
    t.lexer.skip(1)

'''def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value in reserved:
		t.type = reserved[t.value]
	return t
<<<<<<< HEAD
=======
'''
>>>>>>> 6571146c6ba0ebaae6c43aa330bd41b445b03443

# Error handling rule

lexer = lex.lex()
<<<<<<< HEAD
'''
data = """
	while ($i <= 10) {
    echo $i++;
}
"""
=======
data = input("ingresar una expresion de php")
>>>>>>> 6571146c6ba0ebaae6c43aa330bd41b445b03443

lexer.input(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)
'''