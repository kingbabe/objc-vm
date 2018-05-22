# coding=utf-8
import ply.lex as lex
import ply.yacc as yacc

identifier_list = []

tokens = (
    'AUTO', 'BREAK', 'CASE', 'CHAR',
    'CONST', 'CONTINUE', 'DEFAULT', 'DO',
    'DOUBLE', 'ELSE', 'ENUM', 'EXTERN',
    'FLOAT', 'FOR', 'GOTO', 'IF',
    'INLINE', 'INT', 'LONG', 'REGISTER', 'RESTRICT',
    'RETURN', 'SHORT', 'SIGNED', 'SIZEOF',
    'STATIC', 'STRUCT', 'SWITCH', 'TYPEDEF',
    'UNION', 'UNSIGNED', 'VOID', 'VOLATILE',
    'WHILE', 'BOOL_', 'COMPLEX', 'IMAGINERY', 'TRUE',
    'FALSE',
    # reserverd words
    'BOOL', 'Class', 'BYCOPY', 'BYREF', 'ID', 'IMP', 'IN',
    'INOUT', 'NIL', 'NO', 'NULL', 'ONEWAY',
    'OUT', 'PROTOCOL_', 'SEL', 'SELF', 'SUPER',
    'YES', 'AUTORELEASEPOOL', 'CATCH', 'CLASS', 'DYNAMIC',
    'ENCODE', 'END', 'FINALLY', 'IMPLEMENTATION', 'INTERFACE',
    'IMPORT', 'PACKAGE', 'PROTOCOL', 'OPTIONAL', 'PRIVATE',
    'PROPERTY', 'PROTECTED', 'PUBLIC', 'REQUIRED', 'SELECTOR',
    'SYNCHRONIZED', 'SYNTHESIZE', 'THROW', 'TRY', 'ATOMIC',
    'NONATOMIC', 'RETAIN',
    # attributes
    'ATTRIBUTE', 'AUTORELEASING_QUALIFIER', 'BLOCK', 'BRIDGE', 'BRIDGE_RETAINED',
    'BRIDGE_TRANSFER', 'CONVARIANT', 'CONTRAVARIANT', 'DEPRECATED', 'KINDOF',
    'STRING_QUALIFIER', 'TYPEOF', 'UNSAFE_UNRETAINED_QUALIFIER', 'UNUSED', 'WEAK_QUALIFIER',
    # nullability
    'NULL_UNSPECIFIED', 'NULLABLE', 'NONULL', 'NULL_RESETTABLE',
    # NS prefix
    'NS_INLINE', 'NS_ENUM', 'NS_OPTIONS',
    # Property attributes
    'ASSIGN', 'COPY', 'GETTER', 'SETTER', 'STRONG',
    'READONLY', 'READWRITE', 'WEAK', 'UNSAFE_UNRETAINED',
    # Interface builder attributes
    'IB_OUTLET', 'IB_OUTLET_COLLECTION', 'IB_INSPECTABLE', 'IB_DESIGNABLE',
    # Ignored macros
    'NS_ASSUME_NONULL_BEGINE', 'NS_ASSUME_NONULL_END', 'EXTERN_SUFFIX', 'IOS_SUFFIX',
    'MAC_SUFFIX', 'TVOS_PROHIBITED',
    # Separators
    'LP', 'RP', 'LBRACE', 'RBRACE', 'LBRACK', 'RBRACK', 'SEMI', 'COMMA',
    'DOT', 'STRUCTACCESS', 'AT',
    # Operators
    'ASSIGNMENT', 'GT', 'LT', 'BANG', 'TILDE', 'QUESTION', 'COLON', 'EQUAL', 'LE',
    'GE', 'NOTEQUAL', 'AND', 'OR', 'INC', 'DEC', 'ADD', 'SUB', 'MUL', 'DIV', 'BITAND',
    'BITOR', 'BITXOR', 'MOD', 'LSHIFT', 'RSHIFT',
    # Assignments
    'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'AND_ASSIGN', 'OR_ASSIGN',
    'XOR_ASSIGN', 'MOD_ASSIGN', 'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN', 'ELLIPSIS',
    # Literals
    'C_STRING_LITERAL', 'OBJC_STRING_LITERAL',
    'HEX_LITERAL', 'OCTAL_LITERAL', 'BINARY_LITERAL', 'DECIMAL_LITERAL', 'FLOATING_POINT_LITERAL',
    # IDENTIFIER
    'IDENTIFIER', 'TYPE_NAME',
    # WhiteSpace
    'WS',
    # unknown
    'DECLSPEC', 'DLLIMPORT', 'DLLEXPORT'
)

