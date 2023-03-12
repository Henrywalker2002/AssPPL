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

#     def test11(self):
#         input = """main : function void() {
#                     if (!!!!a) {
#                         a = 2;
#                     }
#                     foo(foo(a + 2));
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, Id(a))))), BlockStmt([AssignStmt(Id(a), IntegerLit(2))])), CallStmt(foo, CallStmt(foo, BinExpr(+, Id(a), IntegerLit(2))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 315))

#     def test12(self):
#         input = """main : function void() {
#                         a : array [5] of integer = {2,3,4,5,6};
#                         sum : integer = 0;
#                         for (i = 0, i < size(5), i + 1) {
#                             sum = sum + a[i];
#                         } 
#                         print(sum);
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), CallStmt(size, IntegerLit(5))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(a, [Id(i)])))])), CallStmt(print, Id(sum))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 316))

#     def test13(self):
#         input = """main : function void() {
#                     a : array[5] of integer = {2,3,4,5,6};
#                     print(sum(a));
#                 }

#                 sum : function integer (a: array [2] of integer) {
#                     temp : auto = 0;
#                     for (i = 0, i < size(a), i + 1) {
#                         temp = temp + a[i];
#                     }
#                     return temp;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), CallStmt(print, CallStmt(sum, Id(a)))]))
# 	FuncDecl(sum, IntegerType, [Param(a, ArrayType([2], IntegerType))], None, BlockStmt([VarDecl(temp, AutoType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), CallStmt(size, Id(a))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(temp), BinExpr(+, Id(temp), ArrayCell(a, [Id(i)])))])), ReturnStmt(Id(temp))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 317))

#     def test14(self):
#         input = """main : function void() {
#                     a : array[5] of integer = {2,3,4,5,6};
#                     print(sum(a));
#                 }

#                 sum : function integer (a: array [2] of integer) {
#                     i,temp : auto = 0,0;
#                     while (i < size(a)) {
#                         if (a[i] > 0) temp = temp + a[i];
#                         else return -1;
#                     }
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), CallStmt(print, CallStmt(sum, Id(a)))]))
# 	FuncDecl(sum, IntegerType, [Param(a, ArrayType([2], IntegerType))], None, BlockStmt([VarDecl(i, AutoType, IntegerLit(0)), VarDecl(temp, AutoType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), CallStmt(size, Id(a))), BlockStmt([IfStmt(BinExpr(>, ArrayCell(a, [Id(i)]), IntegerLit(0)), AssignStmt(Id(temp), BinExpr(+, Id(temp), ArrayCell(a, [Id(i)]))), ReturnStmt(UnExpr(-, IntegerLit(1))))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 318))

#     def test15(self):
#         input = """main : function void() {
#                     a : float;
#                     a = arr[5] + 2 + 3*6 < 2;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType), AssignStmt(Id(a), BinExpr(<, BinExpr(+, BinExpr(+, ArrayCell(arr, [IntegerLit(5)]), IntegerLit(2)), BinExpr(*, IntegerLit(3), IntegerLit(6))), IntegerLit(2)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 319))

#     def test16(self):
#         input = """main : function void() {
#                     foo(foo(foo(5.23e10)));
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, CallStmt(foo, CallStmt(foo, FloatLit(52300000000.0))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 320))

#     def test17(self):
#         input = """main : function void() {
#                     a,c : auto = b,foo(foo(foo(5.23e10)));
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, Id(b)), VarDecl(c, AutoType, CallStmt(foo, CallStmt(foo, CallStmt(foo, FloatLit(52300000000.0)))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 321))

#     def test18(self):
#         input = """main : function void() {
#                     a = b +c * c > d + 3.6 + (2 == 3);
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, BinExpr(+, Id(b), BinExpr(*, Id(c), Id(c))), BinExpr(+, BinExpr(+, Id(d), FloatLit(3.6)), BinExpr(==, IntegerLit(2), IntegerLit(3)))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 322))

#     def test19(self):
#         input = """main : function void() {
#                     a [2] = x + 2;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(+, Id(x), IntegerLit(2)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 323))

