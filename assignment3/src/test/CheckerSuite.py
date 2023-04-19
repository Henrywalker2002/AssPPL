import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_short_vardecl(self):
    #     input = """x: integer;"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 300))

    # def test_full_vardecl(self):
    #     input = """x, y, z: integer = 1, 2, 3;"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 301))

    # def test_vardecls(self):
    #     input = """x, y, z: integer = 1, 2, 3;
    #     a, b: float;"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 302))

    # def test_simple_program(self):
    #     """Simple program"""
    #     input = """main: function void () {
    #     }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 303))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """main: function void () {
    #         printInteger(4);
    #     }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 304))
        
    # def test1(self):
    #     input = """x: integer = 65;
    #     fact: function integer (n: integer) {
    #         if (n == 0) return 1;
    #         else return n * fact(n - 1);
    #     }
    #     inc: function void(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = fact(3);
    #         inc(x, delta);
    #         printInteger(x);
    #     }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 305))
    
    
    # def test2(self):
    #     input = """a, b, c: integer = 3, 4, 6;"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 306))
    
    # def test3(self):
    #     input = """main: function void() {
    #         sum : integer  = 0;
    #         for (i = 0, i < b, i +1 ) sum = sum + 2;
    #     }"""
    #     expect = """Undeclared Variable: i"""
    #     self.assertTrue(TestChecker.test(input, expect, 307))

    # def test4(self):
    #     input = """a: array [3] of string;"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 308))

    # def test5(self):
    #     input = """ a : array [2,3] of string;"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 309))

    # def test6(self):
    #     input = """fact : function integer (n :integer) {
    #                 if (n == 1) return 1;
    #                 else return n*fact(n-1);
    #             }
    #             main : function void() {
    #                 print(fact(5));
    #             }"""
    #     expect = """Undeclared Function: print"""
    #     self.assertTrue(TestChecker.test(input, expect, 310))

    # def test7(self):
    #     input = """main : function void() {
    #                 do {
    #                     a = a + 1;
    #                 }
    #                 while (true);
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 311))

    # def test8(self):
    #     input = """main : function void() {
    #                     while (true) a = a +2;
    #                     while (true) {
    #                         while (a > b) {
    #                             a = a + 1;
    #                         }
    #                     }
    #                 }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 312))

    # def test9(self):
    #     input = """main : function void() {
    #                 if ((a > 2) || (b > 2) && (a - 2)) {
    #                     break;
    #                     continue;
    #                 }
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 313))

    # def test10(self):
    #     input = """a : array[3] of integer = {2,3};"""
    #     expect = """Illegal array literal: ArrayLit([IntegerLit(2), IntegerLit(3)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 314))

    # def test11(self):
    #     input = """main : function void() {
    #                 if (!!!!a) {
    #                     a = 2;
    #                 }
    #                 foo(foo(a + 2));
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 315))

    # def test12(self):
    #     input = """main : function void() {
    #                     a : array [5] of integer = {2,3,4,5,6};
    #                     sum : integer = 0;
    #                     for (i = 0, i < size(5), i + 1) {
    #                         sum = sum + a[i];
    #                     } 
    #                     print(sum);
    #             }"""
    #     expect = """Undeclared Variable: i"""
    #     self.assertTrue(TestChecker.test(input, expect, 316))

    # def test13(self):
    #     input = """main : function void() {
    #                 a : array[5] of integer = {2,3,4,5,6};
    #                 print(sum(a));
    #             }
    #             sum : function integer (a: array [2] of integer) {
    #                 temp : auto = 0;
    #                 for (i = 0, i < size(a), i + 1) {
    #                     temp = temp + a[i];
    #                 }
    #                 return temp;
    #             }"""
    #     expect = """Undeclared Function: print"""
    #     self.assertTrue(TestChecker.test(input, expect, 317))

    # def test14(self):
    #     input = """main : function void() {
    #                 a : array[5] of integer = {2,3,4,5,6};
    #                 print(sum(a));
    #             }
    #             sum : function integer (a: array [2] of integer) {
    #                 i,temp : auto = 0,0;
    #                 while (i < size(a)) {
    #                     if (a[i] > 0) temp = temp + a[i];
    #                     else return -1;
    #                 }
    #             }"""
    #     expect = """Undeclared Function: print"""
    #     self.assertTrue(TestChecker.test(input, expect, 318))

    # def test15(self):
    #     input = """main : function void() {
    #                 a : float;
    #                 a = arr[5] + 2 + 3*6 < 2;
    #             }"""
    #     expect = """Undeclared Variable: arr"""
    #     self.assertTrue(TestChecker.test(input, expect, 319))

    # def test16(self):
    #     input = """main : function void() {
    #                 foo(foo(foo(5.23e10)));
    #             }"""
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 320))

    # def test17(self):
    #     input = """main : function void() {
    #                 a,c : auto = b,foo(foo(foo(5.23e10)));
    #             }"""
    #     expect = """Undeclared Variable: b"""
    #     self.assertTrue(TestChecker.test(input, expect, 321))

    # def test18(self):
    #     input = """main : function void() {
    #                 a = b +c * c > d + 3.6 + (2 == 3);
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 322))

    # def test19(self):
    #     input = """main : function void() {
    #                 a [2] = x + 2;
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 323))

    # def test20(self):
    #     input = """main : function void() {
    #                 sum = 0;
    #                 for (i = 0, i < 5, i + 1) {
    #                     for (j = 0, j < 10, j+ 1) 
    #                         sum = sum + a[i,j];
    #                 }
    #             }"""
    #     expect = """Undeclared Variable: sum"""
    #     self.assertTrue(TestChecker.test(input, expect, 324))

    # def test21(self):
    #     input = """main : function void() {
    #                 a, b : array[5] of integer ;
    #             }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 325))

    # def test22(self):
    #     input = """main : function void() {
    #                 a, b : array[2] of integer = {}, {};
    #             }"""
    #     expect = """Illegal array literal: ArrayLit([])"""
    #     self.assertTrue(TestChecker.test(input, expect, 326))

    # def test23(self):
    #     input = """main : function void() {
    #                 for (a[i] = 2, i < 2, i * 2) a[i,2] = 3;
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 327))

    # def test24(self):
    #     input = """main : function void() {
    #                 a = x();
    #             }
    #             x : function array[2] of string() {
    #                 return {"test1", "test2\\t"};
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 328))

    # def test25(self):
    #     input = """main : function void() {
    #                     do { a = 2; } 
    #                     while (true);
    #                 }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 329))

    # def test26(self):
    #     input = """main : function void() {
    #             foo (a[foo(3)], h+5);
    #         }"""
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 330))

    # def test27(self):
    #     input = """main : function void () {
    #                 for (i = 0, i + 2 , i < 2) {
    #                     continue;
    #                 }
    #             }"""
    #     expect = """Undeclared Variable: i"""
    #     self.assertTrue(TestChecker.test(input, expect, 331))

    # def test28(self):
    #     input = """main : function void () {
    #                 r, s: integer;
    #                 r = 2.0;
    #                 a, b: array [5] of integer;
    #                 s = r * r * myPI;
    #                 a[0] = s;
    #             }"""
    #     expect = """Type mismatch in statement: AssignStmt(Id(r), FloatLit(2.0))"""
    #     self.assertTrue(TestChecker.test(input, expect, 332))

    # def test29(self):
    #     input = """x,y,z: integer = 3+2, 4+double(2,3), 6*square(1,2);"""
    #     expect = """Undeclared Function: double"""
    #     self.assertTrue(TestChecker.test(input, expect, 333))
        
    # def test30(self):
    #     input = """fact: function integer (n:integer){
    #                     for (i = 1, i < 10, i + 1.5) {writeInt(i);}
    #                 }"""
    #     expect = """Undeclared Variable: i"""
    #     self.assertTrue(TestChecker.test(input, expect, 334))

    # def test31(self):
    #     input = """main : function void() {
    #                 a = 2 > 3 + 1*6 || 2;
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 335))

    # def test32(self):
    #     input = """main : function void() {
    #                 a = 2 == 2;
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 336))

    # def test32(self):
    #     input = """main : function void() {
    #             }   
    #             subfunc : function boolean() {
    #                 return foo(3) == 2;
    #             }"""
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 337))

    # def test33(self):
    #     input = """main : function void() {
    #                 a, b : boolean = true, false;
    #             }   
    #             subfunc : function string() {
    #                 return foo(3) == 2;
    #             }"""
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 338))

    # def test34(self):
    #     input = """main : function void() {
    #                 a, b : array[2] of integer = {1,2}, foo(3); 
    #             } """
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 339))

    # def test35(self):
    #     input = """main : function void() {
    #                 a, b : array[2] of integer = {1,2}, foo(3); 
    #             }   
    #             subfunc : function array[2] of boolean() {
    #                 a : auto = {2,3} + 6;
    #             } """
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 340))

    # def test36(self):
    #     input = """main : function void() {
    #                 a, b : array[2] of integer = {1,2}, foo(3); 
    #             }   
    #             subfunc : function array[2] of boolean() {
    #                 return {a(3), 2 + 3};
    #             } """
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 341))

    # def test37(self):
    #     input = """main : function void() {
    #                 a, b : array[2] of integer = {1,2}, foo(3); 
    #             }   
    #             subfunc : function array[2] of boolean() {
    #                 return {a(3), 2 + 3, {2,3,4}};
    #             }"""
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 342))


    # def test38(self):
    #     input = """subfunc : function void (inherit out a : string, b : array [2] of string ) inherit abc {
    #                 return a;
    #             }"""
    #     expect = """Undeclared Function: abc"""
    #     self.assertTrue(TestChecker.test(input, expect, 343))

    # def test39(self):
    #     input = """main : function void () {
    #                 a = -------2 + 4 / 5.0::c;
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 344))

    # def test40(self):
    #     input = """main : function void () {
    #                 a = -------_2a + 4 / 5.0::c;
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 345))

    # def test41(self):
    #     input = """main : function void () {
    #                 a = !!!!a && b || c + 4 / 5.0::c;
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 346))

    # def test42(self):
    #     input = """main : function auto () {
    #                 a = (c== b) || c;
    #             }"""
    #     expect = """Undeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 347))

    # def test43(self):
    #     input = """main : function void () {
    #                 return;
    #             }"""
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 348))

    # def test44(self):
    #     input = """main : function void (out a : string) {
    #                 if (a[0]::b[a,foo]) return 2;
    #                 else {
    #                     break;
    #                     continue;
    #                     return; 
    #                 }
    #             }"""
    #     expect = """Type mismatch in expression: ArrayCell(a, [IntegerLit(0)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 349))

    # def test45(self):
    #     input = """main : function void (out a : string) {
    #                 a : array[2] of float; 
    #             }"""
    #     expect = """Redeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 350))

