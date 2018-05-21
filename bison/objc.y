%{
#import <Foundation/NSData.h>
#import <Foundation/NSDictionary.h>
#import <Foundation/NSString.h>

#define YYDEBUG 1

extern void yyerror(const char *);
extern yylex(), yyparse();
extern void _VSetDataToScan(NSData *someData);
extern void _VRegisterTypeName(const char *aTypeName);
extern BOOL _VIsKnownTypeName(const char *aTypeName);
extern char _VCurrentIdentifier[512];

%}

%token IDENTIFIER CONSTANT STRING_LITERAL SIZEOF
%token PTR_OP INC_OP DEC_OP LEFT_OP RIGHT_OP LE_OP GE_OP EQ_OP NE_OP
%token AND_OP OR_OP MUL_ASSIGN DIV_ASSIGN MOD_ASSIGN ADD_ASSIGN
%token SUB_ASSIGN LEFT_ASSIGN RIGHT_ASSIGN AND_ASSIGN
%token XOR_ASSIGN OR_ASSIGN TYPE_NAME

%token TYPEDEF EXTERN STATIC AUTO REGISTER
%token CHAR SHORT INT LONG SIGNED UNSIGNED FLOAT DOUBLE CONST VOLATILE VOID
%token STRUCT UNION ENUM ELLIPSIS

%token CASE DEFAULT IF ELSE SWITCH WHILE DO FOR GOTO CONTINUE BREAK RETURN

%token DECLSPEC DLLIMPORT DLLEXPORT

%token INTERFACE IMPLEMENTATION PROTOCOL END CLASS PRIVATE PUBLIC PROTECTED

%start translation_unit

%%

primary_expression
        : IDENTIFIER
        | CONSTANT
        | STRING_LITERAL
        | '(' expression ')'
        ;

postfix_expression
        : primary_expression
        | postfix_expression '[' expression ']'
        | postfix_expression '(' ')'
        | postfix_expression '(' argument_expression_list ')'
        | postfix_expression '.' IDENTIFIER
        | postfix_expression PTR_OP IDENTIFIER
        | postfix_expression INC_OP
        | postfix_expression DEC_OP
        ;

argument_expression_list
        : assignment_expression
        | argument_expression_list ',' assignment_expression
        ;

unary_expression
        : postfix_expression
        | INC_OP unary_expression
        | DEC_OP unary_expression
        | unary_operator cast_expression
        | SIZEOF unary_expression
        | SIZEOF '(' type_name ')'
        ;

unary_operator
        : '&'
        | '*'
        | '+'
        | '-'
        | '~'
        | '!'
        ;

cast_expression
        : unary_expression
        | '(' type_name ')' cast_expression
        ;

multiplicative_expression
        : cast_expression
        | multiplicative_expression '*' cast_expression
        | multiplicative_expression '/' cast_expression
        | multiplicative_expression '%' cast_expression
        ;

additive_expression
        : multiplicative_expression
        | additive_expression '+' multiplicative_expression
        | additive_expression '-' multiplicative_expression
        ;

shift_expression
        : additive_expression
        | shift_expression LEFT_OP additive_expression
        | shift_expression RIGHT_OP additive_expression
        ;

relational_expression
        : shift_expression
        | relational_expression '<' shift_expression
        | relational_expression '>' shift_expression
        | relational_expression LE_OP shift_expression
        | relational_expression GE_OP shift_expression
        ;

equality_expression
        : relational_expression
        | equality_expression EQ_OP relational_expression
        | equality_expression NE_OP relational_expression
        ;

and_expression
        : equality_expression
        | and_expression '&' equality_expression
        ;

exclusive_or_expression
        : and_expression
        | exclusive_or_expression '^' and_expression
        ;

inclusive_or_expression
        : exclusive_or_expression
        | inclusive_or_expression '|' exclusive_or_expression
        ;

logical_and_expression
        : inclusive_or_expression
        | logical_and_expression AND_OP inclusive_or_expression
        ;

logical_or_expression
        : logical_and_expression
        | logical_or_expression OR_OP logical_and_expression
        ;

