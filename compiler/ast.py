def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class AST(object):
    def __init__(self):
        # self.translationUnits = []
        pass


class TranslationUnits:
    external_declarations = []

    def __init__(self):
        pass

    @staticmethod
    def initialize(external_declaration, tranlation_unit=None):
        unit = None
        if tranlation_unit is not None:
            unit = tranlation_unit
        else:
            unit = TranslationUnits()
        unit.external_declarations.append(external_declaration)


# resolved
class ExternalDeclaration:
    def __init__(self, declaration):
        self.imp = declaration


# external_declaration begin
# resolved
class FunctionDefinition:
    def __init__(self, declarator,
                 compound_statement,
                 declaration_specifiers=None,
                 declaration_list=None):
        self.declarator = declarator
        self.compound_statement = compound_statement
        self.declaration_specifiers = declaration_specifiers
        self.declaration_list = declaration_list


# resolved
class Declaration:
    def __init__(self, declaration_specifiers=None,
                 type_declaration=None,
                 init_declarator_list=None):
        self.declaration_specifiers = declaration_specifiers
        self.type_declaration = type_declaration
        self.init_declarator_list = init_declarator_list


class ClassInterface:
    def __init__(self, class_name,):
        pass


class ClassImplementation:
    def __init__(self):
        pass


class CategoryInterface:
    def __init__(self):
        pass


class CategoryImplementation:
    def __init__(self):
        pass


class ProtocolDeclaration:
    def __init__(self):
        pass


class ClassDeclarationList:
    def __init__(self):
        pass

# external declaration end


# resolved
class DeclarationSpecifiers:
    # typeof TypeSpecifier
    type_specifiers = []

    def __init__(self):
        pass

    @staticmethod
    def initialize(type_specifier, declaration_specifier=None):
        specifier = None
        if declaration_specifier is None:
            specifier = DeclarationSpecifiers()
        else:
            specifier = declaration_specifier
        specifier.type_specifiers.insert(0, type_specifier)


class TypeSpecifier:
    is_struct_or_union = False
    is_enum = False

    def __init__(self, specifier):
        self.specifier = specifier


class Declarator:

    def __init__(self,direct_declarator, pointer=None):
        self.direct_declarator = direct_declarator
        self.pointer = pointer


class DeclarationList:
    declarations = []

    def __init__(self):
        pass

    @staticmethod
    def initialize(declaration, declaration_list=None):
        dlist = None
        if declaration_list is None:
            dlist = DeclarationList()
        else:
            dlist = declaration_list
        dlist.declarations.append(declaration)


class CompoundStatement:
    statement_list = None
    declaration_list = None

    def __init__(self, statement_list=None, declaration_list=None):
        self.statement_list = statement_list
        self.declaration_list = declaration_list


class TypeDeclaration:
    """
    token: TYPEDEF
    """
    def __init__(self, declaration_specifiers, type_declarator):
        self.declaration_specifiers = declaration_specifiers
        self.type_declarator = type_declarator


class InitDeclaratorList:
    init_declarator_list = []

    def __init__(self):
        pass

    @staticmethod
    def initialize(init_declarator, init_declarator_list=None):
        dlist = None
        if init_declarator_list is None:
            dlist = InitDeclaratorList()
        else:
            dlist = init_declarator_list
        dlist.init_declarator_list.append(init_declarator)




