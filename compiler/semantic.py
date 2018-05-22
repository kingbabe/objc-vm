# coding=utf-8
from .lexer import tokens
from ply import yacc

start = 'translation_unit'


# translation_unit (resolved)
def p_translation_unit(p):
    """translation_unit : external_declaration
                        | translation_unit external_declaration
    """
    pass


# external_declaration (resolved)
def p_external_declaration(p):
    """external_declaration : function_definition
                            | declaration
                            | class_interface
                            | class_implementation
                            | category_interface
                            | category_implementation
                            | protocol_declaration
                            | class_declaration_list
    """
    pass


# function_definition (resolved)
def p_function_definition(p):
    """function_definition : declaration_specifiers declarator declaration_list compound_statement
                           | declaration_specifiers declarator compound_statement
                           | declarator declaration_list compound_statement
                           | declarator compound_statement
    """
    pass


# declaration (resolved)
def p_declaration(p):
    """declaration : declaration_specifiers SEMI
                   | type_declaration SEMI
                   | declaration_specifiers init_declarator_list SEMI
    """
    pass


# class_interface (resolved)
def p_class_interface(p):
    """class_interface : INTERFACE class_name instance_variables interface_declaration_list END
                       | INTERFACE class_name COLON superclass_name instance_variables interface_declaration_list END
                       | INTERFACE protocol_reference_list instance_variables interface_declaration_list END
                       | INTERFACE class_name COLON superclass_name protocol_reference_list instance_variables interface_declaration_list END
    """
    print('hello')
    pass


# class_implementation (resolved)
def p_class_implementation(p):
    """class_implementation : IMPLEMENTATION class_name instance_variables implementation_definition_list END
                            | IMPLEMENTATION class_name COLON superclass_name instance_variables implementation_definition_list END
    """
    pass


# category_interface (resolved)
def p_category_interface(p):
    """category_interface : INTERFACE class_name '(' category_name ')' interface_declaration_list END
                          | INTERFACE class_name '(' category_name ')' protocol_reference_list interface_declaration_list END
    """
    pass


# category_implementation (resolved)
def p_category_implementation(p):
    """category_implementation : IMPLEMENTATION class_name '(' category_name ')' implementation_definition_list END
    """
    pass


# protocol_declaration (resolved)
def p_protocol_declaration(p):
    """protocol_declaration : PROTOCOL protocol_name interface_declaration_list END
                            | PROTOCOL protocol_name protocol_reference_list interface_declaration_list END
    """
    pass


# class_declaration_list (resolved)
def p_class_declaration_list(p):
    """class_declaration_list : CLASS class_list
    """
    pass


# declaration_specifiers (resolved)
def p_declaration_specifiers(p):
    """declaration_specifiers : storage_class_specifier
                              | storage_class_specifier declaration_specifiers
                              | type_specifier
                              | type_specifier declaration_specifiers
    """
    pass


# declarator (resolved)
def p_declarator(p):
    """declarator : pointer direct_declarator
                  | direct_declarator
    """
    pass


# declaration_list (resolved)
def p_declaration_list(p):
    """declaration_list : declaration
                        | declaration_list declaration
    """
    pass


# compound_statement (resolved)
def p_compound_statement(p):
    """compound_statement : LBRACE RBRACE
                          | LBRACE statement_list RBRACE
                          | LBRACE declaration_list RBRACE
                          | LBRACE declaration_list statement_list RBRACE
    """
    pass


# type_declaration (resolved)
def p_type_declaration(p):
    """type_declaration : TYPEDEF declaration_specifiers type_declarator
    """
    pass


# init_declarator_list (resolved)
def p_init_declarator_list(p):
    """init_declarator_list : init_declarator
                            | init_declarator_list COMMA init_declarator
    """
    pass


# class_name (resolved)
def p_class_name(p):
    """class_name : IDENTIFIER
    """
    pass


# superclass_name (resolved)
def p_superclass_name(p):
    """superclass_name : IDENTIFIER
    """
    pass