conditional_expression
        : logical_or_expression
        | logical_or_expression '?' expression ':' conditional_expression
        ;

assignment_expression
        : conditional_expression
        | unary_expression assignment_operator assignment_expression
        ;

assignment_operator
        : '='
        | MUL_ASSIGN
        | DIV_ASSIGN
        | MOD_ASSIGN
        | ADD_ASSIGN
        | SUB_ASSIGN
        | LEFT_ASSIGN
        | RIGHT_ASSIGN
        | AND_ASSIGN
        | XOR_ASSIGN
        | OR_ASSIGN
        ;

expression
        : assignment_expression
        | expression ',' assignment_expression
        ;

constant_expression
        : conditional_expression
        ;

declaration
        : declaration_specifiers ';'
        | type_declaration ';'
        | declaration_specifiers init_declarator_list ';'
        ;

declaration_specifiers
        : storage_class_specifier
        | storage_class_specifier declaration_specifiers
        | type_specifier
        | type_specifier declaration_specifiers
        | type_qualifier
        | type_qualifier declaration_specifiers
| declspec storage_class_specifier
| declspec storage_class_specifier declaration_specifiers
| declspec type_specifier
| declspec type_specifier declaration_specifiers
| declspec type_qualifier
| declspec type_qualifier declaration_specifiers
        ;

init_declarator_list
        : init_declarator
        | init_declarator_list ',' init_declarator
        ;

init_declarator
        : declarator
        | declarator '=' initializer
        ;

declspec_type
: DLLIMPORT
| DLLEXPORT
;

declspec
: DECLSPEC '(' declspec_type ')'
;

storage_class_specifier
        : EXTERN
        | STATIC
        | AUTO
        | REGISTER
        ;

type_declarator
        : pointer type_direct_declarator
        | type_direct_declarator
        ;

type_direct_declarator
        : IDENTIFIER
        {
  _VRegisterTypeName(_VCurrentIdentifier);
  }
        | '(' type_declarator ')'
        | type_direct_declarator '[' constant_expression ']'
        | type_direct_declarator '[' ']'
        | type_direct_declarator '(' parameter_type_list ')'
        | type_direct_declarator '(' identifier_list ')'
        | type_direct_declarator '(' ')'
        ;

type_declaration
        : TYPEDEF declaration_specifiers type_declarator
;

type_specifier
        : VOID
        | CHAR
        | SHORT
        | INT
        | LONG
        | FLOAT
        | DOUBLE
        | SIGNED
        | UNSIGNED
        | struct_or_union_specifier
        | enum_specifier
        | TYPE_NAME
        ;

struct_or_union_specifier
        : struct_or_union IDENTIFIER '{' struct_declaration_list '}'
        {
  _VRegisterTypeName(_VCurrentIdentifier);
  }
        | struct_or_union '{' struct_declaration_list '}'
        | struct_or_union IDENTIFIER
        {
  _VRegisterTypeName(_VCurrentIdentifier);
  }
        ;

struct_or_union
        : STRUCT
        | UNION
        ;

struct_declaration_list
        : struct_declaration
        | struct_declaration_list struct_declaration
        ;

struct_declaration
        : specifier_qualifier_list struct_declarator_list ';'
        ;

specifier_qualifier_list
        : type_specifier specifier_qualifier_list
        | type_specifier
        | type_qualifier specifier_qualifier_list
        | type_qualifier
        ;

struct_declarator_list
        : struct_declarator
        | struct_declarator_list ',' struct_declarator
        ;

struct_declarator
        : declarator
        | ':' constant_expression
        | declarator ':' constant_expression
        ;

enum_specifier
        : ENUM '{' enumerator_list '}'
        | ENUM IDENTIFIER '{' enumerator_list '}'
        {
  _VRegisterTypeName(_VCurrentIdentifier);
  }
        | ENUM IDENTIFIER
        {
  _VRegisterTypeName(_VCurrentIdentifier);
  }
        ;

enumerator_list
        : enumerator
        | enumerator_list ',' enumerator
        ;

