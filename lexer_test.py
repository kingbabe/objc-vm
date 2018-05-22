import compiler.lexer
from ply import lex

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

while 1:
    tok = lex.token()
    if not tok: break
    print tok