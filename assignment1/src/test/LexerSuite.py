import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # Test Identifier
    def test1(self):
        self.assertTrue(TestLexer.test('giahuy\t', 'giahuy,<EOF>', 101))
    def test2(self):
        self.assertTrue(TestLexer.test('1ab2', '1,ab2,<EOF>', 102))
    def test3(self):
        self.assertTrue(TestLexer.test('abc', 'abc,<EOF>', 103))
    def test4(self):
        self.assertTrue(TestLexer.test('_ppl', '_ppl,<EOF>', 104))
    def test5(self):
        self.assertTrue(TestLexer.test('Print()', 'Print,(,),<EOF>', 105))
    def test6(self):
        self.assertTrue(TestLexer.test('&abc','Error Token &', 106))
    def test7(self):
        self.assertTrue(TestLexer.test('giahuy_1092002', 'giahuy_1092002,<EOF>', 107))
    def test8(self):
        self.assertTrue(TestLexer.test('_123', '_123,<EOF>', 108))
    def test9(self):
        self.assertTrue(TestLexer.test('_123', '_123,<EOF>', 109))
    def test10(self):
        self.assertTrue(TestLexer.test('giahuy_bachkhoa', 'giahuy_bachkhoa,<EOF>', 110))
    # Test Keywords
    def test11(self):
        self.assertTrue(TestLexer.test('inherit', 'inherit,<EOF>', 111))
    def test12(self):
        self.assertTrue(TestLexer.test('integer', 'integer,<EOF>', 112))
    def test13(self):
        self.assertTrue(TestLexer.test('boolean', 'boolean,<EOF>', 113))
    def test14(self):
        self.assertTrue(TestLexer.test('do', 'do,<EOF>', 114))
    def test15(self):
        self.assertTrue(TestLexer.test('while', 'while,<EOF>', 115))
    def test16(self):
        self.assertTrue(TestLexer.test('function', 'function,<EOF>', 116))
    def test17(self):
        self.assertTrue(TestLexer.test('auto', 'auto,<EOF>', 117))
    def test18(self):
        self.assertTrue(TestLexer.test('continue', 'continue,<EOF>', 118))
    def test19(self):
        self.assertTrue(TestLexer.test('break', 'break,<EOF>', 119))
    def test20(self):
        self.assertTrue(TestLexer.test('of', 'of,<EOF>', 120))
    def test21(self):
        self.assertTrue(TestLexer.test('else', 'else,<EOF>', 121))
    def test22(self):
        self.assertTrue(TestLexer.test('string', 'string,<EOF>', 122))
    def test23(self):
        self.assertTrue(TestLexer.test('array', 'array,<EOF>', 123))
    def test24(self):
        self.assertTrue(TestLexer.test('void', 'void,<EOF>', 124))
    def test25(self):
        self.assertTrue(TestLexer.test('false', 'false,<EOF>', 125))
    def test26(self):
        self.assertTrue(TestLexer.test('return', 'return,<EOF>', 126))
    def test27(self):
        self.assertTrue(TestLexer.test('float', 'float,<EOF>', 127))
    def test28(self):
        self.assertTrue(TestLexer.test('out', 'out,<EOF>', 128))
    def test29(self):
        self.assertTrue(TestLexer.test('true', 'true,<EOF>', 129))
    def test30(self):
        self.assertTrue(TestLexer.test('if', 'if,<EOF>', 130))
    def test31(self):
        self.assertTrue(TestLexer.test('for', 'for,<EOF>', 131))
    # Test operators
    def test32(self):
        self.assertTrue(TestLexer.test('+', '+,<EOF>', 132))
    def test33(self):
        self.assertTrue(TestLexer.test('!', '!,<EOF>', 133))
    def test34(self):
        self.assertTrue(TestLexer.test('!=', '!=,<EOF>', 134))
    def test35(self):
        self.assertTrue(TestLexer.test('::', '::,<EOF>', 135))
    def test36(self):
        self.assertTrue(TestLexer.test('-', '-,<EOF>', 136))
    def test37(self):
        self.assertTrue(TestLexer.test('&&', '&&,<EOF>', 137))
    def test38(self):
        self.assertTrue(TestLexer.test('<', '<,<EOF>', 138))
    def test39(self):
        self.assertTrue(TestLexer.test('*', '*,<EOF>', 139))
    def test40(self):
        self.assertTrue(TestLexer.test('||', '||,<EOF>', 140))
    def test41(self):
        self.assertTrue(TestLexer.test('<=', '<=,<EOF>', 141))
    def test42(self):
        self.assertTrue(TestLexer.test('/', '/,<EOF>', 142))
    def test43(self):
        self.assertTrue(TestLexer.test('==', '==,<EOF>', 143))
    def test44(self):
        self.assertTrue(TestLexer.test('>', '>,<EOF>', 144))
    def test45(self):
        self.assertTrue(TestLexer.test('%', '%,<EOF>', 145))
    def test46(self):
        self.assertTrue(TestLexer.test('>=', '>=,<EOF>', 146))
    # Test seperators
    def test47(self):
        self.assertTrue(TestLexer.test('(', '(,<EOF>', 147))
    def test48(self):
        self.assertTrue(TestLexer.test(')', '),<EOF>', 148))
    def test49(self):
        self.assertTrue(TestLexer.test('[', '[,<EOF>', 149))
    def test50(self):
        self.assertTrue(TestLexer.test(']', '],<EOF>', 150))
    def test51(self):
        self.assertTrue(TestLexer.test('.', 'Error Token .', 151))
    def test52(self):
        self.assertTrue(TestLexer.test(',', ',,<EOF>', 152))
    def test53(self):
        self.assertTrue(TestLexer.test(';', ';,<EOF>', 153))
    def test54(self):
        self.assertTrue(TestLexer.test(':', ':,<EOF>', 154))
    def test55(self):
        self.assertTrue(TestLexer.test('{', '{,<EOF>', 155))
    def test56(self):
        self.assertTrue(TestLexer.test('}', '},<EOF>', 156))
    # Test Literals
    # Test Intlit
    def test57(self):
        self.assertTrue(TestLexer.test('1092002', '1092002,<EOF>', 157))
        
    def test58(self):
        self.assertTrue(TestLexer.test('10_9_2002', '1092002,<EOF>', 158))
        
    def test59(self):
        self.assertTrue(TestLexer.test('123_456', '123456,<EOF>', 159))
        
    def test60(self):
        self.assertTrue(TestLexer.test('1_2_3_4', '1234,<EOF>', 160))
        
    def test61(self):
        self.assertTrue(TestLexer.test('1__2', '12,<EOF>', 161))
        
    def test62(self):
        self.assertTrue(TestLexer.test('0828479273', '0,828479273,<EOF>', 162))
        
    def test63(self):
        self.assertTrue(TestLexer.test('1092002_', '1092002,_,<EOF>', 163))
        
    def test64(self):
        self.assertTrue(TestLexer.test('10_9_2002_', '1092002,_,<EOF>', 164))
        
    def test65(self):
        self.assertTrue(TestLexer.test('_45_6', '_45_6,<EOF>', 165))
        
    def test66(self):
        self.assertTrue(TestLexer.test('456_', '456,_,<EOF>', 166))
    # Test Floatlit
    def test67(self):
        self.assertTrue(TestLexer.test('1_234.567', '1234.567,<EOF>', 167))
        
    def test68(self):
        self.assertTrue(TestLexer.test('10_9.5e67', '109.5e67,<EOF>', 168))
        
    def test69(self):
        self.assertTrue(TestLexer.test('10_9.56e-7', '109.56e-7,<EOF>', 169))
        
    def test70(self):
        self.assertTrue(TestLexer.test('10_9.56E-7', '109.56E-7,<EOF>', 170))
        
    def test71(self):
        self.assertTrue(TestLexer.test('10.9e2', '10.9e2,<EOF>', 171))
        
    def test72(self):
        self.assertTrue(TestLexer.test('10.9e-2', '10.9e-2,<EOF>', 172))
        
    def test73(self):
        self.assertTrue(TestLexer.test('10.9E2', '10.9E2,<EOF>', 173))
        
    def test74(self):
        self.assertTrue(TestLexer.test('10E-9', '10E-9,<EOF>', 174))
        
    def test75(self):
        self.assertTrue(TestLexer.test('10e-9', '10e-9,<EOF>', 175))
        
    def test76(self):
        self.assertTrue(TestLexer.test('10e9', '10e9,<EOF>', 176))
        
    def test77(self):
        self.assertTrue(TestLexer.test('10_9e2', '109e2,<EOF>', 177))
        
    def test78(self):
        self.assertTrue(TestLexer.test('10.9', '10.9,<EOF>', 178))
        
    def test79(self):
        self.assertTrue(TestLexer.test('1.e2', '1.e2,<EOF>', 179))
    # Test Stringlit
    def test80(self):
        self.assertTrue(TestLexer.test('""', ',<EOF>', 180))
        
    def test81(self):
        self.assertTrue(TestLexer.test('" "', ' ,<EOF>', 181))
        
    def test82(self):
        self.assertTrue(TestLexer.test('"Nguyen Luong Gia Huy"', 'Nguyen Luong Gia Huy,<EOF>', 182))
        
    def test83(self):
        self.assertTrue(TestLexer.test('"BACH KHOA"', 'BACH KHOA,<EOF>', 183))
        
    def test84(self):
        self.assertTrue(TestLexer.test('"Nguyen ly ngon ngu lap trinh"', 'Nguyen ly ngon ngu lap trinh,<EOF>', 184))
        
    def test85(self):
        self.assertTrue(TestLexer.test('"1092002"', '1092002,<EOF>', 185))
        
    def test86(self):
        self.assertTrue(TestLexer.test('"giahuy1092002"', 'giahuy1092002,<EOF>', 186))
        
    def test87(self):
        self.assertTrue(TestLexer.test('"h3llo W0rld!"', 'h3llo W0rld!,<EOF>', 187))
        
    def test88(self):
        self.assertTrue(TestLexer.test('"301AH2"', '301AH2,<EOF>', 188))
        
    def test89(self):
        self.assertTrue(TestLexer.test('"Hello World"', 'Hello World,<EOF>', 189))
        
    def test90(self):
        self.assertTrue(TestLexer.test('"123"', '123,<EOF>', 190))
        
    def test91(self):
        self.assertTrue(TestLexer.test('"xyz"', 'xyz,<EOF>', 191))
        
    def test92(self):
        self.assertTrue(TestLexer.test('func1 : function integer(a : array of integer = {1,2,3}){return 1;}', 'func1,:,function,integer,(,a,:,array,of,integer,=,{,1,,,2,,,3,},),{,return,1,;,},<EOF>', 192))
        
    def test93(self):
        self.assertTrue(TestLexer.test(' "\\c 123" ', 'Illegal Escape In String: \c', 193))
        
    def test94(self):
        self.assertTrue(TestLexer.test('"String', 'Unclosed String: String', 194))
    
    def test95(self):
        self.assertTrue(TestLexer.test('//This is cmment\n/*This is comment*/\n123 1_23', "123,123,<EOF>", 195))
        
    def test96(self):
        self.assertTrue(TestLexer.test('"Truong Ha Kieu Nhi"', 'Truong Ha Kieu Nhi,<EOF>', 196))
        
    def test97(self):
        self.assertTrue(TestLexer.test('"He asked me: \\"Where is \\"John?\\""','He asked me: \\"Where is \\"John?\\",<EOF>', 197))
        
    def test98(self):
        self.assertTrue(TestLexer.test('a,b : auto; a = b = 1;', 'a,,,b,:,auto,;,a,=,b,=,1,;,<EOF>', 198))
        
    def test99(self):
        self.assertTrue(TestLexer.test(' "aaa\\" ', 'Unclosed String: aaa\\" ', 199))
        
    def test100(self):
        self.assertTrue(TestLexer.test('"a:integer=?"','a:integer=?,<EOF>',200))

    def test101(self):
        self.assertTrue(TestLexer.test('0.0','0.0,<EOF>',201))
    
    
    
    
    
    
    
