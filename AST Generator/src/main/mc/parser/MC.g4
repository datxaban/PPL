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

program: declaration+ EOF;
declaration: vardeclare|functiondeclare;
functiondeclare: nonvoidfunctiondeclare|voidfunctiondeclare|functionpoitertype;
vardeclare: primitivetype var (COMMA var)* SEMI;
primitivetype: FLOATTYPE|INTTYPE|STRINGTYPE|BOOLTYPE;
var: ID (LS INTLIT RS)?;
voidfunctiondeclare: functiontype ID LB parameterlists RB LP functionbody RP;
functiontype: VOIDTYPE;
functionpoitertype: primitivetype LS RS ID LB parameterlists RB LP functionbody RP;
nonvoidfunctiondeclare: primitivetype ID LB parameterlists RB LP functionbody RP;
parameterlists: variable (COMMA variable)*|;
variable: primitivetype ID (LS RS)?;
functionbody: statement*;
funcall: ID LB param RB;
param: exp (COMMA exp)*|;
exp: funcall|INTLIT|ID|BOOLLIT|FLOATLIT|STRINGLIT|orexpression;
expression: orexpression ASSIGN expression|orexpression;
orexpression: orexpression OR andexpression|andexpression;
andexpression: andexpression AND term|term;
term: compareexpression termop compareexpression|compareexpression;
termop: EQUAL|NOTEQUAL;
compareexpression: arithexpression compareop arithexpression|arithexpression;
compareop: LESSEQUAL|LESS|GREATER|GREATEREQUAL;
arithexpression: arithexpression arithop arithmeticexpression|arithmeticexpression;
arithop: ADD|SUB;
arithmeticexpression: arithmeticexpression arithmeticop negativeexpression|negativeexpression;
arithmeticop: MULTIPLICATION|DIV|MOD;
negativeexpression: negativeop negativeexpression | square;
negativeop: SUB|NOT;
square: operand LS expression RS | ex;
ex: operand|LB expression RB;
operand: INTLIT|FLOATLIT|STRINGLIT|BOOLLIT|ID|funcall;
statement:  expression SEMI
            |blockstatement
            |funcall SEMI
            |ifstatement
            |dowhilestatement
            |forstatement
            |breakstatement
            |continuestatement
            |voidreturnstatement
            |nonvoidreturnstatement
            |vardeclare;
blockstatement: LP statement* RP;
ifstatement:IF LB orexpression RB statement
            |IF LB orexpression RB statement ELSE statement;
dowhilestatement: DO statement+ WHILE orexpression SEMI;
forstatement: FOR LB expression SEMI orexpression SEMI expression RB statement;
breakstatement:BREAK SEMI;
continuestatement:CONTINUE SEMI;
voidreturnstatement: 'return' SEMI;
nonvoidreturnstatement: 'return' orexpression SEMI;

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
BOOLLIT:'true'|'false';
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