#     def test20(self):
#         input = """main : function void() {
#                     sum = 0;
#                     for (i = 0, i < 5, i + 1) {
#                         for (j = 0, j < 10, j+ 1) 
#                             sum = sum + a[i,j];
#                     }
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(a, [Id(i), Id(j)]))))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 324))

#     def test21(self):
#         input = """main : function void() {
#                     a, b : array[5] of integer ;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 325))

#     def test22(self):
#         input = """main : function void() {
#                     a, b : array[2] of integer = {}, {};
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], IntegerType), ArrayLit([])), VarDecl(b, ArrayType([2], IntegerType), ArrayLit([]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 326))

#     def test23(self):
#         input = """main : function void() {
#                     for (a[i] = 2, i < 2, i * 2) a[i,2] = 3;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(*, Id(i), IntegerLit(2)), AssignStmt(ArrayCell(a, [Id(i), IntegerLit(2)]), IntegerLit(3)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 327))

#     def test24(self):
#         input = """main : function void() {
#                     a = x();
#                 }

#                 x : function array[2] of string() {
#                     return {"test1", "test2\\t"};
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), CallStmt(x, ))]))
# 	FuncDecl(x, ArrayType([2], StringType), [], None, BlockStmt([ReturnStmt(ArrayLit([test1, test2\\t]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 328))

#     def test25(self):
#         input = """main : function void() {
#                         do { a = 2; } 
#                         while (true);
#                     }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(2))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 329))

#     def test26(self):
#         input = """main : function void() {
#                 foo (a[foo(3)], h+5);
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, ArrayCell(a, [CallStmt(foo, IntegerLit(3))]), BinExpr(+, Id(h), IntegerLit(5)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 330))

#     def test27(self):
#         input = """main : function void () {
#                     for (i = 0, i + 2 , i < 2) {
#                         continue;
#                     }
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(+, Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(2)), BlockStmt([ContinueStmt()]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 331))

#     def test28(self):
#         input = """main : function void () {
#                     r, s: integer;
#                     r = 2.0;
#                     a, b: array [5] of integer;
#                     s = r * r * myPI;
#                     a[0] = s;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 332))

#     def test29(self):
#         input = """x,y,z: integer = 3+2, 4+double(2,3), 6*square(1,2);"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(3), IntegerLit(2)))
# 	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(4), CallStmt(double, IntegerLit(2), IntegerLit(3))))
# 	VarDecl(z, IntegerType, BinExpr(*, IntegerLit(6), CallStmt(square, IntegerLit(1), IntegerLit(2))))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 333))
        
#     def test30(self):
#         input = """fact: function integer (n:integer){
#                         for (i = 1, i < 10, i + 1.5) {writeInt(i);}
#                     }"""
#         expect = """Program([
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), FloatLit(1.5)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 334))

#     def test31(self):
#         input = """main : function void() {
#                     a = 2 > 3 + 1*6 || 2;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, IntegerLit(2), BinExpr(||, BinExpr(+, IntegerLit(3), BinExpr(*, IntegerLit(1), IntegerLit(6))), IntegerLit(2))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 335))

#     def test32(self):
#         input = """main : function void() {
#                     a = 2 == 2;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(==, IntegerLit(2), IntegerLit(2)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 336))

#     def test32(self):
#         input = """main : function void() {

#                 }   

#                 subfunc : function boolean() {
#                     return foo(3) == 2;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# 	FuncDecl(subfunc, BooleanType, [], None, BlockStmt([ReturnStmt(BinExpr(==, CallStmt(foo, IntegerLit(3)), IntegerLit(2)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 337))

#     def test33(self):
#         input = """main : function void() {
#                     a, b : boolean = true, false;
#                 }   

#                 subfunc : function string() {
#                     return foo(3) == 2;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BooleanLit(True)), VarDecl(b, BooleanType, BooleanLit(True))]))
# 	FuncDecl(subfunc, StringType, [], None, BlockStmt([ReturnStmt(BinExpr(==, CallStmt(foo, IntegerLit(3)), IntegerLit(2)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 338))