#     def test46(self):
#         input = """x,y,z: integer = 3, 4, 6;
#             fact:function integer(n:integer)
#             {
#                 if((n==0)||(n==1)||(n==2)) return 1;
#                 result:integer=1;
#                 a:integer=1;
#                 b:integer=1;
#                 while(n>2)
#                 {
#                     result=a+b;
#                     a=b;
#                     b=result;
#                     n=n-1;
#                 }
#                 return result;
#             }
#             fact: function integer (n: integer) {
#                 if (n == 0) return 1;
#                 else return n * fact(n - 1);
#             }
#             inc: function void(out n: integer, delta: integer) {
#                 n = n + delta;
#             }
#             main: function void() {
#                 delta: integer = fact(3);
#                 inc(x, delta);
#                 printInteger(x);
#             }"""
#         expect = """Redeclared Function: fact"""
#         self.assertTrue(TestChecker.test(input, expect, 351))

#     def test47(self):
#         input = """main: function void () {
#     if (true) 
#         while (false) 
#             return;
#     continue;
# }"""
#         expect = """Must in loop: ContinueStmt()"""
#         self.assertTrue(TestChecker.test(input, expect, 352))

#     def test48(self):
#         input = """main: function void () {
#             a : boolean = true;
#             {
#                 a : string;
#                 a = "";
#             }
#             a = "";
#         }
#             """
#         expect = """Type mismatch in statement: AssignStmt(Id(a), StringLit())"""
#         self.assertTrue(TestChecker.test(input, expect, 353))

