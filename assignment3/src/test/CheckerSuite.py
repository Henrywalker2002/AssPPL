import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test1(self):
        inp = """
        b : array [6] of integer;
        a : auto = 5;
        main: function void () {
           
        }
        
        test1 : function auto (a: auto) {
            for (b[test(2)] = 2, b[1] < 3, b[1]*3) {
                
            }
            return 3;
        }
        
        test : function auto(y : integer) inherit test1 {
            super(2);
            a : string = test1(2);
        }

        """
        out = ""
        self.assertTrue(TestChecker.test(inp, out, 310))