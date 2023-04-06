from Visitor import Visitor
from StaticError import *
from main.mt22.utils.AST import *

class getFunction(Visitor):
    def visitProgram(self, ctx ,o ): 
        o = {}
        for decl in ctx.decls:
            o = self.visit(decl , o)
        return o 
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx, o) :
        if ctx.name in o.keys():
            raise Redeclared(Function(), ctx.name)
        o[ctx.name] = {}
        o[ctx.name]['type'] = ctx.typ 
        return o 

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx, o):
        if ctx.name in o.keys():
            raise Redeclared(Function(), ctx.name)
        o[ctx.name] = {}
        o[ctx.name]['param'] = ctx.params
        o[ctx.name]['returnType'] = ctx.return_type
        return o 
    
def helperType(typ, name, o):
    if isinstance(typ, int):
        if typ == -1:
            typ = o[name]['type'] 
        else:
            typ = o[o[1]]['env'][typ][name]
    return typ 

class StaticChecker(Visitor):
    
    def __init__(self, ctx):
        self.ctx = ctx
    
    def check(self):
        o = None
        return self.visit(self.ctx, o)
    # program decls: List[Decl]
    def visitProgram(self, ctx, o):
        temp = getFunction()
        o = temp.visitProgram(ctx, o)
        o[1] = ""
        o[2] = False #in loop ?
        o["firstline"] = False
        if 'main' not in o.keys() or str(o['main']['returnType']) != "VoidType" or len(o['main']['param']) != 0:
            raise NoEntryPoint()    
        for decl in ctx.decls:
            o = self.visit(decl, o)
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx, o):
        o[1] = ctx.name
        o[ctx.name]['env'] = [{}]
        
        if ctx.inherit is not None :
            if ctx.inherit not in o.keys():
                raise Undeclared(Function(), ctx.inherit)
            o["firstline"] = True
            o["inherit"] = ctx.inherit
        o[ctx.name]['inherit'] = {}
        for decl in ctx.params:
            o = self.visit(decl, o)      
        o = self.visit(ctx.body, o)
        return o
    
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ctx, o):
        if ctx.inherit: 
            o[o[1]]['inherit'][ctx.name] = ctx.typ
        o[o[1]]['env'][-1][ctx.name] = ctx.typ
        return o
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx, o) :
        if ctx.name in o[o[1]]['env'][-1].keys():
            raise Redeclared(Variable(), ctx.name)
        typ = ctx.typ
        if typ.__class__.__name__ == 'AutoType':
            if ctx.init is None:
                raise Invalid(Variable(), ctx.name)
            else :
                typ = self.visit(ctx.init, o)
        # compare type 
        if ctx.init is not None:
            init, temp = self.visit(ctx.init, o)
            if isinstance(init, int):
                if o[o[1]]['env'][init][temp].__class__.__name__ != typ.__class__.__name__:
                    raise TypeMismatchInStatement(ctx)
            else :
                if typ.__class__.__name__ != init.__class__.__name__:
                    raise TypeMismatchInStatement(ctx)
                
        o[o[1]]['env'][-1][ctx.name] = typ 
        return o
        
    # name: str, args: List[Expr]
    def visitCallStmt(self,ctx,o):  
        if ctx.name == "super":
            lst = []
            for arg in ctx.args:
                name = arg.name
                if name in o[o[1]]['env'][-1].keys():
                    raise Redeclared(Parameter(), name)
                if name in  o[o["inherit"]]['inherit'].keys():
                    o[o[1]]['env'][-1][name] = o[o["inherit"]]['inherit'][name]
        return o

    # expr: Expr or None = None
    def visitReturnStmt(self, ctx, o): 
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
        expr, name = self.visit(ctx.cond, o)
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
        lhs, name = self.visit(ctx.init.lhs, o)
        typ = helperType(lhs, name, o)
        if typ.__class__.__name__ != 'IntegerType':
            raise TypeMismatchInStatement(ctx)
        
        rhs, name = self.visit(ctx.init.rhs, o)
        typ = helperType(rhs, name, o)
        if typ.__class__.__name__ != 'IntegerType':
            raise TypeMismatchInStatement(ctx)
        
        cond, name = self.visit(ctx.cond, o)
        typ = helperType(cond, name, o)
        if typ.__class__.__name__ != "BooleanType":
            raise TypeMismatchInStatement(ctx)
        upd, name = self.visit(ctx.upd, o)
        typ = helperType(upd, name, o)
        if typ.__class__.__name__ != "IntegerType":
            raise TypeMismatchInStatement(ctx)
        if ctx.stmt.__class__.__name__ == 'BlockStmt':
            o[o[1]]['env'].append({})
        o[2] = True
        o = self.visit(ctx.stmt, o)
        o[2] = False
        return o
    
    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ctx ,o) : 
        expr,name = self.visit(ctx.cond, o)
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
                raise InvalidStatementInFunction(o[1])
            if temp[0].name == "preventDefault":
                pass 
            elif temp[0].name == "super":
                pass 
            else :
                raise InvalidStatementInFunction(o[1])
        o['firstline'] = False
        for decl in temp:
            if decl.__class__.__name__ == 'BlockStmt':
                o[o[1]]['env'].append({})
            o = self.visit(decl, o)
        o[o[1]]['env'].pop()
        return o
    
    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ctx ,o) : 
        i,name = self.visit(ctx.lhs, o)
        rhs, rhsname = self.visit(ctx.rhs, o)
        if o[o[1]]['env'][-1 - i][name].__class__.__name__ == "AutoType":
            if isinstance(rhs, int):
                o[o[1]]['env'][-1 - i][name] = o[o[1]]['env'][-1 - rhs][rhsname]
            else :
                o[o[1]]['env'][-1 - i][name] = rhs 
        else :
            if isinstance(rhs, int):
                if o[o[1]]['env'][-1 - i].__class__.__name__ != o[o[1]]['env'][-1 - rhs][rhsname].__class__.__name__:
                    raise TypeMismatchInExpression(ctx)
            else :
                if o[o[1]]['env'][-1 - i][name].__class__.__name__ != rhs.__class__.__name__:
                    raise TypeMismatchInExpression(ctx)
        return o
    
    # name: str, args: List[Expr]
    def visitFuncCall(self, ctx ,o) : 
        return o
    # explist: List[Expr]
    #################### not done 
    def visitArrayLit(self, ctx ,o) : 
        typ = None
        i,y = self.visit(ctx.explist[0], o)
        if isinstance(i, int):
            typ = o[o[1]]['env'][i][y]
        else: 
            typ = i
        
        for exp in ctx.explist:
            i, y = self.visit(exp, o)
            if isinstance(i, int):
                if o[o[1]]['env'][i][y].__class__.__name__ != typ.__class__.__name__:
                    raise IllegalArrayLiteral(ctx)
            else: 
                if i.__class__.__name__ != typ.__class__.__name__:
                    raise IllegalArrayLiteral(ctx)
                
        return ArrayType(len(ctx.explist), typ), None

    # val: bool
    def visitBooleanLit(self, ctx ,o) : 
        return BooleanType(), None 
    
    # val: str
    def visitStringLit(self, ctx ,o) : 
        return StringType(), None
    
    # val: float
    def visitFloatLit(self, ctx ,o) : 
        return FloatType(), None
    
    # val: int
    def visitIntegerLit(self, ctx ,o) : 
        return IntegerType(), None
    # name: str, cell: List[Expr]
    def visitArrayCell(self, ctx ,o) : pass 
    
    # name: str
    def visitId(self, ctx ,o) : 
        for i in range(0, len(o[o[1]]['env'])):
            if ctx.name in o[o[1]]['env'][-1 - i]:
                return i, ctx.name
        if ctx.name in o.keys() and 'type' in o[ctx.name].keys():
            return -1, ctx.name
        raise Undeclared(Variable(), ctx.name)
    
    # op: str, val: Expr
    def visitUnExpr(self, ctx ,o) : 
        op = ctx.op 
        expr, name = self.visit(ctx.val, o)
        typ = helperType(expr, name, o)
        if op == '!' and typ.__class__.__name__ != 'BooleanType':
            raise TypeMismatchInExpression(ctx)
        elif op == '-' and (typ.__class__.__name__ != 'FloatType' and typ.__class__.__name__ != 'IntegerType'):
            raise TypeMismatchInExpression(ctx)  
        return typ, None
    
    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ctx ,o) :  
        op = ctx.op 
        left, name1 = self.visit(ctx.left, o)
        right, name2 = self.visit(ctx.right, o)
        typ1 = helperType(left, name1, o) 
        typ2 = helperType(right, name2, o)
        typ = None
        if op == '::':
            if typ1.__class__.__name__ != 'StringType' or typ2.__class__.__name__ != 'StringType':
                raise TypeMismatchInExpression(ctx)
            typ = StringType()
        elif op == "+" or op == '-' or op == '*' or op == '/':
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
            if typ1.__class__.__name__ not in ['IntegerType', 'BooleanType'] or typ2.__class__.__name__  not in ['IntegerType', 'BooleanType']:
                raise TypeMismatchInExpression(ctx)
            typ = BooleanType()
        elif op in ['>', '<', '>=', '<=']:
            if typ1.__class__.__name__ not in ['IntegerType', 'FloatType'] or typ2.__class__.__name__  not in ['IntegerType', 'FloatType']:
                raise TypeMismatchInStatement(ctx)
            typ = BooleanType()
        elif op == '%':
            if typ1.__class__.__name__ != 'IntegerType' or typ2.__class__.__name__ != 'IntegerType':
                raise TypeMismatchInExpression(ctx)
            typ = IntegerType()
        elif op in ['&&', '||']:
            if typ1.__class__.__name__ != 'BooleanType' or typ2.__class__.__name__ != 'BooleanType':
                raise TypeMismatchInExpression(ctx)
            typ = BooleanType()
        return typ, None
            
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
    