#     def test49(self):
#         input = """main: function void () {
#     do {a = a + 3;}
#     while (a == 2);
# }"""
#         expect = """Undeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input, expect, 354))

#     def test50(self):
#         input = """main: function void () {
#     do {a = a + 3;
#         do { }
#         while (a && b);
#         }
#     while (a == 2);
# }"""
#         expect = """Undeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input, expect, 355))

#     def test51(self):
#         input = """main: function void () {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = 2;
#     }
# }"""
#         expect = """Undeclared Variable: i"""
#         self.assertTrue(TestChecker.test(input, expect, 356))

#     def test52(self):
#         input = """main: function void () {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = 2 + foo(a + b / k * l);
#     }
# }"""
#         expect = """Undeclared Variable: i"""
#         self.assertTrue(TestChecker.test(input, expect, 357))

#     def test53(self):
#         input = """main: function void () {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = 2;
#             continue;
#     }
# }"""
#         expect = """Undeclared Variable: i"""
#         self.assertTrue(TestChecker.test(input, expect, 358))

#     def test54(self):
#         input = """main: function void () inherit abc {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = (2 > 2);
#             continue;
#     }
# }"""
#         expect = """Undeclared Function: abc"""
#         self.assertTrue(TestChecker.test(input, expect, 359))

#     def test55(self):
#         input = """main: function void () inherit abc {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = (2 > 2);
#             continue;
#             if (a + 2) {
#                 return main();
#             }
#     }
# }"""
#         expect = """Undeclared Function: abc"""
#         self.assertTrue(TestChecker.test(input, expect, 360))