enumerator
        : IDENTIFIER
        | IDENTIFIER '=' constant_expression
        ;

type_qualifier
        : CONST
        | VOLATILE
        ;

declarator
        : pointer direct_declarator
        | direct_declarator
        ;

direct_declarator
        : IDENTIFIER
        | '(' declarator ')'
        | direct_declarator '[' constant_expression ']'
        | direct_declarator '[' ']'
        | direct_declarator '(' parameter_type_list ')'
        | direct_declarator '(' identifier_list ')'
        | direct_declarator '(' ')'
        ;

pointer
        : '*'
        | '*' type_qualifier_list
        | '*' pointer
        | '*' type_qualifier_list pointer
        ;

type_qualifier_list
        : type_qualifier
        | type_qualifier_list type_qualifier
        ;

parameter_type_list
        : parameter_list
        | parameter_list ',' ELLIPSIS
        ;

parameter_list
        : parameter_declaration
        | parameter_list ',' parameter_declaration
        ;

parameter_declaration
        : declaration_specifiers declarator
        | declaration_specifiers abstract_declarator
        | declaration_specifiers
        ;

identifier_list
        : IDENTIFIER
        | identifier_list ',' IDENTIFIER
        ;

type_name
        : specifier_qualifier_list
        | specifier_qualifier_list abstract_declarator
        ;

abstract_declarator
        : pointer
        | direct_abstract_declarator
        | pointer direct_abstract_declarator
        ;

direct_abstract_declarator
        : '(' abstract_declarator ')'
        | '[' ']'
        | '[' constant_expression ']'
        | direct_abstract_declarator '[' ']'
        | direct_abstract_declarator '[' constant_expression ']'
        | '(' ')'
        | '(' parameter_type_list ')'
        | direct_abstract_declarator '(' ')'
        | direct_abstract_declarator '(' parameter_type_list ')'
        ;

initializer
        : assignment_expression
        | '{' initializer_list '}'
        | '{' initializer_list ',' '}'
        ;

initializer_list
        : initializer
        | initializer_list ',' initializer
        ;

statement
        : labeled_statement
        | compound_statement
        | expression_statement
        | selection_statement
        | iteration_statement
        | jump_statement
        ;

labeled_statement
        : IDENTIFIER ':' statement
        | CASE constant_expression ':' statement
        | DEFAULT ':' statement
        ;

compound_statement
        : '{' '}'
        | '{' statement_list '}'
        | '{' declaration_list '}'
        | '{' declaration_list statement_list '}'
        ;

declaration_list
        : declaration
        | declaration_list declaration
        ;

statement_list
        : statement
        | statement_list statement
        ;

expression_statement
        : ';'
        | expression ';'
        ;

selection_statement
        : IF '(' expression ')' statement
        | IF '(' expression ')' statement ELSE statement
        | SWITCH '(' expression ')' statement
        ;

iteration_statement
        : WHILE '(' expression ')' statement
        | DO statement WHILE '(' expression ')' ';'
        | FOR '(' expression_statement expression_statement ')' statement
        | FOR '(' expression_statement expression_statement expression ')'
statement
        ;

jump_statement
        : GOTO IDENTIFIER ';'
        | CONTINUE ';'
        | BREAK ';'
        | RETURN ';'
        | RETURN expression ';'
        ;

translation_unit
        : external_declaration
        | translation_unit external_declaration
        ;

external_declaration
        : function_definition
        | declaration
| class_interface
| class_implementation
| category_interface
| category_implementation
| protocol_declaration
| class_declaration_list
        ;

function_definition
        : declaration_specifiers declarator declaration_list
compound_statement
        | declaration_specifiers declarator compound_statement
        | declarator declaration_list compound_statement
        | declarator compound_statement
        ;

class_interface
: INTERFACE class_name instance_variables interface_declaration_list END
| INTERFACE class_name ':' superclass_name instance_variables
interface_declaration_list END
| INTERFACE protocol_reference_list instance_variables
interface_declaration_list END
| INTERFACE class_name ':' superclass_name protocol_reference_list
instance_variables interface_declaration_list END
;

