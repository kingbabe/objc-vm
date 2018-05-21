%{
#import <Foundation/NSData.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

extern char _VCurrentIdentifier[512];

void comment();
int check_type();
void _VSetDataToScan(NSData *someData);
extern BOOL _VIsKnownTypeName(const char *aTypeName);

static const char * _VCurrentDataBytes = NULL;
static NSData *_VCurrentData = nil;
static int _VCurrentDataBytesIndex = 0;

#ifdef _WIN32

/* Windows doesn't define the isatty() function.
  As we always read from a file, we can easily
  provide the following simple implementation: */

int isatty (int fd)
{
    return 0;
}
#endif

%}

D                      [0-9]
L                      [a-zA-Z_]
H                      [a-fA-F0-9]
E                      [Ee][+-]?{D}+
FS                      (f|F|l|L)
IS                      (u|U|l|L)*

%{
#include <stdio.h>
#include "y.tab.h"

void count();
%}

%%
"/*"                    { comment(); }

"auto"                  { count(); return(AUTO); }
"break"                { count(); return(BREAK); }
"case"                  { count(); return(CASE); }
"char"                  { count(); return(CHAR); }
"const"                { count(); return(CONST); }
"continue"              { count(); return(CONTINUE); }
"default"              { count(); return(DEFAULT); }
"do"                    { count(); return(DO); }
"double"                { count(); return(DOUBLE); }
"else"                  { count(); return(ELSE); }
"enum"                  { count(); return(ENUM); }
"extern"                { count(); return(EXTERN); }
"float"                { count(); return(FLOAT); }
"for"                  { count(); return(FOR); }
"goto"                  { count(); return(GOTO); }
"if"                    { count(); return(IF); }
"int"                  { count(); return(INT); }
"long"                  { count(); return(LONG); }
"register"              { count(); return(REGISTER); }
"return"                { count(); return(RETURN); }
"short"                { count(); return(SHORT); }
"signed"                { count(); return(SIGNED); }
"sizeof"                { count(); return(SIZEOF); }
"static"                { count(); return(STATIC); }
"struct"                { count(); return(STRUCT); }
"switch"                { count(); return(SWITCH); }
"typedef"              { count(); return(TYPEDEF); }
"union"                { count(); return(UNION); }
"unsigned"              { count(); return(UNSIGNED); }
"void"                  { count(); return(VOID); }
"volatile"              { count(); return(VOLATILE); }
"while"                { count(); return(WHILE); }
"__declspec"  { count(); return(DECLSPEC); }
"dllimport"  { count(); return(DLLIMPORT); }
"dllexport"  { count(); return(DLLEXPORT); }

{L}({L}|{D})*          { count(); return(check_type()); }

0[xX]{H}+{IS}?          { count(); return(CONSTANT); }
0{D}+{IS}?              { count(); return(CONSTANT); }
{D}+{IS}?              { count(); return(CONSTANT); }
L?'(\\.|[^\\'])+'      { count(); return(CONSTANT); }

{D}+{E}{FS}?            { count(); return(CONSTANT); }
{D}*"."{D}+({E})?{FS}?  { count(); return(CONSTANT); }
{D}+"."{D}*({E})?{FS}?  { count(); return(CONSTANT); }

L?\"(\\.|[^\\"])*\"    { count(); return(STRING_LITERAL); }

"..."                  { count(); return(ELLIPSIS); }
">>="                  { count(); return(RIGHT_ASSIGN); }
"<<="                  { count(); return(LEFT_ASSIGN); }
"+="                    { count(); return(ADD_ASSIGN); }
"-="                    { count(); return(SUB_ASSIGN); }
"*="                    { count(); return(MUL_ASSIGN); }
"/="                    { count(); return(DIV_ASSIGN); }
"%="                    { count(); return(MOD_ASSIGN); }
"&="                    { count(); return(AND_ASSIGN); }
"^="                    { count(); return(XOR_ASSIGN); }
"|="                    { count(); return(OR_ASSIGN); }
">>"                    { count(); return(RIGHT_OP); }
"<<"                    { count(); return(LEFT_OP); }
"++"                    { count(); return(INC_OP); }
"--"                    { count(); return(DEC_OP); }
"->"                    { count(); return(PTR_OP); }
"&&"                    { count(); return(AND_OP); }
"||"                    { count(); return(OR_OP); }
"<="                    { count(); return(LE_OP); }
">="                    { count(); return(GE_OP); }
"=="                    { count(); return(EQ_OP); }
"!="                    { count(); return(NE_OP); }
";"                    { count(); return(';'); }
("{"|"<%")              { count(); return('{'); }
("}"|"%>")              { count(); return('}'); }
","                    { count(); return(','); }
":"                    { count(); return(':'); }
"="                    { count(); return('='); }
"("                    { count(); return('('); }
")"                    { count(); return(')'); }
("["|"<:")              { count(); return('['); }
("]"|":>")              { count(); return(']'); }
"."                    { count(); return('.'); }
"&"                    { count(); return('&'); }
"!"                    { count(); return('!'); }
"~"                    { count(); return('~'); }
"-"                    { count(); return('-'); }
"+"                    { count(); return('+'); }
"*"                    { count(); return('*'); }
"/"                    { count(); return('/'); }
"%"                    { count(); return('%'); }
"<"                    { count(); return('<'); }
">"                    { count(); return('>'); }
"^"                    { count(); return('^'); }
"|"                    { count(); return('|'); }
"?"                    { count(); return('?'); }

[ \t\v\n\f]            { count(); }
.                      { /* ignore bad characters */ }

%%

void comment()
{
        char c, c1;

loop:
        while ((c = input()) != '*' && c != 0)
                putchar(c);

        if ((c1 = input()) != '/' && c != 0)
        {
                unput(c1);
                goto loop;
        }

        if (c != 0)
                putchar(c1);
}

int column = 0;

void count()
{
        int i;

        for (i = 0; yytext[i] != '\0'; i++)
                if (yytext[i] == '\n')
                        column = 0;
                else if (yytext[i] == '\t')
                        column += 8 - (column % 8);
                else
                        column++;

        ECHO;
}

int check_type()
{
  strncpy(_VCurrentIdentifier, yytext, 511);

  if(_VIsKnownTypeName(yytext)) {
    return(TYPE_NAME);
  } else {
    return(IDENTIFIER);
  }
}

/* inits the global string to the one we will parse */
void _VSetDataToScan(NSData *someData)
{
  [someData retain];
  [_VCurrentData release];
  _VCurrentData = someData;
  _VCurrentDataBytesIndex = 0;
  _VCurrentDataBytes = [_VCurrentData bytes];
  if (_VCurrentDataBytes != NULL) {
    yy_scan_string(_VCurrentDataBytes);
  }
}

/* tells lex there's really no more input when we're done */
int yywrap() {
    return 1;
}