#     def test56(self):
#         input = """main: function void (out b : string) inherit abc {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = (2 > 2);
#             continue;
#             if (a + 2) {
#                 return main();
#             }
#     }
# }"""
#         expect = """Undeclared Function: abc"""
#         self.assertTrue(TestChecker.test(input, expect, 361))

#     def test57(self):
#         input = """main: function void (out b : string, a : array[3] of float) inherit abc {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = (2 > 2);
#             continue;
#             if (a + 2) {
#                 return main();
#             }
#     }
# }"""
#         expect = """Undeclared Function: abc"""
#         self.assertTrue(TestChecker.test(input, expect, 362))

#     def test58(self):
#         input = """main: function void (out b : string, a : array[3, 4] of boolean) inherit abc {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = (2 > 2);
#             continue;
#             if (a + 2) {
#                 return main();
#             }
#     }
# }"""
#         expect = """Undeclared Function: abc"""
#         self.assertTrue(TestChecker.test(input, expect, 363))

#     def test59(self):
#         input = """main: function void (out b : string, a : array[3, 4] of integer) inherit abc {
#     for (i = 2, i < 3, i + 3) {
#         while (true) 
#             a = (2 > 2);
#             continue;
#             if (a + 2) {
#                 return main();
#             }
#             break;
#     }
# }"""
#         expect = """Undeclared Function: abc"""
#         self.assertTrue(TestChecker.test(input, expect, 364))

#     def test60(self):
#         input = """main: function void (out b : string, a : array[3, 4] of integer) inherit abc {
#     for (i = 2, i < 3, i + 3) {
#         b : integer = 3;
#         while (true) 
#             a = (2 > 2);
#             continue;
#             if (a + 2) {
#                 return main();
#             }
#             break;
#     }
# }"""
#         expect = """Undeclared Function: abc"""
#         self.assertTrue(TestChecker.test(input, expect, 365))

#     def test61(self):
#         input = """main : function boolean() {
    
# }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 366))

#     def test62(self):
#         input = """main : function array [5] of integer() {
    
# }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 367))

#     def test63(self):
#         input = """main : function auto() {
    
# }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 368))

#     def test64(self):
#         input = """main : function float() {
    
# }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 369))

#     def test65(self):
#         input = """main : function auto() {
    
#         }
        
#         foo : function void() {
#             main();
#         }
#         """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 370))

    def test66(self):
        input = """main : function string() {
            a : integer = {a,b, foo(a)};
}"""
        expect = """Illegal array literal: ArrayLit([Id(a), Id(b), FuncCall(foo, [Id(a)])])"""
        self.assertTrue(TestChecker.test(input, expect, 371))

    def test67(self):
        input = """main : function string() {
            a,b,c,d : auto = {a,b, foo(a)}, 2,3, "abc\\n";
}"""
        expect = """Illegal array literal: ArrayLit([Id(a), Id(b), FuncCall(foo, [Id(a)])])"""
        self.assertTrue(TestChecker.test(input, expect, 372))

    def test68(self):
        input = """main : function string() {
            a : integer = {a,b, foo(a)};
}
        b : string = {a,c,d};
"""
        expect = """Illegal array literal: ArrayLit([Id(a), Id(b), FuncCall(foo, [Id(a)])])"""
        self.assertTrue(TestChecker.test(input, expect, 373))

    def test69(self):
        input = """main : function string() {
            a : integer = {a,b, foo(a)};
}
        b : auto = {a,c,d};
"""
        expect = """Illegal array literal: ArrayLit([Id(a), Id(b), FuncCall(foo, [Id(a)])])"""
        self.assertTrue(TestChecker.test(input, expect, 374))

    def test70(self):
        input = """main : function string(inherit out a : auto) {
            a : integer = {a,b, foo(a)};
}
        b : auto = {a,c,d};
"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 375))
        
    def test71(self):
        input = """main : function string(inherit out a : auto) {
            foo();
        }
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 376))
        
    def test72(self):
        input = """main : function string(inherit out a : auto) {
            a = foo() + bc;
        }
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 377))

    def test73(self):
        input = """main : function string(inherit out a : auto) {
            while(full()) {
                continue;
            }
        }
