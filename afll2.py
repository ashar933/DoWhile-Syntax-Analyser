import ply.lex as lex
import ply.yacc as yacc


tokens = ['next', 'do', 'while', 'openCurl', 'closeCurl', 'condition', 'statements', 'openBrack', 'closeBrack', 'semicolon']
t_ignore = ' \t';
t_next = ' \\n';
t_do = r'do';
t_while = r'while';
t_openCurl = r'\{';
t_closeCurl = r'\}';
t_condition = r'condition';
t_statements = r'statements';
t_openBrack = r'\(';
t_closeBrack = r'\)';
t_semicolon = r';';

def p_do(p):
    '''assign : do expr'''
    print("Correct Syntax!");

def p_expr(p):
    '''expr : statementsub next
            | statementsub
            '''

def p_statementsub(p):
    '''statementsub : openCurl next statements semicolon next closeCurl whilesub
                    '''

def p_while(p):
    '''whilesub : while conditionsub semicolon'''

def p_conditionsub(p):
    '''conditionsub : openBrack condition closeBrack'''

def p_error(p):
    print("Wrong Syntax!");

def t_error(p):
    print("Wrong Syntax1");

lex.lex();
yacc.yacc();

data = '''do{
    statements;
}while(condition)
'''

yacc.parse(data)