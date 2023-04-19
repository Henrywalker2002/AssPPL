import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test1(self):
        inp = """
        foo : function boolean(x : auto, y : auto) {
            if (x) {
                printInteger(6);
            }
        }
        
        a : string = boo();
        
        boo : function auto() {
            
        }
        
        b : auto = foo(true, 4.0);

        """
        out = ""
        self.assertTrue(TestChecker.test(inp, out, 310))