# instance_variables (resolved)
def p_instance_variables(p):
    """instance_variables : LBRACE struct_declaration_list RBRACE
                          | LBRACE visibility_specification struct_declaration_list RBRACE
                          | LBRACE struct_declaration_list instance_variables RBRACE
                          | LBRACE visibility_specification struct_declaration_list instance_variables RBRACE
    """
    pass


# interface_declaration_list (resolved)
def p_interface_declaration_list(p):
    """interface_declaration_list : declaration
                                  | method_declaration
                                  | interface_declaration_list declaration
                                  | interface_declaration_list method_declaration
    """
    pass


# protocol_reference_list (resolved)
def p_protocol_reference_list(p):
    """protocol_reference_list : LT protocol_list GT
    """
    pass


# implementation_definition_list (resolved)
def p_implementation_definition_list(p):
    """implementation_definition_list : function_definition
                                      | declaration
                                      | method_definition
                                      | implementation_definition_list function_definition
                                      | implementation_definition_list declaration
                                      | implementation_definition_list method_definition
    """
    pass


# category_name (resolved)
def p_category_name(p):
    """category_name : IDENTIFIER
    """
    pass


# protocol_name (resolved)
def p_protocol_name(p):
    """protocol_name : IDENTIFIER
    """
    pass


# class_list (resolved)
def p_class_list(p):
    """class_list : class_name
                  | class_list COMMA class_name
    """
    pass


# storage_class_specifier (resovled)
def p_storage_class_specifier(p):
    """storage_class_specifier : EXTERN
                               | STATIC
                               | AUTO
                               | REGISTER
    """
    pass


# type_specifier (resolved)
# LOG: TYPE_NAME was renamed to IDENTIFIER
def p_type_specifier(p):
    """type_specifier : VOID
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
    """
    pass


# pointer (resolved)
def p_pointer(p):
    """pointer : MUL
               | MUL pointer
    """
    pass


# direct_declarator (resolved)
def p_direct_declarator(p):
    """direct_declarator : IDENTIFIER
                         | LP declarator RP
                         | direct_declarator LBRACK constant_expression RBRACK
                         | direct_declarator LBRACK RBRACK
                         | direct_declarator LP parameter_type_list RP
                         | direct_declarator LP identifier_list RP
                         | direct_declarator LP RP
    """
    pass


# statement_list (resolved)
def p_statement_list(p):
    """statement_list : statement
                      | statement_list statement
    """
    pass


# type_declarator (resolved)
def p_type_declarator(p):
    """type_declarator : pointer type_direct_declarator
                       | type_direct_declarator
    """
    pass


# init_declarator (resolved)
def p_init_declarator(p):
    """init_declarator : declarator
                       | declarator ASSIGNMENT initializer
    """
    pass


# struct_declaration_list (resolved)
def p_struct_declaration_list(p):
    """struct_declaration_list : struct_declaration
                               | struct_declaration_list struct_declaration
    """
    pass


# visibility_specification (resolved)
def p_visibility_specification(p):
    """visibility_specification : PRIVATE
                                | PUBLIC
                                | PROTECTED
    """
    pass


# method_declaration (resolved)
def p_method_declaration(p):
    """method_declaration : class_method_declaration
                          | instance_method_declaration
    """
    pass


# protocol_list (resolved)
def p_protocol_list(p):
    """protocol_list : protocol_name
                     | protocol_list COMMA protocol_name
    """
    pass


# method_definition (resolved)
def p_method_definition(p):
    """method_definition : class_method_definition
                         | instance_method_definition
    """
    pass


# struct_or_union (resolved)
def p_struct_or_union(p):
    """struct_or_union : STRUCT
                       | UNION
    """
    pass


# struct_or_union_specifier (resolved)
def p_struct_or_union_specifier(p):
    """struct_or_union_specifier : struct_or_union IDENTIFIER LBRACE struct_declaration_list RBRACE
                                 | struct_or_union LBRACE struct_declaration_list RBRACE
                                 | struct_or_union IDENTIFIER
    """
    pass


