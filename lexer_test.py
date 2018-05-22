import compiler.lexer
import compiler.semantic
from ply import lex, yacc

lex.lex(module=compiler.lexer)
a = '''
#import "aaa.h"
@class ViewController;
@"aa\\naaaa"
0xffffff;
acc >> bcc
a < b
'''
print(a)
lex.input(a)
parser = yacc.yacc(module=compiler.semantic)

while 1:
    tok = lex.token()
    if not tok: break
    print tok

