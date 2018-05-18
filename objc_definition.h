//
// Created by stephenwzl on 2018/5/17.
//

#ifndef OBJC_VM_BUILD_OBJC_DEFINITION_H
#define OBJC_VM_BUILD_OBJC_DEFINITION_H

#define namespace_objc_vm_begin namespace {

#define namespace_objc_vm_end }

#include <iostream>
#include <vector>
#include <string>

namespace_objc_vm_begin
/// DO NOT SUPPORT
/// typeof
///

typedef enum {
    objc_boolean_value = 1,
    objc_pointer_value,
    objc_int_value,
    objc_float_value,
    objc_double_value,
    // TODO: may not implement on 1.0
    objc_struct_value,
    objc_union_value,
    objc_enum_value,
} objc_value_type;

typedef enum {
    objc_no = 0,
    objc_yes = 1
} objc_boolean;


class ObjcNode {
public:
    virtual void append(ObjcNode child);
    virtual std::string toString();
};

/// pre declarations
class TopLevelDeclaration;

class TranslationUnit : ObjcNode {
public:
    std::vector<TopLevelDeclaration> declarations;
private:
    /// to judge if this unit is header or source
    bool isHeader;
    bool isSource;
};

/**
 * header translation units recognize dependencies
 * of source code
 * */
class HeaderTranslationUnit : TranslationUnit {

};

/**
 * source translation unit contains the code to generate
 * */
class SourceTranslationUnit : TranslationUnit {

};

class TopLevelDeclaration : ObjcNode {
};

class Declaration : ObjcNode {
};


/**
 * import declaration should:
 * 1. recognize headers to compile
 * 2. recognize external modules
 * 3. resolve unknown symbols
 *
 * this declaration should output the header instance
 * a source translation unit should contains several headers instance
 * */
class ImportDeclaration : TopLevelDeclaration {
public:
    ImportDeclaration(std::string& file, bool isModule, bool isMacro, bool isCInclude) {
        if (isModuleImport) {
            headerFile = nullptr;
        } else {
            headerFile = file;
        }
        isMacroImport = isMacro;
        this->isCInclude = isCInclude;
    }
    std::string headerFile;
private:
    bool isModuleImport = false;        /// in objc-vm, if you imported a module, we ignore this import
    bool isMacroImport = false;         /// objc normal import
    bool isCInclude = false;            /// normal c include
};

class FunctionSignature;
class FunctionDeclaration : TopLevelDeclaration {
public:
    FunctionSignature signature;
};

class FunctionSignature : Declaration {
public:
    std::string selector;
};

class ClassInterface : TopLevelDeclaration {
public:
    std::string className;
    std::string superClassName;
    std::vector<std::string> protocolList;
    void * instanceVariables;       // TODO:  hasn't decided to implement
    void * interfaceDeclarationList; // TODO:  hasn't decided to implement
};


class ClassImplementation : TopLevelDeclaration {
public:
    std::string className;
    void * instanceVariables;       // TODO:  hasn't decided to implement
    void * implementationDefinitionList; // TODO:  hasn't decided to implement
};

class CategoryInterface : TopLevelDeclaration {
public:
    std::string categoryName;
    std::string className;
    void * interfaceDeclarationList; // TODO:  hasn't decided to implement
};

class CategoryImplementation : TopLevelDeclaration {
public:
    std::string categoryName;
    std::string className;
    void * implementationDefinitionList; // TODO:  hasn't decided to implement
};

class ProtocolDeclaration : TopLevelDeclaration {
public:
    std::string protocolName;
    std::vector<std::string> protocolList;
    void * protocolDeclarationSection; // TODO:  hasn't decided to implement
};

/**
 * protocol declaration list is just like:
 *
 * @protocol AProtocol, BProtocol, ....;
 *
 * just used to pre definition for compiling
 *
 * */
class ProtocolDeclarationList : TopLevelDeclaration {
public:
    std::vector<std::string> protocolList;
};

/**
 * class declaration list is just like:
 *
 * @class AClass, BClass, ....;
 *
 * just used to pre definition for compiling
 *
 * */
class ClassDeclarationList : TopLevelDeclaration {
public:
    std::vector<std::string> classList;
};

/**
 * function definition differs from function declaration
 * definition is some kind of implement
 * declaration just defines the interface;
 *
 * */
class FunctionDefinition : TopLevelDeclaration {
public:
    FunctionSignature signature;
    void * compoundStatement = nullptr; // TODO: remain to implement
};


namespace_objc_vm_end
#endif //OBJC_VM_BUILD_OBJC_DEFINITION_H
