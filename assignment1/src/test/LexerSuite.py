import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

     def test0(self):
          input = """{"""
          expect = "{,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,100))
     def test1(self):
          input = """"""
          expect = "<EOF>"
          self.assertTrue(TestLexer.test(input,expect,101))
     #comment
     def test2(self):
          input = """//abc+46/"""
          expect = "<EOF>"
          self.assertTrue(TestLexer.test(input,expect,102))
     def test3(self):
          input = """/* akjkba
                     */ """
          expect = "<EOF>"
          self.assertTrue(TestLexer.test(input,expect,103))
     def test4(self):
          input = """abc /*kabh*/ abc"""
          expect = "abc,abc,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,104))
     def test5(self):
          input = """123//abc+46/"""
          expect = "123,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,105))
     #int
     def test6(self):
          input = """123"""
          expect = "123,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,106))
     def test7(self):
          input = """01"""
          expect = "0,1,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,107))
     def test8(self):
          input = """12_3_4"""
          expect = "1234,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,108))
     def test9(self):
          input = """0123"""
          expect = "0,123,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,109))
     def test10(self):
          input = """123_"""
          expect = "123,_,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,110))
     #float
     def test11(self):
          input = """1_2.012"""
          expect = "12.012,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,111))
     def test12(self):
          input = """1.123"""
          expect = "1.123,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,112))
     def test13(self):
          input = """0"""
          expect = "0,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,113))
     def test14(self):
          input = """0.0"""
          expect = "0.0,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,114))
     def test15(self):
          input = """7E-10"""
          expect = "7E-10,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,115))
     def test16(self):
          input = """1.2e3"""
          expect = "1.2e3,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,116))
     def test17(self):
          input = """1_23.2e3"""
          expect = "123.2e3,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,117))
     def test18(self):
          input = """1_23.2e+3"""
          expect = "123.2e+3,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,118))
     #test keyword
     def test19(self):
          input = """auto"""
          expect = "auto,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,119))
     #test string
     def test20(self):
          input = """\"_str\""""
          expect = "_str,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,120))
     def test21(self):
          input = """\"abcd\""""
          expect = "abcd,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,121))
     #**** check \t************************************
     def test22(self):
          input = """\"abcd \\t anb \\b\""""
          expect = "abcd \\t anb \\b,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,122))
     def test23(self):
          input = """sbc \" \\t\""""
          expect = "sbc, \\t,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,123))
     def test24(self):
          input = """\"abcd \\t ab+/*()89\""""
          expect = "abcd \\t ab+/*()89,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,124))
     #identifi
     def test25(self):
          input = """12a"""
          expect = "12,a,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,125))
     def test26(self):
          input = """12,a"""
          expect = "12,,,a,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,126))
     def test27(self):
          input = """12?a"""
          expect = "12,Error Token ?"
          self.assertTrue(TestLexer.test(input,expect,127))
     def test28(self):
          input = """12 abc 1.2"""
          expect = "12,abc,1.2,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,128))
     #check error
     def test29(self):
          input = """\"abcj"""
          expect = "Unclosed String: abcj"
          self.assertTrue(TestLexer.test(input,expect,129))
     def test30(self):
          input = """\"abcj\t\""""
          expect = "abcj\t,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,130))
     #test iden
     def test31(self):
          input = """_abc"""
          expect = "_abc,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,131))
     def test32(self):
          input = """abc+"""
          expect = "abc,+,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,132))
     def test33(self):
          input = """abc_+-"""
          expect = "abc_,+,-,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,133))
     def test34(self):
          input = """:: abc n"""
          expect = "::,abc,n,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,134))
     def test35(self):
          input = """1.e-2"""
          expect = "1.e-2,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,135)) 
     def test36(self):
          input = """1.e"""
          expect = "1.,e,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,136))
     def test37(self):
          input = """.e3"""
          expect = "Error Token ."
          self.assertTrue(TestLexer.test(input,expect,137))
     def test38(self):
          input = """{1, 5, 7, 12}"""
          expect = "{,1,,,5,,,7,,,12,},<EOF>"
          self.assertTrue(TestLexer.test(input,expect,138))
     def test39(self):
          input = """\"abc \\h\""""
          expect = "Illegal Escape In String: abc \h"
          self.assertTrue(TestLexer.test(input,expect,139))
     def test40(self):
          input = """\"abc \\'\""""
          expect = "abc \\',<EOF>"
          self.assertTrue(TestLexer.test(input,expect,140))
     def test41(self):
        input = """ "'test\\n and \t {"-"#\b\\n" """
        expect = """'test\\n and \t {,-,#\b\\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 141))
     def test42(self):
          input = """\"abc\t"""
          expect = "Unclosed String: abc	"
          self.assertTrue(TestLexer.test(input,expect,142))
     def test43(self):
        input = """"'ITNzHSF\n" """
        expect = """Unclosed String: 'ITNzHSF"""
        self.assertTrue(TestLexer.test(input, expect, 143))
     def test44(self):
        input = """ 1__23 """
        expect = """123,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 144))
     def testKeyWord145(self):
        self.assertTrue(TestLexer.test('auto','auto,<EOF>',145))
     def testKeyWord146(self):
          self.assertTrue(TestLexer.test('break','break,<EOF>',146))
     def testKeyWord147(self):
          self.assertTrue(TestLexer.test('boolean','boolean,<EOF>',147))
     def testKeyWord148(self):
          self.assertTrue(TestLexer.test('do','do,<EOF>',148))
     def testKeyWord149(self):
          self.assertTrue(TestLexer.test('else','else,<EOF>',149))
     def testKeyWord150(self):
          self.assertTrue(TestLexer.test('float','float,<EOF>',150))
     def testKeyWord151(self):
          self.assertTrue(TestLexer.test('for','for,<EOF>',151))
     def testKeyWord152(self):
          self.assertTrue(TestLexer.test('function','function,<EOF>',152))
     def testKeyWord153(self):
          self.assertTrue(TestLexer.test('if','if,<EOF>',153))
     def testKeyWord154(self):
          self.assertTrue(TestLexer.test('integer','integer,<EOF>',154))
     def testKeyWord155(self):
          self.assertTrue(TestLexer.test('return','return,<EOF>',155))
     def testKeyWord156(self):
          self.assertTrue(TestLexer.test('string','string,<EOF>',156))
     def testKeyWord157(self):
          self.assertTrue(TestLexer.test('while','while,<EOF>',157))
     def testKeyWord158(self):
          self.assertTrue(TestLexer.test('void','void,<EOF>',158))
     def testKeyWord159(self):
          self.assertTrue(TestLexer.test('out','out,<EOF>',159))
     def testKeyWord160(self):
          self.assertTrue(TestLexer.test('continue','continue,<EOF>',160))
     def testKeyWord161(self):
          self.assertTrue(TestLexer.test('of','of,<EOF>',161))
     def testKeyWord162(self):
          self.assertTrue(TestLexer.test('inherit','inherit,<EOF>',162))
     def testKeyWord163(self):
          self.assertTrue(TestLexer.test('array','array,<EOF>',163))
     def testKeyWord164(self):
        self.assertTrue(TestLexer.test('+','+,<EOF>',164))
     def testKeyWord165(self):
          self.assertTrue(TestLexer.test('-','-,<EOF>',165))
     def testKeyWord166(self):
          self.assertTrue(TestLexer.test('*','*,<EOF>',166))
     def testKeyWord167(self):
          self.assertTrue(TestLexer.test('/','/,<EOF>',167))
     def testKeyWord168(self):
          self.assertTrue(TestLexer.test('%','%,<EOF>',168))
     def testKeyWord169(self):
          self.assertTrue(TestLexer.test('!','!,<EOF>',169))
     def testKeyWord170(self):
          self.assertTrue(TestLexer.test('&&','&&,<EOF>',170))
     def testKeyWord171(self):
          self.assertTrue(TestLexer.test('||','||,<EOF>',171))
     def testKeyWord172(self):
          self.assertTrue(TestLexer.test('==','==,<EOF>',172))
     def testKeyWord173(self):
          self.assertTrue(TestLexer.test('!=','!=,<EOF>',173))
     def testKeyWord174(self):
          self.assertTrue(TestLexer.test('<','<,<EOF>',174))
     def testKeyWord175(self):
          self.assertTrue(TestLexer.test('<=','<=,<EOF>',175))
     def testKeyWord176(self):
          self.assertTrue(TestLexer.test('>','>,<EOF>',176))
     def testKeyWord177(self):
          self.assertTrue(TestLexer.test('>=','>=,<EOF>',177))
     def testKeyWord178(self):
          self.assertTrue(TestLexer.test('::','::,<EOF>',178))
     def test79(self):
       """test identifiers"""
       self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 179))
     def test80(self):
          input = """_abc75"""
          expect = "_abc75,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,180))
     def test81(self):
          self.assertTrue(TestLexer.test('"1_234.567"','1_234.567,<EOF>', 181))
     def test82(self):
          self.assertTrue(TestLexer.test('"123" "str\\t\\n"','123,str\\t\\n,<EOF>', 182))
     def test83(self):
          self.assertTrue(TestLexer.test('"check \\f"','check \\f,<EOF>', 183))
     def test84(self):
          self.assertTrue(TestLexer.test('"He asked me: \\"Where is John?\\""','He asked me: \\"Where is John?\\",<EOF>', 184))
     def test85(self):
          self.assertTrue(TestLexer.test('"abg_','Unclosed String: abg_', 185))
     def test86(self):
          self.assertTrue(TestLexer.test('"test illegal \p"','Illegal Escape In String: test illegal \p', 186))
     def test87(self):
          self.assertTrue(TestLexer.test('"test\\s"','Illegal Escape In String: test\\s', 187))
     def test88(self):
          input = """//ab\n abc"""
          expect = "abc,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,188))
     def test89(self):
          input = """/* akjkba
                     */ test"""
          expect = "test,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,189))
     def test90(self):
          input = """abc test /*kabh*/ //abc"""
          expect = "abc,test,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,190))
     def test191(self):
          input = """12___"""
          expect = "12,___,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,191))
     def test192(self):
          input = """12__4.1"""
          expect = "124.1,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,192))
     def test193(self):
          input = """12__4.1,abc,string"""
          expect = "124.1,,,abc,,,string,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,193))
     def test194(self):
          input = """12__4.1,abc,string//ancnassj\rabc"""
          expect = "124.1,,,abc,,,string,abc,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,194))
     def test195(self):
          input = """123 abc"""
          expect = "123,abc,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,195))
     def test196(self):
          input = """123 abc"""
          expect = "123,abc,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,196))
     def test97(self):
          input = """\"abcd \\t \""""
          expect = "abcd \\t ,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,197))
     def test98(self):
          input = """ \\t abc \""""
          expect = "Error Token \\"
          self.assertTrue(TestLexer.test(input,expect,198))
     def test99(self):
          input = """abc \""""
          expect = "abc,Unclosed String: "
          self.assertTrue(TestLexer.test(input,expect,199))
     def test100(self):
          input = """0.0"""
          expect = "0.0,<EOF>"
          self.assertTrue(TestLexer.test(input,expect,0))