"""
        expect = """Undeclared Function: full"""
        self.assertTrue(TestChecker.test(input, expect, 378))

    def test74(self):
        input = """main : function string(inherit out a : auto) {
            if (foo(2)) {
                return 1;
            }
        }
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 379))

    def test75(self):
        input = """main : function string(inherit out a : auto) {
            do {
                    
            }
            while (foo(foo(3)));
        }
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 380))

    def test76(self):
        input = """main : function string(inherit out a : auto) {
            do {
                    
            }
            while (foo(foo(3)) + foo(5));
        }
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 381))

    def test77(self):
        input = """main : function string(inherit out a : auto) {
            do {
                    
            }
            while (foo(foo(3)) + foo(5));
        }
        b : string = foo();
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 382))

    def test78(self):
        input = """main : function string(inherit out a : auto) {
            do {
                c : auto = abc();
            }
            while (foo(foo(3)) + foo(5));
        }
        b : string = foo();
"""
        expect = """Undeclared Function: abc"""
        self.assertTrue(TestChecker.test(input, expect, 383))

    def test79(self):
        input = """main : function string(inherit out a : auto) {
            do {
                c : auto = abc() + bc / cl;
            }
            while (foo(foo(3)) + foo(5));
        }
        b : string = foo();
"""
        expect = """Undeclared Function: abc"""
        self.assertTrue(TestChecker.test(input, expect, 384))

    def test80(self):
        input = """main : function string(inherit out a : auto) {
            do {
                c : auto = abc() + bc / -cl;
            }
            while (foo(foo(3)) + foo(5));
        }
        b : string = foo();
"""
        expect = """Undeclared Function: abc"""
        self.assertTrue(TestChecker.test(input, expect, 385))

    def test81(self):
        input = """
                r, s: integer;
                a, b: array [5] of integer;
"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 386))

    def test82(self):
        input = """
fact: function  array [1,2] of integer (out  n: integer) inherit ant{
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 387))

    def test83(self):
        input = """
fact: function  array [1,2, 1, 2] of integer (out  n: integer) inherit ant{
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 388))

    def test84(self):
        input = """
fact :  function  array [1,2, 1, 2] of integer (inherit out  n: integer) inherit ant{
                if (n == 0) return 1;
                else return n * fact(n - 1) / b;
                }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 389))

    def test85(self):
        input = """
fact: function  array [5] of string (inherit out n: integer) inherit ant{
                if (n == 0) return 1 + abc();
                else return n * fact(n - 1) / abc;
                }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 390))

    def test86(self):
        input = """
fact: function  array [5] of string (inherit out n: integer, a : array[5] of string) inherit ant{
                if (n == 0) return 1 + abc();
                else return n * fact(n - 1) / abc;
                }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 391))

    def test87(self):
        input = """
fact: function  array [5] of string (inherit out n: integer, out a : array[5] of string) inherit ant{
                if (n == 0) return 1 + abc();
                else return n * fact(n - 1) / abc;
                }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 392))


    def test88(self):
        input = """
fact: function  array [5] of string (inherit out n: integer, out a : array[5] of string) inherit ant{
                while (1) return 2;
        }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 393))

    def test89(self):
        input = """
fact: function  array [5] of string (inherit out n: integer, out a : array[5] of string) inherit ant{
                while (1) return 2;
                a = a -- b;
                }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 394))

    def test90(self):
        input = """
fact: function  array [5] of string (inherit out n: integer, out a : array[5] of string) inherit ant{
                while (1) return 2;
                a = a -- c * b;
                }
"""
        expect = """Undeclared Function: ant"""
        self.assertTrue(TestChecker.test(input, expect, 395))

    def test91(self):
        input = """
max : function integer (a: array [4] of integer) {
                    temp : auto = a[0];
                    for (i = 1, i < size(a), i + 1) {
                        if (a[i]>temp)
                        temp = a[i];
                    }
                    return temp;
                }
"""
        expect = """Undeclared Variable: i"""
        self.assertTrue(TestChecker.test(input, expect, 396))

    def test92(self):
        input = """
max : function integer (a: array [2] of integer) {
                    temp : auto = a[0];
                    for (i = 1, i < size(a), i + 1) {
                        if (a[i]>temp)
                        temp = a[i];
                    }
                    return temp();
                }
"""
        expect = """Undeclared Variable: i"""
        self.assertTrue(TestChecker.test(input, expect, 397))

    def test93(self):
        input = """
        main : function void () {
                if (1 == 2) {
                        return true;
                }
        }
"""
        expect = """Type mismatch in statement: ReturnStmt(BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 398))

    def test94(self):
        input = """
        main : function void () {
                if (foo(2) == foo(3)) {
                        return true;
                }
        }
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 399))

    def test95(self):
        input = """
        main : function void () {
                if (foo(2) == foo(3)) {
                        return foo(2) == foo(3);
                }
        }
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 400))