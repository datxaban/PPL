//1752159
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  :(vardeclare|functiondeclare)+ EOF;
functiondeclare: nonvoidfunctiondeclare|voidfunctiondeclare|functionpoitertype;
vardeclare: (FLOATTYPE|INTTYPE|STRINGTYPE|BOOLTYPE) var (COMMA var)* SEMI;
variable: (FLOATTYPE|INTTYPE|STRINGTYPE|BOOLTYPE) ID (LS RS)? (COMMA ID (LS RS)?)*;
var: ID (LS INTLIT RS)?;
voidfunctiondeclare: VOIDTYPE ID LB parameterlist? RB LP functionbody voidreturnstatement? RP;
functionpoitertype: (FLOATTYPE LS RS|INTTYPE LS RS|STRINGTYPE LS RS|BOOLTYPE LS RS) ID LB parameterlist? RB LP functionbody nonvoidreturnstatement? RP;
nonvoidfunctiondeclare: (FLOATTYPE|INTTYPE|STRINGTYPE|BOOLTYPE) ID LB parameterlist? RB LP functionbody nonvoidreturnstatement? RP;
parameterlist: variable (COMMA variable)*;
para:(FLOATTYPE|INTTYPE|STRINGTYPE|BOOLTYPE) ID (LS RS)? (COMMA ID (LS RS)?)* ;
//parameterlist: variable (COMMA variable)*;
exp: funcall|INTLIT|ID|BOOLLIT|FLOATLIT|STRINGLIT|orexpression ;
functionbody: statement*;
funcall: ID LB (exp (COMMA exp)*)? RB SEMI;
notfullfuncall: ID LB (exp (COMMA exp)*)? RB;
//buildin function
builtinfunction: getintcall|putintcall|putintlncall|getfloatcall|putfloatcall|putfloatlncall|putboolcall|putboollncall|putstringcall|putstringlncall|putlncall;
getintcall: 'getInt'LB RB SEMI;
putintcall: 'putInt'LB (ID|INTLIT) RB SEMI;
putintlncall: 'putIntLn'LB (ID|INTLIT) RB SEMI;
getfloatcall: 'getFloat'LB RB SEMI;
putfloatcall: 'putFloat'LB (ID|FLOATLIT) RB SEMI;
putfloatlncall: 'putFloatLn'LB (ID|FLOATLIT) RB SEMI;
putboolcall: 'putBool' LB (ID|BOOLLIT) RB SEMI;
putboollncall: 'putBoolLn' LB (ID|BOOLLIT) RB SEMI;
putstringcall: 'putString' LB (ID|STRINGLIT) RB SEMI;
putstringlncall: 'putStringLn' LB (ID|STRINGLIT) RB SEMI;
putlncall: 'putLn'LB RB SEMI;
//expression
expression: orexpression ASSIGN expression|orexpression;
orexpression: orexpression OR andexpression|andexpression;
andexpression: andexpression AND term|term;
term: compareexpression (EQUAL|NOTEQUAL) compareexpression|compareexpression;
compareexpression: arithexpression (LESSEQUAL|LESS|GREATER|GREATEREQUAL) arithexpression|arithexpression;
arithexpression: arithexpression (ADD|SUB) arithmeticexpression|arithmeticexpression;
arithmeticexpression: arithmeticexpression (MULTIPLICATION|DIV|MOD) negativeexpression|negativeexpression;
negativeexpression: (SUB|NOT) negativeexpression | square;
square: operand LS expression RS | ex;
ex: operand|LB expression RB;
operand: INTLIT|FLOATLIT|STRINGLIT|BOOLLIT|ID|notfullfuncall;
//statement
statement:expression SEMI
            |blockstatement
            |builtinfunction
            |ifstatement
            |dowhilestatement
            |forstatement
            |breakstatement
            |continuestatement
            |voidreturnstatement
            |nonvoidreturnstatement
            |vardeclare;
blockstatement: LP statement* RP;
ifstatement:IF LB orexpression RB statement ELSE statement
            |IF LB orexpression RB statement;
dowhilestatement: DO statement+ WHILE expression SEMI;
forstatement: FOR LB expression SEMI orexpression SEMI expression RB statement;
breakstatement:BREAK SEMI;
continuestatement:CONTINUE SEMI;
voidreturnstatement: 'return' SEMI;
nonvoidreturnstatement: 'return' expression SEMI;

//Separator
LS: '[';
RS: ']';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
SEMI: ';';
COMMA: ',';
//keyword
BOOLLIT:TRUE|FALSE;
BREAK:'break';
FOR: 'for';
CONTINUE:'continue';
IF: 'if';
ELSE:'else';
DO: 'do';
WHILE: 'while';
TRUE:'true';
FALSE:'false';
RETURN: 'RETURN';
INTTYPE: 'int' ;
VOIDTYPE: 'void' ;
FLOATTYPE:'float';
STRINGTYPE: 'string';
BOOLTYPE:'boolean';

ID: [_a-zA-Z]+ [_a-zA-Z0-9]* ;
INTLIT: [0-9]+;
FLOATLIT: ([0-9]+  ('.' [0-9]*)?) ([Ee] '-'? [0-9]+)
            |[0-9]* '.' [0-9]+ ([Ee] '-'? [0-9]+)? 
            |[0-9]+  '.' [0-9]* ([Ee] '-'? [0-9]+)? ;


//Operator
ADD: '+';
SUB:'-';
DIV:'/';
MOD: '%';
AND: '&&';
EQUAL: '==';
GREATER: '>';
GREATEREQUAL: '>=';
MULTIPLICATION: '*';
NOT: '!';
OR: '||';
NOTEQUAL: '!=';
LESS: '<';
LESSEQUAL: '<=';
ASSIGN: '=';


//String type and string error
fragment DOUBLEQUOTES:'"';
ILLEGAL_ESCAPE: DOUBLEQUOTES (INSIDESTRING|~[\n\r\b\f\t\\"])* '\\'~[bfrnt\\"];
STRINGLIT: DOUBLEQUOTES (INSIDESTRING|~[\n\r\t\\"])* DOUBLEQUOTES{self.text = self.text[1:-1]};
fragment INSIDESTRING: '\\'[bfrnt"\\];
UNCLOSE_STRING: DOUBLEQUOTES (INSIDESTRING|~[\n\r\t\\"])*;

//No token
WS : [ \f\b\r\t\n]+ -> skip ; // skip spaces, tabs, newlines
INLINECMT: '//' ~[\r\n]* ->skip;
BLOCKCMT: '/*' .*? '*/' ->skip;



//Throw exception
ERROR_CHAR:.;