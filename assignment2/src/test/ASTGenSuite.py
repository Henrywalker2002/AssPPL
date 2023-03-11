import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
#     def test_short_vardecl(self):
#         input = """x: integer;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType)
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 300))

#     def test_full_vardecl(self):
#         input = """x, y, z: integer = 1, 2, 3;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, IntegerLit(3))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 301))

#     def test_vardecls(self):
#         input = """x, y, z: integer = 1, 2, 3;
#         a, b: float;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, IntegerLit(3))
# 	VarDecl(a, FloatType)
# 	VarDecl(b, FloatType)
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 302))

#     def test_simple_program(self):
#         """Simple program"""
#         input = """main: function void () {
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 303))

#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))
        
#     def test1(self):
#         input = """x: integer = 65;
#         fact: function integer (n: integer) {
#             if (n == 0) return 1;
#             else return n * fact(n - 1);
#         }
#         inc: function void(out n: integer, delta: integer) {
#             n = n + delta;
#         }
#         main: function void() {
#             delta: integer = fact(3);
#             inc(x, delta);
#             printInteger(x);
#         }"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(65))
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), CallStmt(fact, BinExpr(-, Id(n), IntegerLit(1))))))]))
# 	FuncDecl(inc, VoidType, [InheritParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, CallStmt(fact, IntegerLit(3))), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 305))
    
    
#     def test2(self):
#         input = """a, b, c: integer = 3, 4, 6;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, IntegerLit(3))
# 	VarDecl(b, IntegerType, IntegerLit(4))
# 	VarDecl(c, IntegerType, IntegerLit(6))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 306))
    
#     def test3(self):
#         input = """main: function void() {
#             sum : integer  = 0;
#             for (i = 0, i < b, i +1 ) sum = sum + 2;
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(b)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), IntegerLit(2))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 307))

#     def test4(self):
#         input = """a: array [3] of string;"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([3], StringType))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 308))

#     def test5(self):
#         input = """ a : array [2,3] of string;"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([2, 3], StringType))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 309))

#     def test6(self):
#         input = """fact : function integer (n :integer) {
#                     if (n == 1) return 1;
#                     else return n*fact(n-1);
#                 }

#                 main : function void() {
#                     print(fact(5));
#                 }"""
#         expect = """Program([
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), CallStmt(fact, BinExpr(-, Id(n), IntegerLit(1))))))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, CallStmt(fact, IntegerLit(5)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 310))

#     def test7(self):
#         input = """main : function void() {
#                     do {
#                         a = a + 1;
#                     }
#                     while (true);
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 311))

#     def test8(self):
#         input = """main : function void() {
#                         while (true) a = a +2;
#                         while (true) {
#                             while (a > b) {
#                                 a = a + 1;
#                             }
#                         }
#                     }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2)))), WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 312))

#     def test9(self):
#         input = """main : function void() {
#                     if ((a > 2) || (b > 2) && (a - 2)) {
#                         break;
#                         continue;
#                     }
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(||, BinExpr(>, Id(a), IntegerLit(2)), BinExpr(>, Id(b), IntegerLit(2))), BinExpr(-, Id(a), IntegerLit(2))), BlockStmt([BreakStmt(), ContinueStmt()]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 313))

#     def test10(self):
#         input = """a : array[3] of integer = {2,3};"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3)]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 314))

    def test11(self):
        input = """main : function void() {
                    if (!!!!a) {
                        a = 2;
                    }
                    foo(foo(a + 2));
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, Id(a))))), BlockStmt([AssignStmt(Id(a), IntegerLit(2))])), CallStmt(foo, CallStmt(foo, BinExpr(+, Id(a), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test12(self):
        input = """main : function void() {
                        a : array [5] of integer = {2,3,4,5,6};
                        sum : integer = 0;
                        for (i = 0, i < size(5), i + 1) {
                            sum = sum + a[i];
                        } 
                        print(sum);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), CallStmt(size, IntegerLit(5))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(a, [Id(i)])))])), CallStmt(print, Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test13(self):
        input = """main : function void() {
                    a : array[5] of integer = {2,3,4,5,6};
                    print(sum(a));
                }

                sum : function integer (a: array [2] of integer) {
                    temp : auto = 0;
                    for (i = 0, i < size(a), i + 1) {
                        temp = temp + a[i];
                    }
                    return temp;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), CallStmt(print, CallStmt(sum, Id(a)))]))
	FuncDecl(sum, IntegerType, [Param(a, ArrayType([2], IntegerType))], None, BlockStmt([VarDecl(temp, AutoType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), CallStmt(size, Id(a))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(temp), BinExpr(+, Id(temp), ArrayCell(a, [Id(i)])))])), ReturnStmt(Id(temp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test14(self):
        input = """main : function void() {
                    a : array[5] of integer = {2,3,4,5,6};
                    print(sum(a));
                }

                sum : function integer (a: array [2] of integer) {
                    i,temp : auto = 0,0;
                    while (i < size(a)) {
                        if (a[i] > 0) temp = temp + a[i];
                        else return -1;
                    }
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), CallStmt(print, CallStmt(sum, Id(a)))]))
	FuncDecl(sum, IntegerType, [Param(a, ArrayType([2], IntegerType))], None, BlockStmt([VarDecl(i, AutoType, IntegerLit(0)), VarDecl(temp, AutoType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), CallStmt(size, Id(a))), BlockStmt([IfStmt(BinExpr(>, ArrayCell(a, [Id(i)]), IntegerLit(0)), AssignStmt(Id(temp), BinExpr(+, Id(temp), ArrayCell(a, [Id(i)]))), ReturnStmt(UnExpr(-, IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test15(self):
        input = """main : function void() {
                    a : float;
                    a = arr[5] + 2 + 3*6 < 2;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), CallStmt(print, CallStmt(sum, Id(a)))]))
	FuncDecl(sum, IntegerType, [Param(a, ArrayType([2], IntegerType))], None, BlockStmt([VarDecl(i, AutoType, IntegerLit(0)), VarDecl(temp, AutoType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), CallStmt(size, Id(a))), BlockStmt([IfStmt(BinExpr(>, ArrayCell(a, [Id(i)]), IntegerLit(0)), AssignStmt(Id(temp), BinExpr(+, Id(temp), ArrayCell(a, [Id(i)]))), ReturnStmt(UnExpr(-, IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))