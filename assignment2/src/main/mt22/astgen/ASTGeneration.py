from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

def getType(s : str):
    if (s == "integer"):
        return IntegerType()
    elif (s == "float"):
        return FloatType()
    elif (s == "string"):
        return StringType()
    elif (s == "string"):
        return StringType()
    else: 
        return


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
            val = ctx.getChild(1)
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
        return self.visit(ctx.functiondecl())
    
    # functiondecl: IDENTIFY ':' 'function' (TYPECONST | ATOMICTYPE | arrDecl | 'void') LB paralist RB ('inherit' IDENTIFY)? body ;
    def visitFunctiondecl(self, ctx: MT22Parser.FunctiondeclContext):
        pass

    # vardecl : idenlist ':' (TYPECONST|ATOMICTYPE|arrDecl) | helper;
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.getChildCount() != 1:
            idenlst = self.visit(ctx.idenlist())
            type_ = getType(ctx.getChild(2).getText())
            return list(map(lambda x : VarDecl(x, type_), idenlst))
        temp = self.visit(ctx.helper())
        idenlst = temp[0]
        type_ = getType(temp[1][-1])
        exprlst = reversed(temp[2])
        return list(map(lambda x , y : VarDecl(x, type_, y), idenlst, exprlst))
    
    # helper : IDENTIFY COMMA helper COMMA expr | IDENTIFY COLON (TYPECONST|ATOMICTYPE|arrDecl) '=' expr; 
    def visitHelper(self, ctx: MT22Parser.HelperContext):
        if ctx.getChild(3).getText() == '=':
            return [ctx.IDENTIFY().getText()],[ctx.getChild(2).getText()],[self.visit(ctx.expr())]
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
            return FloatLit(float(ctx.BOOLLIT().getText()))
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
        return [self.visit(ctx.expr())] + self.visit(ctx.visit(ctx.exprime()))
        
    # arraylit : LP exprlist RP;
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()))

    # idenlist : IDENTIFY COMMA idenlist | IDENTIFY;
    def visitIdenlist(self, ctx: MT22Parser.IdenlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFY().getText()]
        return [(ctx.IDENTIFY().getText())] + self.visit(ctx.idenlist())
    