class_implementation
: IMPLEMENTATION class_name instance_variables
implementation_definition_list END
| IMPLEMENTATION class_name ':' superclass_name instance_variables
implementation_definition_list END
;

category_interface
: INTERFACE class_name '(' category_name ')' interface_declaration_list END
| INTERFACE class_name '(' category_name ')' protocol_reference_list
interface_declaration_list END
;

category_implementation
: IMPLEMENTATION class_name '(' category_name ')'
implementation_definition_list END
;

protocol_declaration
: PROTOCOL protocol_name interface_declaration_list END
| PROTOCOL protocol_name protocol_reference_list interface_declaration_list
END
;

class_declaration_list
: CLASS class_list
;

class_list
: class_name
| class_list ',' class_name
;

protocol_reference_list
: '<' protocol_list '>'
;

protocol_list
: protocol_name
| protocol_list ',' protocol_name
;

class_name
: IDENTIFIER
;

superclass_name
: IDENTIFIER
;

category_name
: IDENTIFIER
;

protocol_name
: IDENTIFIER
;

instance_variables
: '{' struct_declaration_list '}'
| '{' visibility_specification struct_declaration_list '}'
| '{' struct_declaration_list instance_variables '}'
| '{' visibility_specification struct_declaration_list instance_variables
'}'
;

visibility_specification
: PRIVATE
| PUBLIC
| PROTECTED
;

interface_declaration_list
: declaration
| method_declaration
| interface_declaration_list declaration
| interface_declaration_list method_declaration
;

method_declaration
: class_method_declaration
| instance_method_declaration
;

class_method_declaration
: '+' method_selector ';'
| '+' method_type method_selector ';'
;

instance_method_declaration
: '-' method_selector ';'
| '-' method_type method_selector ';'
;

implementation_definition_list
: function_definition
| declaration
| method_definition
| implementation_definition_list function_definition
| implementation_definition_list declaration
| implementation_definition_list method_definition
;

method_definition
: class_method_definition
| instance_method_definition
;

class_method_definition
: '+' method_selector compound_statement
| '+' method_type method_selector compound_statement
| '+' method_selector declaration_list compound_statement
| '+' method_type method_selector declaration_list compound_statement
;

instance_method_definition
: '-' method_selector compound_statement
| '-' method_type method_selector compound_statement
| '-' method_selector declaration_list compound_statement
| '-' method_type method_selector declaration_list compound_statement
;

method_selector
: unary_selector
| keyword_selector
| keyword_selector ',' ELLIPSIS
| keyword_selector ',' parameter_type_list
;

unary_selector
: selector
;

keyword_selector
: keyword_declarator
| keyword_selector keyword_declarator
;

keyword_declarator
: ':' IDENTIFIER
| ':' method_type IDENTIFIER
| selector ':' IDENTIFIER
| selector ':' method_type IDENTIFIER
;

selector
: IDENTIFIER
;

method_type
: '(' type_name ')'
;

%%
#include <stdio.h>

extern char yytext[];
extern int column;

char _VCurrentIdentifier[512];

void yyerror(const char *s)
{
        fflush(stdout);
        printf("\n%*s\n%*s\n", column, "^", column, s);
}

BOOL ParsePreProcessedC(NSData *someData)
{
  _VSetDataToScan(someData); /* sets up lex to scan the data */

  return yyparse();
}

static NSMutableDictionary *typeNameDictionary = nil;

void _VRegisterTypeName(const char *aTypeName)
{
  //fprintf(stderr, "-----------------> %s <------------------\n",
aTypeName);

  if(nil == typeNameDictionary) {
    typeNameDictionary = [[NSMutableDictionary alloc] init];
  }

  [typeNameDictionary setObject:[NSString stringWithCString:aTypeName]
forKey:[NSString stringWithCString:aTypeName]];
}

BOOL _VIsKnownTypeName(const char *aTypeName)
{
  return (nil != [typeNameDictionary objectForKey:[NSString
stringWithCString:aTypeName]]);
}
