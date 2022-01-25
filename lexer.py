# List of token names.   This is always required
import ply.lex as lex

tokens = [
    'INT', 'FLOAT',  # Numbers
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',  # operations
    'MODULO',
    'POWER',
    # Parentheses and brackets and braces
    'ID',
    'STRING',
    'EQUALS',  # delimiters
    'INCREMENTATION', 'DECREMENTATION',
    'SUP', 'INF', 'EQUALSCOMP', 'INFEQUALS', 'SUPEQUALS', 'DIFFERENT',  # comparison ops
]

reserved = {
    'chhapo': 'CHHAPO',  # print
    'athva': 'ATHVA',  # else
    'jya': 'JYA',  # while
    'khotu': 'KHOTU',  # false
    'jo': 'JO',  # if
    'ane': 'ANE',  # and
    'ya': 'YA',  # or
    'sachu': 'SACHU',  # true
    'bahar': 'BAHAR',  # break
    'walo': 'WALO',  # None
    'mahiti': 'MAHITI',  # input
    'chalu': 'CHALU',  # continue
    'kro': 'KRO',  # do
    'prayas': 'PRAYAS',  # try
    'sivay': 'SIVAY',  # except
    'akhiran': 'AKHIRAN',  # finally
    'mate': 'MATE',  # for
    'nahi': 'NAHI',  # not
    'mojod':  'MOJOD',  # global
    'moklo': 'MOKLO',  # return
    'banavo': 'BANAVO',  # function
    # array ta3riftions
    'kul': 'KUL',  # len
    'jodo': 'JODO',  # append
    'kber': 'KBER',  # extend
    'hatavo': 'HATAVO',  # pop
    'dkhel': 'DKHEL',  # insert
    'khwi': 'KHWI',  # clear
    # other fuctions, example

}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_EQUALSCOMP = r'\=\='
t_DIFFERENT = r'\!\='
t_MODULO = r'\%'
t_POWER = r'\^'
t_SUP = r'\>'
t_INF = r'\<'
t_INFEQUALS = r'\<\='
t_SUPEQUALS = r'\>\='
t_INCREMENTATION = r'\+\+'
t_DECREMENTATION = r'--'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'\='
literals = [',', '[', ']', '{', '}', '(', ')', '+', ';', '.', ':']


def t_COMMENT(t):
    r'\#.*'

    # A regular expression rule with some action code


def t_STRING(t):
    # [^"] : means any character except ", this way "hello" + "there" wont be considered a "String" but "string" + "string"
    r'("[^"]*")|(\'[^\']*\')'
    if t.value[0] == '"':
        t.value = t.value[1:-1]
    elif t.value[0] == "'":
        t.value = t.value[1:-1]
    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_S7I7(t):
    r's7i7'
    t.value = True
    return t


def t_KHATE2(t):
    r'khate2'
    t.value = False
    return t


def t_WALO(t):
    r'walo'
    t.value = None
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

    # Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


    # A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_error(t):
    print("F ster : ", t.lineno)
    print("Kayn mouchkil fhad ramz: %s" % t.value[0])
    exit()


lexer = lex.lex()