# enum_specifier (resolved)
def p_enum_specifier(p):
    """enum_specifier : ENUM LBRACE enumerator_list RBRACE
                      | ENUM IDENTIFIER LBRACE enumerator_list RBRACE
                      | ENUM IDENTIFIER
    """
    pass


# constant_expression (resolved)
def p_constant_expression(p):
    """constant_expression : conditional_expression
    """
    pass


# parameter_type_list (resolved)
def p_parameter_type_list(p):
    """parameter_type_list : parameter_list
                           | parameter_list COMMA ELLIPSIS
    """
    pass


# identifier_list (resolved)
def p_identifier_list(p):
    """identifier_list : IDENTIFIER
                       | identifier_list COMMA IDENTIFIER
    """
    pass


# statement (resolved)
def p_statement(p):
    """statement : labeled_statement
                 | compound_statement
                 | expression_statement
                 | selection_statement
                 | iteration_statement
                 | jump_statement
    """
    pass


# type_direct_declarator (resolved)
def p_type_direct_declarator(p):
    """type_direct_declarator : IDENTIFIER
                              | LP type_declarator RP
                              | type_direct_declarator LBRACK constant_expression RBRACK
                              | type_direct_declarator LBRACK RBRACK
                              | type_direct_declarator LP parameter_type_list RP
                              | type_direct_declarator LP identifier_list RP
                              | type_direct_declarator LP RP
    """
    pass


# initializer (resolved)
def p_initializer(p):
    """initializer : assignment_expression
                   | LBRACE initializer_list RBRACE
                   | LBRACE initializer_list COMMA RBRACE
    """
    pass


# struct_declaration (resolved)
def p_struct_declaration(p):
    """struct_declaration : specifier_qualifier_list struct_declarator_list SEMI
    """
    pass


# class_method_declaration (resolved)
def p_class_method_declaration(p):
    """class_method_declaration : ADD method_selector SEMI
                                | ADD method_type method_selector SEMI
    """
    pass


# instance_method_declaration (resolved)
def p_instance_method_declaration(p):
    """instance_method_declaration : SUB method_selector SEMI
                                   | SUB method_type method_selector SEMI
    """
    pass


# class_method_definition (resolved)
def p_class_method_definition(p):
    """class_method_definition : ADD method_selector compound_statement
                               | ADD method_type method_selector compound_statement
                               | ADD method_selector declaration_list compound_statement
                               | ADD method_type method_selector declaration_list compound_statement
    """
    pass


# instance_method_definition (resolved)
def p_instance_method_definition(p):
    """instance_method_definition : SUB method_selector compound_statement
                                  | SUB method_type method_selector compound_statement
                                  | SUB method_selector declaration_list compound_statement
                                  | SUB method_type method_selector declaration_list compound_statement
    """
    pass


# enumerator_list (resolved)
def p_enumerator_list(p):
    """enumerator_list : enumerator
                       | enumerator_list COMMA enumerator
    """
    pass


# conditional_expression (resolved)
def p_conditional_expression(p):
    """conditional_expression : logical_or_expression
                              | logical_or_expression QUESTION expression COLON conditional_expression
    """
    pass


# parameter_list (resolved)
def p_parameter_list(p):
    """parameter_list : parameter_declaration
                      | parameter_list COMMA parameter_declaration
    """
    pass


# labeled_statement (resolved)
def p_labeled_statement(p):
    """labeled_statement : IDENTIFIER COLON statement
                         | CASE constant_expression COLON statement
                         | DEFAULT COLON statement
    """
    pass


# expression_statement (resolved)
def p_expression_statement(p):
    """expression_statement : SEMI
                            | expression SEMI
    """
    pass


# selection_statement (resolved)
def p_selection_statement(p):
    """selection_statement : IF LP expression RP statement
                           | IF LP expression RP statement ELSE statement
                           | SWITCH LP expression RP statement
    """
    pass


# iteration_statement (resolved)
def p_iteration_statement(p):
    """iteration_statement : WHILE LP expression RP statement
                           | DO statement WHILE LP expression RP SEMI
                           | FOR LP expression_statement expression_statement RP statement
                           | FOR LP expression_statement expression_statement expression RP
    """
    pass


