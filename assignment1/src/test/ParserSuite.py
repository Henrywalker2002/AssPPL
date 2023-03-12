import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """delta: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test_simple_program2(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program3(self):
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    
    def test_simple_program4(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    
    def test_program5(self):
        input = """ a,b,c,d : integer = 1,2,3 ; """
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_program5(self):
        input = """ a,b,c,d : integer = 1,2,3 ; """
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_program6(self):
        input = """ main: function void() {
            sum : integer  = 0;
            for (i = 0, i < b, i +1 ) sum = sum + 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    
    def test_program7(self):
        input = """a: array [3] of string;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    
    def testprogram8(self):
        input = """ a : array [2,3] of string;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    
    def testprogram9(self):
        input = """x: function integer (out a: integer, inherit b : string) {
                    while (true) {
                        break;
                    }
                    a : string = 2
                }"""
        expect = "Error on line 6 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 209))

    # test if stmt
    
    def testprogram10(self):
        input = """x: function integer (out a: integer, inherit b : string) {
                        a : integer = b[2,3];
                        if (a == 2) {
                            return true;
                        }
                        else {
                            return false
                        }
                    }"""
        expect = "Error on line 8 col 24: }"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    
    def testprogram11(self):
        input = """x : function void() {
                    if ((a == 2) && (b == 2)) {
                        return true;
                    }
                    if (a == 2 && b == 2) {
                        return false;
                    }
                }"""
        expect = "Error on line 5 col 36: =="
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def testprogram12(self):
        input = """fact : function integer (n :integer) {
                    if (n == 1) return 1;
                    else return n*fact(n-1);
                }

                main : function void() {
                    print(fact(5));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    
    def testprogram13(self):
        input = """fact : function integer (n :integer) inherit temp {
                    if (n == 1) return 1;
                    else return n*fact(n-1);
                }
                main : function void() {
                    print(fact(5));
                    a,b : string = a,c,d;
                }"""
        expect = "Error on line 7 col 38: ,"
        self.assertTrue(TestParser.test(input, expect, 213))

    def testprogram14(self):
        input = """fact : function integer (n :integer) inherit 1 {
                    if (n == 1) return 1;
                    else return n*fact(n-1);
                }

                main : function void() {
                    print(fact(5));
                    a,b : string = a;
                }"""
        expect = "Error on line 1 col 45: 1"
        self.assertTrue(TestParser.test(input, expect, 214))
    
    def testprogram15(self):
        input = """main : function void() {
                    print(fact(5));
                    1 = 2;
                }"""
        expect = "Error on line 3 col 20: 1"
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def testprogram16(self):
        input = """a = 2;
                main : function void() {

                }"""
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def testprogram17(self):
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 217))

    def testprogram18(self):
        input = input = """a,b,c: string = "hello", "hello, World", "hello" ; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def testprogram19(self):
        input = input = """a,b,c: string = "hello", "hello, World", "hello" ; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def testprogram19(self):
        input = input = """// test float 
                        x : function float() {
                            return 1.2;
                        }

                        main :function void() {
                            print(x());
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def testprogram20(self):
        input = input = """// test float 
                        float : function float() {
                            return 1.2;
                        }

                        main :function void() {
                            print(x());
                        }"""
        expect = "Error on line 2 col 24: float"
        self.assertTrue(TestParser.test(input, expect, 220))    
    
    def testprogram21(self):
        input = """a,b,c : float = 2,foo(foo(3)), 3 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))   
    
    def testprogram22(self):
        input = """a,b,c : float = 2,foo(foo(3+ 5)), 3 *9, 3+4;"""
        expect = "Error on line 1 col 38: ,"
        self.assertTrue(TestParser.test(input, expect, 222))   
    
    def testprogram23(self):
        input = """main : function void() {
                    do {
                        a = a + 1;
                    }
                    while (true);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))   

    def testprogram24(self):
        input = """main : function void() {
                    do {
                        a = a + 1;
                    }
                    while (true)
                }"""
        expect = "Error on line 6 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 224))   

    def testprogram25(self):
        input = """main : function void() {
                        while (true) a = a +2;
                        while (true) {
                            while (a > b) {
                                a = a + 1;
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))  

    def testprogram26(self):
        input = """main : function void() {
                    if ((a > 2) || (b > 2) && (a - 2)) {
                        break;
                        continue;?
                    }
                }"""
        expect = "?"
        self.assertTrue(TestParser.test(input, expect, 226))  

    def testprogram27(self):
        input = """main : function void() {
                    a: string = "string ;
                }"""
        expect = "string ;"
        self.assertTrue(TestParser.test(input, expect, 227)) 

    def testprogram28(self):
        input = """main : function void() {
                    a: string = "string\\p" ;
                }"""
        expect = "string\\p"
        self.assertTrue(TestParser.test(input, expect, 228)) 

    def testprogram29(self):
        input = """main : function void() {
                    a: string = "string\\t" ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229)) 

    def testprogram30(self):
        input = """a : array[3] of integer = {2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230)) 

    def testprogram31(self):
        input = """a : array[3] of integer = 2,3;"""
        expect = "Error on line 1 col 27: ,"
        self.assertTrue(TestParser.test(input, expect, 231))
    
    def testprogram32(self):
        input = """main : function void() {
                    if (!!!!a) {
                        a = 2;
                    }
                    foo(foo(a + 2));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def testprogram33(self):
        input = """main : function void() {
                    if (!!!!a) {
                        a = 2;
                    }
                    foo(foo(a + 2));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def testprogram34(self):
        input = """main : function void() {
                        a : array [5] of integer = {2,3,4,5,6};
                        sum : integer = 0;
                        for (i = 0, i < size(5), i + 1) {
                            sum = sum + a[i];
                        } 
                        print(sum);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    

    def testprogram35(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def testprogram36(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def testprogram37(self):
        input = """main : function void() {
                    a : float;
                    a = arr[5] + 2 + 3*6 < 2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def testprogram38(self):
        input = """main : function void() {
                    a[a[a[5]]];
                }"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 238))
    
    def testprogram39(self):
        input = """main : function void() {
                    foo(foo(foo(5.23e10)));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def testprogram40(self):
        input = """main : function void() {
                    a,c : auto = b,foo(foo(foo(5.23e10)));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    
    def testprogram41(self):
        input = """main : function void() {
                    a = b +c * c > d + 3.6 + (2 == 3);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    

    def testprogram42(self):
        input = """main : function void() {
                    a = b +c * c > d + 3.6 + 2 == 3;
                }"""
        expect = "Error on line 2 col 47: =="
        self.assertTrue(TestParser.test(input, expect, 242))
    
    def testprogram43(self):
        input = """main : function void() {
                    a = b +c * c > d + 3.6 + (2 == 3);
                    foo(foo(3) + 2, arr);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    
    def testprogram44(self):
        input = """main : function void() {
                    a : array [5] of float;
                    for (i = 0, i < 5, i + 1) {
                        a[i] = Float(i);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def testprogram45(self):
        input = """main : function void() {
                    a [2] = x + 2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    
    def testprogram46(self):
        input = """main : function void() {
                    sum = 0;
                    for (i = 0, i < 5, i + 1) {
                        for (j = 0, j < 10, j+ 1) 
                            sum = sum + a[i,j];
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def testprogram47(self):
        input = """main : function void() {
                    a, b : array[5] of integer ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    
    def testprogram48(self):
        input = """main : function void() {
                    a, b : array[2] of integer = {}, {};
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def testprogram49(self):
        input = """main : function void() {
                    a, b : array[2] of integer = {};
                }"""
        expect = "Error on line 2 col 51: ;"
        self.assertTrue(TestParser.test(input, expect, 249))

    def testprogram50(self):
        input = """return a;"""
        expect = "Error on line 1 col 0: return"
        self.assertTrue(TestParser.test(input, expect, 250))

    def testprogram51(self):
        input = """main : function void() {
                if a == 2 return 1;
            }"""
        expect = "Error on line 2 col 19: a"
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def testprogram52(self):
        input = """main : function void() {
                    if (a == 2) return 1,
                }"""
        expect = "Error on line 2 col 40: ,"
        self.assertTrue(TestParser.test(input, expect, 252))

    def testprogram53(self):
        input = """main : function void() {
                    for (a[i] = 2, i < 2, i * 2) a[i,2] = 3;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def testprogram54(self):
        input = """main : function void() {
                    for (a[i] = 2, i < 2, i * 2) a[i,2] = 3;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def testprogram55(self):
        input = """main : function void() {
                    a = x();
                }

                x : function array[2] of string() {
                    return {"test1", "test2\\t"};
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    
    def testprogram56(self):
        input = """main : function void() {
                    a = x();
                }

                x : function array[2] of string() {
                    return {"test1", "test2\\t"}, 2;
                }"""
        expect = "Error on line 6 col 47: ,"
        self.assertTrue(TestParser.test(input, expect, 256))

    def testprogram57(self):
        input = """main : function void() {
                        do a = 2 
                        while (true);
                    }"""
        expect = "Error on line 2 col 27: a"
        self.assertTrue(TestParser.test(input, expect, 257))
    
    def testprogram58(self):
        input = """main : function void() {
                        do { a = 2 } 
                        while (true)
                    }"""
        expect = "Error on line 2 col 35: }"
        self.assertTrue(TestParser.test(input, expect, 258))

    def testprogram59(self):
        input = """main : function void() {
                foo (a[foo(3)], h+5);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def testprogram60(self):
        input = """main : function void() {
                foo (a[foo(3)]; h+5);
            }"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 260))

    def testprogram61(self):
        input = """main : function void () {
                    for (i = 0; i + 2 , i < 2) {
                        continue;
                    }
                }"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 261))

    def testprogram62(self):
        input = """main : function a () {
                    for (i = 0; i + 2 , i < 2) {
                        continue;
                    }
                }"""
        expect = "Error on line 1 col 16: a"
        self.assertTrue(TestParser.test(input, expect, 262))

    def testprogram63(self):
        input = """main : function void () {
                    r, s: integer;
                    r = 2.0;
                    a, b: array [5] of integer;
                    s = r * r * myPI;
                    a[0] = s;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def testprogram64(self):
        input = """auto : integer;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 264))
    
    def testprogram65(self):
        input = """x,y,z: integer = 3+2, 4+double(2,3), 6*square(1,2);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def testprogram66(self):
        input = """fact: function integer (n:integer){
                        for (i = 1, i < 10, i + 1.5) {writeInt(i);}
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def testprogram67(self):
        input = """main : function void() {
    
                };"""
        expect = "Error on line 3 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 267))

    def testprogram68(self):
        input = """main : function void() {
                    a = 2 > 3 + 1*6 || 2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def testprogram69(self):
        input = """main : function void() {
                    a = 2 > 3 + 1*6 == 2;
                }"""
        expect = "Error on line 2 col 36: =="
        self.assertTrue(TestParser.test(input, expect, 269))
    
    def testprogram70(self):
        input = """main : function void() {
                    a = 2 == 2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def testprogram71(self):
        input = """main : function void() {
                    subfunc : function boolean() {
                        return foo(3) == 2;
                    }
                }   """
        expect = "Error on line 2 col 30: function"
        self.assertTrue(TestParser.test(input, expect, 271))
    
    def testprogram72(self):
        input = """main : function void() {

                }   

                subfunc : function boolean() {
                    return foo(3) == 2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def testprogram73(self):
        input = """main : function void() {
                    a, b : boolean = true, false;
                }   

                subfunc : function string() {
                    return foo(3) == 2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def testprogram74(self):
        input = """main : function void() {
                    a, b : array[2] of integer = {1,2}, foo(3); 
                }   

                subfunc : function array() {
                    return foo(3) == 2;
                }"""
        expect = "Error on line 5 col 40: ("
        self.assertTrue(TestParser.test(input, expect, 274))

    def testprogram75(self):
        input = """main : function void() {
                    a, b : array[2] of integer = {1,2}, foo(3); 
                }   

                subfunc : function array[2] of boolean() {
                    a : void;
                }"""
        expect = "Error on line 6 col 24: void"
        self.assertTrue(TestParser.test(input, expect, 275))

    def testprogram76(self):
        input = """main : function void() {
                    a, b : array[2] of integer = {1,2}, foo(3); 
                }   

                subfunc : function array[2] of boolean() {
                    a : auto = {2,3} + 6;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def testprogram77(self):
        input = """main : function void() {
                    a, b : array[2] of integer = {1,2}, foo(3); 
                }   

                subfunc : function array[2] of boolean() {
                    return {a(3), 2 + 3};
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def testprogram78(self):
        input = """main : function void() {
                    a, b : array[2] of integer = {1,2}, foo(3); 
                }   

                subfunc : function array[2] of boolean() {
                    return {a(3), 2 + 3, {2,3,4}};
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def testprogram79(self):
        input = """main : // function void() {
                    a, b : array[2] of integer = {1,2}, foo(3); 
                }   

                subfunc : function array[2] of boolean() {
                    return {a(3), 2 + 3, {2,3,4}};
                }"""
        expect = "Error on line 2 col 20: a"
        self.assertTrue(TestParser.test(input, expect, 279))

    def testprogram80(self):
        input = """main : /* function void() {
                    a, b : array[2] of integer = {1,2}, foo(3); 
                }  */ 

                subfunc : function array[2] of boolean() {
                    return {a(3), 2 + 3, {2,3,4}};
                }"""
        expect = "Error on line 5 col 16: subfunc"
        self.assertTrue(TestParser.test(input, expect, 280))

    def testprogram81(self):
        input = """subfunc : function void (inherit out a : string, b : array [2] of string ) inherit abc {
                    return a;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def testprogram82(self):
        input = """subfunc : function void (inherit out a : string, b : array [2] of string ) inherit 2 {
                    return a;
                }"""
        expect = "Error on line 1 col 83: 2"
        self.assertTrue(TestParser.test(input, expect, 282))

    def testprogram83(self):
        input = """/* abc */ */"""
        expect = "Error on line 1 col 10: *"
        self.assertTrue(TestParser.test(input, expect, 283))

    def testprogram84(self):
        input = """main : function void () {
                    a = -------2 + 4 / 5.0::c;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def testprogram84(self):
        input = """main : function void () {
                    a = -------_2a + 4 / 5.0::c;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def testprogram85(self):
        input = """main : function void () {
                    a = -------2a + 4 / 5.0::c;
                }"""
        expect = "Error on line 2 col 32: a"
        self.assertTrue(TestParser.test(input, expect, 285))

    def testprogram86(self):
        input = """main : function void () {
                    a = !!!!a && b || c + 4 / 5.0::c;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def testprogram87(self):
        input = """main : function void () {
                    a,b = 2,2;
                }"""
        expect = "Error on line 2 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 287))

    def testprogram88(self):
        input = """main : function void () {
                    a = c== b ==d;
                }"""
        expect = "Error on line 2 col 30: =="
        self.assertTrue(TestParser.test(input, expect, 288))

    def testprogram89(self):
        input = """main : function auto () {
                    a = (c== b) || c;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def testprogram90(self):
        input = """main : function void () {
                    return;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def testprogram91(self):
        input = """main : function void () {
                    return 2,3;
                }"""
        expect = "Error on line 2 col 28: ,"
        self.assertTrue(TestParser.test(input, expect, 291))

    def testprogram92(self):
        input = """main : function void (out a : void) {
                return;
            }"""
        expect = "Error on line 1 col 30: void"
        self.assertTrue(TestParser.test(input, expect, 292))

    def testprogram93(self):
        input = """main : function void (out a : string) {
                    if (a[0]::b[a,foo]) return 2;
                    else {
                        break;
                        continue;
                        return; 
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def testprogram94(self):
        input = """main : function void (out a : string) {
                    a = (a+b)[1,2];
                }"""
        expect = "Error on line 2 col 29: ["
        self.assertTrue(TestParser.test(input, expect, 294))

    def testprogram95(self):
        input = """main : function void (out a : string) {
                    a : array[2] of float; 
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def testprogram96(self):
        input = """float : function void (out a : string) {
                    a : array[2] of float; 
                }"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input, expect, 296))

    def testprogram97(self):
        input = """main : function void (out a : string) {
                    return float(2.0) + 1;
                }"""
        expect = "Error on line 2 col 27: float"
        self.assertTrue(TestParser.test(input, expect, 297))

    def testprogram98(self):
        input = """main : function void (out a : string) {
                    a = "abc\\t";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def testprogram99(self):
        input = """main : function void (out a : string) {
                    a = "abc\\t\\i";
                }"""
        expect = "abc\\t\\i"
        self.assertTrue(TestParser.test(input, expect, 299))

    def testprogram100(self):
        input = """main : function void (out a : string) {
                    a = "abc\\t;
                }"""
        expect = "abc\\t;"
        self.assertTrue(TestParser.test(input, expect, 300))

    def testprogram101(self):
        input = """x,y,z: integer = 3, 4, 6;
            fact:function integer(n:integer)
            {
                if((n==0)||(n==1)||(n==2))return 1;
                result:integer=1;
                a:integer=1;
                b:integer=1;
                while(n>2)
                {
                    result=a+b;
                    a=b;
                    b=result;
                    n=n-1;
                }
                return result;
            }
            fact: function integer (n: integer) {
                if (n == 0) return 1;
                else return n * fact(n - 1);
            }
            inc: function void(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                delta: integer = fact(3);
                inc(x, delta);
                printInteger(x);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 301))