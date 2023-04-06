import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1(self):
        inp = """main: function void () {
        }
        
        test1 : function void() {
            i : integer;
            for (i = 2.0, i < 10, i + 1) {
                
            }
        }
        """
        out = ""
        self.assertTrue(TestParser.test(inp, out, 310))
