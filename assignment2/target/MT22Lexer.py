# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u01cf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u00ff\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u010a\n\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0139\n-\3.\3")
        buf.write(".\3.\3.\5.\u013f\n.\3/\3/\7/\u0143\n/\f/\16/\u0146\13")
        buf.write("/\3/\7/\u0149\n/\f/\16/\u014c\13/\3/\6/\u014f\n/\r/\16")
        buf.write("/\u0150\7/\u0153\n/\f/\16/\u0156\13/\3\60\3\60\3\61\3")
        buf.write("\61\5\61\u015c\n\61\3\61\3\61\3\61\5\61\u0161\n\61\3\61")
        buf.write("\5\61\u0164\n\61\3\61\5\61\u0167\n\61\3\61\3\61\3\62\3")
        buf.write("\62\7\62\u016d\n\62\f\62\16\62\u0170\13\62\3\63\3\63\5")
        buf.write("\63\u0174\n\63\3\63\6\63\u0177\n\63\r\63\16\63\u0178\3")
        buf.write("\64\3\64\7\64\u017d\n\64\f\64\16\64\u0180\13\64\3\65\3")
        buf.write("\65\7\65\u0184\n\65\f\65\16\65\u0187\13\65\3\65\3\65\3")
        buf.write("\65\3\66\3\66\5\66\u018e\n\66\3\67\3\67\3\67\38\38\38")
        buf.write("\58\u0196\n8\39\39\39\39\79\u019c\n9\f9\169\u019f\139")
        buf.write("\39\39\39\39\39\39\79\u01a7\n9\f9\169\u01aa\139\59\u01ac")
        buf.write("\n9\39\39\3:\6:\u01b1\n:\r:\16:\u01b2\3:\3:\3;\3;\7;\u01b9")
        buf.write("\n;\f;\16;\u01bc\13;\3;\5;\u01bf\n;\3;\3;\3<\3<\7<\u01c5")
        buf.write("\n<\f<\16<\u01c8\13<\3<\3<\3<\3=\3=\3=\3\u019d\2>\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\2_\2a\60c\2e\2g\61i\62k\2m\2o\2q\63s\64u\65")
        buf.write("w\66y\67\3\2\16\3\2\63;\3\2\62;\4\2GGgg\4\2--//\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\6\2\f\f\17\17$$^^\n\2$$))^^ddhhpp")
        buf.write("ttvv\3\2^^\4\2\f\f\17\17\5\2\13\f\17\17\"\"\7\3\n\f\16")
        buf.write("\17$$))^^\2\u01e2\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2a\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3{\3\2\2")
        buf.write("\2\5\u0080\3\2\2\2\7\u0088\3\2\2\2\t\u008c\3\2\2\2\13")
        buf.write("\u0095\3\2\2\2\r\u009a\3\2\2\2\17\u00a0\3\2\2\2\21\u00a2")
        buf.write("\3\2\2\2\23\u00a4\3\2\2\2\25\u00a7\3\2\2\2\27\u00aa\3")
        buf.write("\2\2\2\31\u00ad\3\2\2\2\33\u00b2\3\2\2\2\35\u00b8\3\2")
        buf.write("\2\2\37\u00bc\3\2\2\2!\u00bf\3\2\2\2#\u00c6\3\2\2\2%\u00cc")
        buf.write("\3\2\2\2\'\u00d5\3\2\2\2)\u00d7\3\2\2\2+\u00d9\3\2\2\2")
        buf.write("-\u00db\3\2\2\2/\u00dd\3\2\2\2\61\u00df\3\2\2\2\63\u00e1")
        buf.write("\3\2\2\2\65\u00e3\3\2\2\2\67\u00fe\3\2\2\29\u0109\3\2")
        buf.write("\2\2;\u010b\3\2\2\2=\u010d\3\2\2\2?\u010f\3\2\2\2A\u0111")
        buf.write("\3\2\2\2C\u0113\3\2\2\2E\u0115\3\2\2\2G\u0117\3\2\2\2")
        buf.write("I\u011a\3\2\2\2K\u011d\3\2\2\2M\u011f\3\2\2\2O\u0122\3")
        buf.write("\2\2\2Q\u0125\3\2\2\2S\u0127\3\2\2\2U\u0129\3\2\2\2W\u012c")
        buf.write("\3\2\2\2Y\u0138\3\2\2\2[\u013e\3\2\2\2]\u0140\3\2\2\2")
        buf.write("_\u0157\3\2\2\2a\u0166\3\2\2\2c\u016a\3\2\2\2e\u0171\3")
        buf.write("\2\2\2g\u017a\3\2\2\2i\u0181\3\2\2\2k\u018d\3\2\2\2m\u018f")
        buf.write("\3\2\2\2o\u0195\3\2\2\2q\u01ab\3\2\2\2s\u01b0\3\2\2\2")
        buf.write("u\u01b6\3\2\2\2w\u01c2\3\2\2\2y\u01cc\3\2\2\2{|\7c\2\2")
        buf.write("|}\7w\2\2}~\7v\2\2~\177\7q\2\2\177\4\3\2\2\2\u0080\u0081")
        buf.write("\7k\2\2\u0081\u0082\7p\2\2\u0082\u0083\7j\2\2\u0083\u0084")
        buf.write("\7g\2\2\u0084\u0085\7t\2\2\u0085\u0086\7k\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\6\3\2\2\2\u0088\u0089\7q\2\2\u0089\u008a")
        buf.write("\7w\2\2\u008a\u008b\7v\2\2\u008b\b\3\2\2\2\u008c\u008d")
        buf.write("\7h\2\2\u008d\u008e\7w\2\2\u008e\u008f\7p\2\2\u008f\u0090")
        buf.write("\7e\2\2\u0090\u0091\7v\2\2\u0091\u0092\7k\2\2\u0092\u0093")
        buf.write("\7q\2\2\u0093\u0094\7p\2\2\u0094\n\3\2\2\2\u0095\u0096")
        buf.write("\7x\2\2\u0096\u0097\7q\2\2\u0097\u0098\7k\2\2\u0098\u0099")
        buf.write("\7f\2\2\u0099\f\3\2\2\2\u009a\u009b\7c\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\u009d\7t\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7{\2\2\u009f\16\3\2\2\2\u00a0\u00a1\7]\2\2\u00a1\20\3")
        buf.write("\2\2\2\u00a2\u00a3\7_\2\2\u00a3\22\3\2\2\2\u00a4\u00a5")
        buf.write("\7q\2\2\u00a5\u00a6\7h\2\2\u00a6\24\3\2\2\2\u00a7\u00a8")
        buf.write("\7<\2\2\u00a8\u00a9\7<\2\2\u00a9\26\3\2\2\2\u00aa\u00ab")
        buf.write("\7k\2\2\u00ab\u00ac\7h\2\2\u00ac\30\3\2\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\u00af\7n\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\32\3\2\2\2\u00b2\u00b3\7y\2\2\u00b3\u00b4")
        buf.write("\7j\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\34\3\2\2\2\u00b8\u00b9\7h\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\u00bb\7t\2\2\u00bb\36\3\2\2\2\u00bc\u00bd")
        buf.write("\7f\2\2\u00bd\u00be\7q\2\2\u00be \3\2\2\2\u00bf\u00c0")
        buf.write("\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7w\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7p\2\2\u00c5\"")
        buf.write("\3\2\2\2\u00c6\u00c7\7d\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7m\2\2\u00cb$\3")
        buf.write("\2\2\2\u00cc\u00cd\7e\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4\7g\2\2\u00d4&\3")
        buf.write("\2\2\2\u00d5\u00d6\7$\2\2\u00d6(\3\2\2\2\u00d7\u00d8\7")
        buf.write("}\2\2\u00d8*\3\2\2\2\u00d9\u00da\7\177\2\2\u00da,\3\2")
        buf.write("\2\2\u00db\u00dc\7*\2\2\u00dc.\3\2\2\2\u00dd\u00de\7+")
        buf.write("\2\2\u00de\60\3\2\2\2\u00df\u00e0\7.\2\2\u00e0\62\3\2")
        buf.write("\2\2\u00e1\u00e2\7<\2\2\u00e2\64\3\2\2\2\u00e3\u00e4\7")
        buf.write("=\2\2\u00e4\66\3\2\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea")
        buf.write("\7i\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ff\7t\2\2\u00ec\u00ed")
        buf.write("\7h\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00ff\7v\2\2\u00f1\u00f2\7d\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\u00f7\7c\2\2\u00f7\u00ff\7p\2\2\u00f8\u00f9")
        buf.write("\7u\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7p\2\2\u00fd\u00ff\7i\2\2\u00fe\u00e5")
        buf.write("\3\2\2\2\u00fe\u00ec\3\2\2\2\u00fe\u00f1\3\2\2\2\u00fe")
        buf.write("\u00f8\3\2\2\2\u00ff8\3\2\2\2\u0100\u0101\7c\2\2\u0101")
        buf.write("\u0102\7w\2\2\u0102\u0103\7v\2\2\u0103\u010a\7q\2\2\u0104")
        buf.write("\u0105\7c\2\2\u0105\u0106\7t\2\2\u0106\u0107\7t\2\2\u0107")
        buf.write("\u0108\7c\2\2\u0108\u010a\7{\2\2\u0109\u0100\3\2\2\2\u0109")
        buf.write("\u0104\3\2\2\2\u010a:\3\2\2\2\u010b\u010c\7\'\2\2\u010c")
        buf.write("<\3\2\2\2\u010d\u010e\7-\2\2\u010e>\3\2\2\2\u010f\u0110")
        buf.write("\7?\2\2\u0110@\3\2\2\2\u0111\u0112\7,\2\2\u0112B\3\2\2")
        buf.write("\2\u0113\u0114\7\61\2\2\u0114D\3\2\2\2\u0115\u0116\7/")
        buf.write("\2\2\u0116F\3\2\2\2\u0117\u0118\7(\2\2\u0118\u0119\7(")
        buf.write("\2\2\u0119H\3\2\2\2\u011a\u011b\7~\2\2\u011b\u011c\7~")
        buf.write("\2\2\u011cJ\3\2\2\2\u011d\u011e\7#\2\2\u011eL\3\2\2\2")
        buf.write("\u011f\u0120\7?\2\2\u0120\u0121\7?\2\2\u0121N\3\2\2\2")
        buf.write("\u0122\u0123\7#\2\2\u0123\u0124\7?\2\2\u0124P\3\2\2\2")
        buf.write("\u0125\u0126\7>\2\2\u0126R\3\2\2\2\u0127\u0128\7@\2\2")
        buf.write("\u0128T\3\2\2\2\u0129\u012a\7>\2\2\u012a\u012b\7?\2\2")
        buf.write("\u012bV\3\2\2\2\u012c\u012d\7@\2\2\u012d\u012e\7?\2\2")
        buf.write("\u012eX\3\2\2\2\u012f\u0130\7v\2\2\u0130\u0131\7t\2\2")
        buf.write("\u0131\u0132\7w\2\2\u0132\u0139\7g\2\2\u0133\u0134\7h")
        buf.write("\2\2\u0134\u0135\7c\2\2\u0135\u0136\7n\2\2\u0136\u0137")
        buf.write("\7u\2\2\u0137\u0139\7g\2\2\u0138\u012f\3\2\2\2\u0138\u0133")
        buf.write("\3\2\2\2\u0139Z\3\2\2\2\u013a\u013f\7\62\2\2\u013b\u013c")
        buf.write("\5]/\2\u013c\u013d\b.\2\2\u013d\u013f\3\2\2\2\u013e\u013a")
        buf.write("\3\2\2\2\u013e\u013b\3\2\2\2\u013f\\\3\2\2\2\u0140\u0144")
        buf.write("\t\2\2\2\u0141\u0143\5_\60\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0154\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0149\7")
        buf.write("a\2\2\u0148\u0147\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148")
        buf.write("\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014e\3\2\2\2\u014c")
        buf.write("\u014a\3\2\2\2\u014d\u014f\5_\60\2\u014e\u014d\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3")
        buf.write("\2\2\2\u0151\u0153\3\2\2\2\u0152\u014a\3\2\2\2\u0153\u0156")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("^\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\t\3\2\2\u0158")
        buf.write("`\3\2\2\2\u0159\u015c\5]/\2\u015a\u015c\7\62\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d\u0167\5c\62\2\u015e\u0161\5]/\2\u015f\u0161\7\62")
        buf.write("\2\2\u0160\u015e\3\2\2\2\u0160\u015f\3\2\2\2\u0161\u0163")
        buf.write("\3\2\2\2\u0162\u0164\5c\62\2\u0163\u0162\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\5e\63\2")
        buf.write("\u0166\u015b\3\2\2\2\u0166\u0160\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168\u0169\b\61\3\2\u0169b\3\2\2\2\u016a\u016e")
        buf.write("\7\60\2\2\u016b\u016d\t\3\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016fd\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173\t\4\2")
        buf.write("\2\u0172\u0174\t\5\2\2\u0173\u0172\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0177\t\3\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179f\3\2\2\2\u017a\u017e\t\6\2")
        buf.write("\2\u017b\u017d\t\7\2\2\u017c\u017b\3\2\2\2\u017d\u0180")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("h\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0185\7$\2\2\u0182")
        buf.write("\u0184\5k\66\2\u0183\u0182\3\2\2\2\u0184\u0187\3\2\2\2")
        buf.write("\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188\3")
        buf.write("\2\2\2\u0187\u0185\3\2\2\2\u0188\u0189\7$\2\2\u0189\u018a")
        buf.write("\b\65\4\2\u018aj\3\2\2\2\u018b\u018e\n\b\2\2\u018c\u018e")
        buf.write("\5m\67\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e")
        buf.write("l\3\2\2\2\u018f\u0190\7^\2\2\u0190\u0191\t\t\2\2\u0191")
        buf.write("n\3\2\2\2\u0192\u0193\7^\2\2\u0193\u0196\n\t\2\2\u0194")
        buf.write("\u0196\n\n\2\2\u0195\u0192\3\2\2\2\u0195\u0194\3\2\2\2")
        buf.write("\u0196p\3\2\2\2\u0197\u0198\7\61\2\2\u0198\u0199\7,\2")
        buf.write("\2\u0199\u019d\3\2\2\2\u019a\u019c\13\2\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019e\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019d\3\2\2\2")
        buf.write("\u01a0\u01a1\7,\2\2\u01a1\u01ac\7\61\2\2\u01a2\u01a3\7")
        buf.write("\61\2\2\u01a3\u01a4\7\61\2\2\u01a4\u01a8\3\2\2\2\u01a5")
        buf.write("\u01a7\n\13\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2")
        buf.write("\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ac")
        buf.write("\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u0197\3\2\2\2\u01ab")
        buf.write("\u01a2\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\b9\5\2")
        buf.write("\u01aer\3\2\2\2\u01af\u01b1\t\f\2\2\u01b0\u01af\3\2\2")
        buf.write("\2\u01b1\u01b2\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\b:\5\2\u01b5")
        buf.write("t\3\2\2\2\u01b6\u01ba\7$\2\2\u01b7\u01b9\5k\66\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01ba\u01bb\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3")
        buf.write("\2\2\2\u01bd\u01bf\t\r\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u01c1\b;\6\2\u01c1v\3\2\2\2\u01c2\u01c6")
        buf.write("\7$\2\2\u01c3\u01c5\5k\66\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca\5")
        buf.write("o8\2\u01ca\u01cb\b<\7\2\u01cbx\3\2\2\2\u01cc\u01cd\13")
        buf.write("\2\2\2\u01cd\u01ce\b=\b\2\u01cez\3\2\2\2\35\2\u00fe\u0109")
        buf.write("\u0138\u013e\u0144\u014a\u0150\u0154\u015b\u0160\u0163")
        buf.write("\u0166\u016e\u0173\u0178\u017e\u0185\u018d\u0195\u019d")
        buf.write("\u01a8\u01ab\u01b2\u01ba\u01be\u01c6\t\3.\2\3\61\3\3\65")
        buf.write("\4\b\2\2\3;\5\3<\6\3=\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    DB = 19
    LP = 20
    RP = 21
    LB = 22
    RB = 23
    COMMA = 24
    COLON = 25
    SEMI = 26
    ATOMICTYPE = 27
    TYPECONST = 28
    REMAINOP = 29
    ADDOP = 30
    ASSIGNOP = 31
    MULOP = 32
    DIVOP = 33
    SUBOP = 34
    AND = 35
    OR = 36
    NEG = 37
    EQ = 38
    NE = 39
    LT = 40
    GT = 41
    LE = 42
    GE = 43
    BOOLLIT = 44
    INTLIT = 45
    FLOATLIT = 46
    IDENTIFY = 47
    STRINGLIT = 48
    CMT = 49
    WS = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52
    ERROR_CHAR = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'inherit'", "'out'", "'function'", "'void'", "'array'", 
            "'['", "']'", "'of'", "'::'", "'if'", "'else'", "'while'", "'for'", 
            "'do'", "'return'", "'break'", "'continue'", "'\"'", "'{'", 
            "'}'", "'('", "')'", "','", "':'", "';'", "'%'", "'+'", "'='", 
            "'*'", "'/'", "'-'", "'&&'", "'||'", "'!'", "'=='", "'!='", 
            "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "DB", "LP", "RP", "LB", "RB", "COMMA", "COLON", "SEMI", "ATOMICTYPE", 
            "TYPECONST", "REMAINOP", "ADDOP", "ASSIGNOP", "MULOP", "DIVOP", 
            "SUBOP", "AND", "OR", "NEG", "EQ", "NE", "LT", "GT", "LE", "GE", 
            "BOOLLIT", "INTLIT", "FLOATLIT", "IDENTIFY", "STRINGLIT", "CMT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "DB", "LP", "RP", 
                  "LB", "RB", "COMMA", "COLON", "SEMI", "ATOMICTYPE", "TYPECONST", 
                  "REMAINOP", "ADDOP", "ASSIGNOP", "MULOP", "DIVOP", "SUBOP", 
                  "AND", "OR", "NEG", "EQ", "NE", "LT", "GT", "LE", "GE", 
                  "BOOLLIT", "INTLIT", "INTPART", "DIGIT", "FLOATLIT", "DECPART", 
                  "EXPPART", "IDENTIFY", "STRINGLIT", "STR_CHAR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "CMT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[44] = self.INTLIT_action 
            actions[47] = self.FLOATLIT_action 
            actions[51] = self.STRINGLIT_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text=self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		possible = [ '\n', '\r', '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