# jump_statement (resolved)
def p_jump_statement(p):
    """jump_statement : GOTO IDENTIFIER SEMI
                      | CONTINUE SEMI
                      | BREAK SEMI
                      | RETURN SEMI
                      | RETURN expression SEMI
    """
    pass


# assignment_expression (resolved)
def p_assignment_expression(p):
    """assignment_expression : conditional_expression
                             | unary_expression assignment_operator assignment_expression
    """
    pass


# initializer_list (resolved)
def p_initializer_list(p):
    """initializer_list : initializer
                        | initializer_list COMMA initializer
    """
    pass


# specifier_qualifier_list (resolved)
# TODO: 这里貌似重复?
def p_specifier_qualifier_list(p):
    """specifier_qualifier_list : type_specifier
                                | type_specifier specifier_qualifier_list
    """
    pass


# struct_declarator_list (resolved)
def p_struct_declarator_list(p):
    """struct_declarator_list : struct_declarator
                              | struct_declarator_list COMMA struct_declarator
    """
    pass


# method_selector (resolved)
def p_method_selector(p):
    """method_selector : unary_selector
                       | keyword_selector
                       | keyword_selector COMMA ELLIPSIS
                       | keyword_selector COMMA parameter_type_list
    """
    pass


# method_type (resolved)
def p_method_type(p):
    """method_type : LP type_name RP
    """
    pass


# type_name (resolved)
def p_type_name(p):
    """type_name : specifier_qualifier_list
                 | specifier_qualifier_list abstract_declarator
    """
    pass


# enumerator (resolved)
def p_enumerator(p):
    """enumerator : IDENTIFIER
                  | IDENTIFIER ASSIGNMENT constant_expression
    """
    pass


# logical_or_expression (resolved)
def p_logical_or_expression(p):
    """logical_or_expression : logical_and_expression
                             | logical_or_expression OR logical_and_expression
    """
    pass


# expression (resolved)
def p_expression(p):
    """expression : assignment_expression
                  | expression COMMA assignment_expression
    """
    pass


# parameter_declaration (resolved)
def p_parameter_declaration(p):
    """parameter_declaration : declaration_specifiers declarator
                             | declaration_specifiers abstract_declarator
                             | declaration_specifiers
    """
    pass


# unary_expression (resolved)
def p_unary_expression(p):
    """unary_expression : postfix_expression
                        | INC unary_expression
                        | DEC unary_expression
                        | unary_operator cast_expression
                        | SIZEOF unary_expression
                        | SIZEOF LP type_name RP
    """
    pass


# assignment_operator (resolved)
def p_assignment_operator(p):
    """assignment_operator : ASSIGNMENT
                           | MUL_ASSIGN
                           | DIV_ASSIGN
                           | MOD_ASSIGN
                           | ADD_ASSIGN
                           | SUB_ASSIGN
                           | LSHIFT_ASSIGN
                           | RSHIFT_ASSIGN
                           | AND_ASSIGN
                           | XOR_ASSIGN
                           | OR_ASSIGN
    """
    pass


# struct_declarator (resolved)
def p_struct_declarator(p):
    """struct_declarator : declarator
                         | COLON constant_expression
                         | declarator COLON constant_expression
    """
    pass


# unary_selector (resolved)
def p_unary_selector(p):
    """unary_selector : selector
    """
    pass


# keyword_selector (resolved)
def p_keyword_selector(p):
    """keyword_selector : keyword_declarator
                        | keyword_selector keyword_declarator
    """
    pass


# abstract_declarator (resolved)
def p_abstract_declarator(p):
    """abstract_declarator : pointer
                           | direct_abstract_declarator
                           | pointer direct_abstract_declarator
    """
    pass


# logical_and_expression (resolved)
def p_logical_and_expression(p):
    """logical_and_expression : inclusive_or_expression
                              | logical_and_expression AND inclusive_or_expression
    """
    pass