t_AUTO = r'auto'
t_BREAK = r'break'
t_CASE = r'case'
t_CHAR = r'char'
t_CONST = r'const'
t_CONTINUE = r'continue'
t_DEFAULT = r'default'
t_DO = r'do'
t_DOUBLE = r'double'
t_ELSE = r'else'
t_ENUM = r'enum'
t_EXTERN = r'extern'
t_FLOAT = r'float'
t_FOR = r'for'
t_GOTO = r'goto'
t_IF = r'if'
t_INLINE = r'inline'
t_INT = r'int'
t_LONG = r'long'
t_REGISTER = r'register'
t_RESTRICT = r'restrict'
t_RETURN = r'return'
t_SHORT = r'short'
t_SIGNED = r'signed'
t_SIZEOF = r'sizeof'
t_STATIC = r'static'
t_STRUCT = r'struct'
t_SWITCH = r'switch'
t_TYPEDEF = r'typedef'
t_UNION = r'union'
t_UNSIGNED = r'unsigned'
t_VOID = r'void'
t_VOLATILE = r'volatile'
t_WHILE = r'while'
t_BOOL_ = r'_Bool'
t_COMPLEX = r'_Complex'
t_IMAGINERY = r'_Imaginery'
t_TRUE = 'true'
t_FALSE = 'false'

# reserved words

t_BOOL = r'BOOL'
t_Class = r'Class'
t_BYCOPY = r'bycopy'
t_BYREF = r'byref'
t_ID = r'id'
t_IMP = r'IMP'
t_IN = r'in'
t_INOUT = r'inout'
t_NIL = r'nil'
t_NO = r'NO'
t_NULL = r'NULL'
t_ONEWAY = r'oneway'
t_OUT = r'out'
t_PROTOCOL_ = r'Protocol'
t_SEL = r'SEL'
t_SELF = r'self'
t_SUPER = r'super'
t_YES = r'YES'
t_AUTORELEASEPOOL = r'@autoreleasepool'
t_CATCH = r'@catch'
t_CLASS = r'@class'
t_DYNAMIC = r'@dynamic'
t_ENCODE = r'@encode'
t_END = r'@end'
t_FINALLY = r'@finally'
t_IMPLEMENTATION = r'@implementation'
t_INTERFACE = r'@interface'
t_IMPORT = r'@import'
t_PACKAGE = r'@package'
t_PROTOCOL = r'@protocol'
t_OPTIONAL = r'@optional'
t_PRIVATE = r'@private'
t_PROPERTY = r'@property'
t_PROTECTED = r'@protected'
t_PUBLIC = r'@public'
t_REQUIRED = r'@required'
t_SELECTOR = r'@selector'
t_SYNCHRONIZED = r'@synchronized'
t_SYNTHESIZE = r'@synthesize'
t_THROW = r'@throw'
t_TRY = r'@try'
t_ATOMIC = r'atomic'
t_NONATOMIC = r'nonatomic'
t_RETAIN = r'retain'

# attributes (ignore)
t_ignore_ATTRIBUTE = r'__attribute__'
t_ignore_AUTORELEASING_QUALIFIER = r'__autoreleasing'
t_ignore_BLOCK = r'__block'
t_ignore_BRIDGE = r'__bridge'
t_ignore_BRIDGE_RETAINED = r'__bridge_retained'
t_ignore_BRIDGE_TRANSFER = r'__bridge_transfer'
t_ignore_CONVARIANT = r'__convariant'
t_ignore_CONTRAVARIANT = r'__contravariant'
t_ignore_DEPRECATED = r'__deprecated'
t_ignore_KINDOF = r'__kindof'
t_ignore_STRONG_QUALIFIER = r'__strong'
t_ignore_TYPEOF = r'typeof|__typeof|__typeof__'
t_ignore_UNSAFE_UNRETAINED_QUALIFIER = r'__unsafe_unretained'
t_ignore_UNUSED = r'__unused'
t_ignore_WEAK_QUALIFIER = r'__weak'

# nullability (ignore)
t_ignore_NULL_UNSPECIFIED = r'null_unspecified|__null_unspecified|_Null_unspecified'
t_ignore_NULLABLE = r'nullable|__nullable|_Nullable'
t_ignore_NONNULL = r'nonull|__nonnull|_Nonnull'
t_ignore_NULL_RESETTABLE = r'null_resettable'

