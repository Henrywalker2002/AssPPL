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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u01cc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u00f8")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\5,\u012c\n,\3-\3-\3-\3-\5-\u0132\n")
        buf.write("-\3.\3.\7.\u0136\n.\f.\16.\u0139\13.\3.\7.\u013c\n.\f")
        buf.write(".\16.\u013f\13.\3.\6.\u0142\n.\r.\16.\u0143\7.\u0146\n")
        buf.write(".\f.\16.\u0149\13.\3/\3/\3\60\3\60\5\60\u014f\n\60\3\60")
        buf.write("\3\60\3\60\5\60\u0154\n\60\3\60\5\60\u0157\n\60\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u015d\n\60\3\60\6\60\u0160\n\60\r\60")
        buf.write("\16\60\u0161\5\60\u0164\n\60\3\60\3\60\3\61\3\61\7\61")
        buf.write("\u016a\n\61\f\61\16\61\u016d\13\61\3\62\3\62\5\62\u0171")
        buf.write("\n\62\3\62\6\62\u0174\n\62\r\62\16\62\u0175\3\63\3\63")
        buf.write("\7\63\u017a\n\63\f\63\16\63\u017d\13\63\3\64\3\64\7\64")
        buf.write("\u0181\n\64\f\64\16\64\u0184\13\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\5\65\u018b\n\65\3\66\3\66\3\66\3\67\3\67\3\67\5")
        buf.write("\67\u0193\n\67\38\38\38\38\78\u0199\n8\f8\168\u019c\13")
        buf.write("8\38\38\38\38\38\38\78\u01a4\n8\f8\168\u01a7\138\58\u01a9")
        buf.write("\n8\38\38\39\69\u01ae\n9\r9\169\u01af\39\39\3:\3:\7:\u01b6")
        buf.write("\n:\f:\16:\u01b9\13:\3:\5:\u01bc\n:\3:\3:\3;\3;\7;\u01c2")
        buf.write("\n;\f;\16;\u01c5\13;\3;\3;\3;\3<\3<\3<\3\u019a\2=\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[\2]\2_/a\2c\2e\60g\61i\2k\2m\2o\62q\63s\64u\65")
        buf.write("w\66\3\2\16\3\2\63;\3\2\62;\4\2GGgg\4\2--//\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttv")
        buf.write("v\3\2^^\4\2\f\f\17\17\5\2\13\f\17\17\"\"\7\3\n\f\16\17")
        buf.write("$$))^^\2\u01e1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2_\3")
        buf.write("\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5\u0081\3\2")
        buf.write("\2\2\7\u0085\3\2\2\2\t\u008e\3\2\2\2\13\u0093\3\2\2\2")
        buf.write("\r\u0099\3\2\2\2\17\u009b\3\2\2\2\21\u009d\3\2\2\2\23")
        buf.write("\u00a0\3\2\2\2\25\u00a3\3\2\2\2\27\u00a6\3\2\2\2\31\u00ab")
        buf.write("\3\2\2\2\33\u00b1\3\2\2\2\35\u00b5\3\2\2\2\37\u00b8\3")
        buf.write("\2\2\2!\u00bf\3\2\2\2#\u00c5\3\2\2\2%\u00ce\3\2\2\2\'")
        buf.write("\u00d0\3\2\2\2)\u00d2\3\2\2\2+\u00d4\3\2\2\2-\u00d6\3")
        buf.write("\2\2\2/\u00d8\3\2\2\2\61\u00da\3\2\2\2\63\u00dc\3\2\2")
        buf.write("\2\65\u00f7\3\2\2\2\67\u00f9\3\2\2\29\u00fe\3\2\2\2;\u0100")
        buf.write("\3\2\2\2=\u0102\3\2\2\2?\u0104\3\2\2\2A\u0106\3\2\2\2")
        buf.write("C\u0108\3\2\2\2E\u010a\3\2\2\2G\u010d\3\2\2\2I\u0110\3")
        buf.write("\2\2\2K\u0112\3\2\2\2M\u0115\3\2\2\2O\u0118\3\2\2\2Q\u011a")
        buf.write("\3\2\2\2S\u011c\3\2\2\2U\u011f\3\2\2\2W\u012b\3\2\2\2")
        buf.write("Y\u0131\3\2\2\2[\u0133\3\2\2\2]\u014a\3\2\2\2_\u0163\3")
        buf.write("\2\2\2a\u0167\3\2\2\2c\u016e\3\2\2\2e\u0177\3\2\2\2g\u017e")
        buf.write("\3\2\2\2i\u018a\3\2\2\2k\u018c\3\2\2\2m\u0192\3\2\2\2")
        buf.write("o\u01a8\3\2\2\2q\u01ad\3\2\2\2s\u01b3\3\2\2\2u\u01bf\3")
        buf.write("\2\2\2w\u01c9\3\2\2\2yz\7k\2\2z{\7p\2\2{|\7j\2\2|}\7g")
        buf.write("\2\2}~\7t\2\2~\177\7k\2\2\177\u0080\7v\2\2\u0080\4\3\2")
        buf.write("\2\2\u0081\u0082\7q\2\2\u0082\u0083\7w\2\2\u0083\u0084")
        buf.write("\7v\2\2\u0084\6\3\2\2\2\u0085\u0086\7h\2\2\u0086\u0087")
        buf.write("\7w\2\2\u0087\u0088\7p\2\2\u0088\u0089\7e\2\2\u0089\u008a")
        buf.write("\7v\2\2\u008a\u008b\7k\2\2\u008b\u008c\7q\2\2\u008c\u008d")
        buf.write("\7p\2\2\u008d\b\3\2\2\2\u008e\u008f\7x\2\2\u008f\u0090")
        buf.write("\7q\2\2\u0090\u0091\7k\2\2\u0091\u0092\7f\2\2\u0092\n")
        buf.write("\3\2\2\2\u0093\u0094\7c\2\2\u0094\u0095\7t\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7c\2\2\u0097\u0098\7{\2\2\u0098\f")
        buf.write("\3\2\2\2\u0099\u009a\7]\2\2\u009a\16\3\2\2\2\u009b\u009c")
        buf.write("\7_\2\2\u009c\20\3\2\2\2\u009d\u009e\7q\2\2\u009e\u009f")
        buf.write("\7h\2\2\u009f\22\3\2\2\2\u00a0\u00a1\7<\2\2\u00a1\u00a2")
        buf.write("\7<\2\2\u00a2\24\3\2\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7h\2\2\u00a5\26\3\2\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8")
        buf.write("\7n\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa\7g\2\2\u00aa\30")
        buf.write("\3\2\2\2\u00ab\u00ac\7y\2\2\u00ac\u00ad\7j\2\2\u00ad\u00ae")
        buf.write("\7k\2\2\u00ae\u00af\7n\2\2\u00af\u00b0\7g\2\2\u00b0\32")
        buf.write("\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4")
        buf.write("\7t\2\2\u00b4\34\3\2\2\2\u00b5\u00b6\7f\2\2\u00b6\u00b7")
        buf.write("\7q\2\2\u00b7\36\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00be\7p\2\2\u00be \3\2\2\2\u00bf\u00c0")
        buf.write("\7d\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7m\2\2\u00c4\"\3\2\2\2\u00c5\u00c6")
        buf.write("\7e\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc")
        buf.write("\7w\2\2\u00cc\u00cd\7g\2\2\u00cd$\3\2\2\2\u00ce\u00cf")
        buf.write("\7$\2\2\u00cf&\3\2\2\2\u00d0\u00d1\7}\2\2\u00d1(\3\2\2")
        buf.write("\2\u00d2\u00d3\7\177\2\2\u00d3*\3\2\2\2\u00d4\u00d5\7")
        buf.write("*\2\2\u00d5,\3\2\2\2\u00d6\u00d7\7+\2\2\u00d7.\3\2\2\2")
        buf.write("\u00d8\u00d9\7.\2\2\u00d9\60\3\2\2\2\u00da\u00db\7<\2")
        buf.write("\2\u00db\62\3\2\2\2\u00dc\u00dd\7=\2\2\u00dd\64\3\2\2")
        buf.write("\2\u00de\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7")
        buf.write("v\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7i\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\u00f8\7t\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7c\2\2\u00e9\u00f8")
        buf.write("\7v\2\2\u00ea\u00eb\7d\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f8\7p\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f8\7i\2\2\u00f7\u00de\3\2\2\2\u00f7\u00e5")
        buf.write("\3\2\2\2\u00f7\u00ea\3\2\2\2\u00f7\u00f1\3\2\2\2\u00f8")
        buf.write("\66\3\2\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7w\2\2\u00fb")
        buf.write("\u00fc\7v\2\2\u00fc\u00fd\7q\2\2\u00fd8\3\2\2\2\u00fe")
        buf.write("\u00ff\7\'\2\2\u00ff:\3\2\2\2\u0100\u0101\7-\2\2\u0101")
        buf.write("<\3\2\2\2\u0102\u0103\7?\2\2\u0103>\3\2\2\2\u0104\u0105")
        buf.write("\7,\2\2\u0105@\3\2\2\2\u0106\u0107\7\61\2\2\u0107B\3\2")
        buf.write("\2\2\u0108\u0109\7/\2\2\u0109D\3\2\2\2\u010a\u010b\7(")
        buf.write("\2\2\u010b\u010c\7(\2\2\u010cF\3\2\2\2\u010d\u010e\7~")
        buf.write("\2\2\u010e\u010f\7~\2\2\u010fH\3\2\2\2\u0110\u0111\7#")
        buf.write("\2\2\u0111J\3\2\2\2\u0112\u0113\7?\2\2\u0113\u0114\7?")
        buf.write("\2\2\u0114L\3\2\2\2\u0115\u0116\7#\2\2\u0116\u0117\7?")
        buf.write("\2\2\u0117N\3\2\2\2\u0118\u0119\7>\2\2\u0119P\3\2\2\2")
        buf.write("\u011a\u011b\7@\2\2\u011bR\3\2\2\2\u011c\u011d\7>\2\2")
        buf.write("\u011d\u011e\7?\2\2\u011eT\3\2\2\2\u011f\u0120\7@\2\2")
        buf.write("\u0120\u0121\7?\2\2\u0121V\3\2\2\2\u0122\u0123\7v\2\2")
        buf.write("\u0123\u0124\7t\2\2\u0124\u0125\7w\2\2\u0125\u012c\7g")
        buf.write("\2\2\u0126\u0127\7h\2\2\u0127\u0128\7c\2\2\u0128\u0129")
        buf.write("\7n\2\2\u0129\u012a\7u\2\2\u012a\u012c\7g\2\2\u012b\u0122")
        buf.write("\3\2\2\2\u012b\u0126\3\2\2\2\u012cX\3\2\2\2\u012d\u0132")
        buf.write("\7\62\2\2\u012e\u012f\5[.\2\u012f\u0130\b-\2\2\u0130\u0132")
        buf.write("\3\2\2\2\u0131\u012d\3\2\2\2\u0131\u012e\3\2\2\2\u0132")
        buf.write("Z\3\2\2\2\u0133\u0137\t\2\2\2\u0134\u0136\5]/\2\u0135")
        buf.write("\u0134\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2")
        buf.write("\u0137\u0138\3\2\2\2\u0138\u0147\3\2\2\2\u0139\u0137\3")
        buf.write("\2\2\2\u013a\u013c\7a\2\2\u013b\u013a\3\2\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0142\5]/\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u013d\3")
        buf.write("\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\\\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b")
        buf.write("\t\3\2\2\u014b^\3\2\2\2\u014c\u014f\5[.\2\u014d\u014f")
        buf.write("\7\62\2\2\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0164\5a\61\2\u0151\u0154\5[.\2\u0152")
        buf.write("\u0154\7\62\2\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2")
        buf.write("\2\u0154\u0156\3\2\2\2\u0155\u0157\5a\61\2\u0156\u0155")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write("\u0164\5c\62\2\u0159\u015a\7\60\2\2\u015a\u015c\t\4\2")
        buf.write("\2\u015b\u015d\7-\2\2\u015c\u015b\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u015f\3\2\2\2\u015e\u0160\t\3\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u014e\3")
        buf.write("\2\2\2\u0163\u0153\3\2\2\2\u0163\u0159\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0166\b\60\3\2\u0166`\3\2\2\2\u0167\u016b")
        buf.write("\7\60\2\2\u0168\u016a\t\3\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016cb\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0170\t\4\2")
        buf.write("\2\u016f\u0171\t\5\2\2\u0170\u016f\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0174\t\3\2\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176d\3\2\2\2\u0177\u017b\t\6\2")
        buf.write("\2\u0178\u017a\t\7\2\2\u0179\u0178\3\2\2\2\u017a\u017d")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("f\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0182\7$\2\2\u017f")
        buf.write("\u0181\5i\65\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\7$\2\2\u0186\u0187")
        buf.write("\b\64\4\2\u0187h\3\2\2\2\u0188\u018b\n\b\2\2\u0189\u018b")
        buf.write("\5k\66\2\u018a\u0188\3\2\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("j\3\2\2\2\u018c\u018d\7^\2\2\u018d\u018e\t\t\2\2\u018e")
        buf.write("l\3\2\2\2\u018f\u0190\7^\2\2\u0190\u0193\n\t\2\2\u0191")
        buf.write("\u0193\n\n\2\2\u0192\u018f\3\2\2\2\u0192\u0191\3\2\2\2")
        buf.write("\u0193n\3\2\2\2\u0194\u0195\7\61\2\2\u0195\u0196\7,\2")
        buf.write("\2\u0196\u019a\3\2\2\2\u0197\u0199\13\2\2\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u019b\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019d\u019e\7,\2\2\u019e\u01a9\7\61\2\2\u019f\u01a0\7")
        buf.write("\61\2\2\u01a0\u01a1\7\61\2\2\u01a1\u01a5\3\2\2\2\u01a2")
        buf.write("\u01a4\n\13\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7\3\2\2")
        buf.write("\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a9")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u0194\3\2\2\2\u01a8")
        buf.write("\u019f\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\b8\5\2")
        buf.write("\u01abp\3\2\2\2\u01ac\u01ae\t\f\2\2\u01ad\u01ac\3\2\2")
        buf.write("\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\b9\5\2\u01b2")
        buf.write("r\3\2\2\2\u01b3\u01b7\7$\2\2\u01b4\u01b6\5i\65\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01ba\u01bc\t\r\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u01be\b:\6\2\u01bet\3\2\2\2\u01bf\u01c3")
        buf.write("\7$\2\2\u01c0\u01c2\5i\65\2\u01c1\u01c0\3\2\2\2\u01c2")
        buf.write("\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\5")
        buf.write("m\67\2\u01c7\u01c8\b;\7\2\u01c8v\3\2\2\2\u01c9\u01ca\13")
        buf.write("\2\2\2\u01ca\u01cb\b<\b\2\u01cbx\3\2\2\2\36\2\u00f7\u012b")
        buf.write("\u0131\u0137\u013d\u0143\u0147\u014e\u0153\u0156\u015c")
        buf.write("\u0161\u0163\u016b\u0170\u0175\u017b\u0182\u018a\u0192")
        buf.write("\u019a\u01a5\u01a8\u01af\u01b7\u01bb\u01c3\t\3-\2\3\60")
        buf.write("\3\3\64\4\b\2\2\3:\5\3;\6\3<\7")
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
    DB = 18
    LP = 19
    RP = 20
    LB = 21
    RB = 22
    COMMA = 23
    COLON = 24
    SEMI = 25
    ATOMICTYPE = 26
    TYPECONST = 27
    REMAINOP = 28
    ADDOP = 29
    ASSIGNOP = 30
    MULOP = 31
    DIVOP = 32
    SUBOP = 33
    AND = 34
    OR = 35
    NEG = 36
    EQ = 37
    NE = 38
    LT = 39
    GT = 40
    LE = 41
    GE = 42
    BOOLLIT = 43
    INTLIT = 44
    FLOATLIT = 45
    IDENTIFY = 46
    STRINGLIT = 47
    CMT = 48
    WS = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'inherit'", "'out'", "'function'", "'void'", "'array'", "'['", 
            "']'", "'of'", "'::'", "'if'", "'else'", "'while'", "'for'", 
            "'do'", "'return'", "'break'", "'continue'", "'\"'", "'{'", 
            "'}'", "'('", "')'", "','", "':'", "';'", "'auto'", "'%'", "'+'", 
            "'='", "'*'", "'/'", "'-'", "'&&'", "'||'", "'!'", "'=='", "'!='", 
            "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "DB", "LP", "RP", "LB", "RB", "COMMA", "COLON", "SEMI", "ATOMICTYPE", 
            "TYPECONST", "REMAINOP", "ADDOP", "ASSIGNOP", "MULOP", "DIVOP", 
            "SUBOP", "AND", "OR", "NEG", "EQ", "NE", "LT", "GT", "LE", "GE", 
            "BOOLLIT", "INTLIT", "FLOATLIT", "IDENTIFY", "STRINGLIT", "CMT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "DB", "LP", "RP", "LB", "RB", 
                  "COMMA", "COLON", "SEMI", "ATOMICTYPE", "TYPECONST", "REMAINOP", 
                  "ADDOP", "ASSIGNOP", "MULOP", "DIVOP", "SUBOP", "AND", 
                  "OR", "NEG", "EQ", "NE", "LT", "GT", "LE", "GE", "BOOLLIT", 
                  "INTLIT", "INTPART", "DIGIT", "FLOATLIT", "DECPART", "EXPPART", 
                  "IDENTIFY", "STRINGLIT", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "CMT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[43] = self.INTLIT_action 
            actions[46] = self.FLOATLIT_action 
            actions[50] = self.STRINGLIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
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
     