#     def test34(self):
#         input = """main : function void() {
#                     a, b : array[2] of integer = {1,2}, foo(3); 
#                 } """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)])), VarDecl(b, ArrayType([2], IntegerType), CallStmt(foo, IntegerLit(3)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 339))

#     def test35(self):
#         input = """main : function void() {
#                     a, b : array[2] of integer = {1,2}, foo(3); 
#                 }   

#                 subfunc : function array[2] of boolean() {
#                     a : auto = {2,3} + 6;
#                 } """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)])), VarDecl(b, ArrayType([2], IntegerType), CallStmt(foo, IntegerLit(3)))]))
# 	FuncDecl(subfunc, ArrayType([2], BooleanType), [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(+, ArrayLit([IntegerLit(2), IntegerLit(3)]), IntegerLit(6)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 340))

#     def test36(self):
#         input = """main : function void() {
#                     a, b : array[2] of integer = {1,2}, foo(3); 
#                 }   

#                 subfunc : function array[2] of boolean() {
#                     return {a(3), 2 + 3};
#                 } """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)])), VarDecl(b, ArrayType([2], IntegerType), CallStmt(foo, IntegerLit(3)))]))
# 	FuncDecl(subfunc, ArrayType([2], BooleanType), [], None, BlockStmt([ReturnStmt(ArrayLit([CallStmt(a, IntegerLit(3)), BinExpr(+, IntegerLit(2), IntegerLit(3))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 341))

#     def test37(self):
#         input = """main : function void() {
#                     a, b : array[2] of integer = {1,2}, foo(3); 
#                 }   

#                 subfunc : function array[2] of boolean() {
#                     return {a(3), 2 + 3, {2,3,4}};
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)])), VarDecl(b, ArrayType([2], IntegerType), CallStmt(foo, IntegerLit(3)))]))
# 	FuncDecl(subfunc, ArrayType([2], BooleanType), [], None, BlockStmt([ReturnStmt(ArrayLit([CallStmt(a, IntegerLit(3)), BinExpr(+, IntegerLit(2), IntegerLit(3)), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)])]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 342))


#     def test38(self):
#         input = """subfunc : function void (inherit out a : string, b : array [2] of string ) inherit abc {
#                     return a;
#                 }"""
#         expect = """Program([
# 	FuncDecl(subfunc, VoidType, [InheritOutParam(a, StringType), Param(b, ArrayType([2], StringType))], abc, BlockStmt([ReturnStmt(Id(a))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 343))

#     def test39(self):
#         input = """main : function void () {
#                     a = -------2 + 4 / 5.0::c;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(+, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(2)))))))), BinExpr(/, IntegerLit(4), FloatLit(5.0))), Id(c)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 344))

#     def test40(self):
#         input = """main : function void () {
#                     a = -------_2a + 4 / 5.0::c;
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(+, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, Id(_2a)))))))), BinExpr(/, IntegerLit(4), FloatLit(5.0))), Id(c)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 345))

    def test41(self):
        input = """main : function void () {
                    a = !!!!a && b || c + 4 / 5.0::c;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(||, BinExpr(&&, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, Id(a))))), Id(b)), BinExpr(+, Id(c), BinExpr(/, IntegerLit(4), FloatLit(5.0)))), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test42(self):
        input = """main : function auto () {
                    a = (c== b) || c;
                }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(==, Id(c), Id(b)), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test43(self):
        input = """main : function void () {
                    return;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test44(self):
        input = """main : function void (out a : string) {
                    if (a[0]::b[a,foo]) return 2;
                    else {
                        break;
                        continue;
                        return; 
                    }
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritParam(a, StringType)], None, BlockStmt([IfStmt(BinExpr(::, ArrayCell(a, [IntegerLit(0)]), ArrayCell(b, [Id(a), Id(foo)])), ReturnStmt(IntegerLit(2)), BlockStmt([BreakStmt(), ContinueStmt(), ReturnStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test45(self):
        input = """main : function void (out a : string) {
                    a : array[2] of float; 
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritParam(a, StringType)], None, BlockStmt([VarDecl(a, ArrayType([2], FloatType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))