# NS prefix
t_NS_INLINE = r'NS_INLINE'
t_NS_ENUM = r'NS_ENUM'
t_NS_OPTIONS = r'NS_OPTIONS'

# Property attributes
t_ASSIGN = r'assign'
t_COPY = r'copy'
t_GETTER = r'getter'
t_SETTER = r'setter'
t_STRONG = r'strong'
t_READONLY = r'readonly'
t_READWRITE = r'readwrite'
t_WEAK = r'weak'
t_UNSAFE_UNRETAINED = r'unsafe_unretained'

# Interface Builder attributes (ignore)
t_ignore_IB_OUTLET = r'IBOutlet'
t_ignore_IB_OUTLET_COLLECTION = r'IBOutletCollection'
t_ignore_IB_INSPECTABLE = r'IBInspectable'
t_ignore_IB_DESIGNABLE = r'IB_DESIGNABLE'

# ignored macros
t_ignore_NS_ASSUME_NONNULL_BEGIN = r'NS_ASSUME_NONNULL_BEGIN'
t_ignore_NS_ASSUME_NONNULL_END = r'NS_ASSUME_NONNULL_END'
t_ignore_EXTERN_SUFFIX = r'[_A-Z]+_EXTERN'
t_ignore_IOS_SUFFIX = r'[_A-Z]+_IOS\(.+\)'
t_ignore_MAC_SUFFIX = r'[_A-Z]+_MAC\(.+\)'
t_ignore_PROHIBITED = r'__TVOS_PROHIBITED'

# Separators

t_LP = r'\('
t_RP = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_SEMI = r';'
t_COMMA = r','
t_DOT = r'\.'
t_STRUCTACCESS = r'->'
t_AT = r'@'

# Operators

t_ASSIGNMENT = r'='
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_GT = r'>'
t_LT = r'<'
t_BANG = r'!'
t_TILDE = r'~'
t_QUESTION = r'\?'
t_COLON = r':'
t_EQUAL = r'=='
t_LE = r'<='
t_GE = r'>='
t_NOTEQUAL = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_INC = r'\+\+'
t_DEC = r'--'
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'\/'
t_BITAND = r'&'
t_BITOR = r'\|'
t_BITXOR = r'\^'
t_MOD = r'%'

# Assignments
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'\/='
t_AND_ASSIGN = r'&='
t_OR_ASSIGN = r'\|='
t_XOR_ASSIGN = r'\^='
t_MOD_ASSIGN = r'%='
t_LSHIFT_ASSIGN = r'<<='
t_RSHIFT_ASSIGN = r'>>='
t_ELLIPSIS = r'\.\.\.'

# Identifier
# t_IDENTIFIER = r'[A-Za-z_][A-Za-z_0-9]*'


def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z_0-9]*'
    if t.value in identifier_list:
        t.type = 'TYPE_NAME'
    else:
        t.type = 'IDENTIFIER'
        identifier_list.append(t.value)
    return t


#
# def t_TYPE_NAME(t):
#     r'[A-Za-z_][A-Za-z_0-9]*'
#     if t.value in identifier_list:
#         t.type = 'TYPE_NAME'
#     else:
#         t.type = 'IDENTIFIER'
#         identifier_list.append(t.value)
#     return t


# literals
t_C_STRING_LITERAL = r'\"([^\\\n]|(\\.))*?\"'
t_OBJC_STRING_LITERAL = r'@\"([^\\\n]|(\\.))*?\"'
t_HEX_LITERAL = r'0[xX][0-9a-fA-F]+'
t_OCTAL_LITERAL = r'0[0-7]+'
t_BINARY_LITERAL = r'0[bB][01]+'
t_DECIMAL_LITERAL = r'[0-9]+'
t_FLOATING_POINT_LITERAL = r'([0-9]+\.[0-9]*|\.[0-9]+)[fFdD]?'

# ignores
t_ignore_WS = r'[ \r\n\t\u000C]'

# unknown
t_DECLSPEC = r'__declspec'
t_DLLIMPORT = r'dllimport'
t_DLLEXPORT = r'dllexport'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Comments
def t_multiline_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count("\n")


def t_singleline_comment(t):
    r'//.*\n'
    t.lexer.lineno += 1


def t_precompile_macros(t):
    r'\#(.|n)*'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("非法字符: '%s'" % t.value[0])
    t.lexer.skip(1)
