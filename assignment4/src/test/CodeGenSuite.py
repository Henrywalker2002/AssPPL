import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestCodeGen.test(input, expect, 501))
