import math


TOKENS = (
    'NAME',
    'NUMBER_INT', 'NUMBER_DOUBLE',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'COLON'

)
Y_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


Y_COLON = r','
Y_EQUALS = r'='
Y_PLUS = r'\+'
Y_MINUS = r'-'
Y_TIMES = r'\*'
Y_DIVIDE = r'/'
Y_IGNORE = ' \t'


def y_NUMBER_DOUBLE(y):
    r'\d+\.\d+'
    try:
        y.value = float(y.value)
    except ValueError:
        print('Integer value too large %d', y.value)
        y.value = 0
    return y


def y_NUMBER_INT(y):
    r'\d+'
    try:
        y.value = int(y.value)
    except ValueError:
        print('Integer value too large %d', y.value)
        y.value = 0
    return y


def y_newline(y):
    r'\n+'
    y.lexer.lineno += y.value.count('\n')


def y_error(y):
    print('Illegal character \'%s\'' % y.value[0])
    y.lexer.skip(1)


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

variables = {
    'pi': math.pi,
    'e': math.e,
}
start = 'statement'


def p_statement_assign(y):
    '''
    statement : NAME EQUALS expression
    '''
    variables[y[1]] = y[3]


def p_statement_expression(y):
    '''
    statement : expression
    '''
    print(y[1])


def p_expression_binop(y):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression DIVIDE expression
               | expression TIMES expression
    '''
    if y[2] == '+':
        y[0] = y[1] + y[3]
    elif y[2] == '-':
        y[0] = y[1] - y[3]
    elif y[2] == '*':
        y[0] = y[1] * y[3]
    elif y[2] == '/':
        y[0] = y[1] / y[3]


def p_expression_uminus(y):
    '''
    expression : MINUS expression %prec UMINUS
    '''
    y[0] = -y[2]


def p_expression_group(y):
    '''
    expression : LPAREN expression RPAREN
    '''
    y[0] = y[2]


def p_expressions(y):
    '''
    expressions : expressions COLON expression
               | expression
               |
    '''
    if len(y) == 0:
        y[0] = None
        return
    y[0] = [y[1]] if len(y) == 2 else y[1] + [y[3]]


def p_expression_function(y):
    '''
        expressions : angle expression
                   | expression
                   |
        '''
    if y[1] == 'sin':
        if len(y[3]) == 1:
            y[0] = math.sin(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'cos':
        if len(y[3]) == 1:
            y[0] = math.cos(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'log':
        if len(y[3]) == 1:
            y[0] = math.log(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'log10':
        if len(y[3]) == 1:
            y[0] = math.log10(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'log2':
        if len(y[3]) == 1:
            y[0] = math.log2(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'exp':
        if len(y[3]) == 1:
            y[0] = math.exp(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return




    elif y[1] == 'sqrt':
        if len(y[3]) == 1:
            y[0] = math.sqrt(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'acos':
        if len(y[3]) == 1:
            y[0] = math.acos(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'atan':
        if len(y[3]) == 1:
            y[0] = math.atan(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'radians':
        if len(y[3]) == 1:
            y[0] = math.radians(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'sinh':
        if len(y[3]) == 1:
            y[0] = math.sinh(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'cosh':
        if len(y[3]) == 1:
            y[0] = math.cosh(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'tanh':
        if len(y[3]) == 1:
            y[0] = math.tanh(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'asin':
        if len(y[3]) == 1:
            y[0] = math.asin(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return



    elif y[1] == 'ceil':
        if len(y[3]) == 1:
            y[0] = math.ceil(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'fabs':
        if len(y[3]) == 1:
            y[0] = math.fabs(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'factorial':
        if len(y[3]) == 1:
            y[0] = math.factorial(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'floor':
        if len(y[3]) == 1:
            y[0] = math.floor(float(y[3][0]))
        else:
            print('%s() function need one arguments' % y[1])
        return
    elif y[1] == 'copysign':
        if len(y[3]) == 2:
            y[0] = math.copysign(int(y[3][0]), int(y[3][1]))
        else:
            print('%s() function need two arguments' % y[1])
        return
    elif y[1] == 'pow':
        if len(y[3]) == 2:
            y[0] = math.pow(int(y[3][0]), int(y[3][1]))
        else:
            print('%s() function need two arguments' % y[1])
        return
    print('Undefined function \'%s\'' % y[1])
    y[0] = None


def p_expression_number(y):
    '''
    expression : NUMBER_INT
               | NUMBER_DOUBLE
    '''
    y[0] = y[1]


def p_expression_name(y):
    '''
    expression : NAME
    '''
    try:
        y[0] = variables[y[1]]
    except LookupError:
        print('Undefined name \'%s\'' % y[1])
        y[0] = None


def p_error(y):
    print('Syntax error at \'%s\'' % y.value)



while True:
    try:
        S = input('> ')
    except EOFError:
        break
