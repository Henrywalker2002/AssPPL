import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test1(self):
        inp = """main: function void () {
        }
        
        test1 : function void() {
            i : integer;
            for (i = 2, i < 10, i + 1) {
                
            }
        }
        """
        out = ""
        self.assertTrue(TestChecker.test(inp, out, 310))