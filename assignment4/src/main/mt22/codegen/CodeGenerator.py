from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()],
                       VoidType()), CName(self.libName))
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(Visitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.emit = Emitter("test.txt")
        self.className = "MT22Class"

    def visitProgram(self, ast, c):
        c = {}
        [self.visit(i, c)for i in ast.decls]
        self.emit.emitEPILOG()
        return c

    def visitClassDecl(self, ast, c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        [self.visit(ele, SubBody(None, self.env))
         for ele in ast.memlist if type(ele) == MethodDecl]
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), None, Block([], [])), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.typ, consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
            glenv = local.sym+glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntegerType()

    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
    
    # begin code 
    
    def visitVarDecl(self, ctx , o):
        if "frame" in o.keys(): 
            index = o.frame.getNewIndex()
            code = self.emit.emitVAR(index, ctx.name, ctx.typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
            self.emit.printout(code)
            if ctx.init : 
                self.visit(AssignStmt(Id(ctx.name), ctx.init))
            return Symbol(ctx.name, ctx.typ, Index(index))
        else : 
            code = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False)
            self.emit.printout(code)
            if ctx.init : 
                self.visit(AssignStmt(Id(ctx.name), ctx.init))            
            return Symbol(ctx.name, ctx.typ, CName(self.className))

    def visitIntegerLit(self, ctx, o):
        code = self.emit.emitPUSHICONST(ctx.val, o.frame)
        return code, IntType()

    def visitFloatLit(self, ctx, o):
        code = self.emit.emitPUSHFCONST(ctx.val, o.frame)
        return code, FloatType()
    
    def visitStringLit(self, ctx, o):
        code = self.emit.emitPUSHCONST(ctx.val, StringType(), o.frame) 
        return code, StringType()

    def visitBooleanLit(self, ctx, o):
        code = self.emit.emitPUSHICONST(ctx.val, o.frame)
        return code, BooleanType()
    
    def visitArrayLit(self, ctx, o):
        pass 
    
    def visitBinExpr(self, ctx, o):
        e1, e1t = self.visit(ctx.left, o) 
        e2, e2t = self.visit(ctx.right, o)
        
        if type(e1t) != type(e2t):
            if isinstance(e1t, IntType):
                e1 = e1 + self.emit.emitI2F(o.frame)
            else :
                e2 = e2 + self.emit.emitI2F(o.frame) 
            rt = FloatType()
        else : 
            rt = e1t
        
        if ctx.op in ['+', '-']:
            code = self.emit.emitADDOP(ctx.op, rt, o.frame)        
        elif ctx.op in ['*', '/']:
            code = self.emit.emitMULOP(ctx.op, rt, o.frame) 
        elif ctx.op in ['>', '<', '==', '!=', '>=', '<=']:
            code = self.emit.emitREOP(ctx.op, rt, o.frame) 
            rt = IntType()
        elif ctx.op == '%':
            code = self.emit.emitMOD(o.frame) 
        elif ctx.op == '&&':
            code = self.emit.emitANDOP(o.frame)
            rt = IntType()
        elif ctx.op == '||':
            code = self.emit.emitOROP(o.frame)
            rt = IntType()
        else : 
            pass 
        
        return e1 + e2 + code, rt 
    
    def visitUpExpr(self, ctx, o):
        e, et = self.visit(ctx.val, o)
        if ctx.op == '-':
            code = self.emit.emitNEGOP(et, o.frame)
        elif ctx.op == '!':
            code = self.emit.emitNOT(et, o.frame)
        else : 
            # index operator
            pass 
        return e + code, et 

    def visitIfStmt(self, ctx, o):
        cond, condt = self.visit(ctx.cond, Access(o.frame, o.sym, False))
        self.emit.printout(cond) 
        flabel, elabel = o.frame.getNewLabel(), o.frame.getNewLabel()
        # goto 
        code = self.emit.emitIFFALSE(flabel, o.frame)
        self.emit.printout(code)
        # true statement
        self.visit(ctx.tstmt, o)
        code = self.emit.emitLABEL(flabel, o.frame)
        self.emit.printout(code) 
        
        if ctx.fstmt:
            self.visit(ctx.fstmt, o) 
        
        code = self.emit.emitLABEL(elabel, o.frame)
        self.emit.printout(code)
            
    def visitWhileStmt(self, ctx, o):
        o.frame.enterLoop()
        blabel, elabel, breakLabel, conLabel = o.frame.getNewLabel(), o.frame.getNewLabel(), o.frame.getBreakLabel(), o.frame.getContinueLabel()

        self.emit.printout(self.emit.emitLABEL(conLabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(blabel, o.frame)) 
        cond, condt = self.visit(ctx.cond, Access(o.frame, o.sym, False))
        self.emit.printout(cond) 
        # goto
        self.emit.emitIFFALSE(elabel, o.frame)
        # stmt 
        self.visit(ctx.stmt, o)
        self.emit.printout(self.emit.emitGOTO(blabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, o.frame))
        o.frame.exitLoop()
        self.emit.printout(self.emit.emitLABEL(elabel, o.frame))

    def visitDoWhileStmt(self, ctx, o):
        o.frame.enterLoop() 
        blabel, breakLabel, conLabel = o.frame.getNewLabel(), o.frame.getBreakLabel(), o.frame.getContinueLabel()

        self.emit.printout(self.emit.emitLABEL(blabel, o.frame))
        
        # statement
        self.visit(ctx.stmt, o)
        # cond
        self.emit.printout(self.emit.emitLABEL(conLabel, o.frame)) 
        expr, exprT = self.visit(ctx.cond, Access(o.frame, o.sym, False))
        self.emit.printout(expr)
        # goto 
        self.emit.printout(self.emit.emitIFTRUE(blabel, o.frame))
        # break label
        self.emit.printout(self.emit.emitLABEL(breakLabel, o.frame))
        # exit 
        o.frame.exitLoop()
        
    def visitBreakStmt(self, ctx, o):
        breakLabel = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(breakLabel, o.frame))
    
    def visitContinueStmt(self, ctx, o):
        conLabel = o.frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(conLabel, o.frame))
    
    def visitReturnStmt(self,ctx, o):
        expr, exprT = self.visit(ctx.expr, Access(o.frame, o.sym, False))
        self.emit.printout(expr)
        code = self.emit.emitRETURN(exprT, o.frame)
        self.emit.printout(code)
    
    # def visitCallStmt(self, ctx, o):
    #     pass 
    
    def visitForStmt(self, ctx, o):
        o.frame.enterLoop()
        blabel, elabel = o.frame.getNewLabel(), o.frame.getNewLabel()
        conLabel, breakLabel = o.frame.getContinueLabel(), o.frame.getBreakLabel()
        self.visit(ctx.init, o)
        self.emit.printout(self.emit.emitLABEL(blabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(conlabel, o.frame))
        # cond
        expr, exprT = self.visit(ctx.cond, Access(o.frame, o.sym, False))
        self.emit.printout(expr)
        # goto 
        self.emit.printout(self.emit.emitIFFALSE(elabel, o.frame))
        # stmt 
        self.visit(ctx.stmt, o)
        upd, updT = self.visit(ctx.upd, Access(o.frame, o.sym, False))
        self.emit.printout(upd)
        # turn around 
        self.emit.printout(self.emit.emitGOTO(blabel, o.frame))
        # label 
        self.emit.printout(self.emit.emitLABEL(breakLabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(elabel, o.frame))
        o.frame.exitLoop()
    
    #     def __init__(self, lhs: LHS, rhs: Expr):
    def visitAssignStmt(self, ctx, o):
        rhs, rhsT = self.visit(ctx.rhs, Access(o.frame, o.sym, False))
        lhs, lhsT = self.visit(ctx.lhs , Access(o.frame, o.sym, True))
        if type(ctx.lhs) is not ArrayCell :
            self.emit.printout(rhs)
            self.emit.printout(lhs)
        else : 
            self.emit.printout(lhs[0])
            self.emit.printout(lhs[1])
            self.emit.printout(rhs)
            self.emit.printout(lhs[2])
            
    
    def visitId(self, ctx, o): 
        sym = list(filter(lambda x : x.name == ctx.name, o.sym))[0]
        # inner function 
        if isinstance(sym.value.value, int):
            if o.left: 
                code = self.emit.emitWRITEVAR(ctx.name, sym.mtype, sym.value.value, o.frame)
            else : 
                code = self.emit.emitREADVAR(ctx.name, sym.mtype, sym.value.value, o,frame)
        else : 
            if o.left:
                code = self.emit.emitPUTSTATIC(sym.value.value + '.' + ctx.name, sym.mtype, o.frame)
            else:
                code = self.emit.emitGETSTATIC(sym.value.value + '.' + ctx.name, sym.mtype, o.frame)
        return code, sym.mtype 

    def visitArrayCell(self, ctx ,o):
        # array ref 
        temp, tempt = self.visit(Id(ctx.name), Access(o.frame, o.sym, False))
        # index
        index, indext =  self.visit(ctx.cell, Access(o.frame, o.sym, False))
        if o.left:
            # array ref , index , value 
            code = self.emit.emitASTORE(sym.value.value, o.frame)
            return (temp, index ,code), tempt
        else : 
            code = self.emit.emitALOAD(sym.value.value, o.frame)
            return temp + index + code , tempt

    