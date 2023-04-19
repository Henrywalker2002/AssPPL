from Visitor import Visitor
from StaticError import *
# from main.mt22.utils.AST import *
from functools import reduce
from abc import ABC, abstractmethod, ABCMeta
from typing import List, Tuple

class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)

class Type(AST):
    pass


class Decl(AST):
    pass

# Types


class AtomicType(Type):
    pass


class IntegerType(AtomicType):
    def __str__(self):
        return self.__class__.__name__


class FloatType(AtomicType):
    def __str__(self):
        return self.__class__.__name__


class BooleanType(AtomicType):
    def __str__(self):
        return self.__class__.__name__


class StringType(AtomicType):
    def __str__(self):
        return self.__class__.__name__


class ArrayType(Type):
    def __init__(self, dimensions: List[int], typ: AtomicType):
        self.dimensions = dimensions
        self.typ = typ

    def __str__(self):
        return "ArrayType([{}], {})".format(", ".join([str(dimen) for dimen in self.dimensions]), str(self.typ))


class AutoType(Type):
    def __str__(self):
        return self.__class__.__name__


class VoidType(Type):
    def __str__(self):
        return self.__class__.__name__
    

class getFunction(Visitor):
    def __init__(self, ast):
        self.ast = ast
    
    def visitProgram(self, ctx ,o ): 
        o = {}
        for decl in ctx.decls:
            o = self.visit(decl , o)
        return o 
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx, o) :
        if ctx.name in o.keys():
            raise Redeclared(Variable(), ctx.name)
        o[ctx.name] = {}
        o[ctx.name]['type'] = ctx.typ 
        return o 

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx, o):
        o[1] = ctx.name
        if ctx.name in o.keys():
            raise Redeclared(Function(), ctx.name)
        o[ctx.name] = {}
        o[ctx.name]['param'] = {}
        o[ctx.name]['inherit'] = {}
        for decl in ctx.params:
            o = self.visit(decl, o)     
        o[ctx.name]['returnType'] = ctx.return_type
        return o 

    def visitParamDecl(self, ctx, o):
        if ctx.inherit: 
            o[o[1]]['inherit'][ctx.name] = ctx.typ
        o[o[1]]['param'][ctx.name] = ctx.typ 
        return o
    
def helperType(typ, name, o):
    if isinstance(typ, int):
        if typ == -1:
            typ = o[name]['type'] 
        else:
            typ = o[o[1]]['env'][typ][name]
    return typ     
    
