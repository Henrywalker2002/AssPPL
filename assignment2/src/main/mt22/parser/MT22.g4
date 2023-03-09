// ID : 2013368
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// const 
DB: '"';
LP: '{'; RP : '}'; LB : '('; RB : ')';
COMMA : ','; COLON : ':'; SEMI : ';';
ATOMICTYPE : 'integer' | 'float' | 'boolean' | 'string';
TYPECONST :  'auto' | 'array';
REMAINOP : '%';
ADDOP : '+'; ASSIGNOP : '='; MULOP : '*';DIVOP : '/'; SUBOP : '-';
AND : '&&'; OR : '||'; NEG: '!'; EQ: '=='; NE : '!='; LT : '<'; GT : '>'; LE : '<=';GE : '>=';

// parser

arraylit : LP exprlist RP;
arraylst : arraylit COMMA arraylst | arraylit;
intlst : INTLIT COMMA intlst | INTLIT;
stringlst : STRINGLIT COMMA stringlst | STRINGLIT;
idenlist : IDENTIFY COMMA idenlist | IDENTIFY;

// declare 
vardecl : idenlist ':' (TYPECONST|ATOMICTYPE|arrDecl) | helper;
helper : IDENTIFY COMMA helper COMMA expr | IDENTIFY COLON (TYPECONST|ATOMICTYPE|arrDecl) '=' expr; 

// function declare
parameterdecl : 'inherit'? 'out'? IDENTIFY ':' (TYPECONST|ATOMICTYPE | arrDecl);
paralist : paraprime | ;
paraprime : parameterdecl COMMA paraprime | parameterdecl;

functiondecl: IDENTIFY ':' 'function' (TYPECONST | ATOMICTYPE | arrDecl | 'void') LB paralist RB ('inherit' IDENTIFY)? body ;
body : blockstmt;

// array declare 
arrDecl : 'array' '[' exprlist ']' 'of' ATOMICTYPE;

decl : (vardecl SEMI) | functiondecl ;

// expression 
exprlist : exprime | ;
exprime : expr COMMA exprime | expr;

expr : expr2 '::' expr2 | expr2;
expr2 : expr3 (EQ|NE|LT|GT|LE|GE) expr3 | expr3;
expr3 : expr3 (AND|OR) expr4 | expr4;
expr4 : expr4 (ADDOP|SUBOP) expr5 | expr5;
expr5 : expr5 (MULOP|DIVOP|REMAINOP) expr6 | expr6;
expr6 : NEG expr6 | expr7 ;
expr7 : SUBOP expr7 | expr8 ;
expr8 : IDENTIFY '[' exprlist ']' | expr9;
expr9 : IDENTIFY | STRINGLIT | INTLIT | FLOATLIT | BOOLLIT | arraylit | funccallstmt| (LB expr RB);
// expr : exprInt | exprFloat | exprBool | exprStr | exprIndex;

// // FLOAT OPERATOR
// exprFloat : exprFloat2 (LE|GE|LT|GT) exprFloat2|exprFloat2;
// exprFloat2: exprFloat2 (ADDOP|SUBOP) exprFloat3|exprInt3;
// exprFloat3: exprFloat3 (MULOP|DIVOP) exprFloat4|exprFloat4;
// exprFloat4: LB exprFloat RB|exprFloat5;
// exprFloat5: SUBOP exprFloat5 | exprFloat6;
// exprFloat6: FLOATLIT | IDENTIFY | funccallstml;

// // INT OPERATOR 
// exprInt : exprInt2 (EQ|NE|LE|GE|LT|GT) exprInt2|exprInt2;
// exprInt2: exprInt2 (ADDOP|SUBOP) exprInt3
// 		|exprInt3;
// exprInt3: exprInt3 (MULOP|DIVOP|REMAINOP) exprInt4|exprInt4;
// exprInt4: LB exprInt RB|exprInt5;
// exprInt5: SUBOP exprInt5 | exprInt6;
// exprInt6: INTLIT | IDENTIFY | funccallstml;

// // string operator
// exprStr : (STRINGLIT | IDENTIFY | funccallstml) '::' (STRINGLIT | IDENTIFY | funccallstml);

// // bool operator
// exprBool: exprBool2 (EQ|NE) exprBool2|exprBool2;
// exprBool2: exprBool2 (AND|OR) exprBool3 | exprBool3;
// exprBool3: NEG exprBool3 | exprBool4;
// exprBool4: BOOLLIT | IDENTIFY | funccallstml;

// index operator 
exprIndex : IDENTIFY '[' exprlist ']';

// statement
// assign
assignstmt : (IDENTIFY|exprIndex) '=' expr;

//if statement
ifstmt : 'if' LB expr RB stmt ('else' stmt)?;

// while statement 
whilestmt: 'while' LB expr RB stmt;

//for statement
forstmt: 'for' LB (IDENTIFY|exprIndex) '=' INTLIT COMMA expr COMMA expr RB stmt;

//do while
dowhilestmt: 'do' blockstmt 'while' expr;

//return stmt
returnstmt: 'return' expr?;

//call stmt
funccallstmt : IDENTIFY LB (exprlist) RB;

stmt: (('break'|'continue'|returnstmt|assignstmt|dowhilestmt|funccallstmt|vardecl) SEMI)|(blockstmt|forstmt|ifstmt|whilestmt);

stmtlist: stmt stmtlist | stmt;

blockstmt: LP (stmtlist |) RP;

// lexer 

BOOLLIT : 'true' | 'false';

INTLIT : '0'
		| INTPART {self.text = self.text.replace('_', '')};

fragment INTPART : [1-9] DIGIT* ('_'* DIGIT+)* ;

fragment DIGIT : [0-9];

FLOATLIT : ((INTPART|'0') DECPART | (INTPART|'0') DECPART? EXPPART ) {self.text=self.text.replace("_","")};

fragment DECPART : '.' [0-9]* ;
fragment EXPPART : [Ee][+-]? [0-9]+ ;

IDENTIFY : [a-zA-Z_] [a-zA-Z0-9_]*;

STRINGLIT : '"' STR_CHAR* '"' {self.text=self.text[1:-1]};

fragment STR_CHAR: ~["\\\n\r] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [btnfr"'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;

decllist: decl decllist | decl;

CMT: (('/*' .*? '*/') | ('//' (~[\r\n])*)) -> skip;

// program
program: decllist EOF;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = [ '\n', '\r', '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;

ERROR_CHAR: . {raise ErrorToken(self.text)};