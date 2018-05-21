from .tokens import tokens
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
                       | INTERFACE class_name ':' superclass_name instance_variables interface_declaration_list END
                       | INTERFACE protocol_reference_list instance_variables interface_declaration_list END
                       | INTERFACE class_name ':' superclass_name protocol_reference_list instance_variables
                         interface_declaration_list END
    """
    pass


# class_implementation (resolved)
def p_class_implementation(p):
    """class_implementation : IMPLEMENTATION class_name instance_variables implementation_definition_list END
                            | IMPLEMENTATION class_name ':' superclass_name instance_variables
                              implementation_definition_list END
    """
    pass


# category_interface (resolved)
def p_category_interface(p):
    """category_interface : INTERFACE class_name '(' category_name ')' interface_declaration_list END
                          | INTERFACE class_name '(' category_name ')' protocol_reference_list
                            interface_declaration_list END
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
                              | type_qualifier
                              | type_qualifier declaration_specifiers
                              | declspec storage_class_specifier
                              | declspec storage_class_specifier declaration_specifiers
                              | declspec type_specifier
                              | declspec type_specifier declaration_specifiers
                              | declspec type_qualifier
                              | declspec type_qualifier declaration_specifiers
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
                            | init_declarator_list ',' init_declarator
    """
    pass


# class_name
def p_class_name(p):
    """class_name : IDENTIFIER
    """
    pass


# superclass_name
def p_superclass_name(p):
    """superclass_name : IDENTIFIER
    """
    pass


# instance_variables
def p_instance_variables(p):
    """instance_variables : '{' struct_declaration_list '}'
                          | '{' visibility_specification struct_declaration_list '}'
                          | '{' struct_declaration_list instance_variables '}'
                          | '{' visibility_specification struct_declaration_list instance_variables '}'
    """
    pass


# interface_declaration_list
def p_interface_declaration_list(p):
    """interface_declaration_list : declaration
                                  | method_declaration
                                  | interface_declaration_list declaration
                                  | interface_declaration_list method_declaration
    """
    pass


# protocol_reference_list
def p_protocol_reference_list(p):
    """protocol_reference_list : '<' protocol_list '>'
    """
    pass


# implementation_definition_list
def p_implementation_definition_list(p):
    """implementation_definition_list : function_definition
                                      | declaration
                                      | method_definition
                                      | implementation_definition_list function_definition
                                      | implementation_definition_list declaration
                                      | implementation_definition_list method_definition
    """
    pass


# category_name
def p_category_name(p):
    """category_name : IDENTIFIER
    """
    pass


# protocol_name
def p_protocol_name(p):
    """protocol_name: IDENTIFIER
    """
    pass


# class_list
def p_class_list(p):
    """class_list : class_name
                  | class_list ',' class_name
    """
    pass


# storage_class_specifier
def p_storage_class_specifier(p):
    """storage_class_specifier : EXTERN
                               | STATIC
                               | AUTO
                               | REGISTER
    """
    pass


# type_specifier
# TODO: TYPE_NAME not resolved
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


# type_qualifier
def p_type_qualifier(p):
    """type_qualifier : CONST
                      | VOLATILE
    """
    pass


# declspec
def p_declspec(p):
    """declspec : DECLSPEC '(' declspec_type ')'
    """
    pass


# pointer
def p_pointer(p):
    """pointer : '*'
               | '*' type_qualifier_list
               | '*' pointer
               | '*' type_qualifier_list pointer
    """
    pass


# direct_declarator
def p_direct_declarator(p):
    """direct_declarator : IDENTIFIER
                         | '(' declarator ')'
                         | direct_declarator '[' constant_expression ']'
                         | direct_declarator '[' ']'
                         | direct_declarator '(' parameter_type_list ')'
                         | direct_declarator '(' identifier_list ')'
                         | direct_declarator '(' ')'
    """
    pass


# statement_list
def p_statement_list(p):
    """statement_list : statement
                      | statement_list statement
    """
    pass


# type_declarator
def p_type_declarator(p):
    """type_declarator : pointer type_direct_declarator
                       | type_direct_declarator
    """
    pass


# init_declarator
def p_init_declarator(p):
    """init_declarator : declarator
                       | declarator '=' initializer
    """
    pass

