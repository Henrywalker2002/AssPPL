from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

def getType(s : str):
    if (s == "integer"):
        return IntegerType()
    elif (s == "float"):
        return FloatType()
    elif (s == "string"):
        return StringType()
    elif (s == "string"):
        return StringType()
    elif (s == "void"):
        return VoidType()
    elif s == "auto":
        return AutoType()
    return None

def flatten(lst):
    res = []
    for x in lst: 
        if isinstance(x, list):
            for i in x: 
                res.append(i)
        else:
            res.append(x)
    return res

class ASTGeneration(MT22Visitor):

    def helperBinExpr(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else :
            op = ctx.getChild(1).getText()
            left = ctx.getChild(0)
            right = ctx.getChild(2)
            return BinExpr(op, self.visit(left), self.visit(right))
    
    def HelperUnExpr(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else :
            op = ctx.getChild(0)
            val = self.visit(ctx.getChild(1))
            return UnExpr(op, val)

    # program: decllist EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))

    #decllist: decl decllist | decl;
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist()) 
    
    # decl : (vardecl SEMI) | functiondecl ;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.vardecl())
        return [self.visit(ctx.functiondecl())]
    
    # parameterdecl : 'inherit'? 'out'? IDENTIFY ':' ('auto'|ATOMICTYPE | arrDecl);
    def visitParameterdecl(self, ctx: MT22Parser.ParameterdeclContext):
        inherit = False
        out = False
        if ctx.getChildCount() == 4:
            if ctx.getChild(0) == "out":
                out = True
            else :
                inherit = True
        elif ctx.getChildCount() == 5:
            out = inherit = True
        iden = ctx.IDENTIFY().getText()
        type_ = getType(ctx.getChild(-1).getText())
        if type_ is None:
            type_ = self.visit(ctx.arrDecl())
        return ParamDecl(iden, type_, out, inherit)

    # paralist : paraprime | ;
    def visitParalist(self, ctx: MT22Parser.ParalistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paraprime())

    # paraprime : parameterdecl COMMA paraprime | parameterdecl;
    def visitParaprime(self, ctx: MT22Parser.ParaprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameterdecl())]
        return [self.visit(ctx.parameterdecl())] + self.visit(ctx.paraprime())
    
    # functiondecl: IDENTIFY ':' 'function' (TYPECONST | ATOMICTYPE | arrDecl | 'void') LB paralist RB ('inherit' IDENTIFY)? body ;
    def visitFunctiondecl(self, ctx: MT22Parser.FunctiondeclContext):
        funcname = ctx.getChild(0).getText()
        type_ = getType(ctx.getChild(3).getText())
        if type_ is None:
            type_ = self.visit(ctx.arrDecl())
        paralist = self.visit(ctx.paralist())
        inheritname = None
        if len(ctx.IDENTIFY()) == 2:
            inheritname = ctx.IDENTIFY()[1]
        body = self.visit(ctx.body())
        return FuncDecl(funcname, type_, paralist, inheritname, body)
    
    # body : blockstmt;
    def visitBody(self, ctx: MT22Parser.BodyContext):
        return self.visit(ctx.blockstmt())
    
    # blockstmt: LP (stmtlist |) RP;
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        if ctx.getChildCount() == 2:
            return BlockStmt([])
        temp = self.visit(ctx.stmtlist())
        return BlockStmt(temp)
    
    # stmtlist: stmt stmtlist | stmt;
    def visitStmtlist(self, ctx: MT22Parser.StmtlistContext):
        temp = self.visit(ctx.stmt())
        if ctx.getChildCount() == 1:
            return temp if isinstance(temp, list) else [temp]
        return (temp if isinstance(temp, list) else [temp]) + self.visit(ctx.stmtlist())
    
    #stmt: (('break'|'continue'|returnstmt|assignstmt|dowhilestmt|funccallstmt|vardecl) SEMI)|(blockstmt|forstmt|ifstmt|whilestmt);
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.getChild(0).getText() == 'break':
            return BreakStmt()
        elif ctx.getChild(0).getText() == 'continue':
            return ContinueStmt()
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.dowhilestmt():
            return self.visit(ctx.dowhilestmt())
        elif ctx.funccallstmt():
            return self.visit(ctx.funccallstmt())
        elif ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.whilestmt():
            return self.visit(ctx.whilestmt())
    
    # returnstmt: 'return' expr?;
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        expr = None
        if ctx.getChildCount() == 2:
            expr = self.visit(ctx.expr())
        return ReturnStmt(expr)

    # exprIndex : IDENTIFY '[' exprlist ']';
    def visitExprIndex(self, ctx: MT22Parser.ExprIndexContext):
        name = ctx.IDENTIFY().getText()
        exprlst = ctx.visit(ctx.exprlist())
        return ArrayCell(name, exprlst)

    # assignstmt : (IDENTIFY|exprIndex) '=' expr;
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        lhs = None
        if ctx.IDENTIFY():
            lhs = Id(ctx.IDENTIFY().getText())
        else :
            lhs = self.visit(ctx.exprIndex())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)
    
    # dowhilestmt: 'do' blockstmt 'while' expr;
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.blockstmt())
        return DoWhileStmt(cond, stmt)
    
    # funccallstmt : IDENTIFY LB (exprlist) RB;
    def visitFunccallstmt(self, ctx: MT22Parser.FunccallstmtContext):
        name = ctx.IDENTIFY().getText()
        exprlst = self.visit(ctx.exprlist())
        return CallStmt(name, exprlst)
    
    # forstmt: 'for' LB (IDENTIFY|exprIndex) '=' INTLIT COMMA expr COMMA expr RB stmt;
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        stmt  = self.visit(ctx.stmt())
        lhs = None
        if ctx.IDENTIFY():
            lhs = Id(ctx.IDENTIFY().getText())
        else :
            lhs = self.visit(ctx.exprIndex())
        rhs = IntegerLit(int(ctx.INTLIT().getText()))
        init = AssignStmt(lhs, rhs)
        exprlst = ctx.expr()
        cond = self.visit(exprlst[0])
        expr = self.visit(exprlst[1])
        return ForStmt(init, cond, expr, stmt)

    # ifstmt : 'if' LB expr RB stmt ('else' stmt)?;
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        cond = self.visit(ctx.expr())
        tstmt, fstmt = None, None
        if ctx.getChildCount() == 5:
            tstmt = self.visit(ctx.stmt()[0])
        else :
            tstmt = self.visit(ctx.stmt()[0])
            fstmt = self.visit(ctx.stmt()[1])
        return IfStmt(cond, tstmt, fstmt)
    
    # whilestmt: 'while' LB expr RB stmt;
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(cond, stmt)

    # arrDecl : 'array' '[' intlst ']' 'of' ATOMICTYPE;
    def visitArrDecl(self, ctx: MT22Parser.ArrDeclContext):
        dimen = self.visit(ctx.intlst())
        type_ = getType(ctx.getChild(-1).getText())
        return ArrayType(dimen, type_)
    
    # intlst : INTLIT COMMA intlst | INTLIT;
    def visitIntlst(self, ctx: MT22Parser.IntlstContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.intlst())

    # vardecl : idenlist ':' (TYPECONST|ATOMICTYPE|arrDecl) | helper;
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.getChildCount() != 1:
            idenlst = self.visit(ctx.idenlist())
            type_ = getType(ctx.getChild(2).getText())
            if type_ is None:
                type_ = self.visit(ctx.arrDecl())
            return list(map(lambda x : VarDecl(x, type_), idenlst))
        temp = self.visit(ctx.helper())
        idenlst = temp[0]
        type_ = temp[1][-1]
        exprlst = reversed(temp[2])
        return list(map(lambda x , y : VarDecl(x, type_, y), idenlst, exprlst))
    
    # helper : IDENTIFY COMMA helper COMMA expr | IDENTIFY COLON (TYPECONST|ATOMICTYPE|arrDecl) '=' expr; 
    def visitHelper(self, ctx: MT22Parser.HelperContext):
        if ctx.getChild(3).getText() == '=':
            type_ = getType(ctx.getChild(2).getText())
            if type_ is None:
                type_ = self.visit(ctx.arrDecl())
            return [ctx.IDENTIFY().getText()],[type_],[self.visit(ctx.expr())]
        temp = self.visit(ctx.helper())
        return [ctx.IDENTIFY().getText()] + temp[0],[None] + temp[1],[self.visit(ctx.expr())] + temp[2]

    # expr : expr2 '::' expr2 | expr2;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        return self.helperBinExpr(ctx)
    
    #expr2 : expr3 (EQ|NE|LT|GT|LE|GE) expr3 | expr3; 
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        return self.helperBinExpr(ctx)
    
    # expr3 : expr3 (AND|OR) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        return self.helperBinExpr(ctx)

    # expr4 : expr4 (ADDOP|SUBOP) expr5 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        return self.helperBinExpr(ctx)
    
    # expr5 : expr5 (MULOP|DIVOP|REMAINOP) expr6 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        return self.helperBinExpr(ctx)

    # expr6 : NEG expr6 | expr7 ;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        return self.HelperUnExpr(ctx)
    
    # expr7 : SUBOP expr7 | expr8 ;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        return self.HelperUnExpr(ctx)
    
    # expr8 : IDENTIFY '[' exprlist ']' | expr9;
    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return ArrayCell(ctx.IDENTIFY().getText(), self.visit(ctx.exprlist()))

    # expr9 : IDENTIFY | STRINGLIT | INTLIT | FLOATLIT | BOOLLIT | arraylit | funccallstmt| (LB expr RB);
    def visitExpr9(self, ctx: MT22Parser.Expr9Context):
        if ctx.IDENTIFY():
            return Id(ctx.IDENTIFY().getText())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLit(bool(ctx.BOOLLIT().getText()))
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.funccallstmt():
            return self.visit(ctx.funccallstmt())
        return self.visit(ctx.expr())

    # exprlist : exprime | ;
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprime())
        return []

    # exprime : expr COMMA exprime | expr;
    def visitExprime(self, ctx: MT22Parser.ExprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprime())
        
    # arraylit : LP exprlist RP;
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()))

    # idenlist : IDENTIFY COMMA idenlist | IDENTIFY;
    def visitIdenlist(self, ctx: MT22Parser.IdenlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFY().getText()]
        return [(ctx.IDENTIFY().getText())] + self.visit(ctx.idenlist())