class StaticChecker(Visitor):
    
    # def __init__(self, ast):
    #     self.ast = ast
    
    # def check(self):
    #     o = None
    #     return self.visit(self.ctx, o)
    
    # program decls: List[Decl]
    def visitProgram(self, ctx, o):
        temp = getFunction(self.ast)
        o = temp.visitProgram(ctx, o)
        o['super'] = {}
        o['super']['returnType'] = VoidType()
        o['preventDefault'] = {}
        o['preventDefault']['returnType'] = VoidType()
        o[1] = ""
        o[2] = False #in loop ?
        o[3] = False
        o[4] = 0
        o["firstline"] = False    
        for decl in ctx.decls:
            o = self.visit(decl, o)
        if 'main' not in o.keys() or str(o['main']['returnType']) != "VoidType" or len(o['main']['param']) != 0:
            raise NoEntryPoint() 
        
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx, o):
        o[1] = ctx.name
        o[ctx.name]['env'] = [{}]
        
        if ctx.inherit is not None :
            if ctx.inherit not in o.keys():
                raise Undeclared(Function(), ctx.inherit)
            o["firstline"] = True
            o[ctx.name]['parent'] = ctx.inherit
        o[ctx.name]['inherit'] = {}
        o[ctx.name]['param'] = {}
        for decl in ctx.params:
            o = self.visit(decl, o)      
        o = self.visit(ctx.body, o)
        o[1] = ''
        return o
    
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ctx, o):
        if ctx.inherit: 
            o[o[1]]['inherit'][ctx.name] = ctx.typ
        if ctx.name in o[o[1]]['env'][-1].keys():
            raise Redeclared(Parameter(), ctx.name)
        o[o[1]]['env'][-1][ctx.name] = ctx.typ
        o[o[1]]['param'][ctx.name] = ctx.typ 
        return o
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx, o) :
        if ctx.typ.__class__.__name__ == 'ArrayType':
            o[3] = ctx.typ.typ
            o[4] = reduce(lambda x, y : x * y, ctx.typ.dimensions, 1)
        # in function
        if o[1] != '':
            if ctx.name in o[o[1]]['env'][-1].keys():
                raise Redeclared(Variable(), ctx.name)
            typ = ctx.typ
            if typ.__class__.__name__ == 'AutoType':
                if ctx.init is None:
                    raise Invalid(Variable(), ctx.name)
                else :
                    typ, name,o = self.visit(ctx.init, o)
                    typ = helperType(typ, name, o)
                    if typ.__class__.__name__ == 'AutoType':
                        raise Invalid(Variable(), ctx.name)
                    o[o[1]]['env'][-1][ctx.name] = typ 
                    return o
                    
            # compare type 
            if ctx.init is not None:
                init, temp,o = self.visit(ctx.init, o)
                if init.__class__.__name__ == 'AutoType':
                    o[temp]['returnType'] = typ 
                elif isinstance(init, int):
                    init = helperType(init, temp, o)
                    if init.__class__.__name__ != typ.__class__.__name__:
                        raise TypeMismatchInVarDecl(ctx)
                else :
                    if typ.__class__.__name__ == 'FloatType' and init.__class__.__name__ == 'IntegerType':
                        pass 
                    elif typ.__class__.__name__ != init.__class__.__name__:
                        raise TypeMismatchInVarDecl(ctx)
                    
            o[o[1]]['env'][-1][ctx.name] = typ 
        # not in function
        else : 
            typ = ctx.typ
            if typ.__class__.__name__ == 'AutoType':
                if ctx.init is None:
                    raise Invalid(Variable(), ctx.name)
                else :
                    rhs, temp,o = self.visit(ctx.init, o)
                    if rhs.__class__.__name__ == 'AutoType':
                        raise Invalid(Variable(), ctx.name)
                    rhs = helperType(rhs, temp, o)
                    o[ctx.name]['type'] = rhs
                    return o
            # compare type 
            if ctx.init is not None:
                init, temp,o = self.visit(ctx.init, o)
                if init.__class__.__name__ == 'AutoType':
                    o[temp]['returnType'] = typ
                else: 
                    init = helperType(init, temp, o)
                    if typ.__class__.__name__ == 'FloatType' and init.__class__.__name__ == 'IntegerType':
                        pass 
                    elif typ.__class__.__name__ != init.__class__.__name__:
                        raise TypeMismatchInVarDecl(ctx)
        return o
        
    # name: str, args: List[Expr]
    def visitCallStmt(self,ctx,o):  
        if ctx.name == "super":
            if 'parent' not in o[o[1]].keys():
                raise InvalidStatementInFunction(ctx.name)
            return self.visit(CallStmt(o[o[1]]['parent'], ctx.args), o)
        elif ctx.name == "preventDefault" : 
            if 'parent' not in o[o[1]].keys():
               raise InvalidStatementInFunction(ctx.name)
            return o
        if ctx.name not in o.keys() or 'returnType' not in o[ctx.name]:
            raise Undeclared(Function(), ctx.name)
        # check if void type
        
        # handle function param
        params = o[ctx.name]['param']
        if len(params) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        index = 0
        for k,v in params.items():
            arg, name,o = self.visit(ctx.args[index], o)
            arg = helperType(arg, name, o)
            if v.__class__.__name__ == 'AutoType':
                if arg.__class__.__name__ == 'AutoType':
                    pass 
                else :
                    o[ctx.name]['param'][k] = arg
            elif arg.__class__.__name__== 'AutoType':
                o[name]['returnType'] = v 
            elif v.__class__.__name__ == 'FloatType' and arg.__class__.__name__ == 'IntegerType':
                pass 
            elif v.__class__.__name__ != arg.__class__.__name__:
                raise TypeMismatchInExpression(ctx)
            index += 1
        
        return o

    # expr: Expr or None = None
    def visitReturnStmt(self, ctx, o): 
        if ctx.expr is None:
            return VoidType()
        else:
            typ, name, o = self.visit(ctx.expr, o)
            typ = helperType(typ, name, o)
            if typ.__class__.__name__ == 'AutoType':
                if o[o[1]]['returnType'].__class__.__name__ == 'AutoType':
                    pass 
                else :
                    o[name]['returnType'] = typ
            else:
                if o[o[1]]['returnType'].__class__.__name__ == 'AutoType':
                    o[o[1]]['returnType'] = typ
                else :
                    if typ.__class__.__name__ != o[o[1]]['returnType'].__class__.__name__:
                        raise TypeMismatchInStatement(ctx)
        return o     
    
    def visitContinueStmt(self, ctx, o): 
        if not o[2]:
            raise MustInLoop(ctx)
        return o
        
    def visitBreakStmt(self, ctx ,o) : 
        if not o[2]:
            raise MustInLoop(ctx)
        return o
        
    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ctx ,o) : 
        expr, name = self.visit(ctx.cond, o)
        typ = helperType(expr, name, o)
        if typ.__class__.__name__ != "BooleanType":
            raise TypeMismatchInStatement(ctx)
        o[2] = True
        o[o[1]]['env'].append({})
        stmt = self.visit(ctx.stmt, o)
        o[2] = False
        return o
    
    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ctx ,o) : 
        expr, name.o = self.visit(ctx.cond, o)
        typ = helperType(expr, name, o)
        if typ.__class__.__name__ != "BooleanType":
            raise TypeMismatchInStatement(ctx)
        o[2] = True
        if ctx.stmt.__class__.__name__ == "BlockStmt":
            o[o[1]]['env'].append({})
        stmt = self.visit(ctx.stmt, o)
        o[2] = False
        return o
    
    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ctx ,o) : 
        # handle init
        lhs, name,o = self.visit(ctx.init.lhs, o)
        typ = helperType(lhs, name, o)
        if typ.__class__.__name__ != 'IntegerType':
            raise TypeMismatchInStatement(ctx)
        
        rhs, name,o = self.visit(ctx.init.rhs, o)
        typ = helperType(rhs, name, o)
        
        if typ.__class__.__name__ == 'AutoType':
            o[name]['returnType'] = IntegerType()
        elif typ.__class__.__name__ != 'IntegerType':
            raise TypeMismatchInStatement(ctx)
        
        cond, name, o = self.visit(ctx.cond, o)
        typ = helperType(cond, name, o)
        if typ.__class__.__name__ == 'AutoType':
            o[name]['returnType'] = IntegerType()
        elif typ.__class__.__name__ != "BooleanType":
            raise TypeMismatchInStatement(ctx)
        
        upd, name, o = self.visit(ctx.upd, o)
        typ = helperType(upd, name, o)
        if typ.__class__.__name__ == 'AutoType':
            o[name]['returnType'] = IntegerType()
        elif typ.__class__.__name__ != "IntegerType":
            raise TypeMismatchInStatement(ctx)
        
        if ctx.stmt.__class__.__name__ == 'BlockStmt':
            o[o[1]]['env'].append({})
        o[2] = True
        o = self.visit(ctx.stmt, o)
        o[2] = False
        return o
    
    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ctx ,o) : 
        expr,name,o = self.visit(ctx.cond, o)
        typ = helperType(expr, name, o)
        if typ.__class__.__name__ != "BooleanType":
            raise TypeMismatchInStatement(ctx)
        if ctx.tstmt.__class__.__name__ == "BlockStmt":
            o[o[1]]['env'].append({})
        o = self.visit(ctx.tstmt, o)
        if ctx.fstmt:
            if ctx.fstmt.__class__.__name__ == "BlockStmt":
                o[o[1]]['env'].append({})
            o = self.visit(ctx.fstmt, o)
        return o
    
    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ctx ,o) : 
        temp = ctx.body
        if o["firstline"]:
            if len(temp) == 0:
                o = self.visit(CallStmt("super", []), o)
            elif temp[0].__class__.__name__ == "CallStmt":
                if temp[0].name == "preventDefault":
                    pass 
                elif temp[0].name == "super":
                    pass 
                else :
                    o = self.visit(CallStmt("super", []), o)
            else :
                o = self.visit(CallStmt("super", []), o)
        o['firstline'] = False
        for decl in temp:
            if decl.__class__.__name__ == 'BlockStmt':
                o[o[1]]['env'].append({})
            o = self.visit(decl, o)
        o[o[1]]['env'].pop()
        return o
    
    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ctx ,o) : 
        i,name,o = self.visit(ctx.lhs, o)
        rhs, rhsname,o = self.visit(ctx.rhs, o)
        lhs = helperType(i, name, o)
        rhs = helperType(rhs, rhsname, o)
        
        if lhs.__class__.__name__ == "AutoType":
            if rhs.__class__.__name__ == 'AutoType':
                raise Invalid(Variable(), name)
            else :
                if i != -1: 
                    o[o[1]]['env'][-1 - i][name] = rhs 
                else : 
                    o[name]['type'] = rhs
        else :
            rhs = helperType(rhs, rhsname, o)
            if rhs.__class__.__name__ == 'AutoType':
                o[rhsname]['returnType'] = lhs
            elif lhs.__class__.__name__ == 'FloatType' and rhs.__class__.__name__ == 'IntegerType':
                pass 
            elif rhs.__class__.__name__  != lhs.__class__.__name__: 
                raise TypeMismatchInExpression(ctx)
        return o
    
    # name: str, args: List[Expr]
    # o[o[1]]['param'][ctx.name] = ctx.typ 
    def visitFuncCall(self, ctx ,o) : 
        if ctx.name not in o.keys() or 'returnType' not in o[ctx.name].keys():
            raise Undeclared(Function(), ctx.name)
        # handle args : 
        params = o[ctx.name]['param']
        if o[ctx.name]['returnType'].__class__.__name__ == 'VoidType':
            raise TypeMismatchInExpression(ctx)
        if len(params) != len(ctx.args):
            raise TypeMismatchInExpression(ctx)
        index = 0
        for k,v in params.items():
            arg, name,o = self.visit(ctx.args[index], o)
            arg = helperType(arg, name, o)
            if v.__class__.__name__ == 'AutoType':
                if arg.__class__.__name__ == 'AutoType':
                    pass 
                else :
                    o[ctx.name]['param'][k] = arg
            elif arg.__class__.__name__== 'AutoType':
                o[name]['returnType'] = v 
            elif v.__class__.__name__ == 'FloatType' and arg.__class__.__name__ == 'IntegerType':
                pass 
            elif v.__class__.__name__ != arg.__class__.__name__:
                raise TypeMismatchInExpression(ctx)
            index += 1
        return o[ctx.name]['returnType'], ctx.name, o
    
    # explist: List[Expr]
    #################### not done 
    def visitArrayLit(self, ctx ,o) : 
        typ = o[3]
        
        if len(ctx.explist) != o[4]:
            raise IllegalArrayLiteral(ctx)
        for exp in ctx.explist:
            i, y = self.visit(exp, o)
            temp = helperType(i, y, o)
            if temp.__class__.__name__ not in ['FloatType', 'IntegerType', 'StringType', 'BooleanType']:
                raise TypeMismatchInExpression(ctx)
            if typ.__class__.__name__ == 'FloatType' and temp.__class__.__name__ == 'IntegerType':
                pass 
            elif typ.__class__.__name__ != temp.__class__.__name__:
                raise IllegalArrayLiteral(ctx)
            
        o[3] = False
        o[4] = 0
        return ArrayType(len(ctx.explist), typ), None, o

    # val: bool
    def visitBooleanLit(self, ctx ,o) : 
        return BooleanType(), None ,o
    
    # val: str
    def visitStringLit(self, ctx ,o) : 
        return StringType(), None,o
    
    # val: float
    def visitFloatLit(self, ctx ,o) : 
        return FloatType(), None,o
    
    # val: int
    def visitIntegerLit(self, ctx ,o) : 
        return IntegerType(), None,o
    
    # name: str, cell: List[Expr]
    def visitArrayCell(self, ctx ,o) :
        typ,name,o = self.visit(Id(ctx.name), o)
        typ = helperType(typ, name, o)
        if typ.__class__.__name__ != 'ArrayType':
            raise TypeMismatchInExpression(ctx)
        for cell in ctx.cell: 
            t1, t2, o = self.visit(cell, o)
            t1 = helperType(t1, t1, o)
            if t1.__class__.__name__ == 'AutoType':
                o[t2]['returnType'] = IntegerType()
            elif t1.__class__.__name__ != 'IntegerType':
                raise TypeMismatchInExpression(ctx)
        return typ.typ, None,o
    
    # name: str
    def visitId(self, ctx ,o) : 
        if o[1] != '':
            for i in range(0, len(o[o[1]]['env'])):
                if ctx.name in o[o[1]]['env'][-1 - i]:
                    return i, ctx.name,o
        if ctx.name in o.keys() and 'type' in o[ctx.name].keys():
            return -1, ctx.name,o
        raise Undeclared(Variable(), ctx.name)
    
    # op: str, val: Expr
    def visitUnExpr(self, ctx ,o) : 
        op = ctx.op 
        expr, name, o = self.visit(ctx.val, o)
        typ = helperType(expr, name, o)
        
        if op == '!' and typ.__class__.__name__ != 'AutoType':
            o[name]['returnType'] = BooleanType()
        elif op == '!' and typ.__class__.__name__ != 'BooleanType':
            raise TypeMismatchInExpression(ctx)
        elif op == '-' and typ.__class__.__name__ != 'AutoType':
            o[name]['returnType'] = FloatType()
        elif op == '-' and (typ.__class__.__name__ != 'FloatType' and typ.__class__.__name__ != 'IntegerType'):
            raise TypeMismatchInExpression(ctx)  
        return typ, None,o
    
    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ctx ,o) :  
        op = ctx.op 
        left, name1,o = self.visit(ctx.left, o)
        right, name2,o = self.visit(ctx.right, o)
        typ1 = helperType(left, name1, o) 
        typ2 = helperType(right, name2, o)
        typ = None
        if op == '::':
            if typ1.__class__.__name__ == 'AutoType':
                o[name1]['returnType'] = StringType()
                typ1 = StringType()
            if typ2.__class__.__name__ == 'AutoType':
                o[name2]['returnType'] = StringType()
                typ2 = StringType()
            if typ1.__class__.__name__ != 'StringType' or typ2.__class__.__name__ != 'StringType':
                raise TypeMismatchInExpression(ctx)
            typ = StringType()
        elif op == "+" or op == '-' or op == '*' or op == '/':
            if typ1.__class__.__name__ == 'AutoType':
                o[name1]['returnType'] = FloatType()
                typ1 = FloatType()
            if typ2.__class__.__name__ == 'AutoType':
                o[name2]['returnType'] = FloatType()
                typ2 = FloatType()
            
            if typ1.__class__.__name__ == 'FloatType' and typ2.__class__.__name__ == 'FloatType':
                typ = FloatType()
            elif typ1.__class__.__name__ == 'FloatType' and typ2.__class__.__name__ == 'IntegerType':
                typ = FloatType()
            elif typ1.__class__.__name__ == 'IntegerType' and typ2.__class__.__name__ == 'FloatType':
                typ = FloatType()
            elif typ1.__class__.__name__ == 'IntegerType' and typ2.__class__.__name__ == 'IntegerType':
                typ = IntegerType()
            else :
                raise TypeMismatchInExpression(ctx)
        elif op in ['==', '!=']: 
            if typ1.__class__.__name__ == "AutoType" and typ2.__class__.__name__ in ['IntegerType', "BooleanType"]:
                o[name1]['returnType'] = typ2
            if typ2.__class__.__name__ == "AutoType" and typ1.__class__.__name__ in ['IntegerType', "BooleanType"]:
                o[name2]['returnType'] = typ1
            
            if typ1.__class__.__name__ not in ['IntegerType', 'BooleanType'] or typ2.__class__.__name__  not in ['IntegerType', 'BooleanType']:
                raise TypeMismatchInExpression(ctx)
            typ = BooleanType()
        elif op in ['>', '<', '>=', '<=']:
            if typ1.__class__.__name__ == 'AutoType':
                o[name1]['returnType'] = FloatType()
                typ1 = FloatType()
            if typ2.__class__.__name__ == 'AutoType':
                o[name2]['returnType'] = FloatType()
                typ2 = FloatType()
            
            if typ1.__class__.__name__ not in ['IntegerType', 'FloatType'] or typ2.__class__.__name__  not in ['IntegerType', 'FloatType']:
                raise TypeMismatchInStatement(ctx)
            typ = BooleanType()
        elif op == '%':
            if typ1.__class__.__name__ == 'AutoType':
                o[name1]['returnType'] = IntegerType()
                typ1 = IntegerType()
            if typ2.__class__.__name__ == 'AutoType':
                o[name2]['returnType'] = IntegerType()
                typ2 = IntegerType()
            
            if typ1.__class__.__name__ != 'IntegerType' or typ2.__class__.__name__ != 'IntegerType':
                raise TypeMismatchInExpression(ctx)
            typ = IntegerType()
        elif op in ['&&', '||']:
            if typ1.__class__.__name__ == 'AutoType':
                o[name1]['returnType'] = BooleanType()
                typ1 = BooleanType()
            if typ2.__class__.__name__ == 'AutoType':
                o[name2]['returnType'] = BooleanType()
                typ2 = BooleanType()
                
            if typ1.__class__.__name__ != 'BooleanType' or typ2.__class__.__name__ != 'BooleanType':
                raise TypeMismatchInExpression(ctx)
            typ = BooleanType()
        return typ, None,o
            
    # type 
    def visitVoidType(self, ctx ,o) : pass 
    # type 
    def visitAutoType(self, ctx ,o) : pass 
    # type 
    def visitArrayType(self, ctx ,o) : pass 
    # type 
    def visitStringType(self, ctx ,o) : pass 
    # type 
    def visitBooleanType(self, ctx ,o) : pass 
    # type 
    def visitFloatType(self, ctx ,o) : pass 
    # type 
    def visitIntegerType(self, ctx ,o) : pass 
    