# postfix_expression (resolved)
def p_postfix_expression(p):
    """postfix_expression : primary_expression
                          | postfix_expression LBRACK expression RBRACK
                          | postfix_expression LP RP
                          | postfix_expression LP argument_expression_list RP
                          | postfix_expression DOT IDENTIFIER
                          | postfix_expression STRUCTACCESS IDENTIFIER
                          | postfix_expression INC
                          | postfix_expression DEC
    """
    pass


# unary_operator (resolved)
def p_unary_operator(p):
    """unary_operator : BITAND
                      | MUL
                      | ADD
                      | SUB
                      | TILDE
                      | BANG
    """
    pass


# cast_expression (resolved)
def p_cast_expression(p):
    """cast_expression : unary_expression
                       | LP type_name RP cast_expression
    """
    pass


# selector (resolved)
def p_selector(p):
    """selector : IDENTIFIER
    """
    pass


# keyword_declarator (resolved)
def p_keyword_declarator(p):
    """keyword_declarator : COLON IDENTIFIER
                          | COLON method_type IDENTIFIER
                          | selector COLON IDENTIFIER
                          | selector COLON method_type IDENTIFIER
    """
    pass


# direct_abstract_declarator (resolved)
def p_direct_abstract_declarator(p):
    """direct_abstract_declarator : LP abstract_declarator RP
                                  | LBRACK RBRACK
                                  | LBRACK constant_expression RBRACK
                                  | direct_abstract_declarator LBRACK RBRACK
                                  | direct_abstract_declarator LBRACK constant_expression RBRACK
                                  | LP RP
                                  | LP parameter_type_list RP
                                  | direct_abstract_declarator LP RP
                                  | direct_abstract_declarator LP parameter_type_list RP
    """
    pass


# inclusive_or_expression (resolved)
def p_inclusive_or_expression(p):
    """inclusive_or_expression : exclusive_or_expression
                               | inclusive_or_expression BITOR exclusive_or_expression
    """
    pass


# primary_expression (resolved)
# LOG: here, CONSTANT has been translate to literals
def p_primary_expression(p):
    """primary_expression : IDENTIFIER
                          | HEX_LITERAL
                          | OCTAL_LITERAL
                          | BINARY_LITERAL
                          | DECIMAL_LITERAL
                          | FLOATING_POINT_LITERAL
                          | C_STRING_LITERAL
                          | OBJC_STRING_LITERAL
                          | LP expression RP
    """
    pass


# argument_expression_list (resolved)
def p_argument_expression_list(p):
    """argument_expression_list : assignment_expression
                                | argument_expression_list COMMA assignment_expression
    """
    pass


# exclusive_or_expression (resolved)
def p_exclusive_or_expression(p):
    """exclusive_or_expression : and_expression
                               | exclusive_or_expression BITXOR and_expression
    """
    pass


# and_expression (resolved)
def p_and_expression(p):
    """and_expression : equality_expression
                      | and_expression BITAND equality_expression
    """
    pass


# equality_expression （resolved)
def p_equality_expression(p):
    """equality_expression : relational_expression
                           | equality_expression EQUAL relational_expression
                           | equality_expression NOTEQUAL relational_expression
    """
    pass


# relational_expression (resolved)
def p_relational_expression(p):
    """relational_expression : shift_expression
                             | relational_expression LT shift_expression
                             | relational_expression GT shift_expression
                             | relational_expression LE shift_expression
                             | relational_expression GE shift_expression
    """
    pass


# shift_expression (resolved)
def p_shift_expression(p):
    """shift_expression : additive_expression
                        | shift_expression LSHIFT additive_expression
                        | shift_expression RSHIFT additive_expression"""
    pass


# additive_expression (resolved)
def p_additive_expression(p):
    """additive_expression : multiplicative_expression
                           | additive_expression ADD multiplicative_expression
                           | additive_expression SUB multiplicative_expression
    """
    pass


# multiplicative_expression
def p_multiplicative_expression(p):
    """multiplicative_expression : cast_expression
                                 | multiplicative_expression MUL cast_expression
                                 | multiplicative_expression DIV cast_expression
                                 | multiplicative_expression MOD cast_expression
    """
    pass


def p_error(e):
    pass