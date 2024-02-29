import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",1))
    def test_identifier_underscore_start(self):
        """test identifiers start with underscore"""
        self.assertTrue(TestLexer.checkLexeme("_abc","_abc,<EOF>",2))
    def test_lower_upper_identifier(self):
        """test identifiers with lower, upper case identifier"""
        self.assertTrue(TestLexer.checkLexeme("abcXyZvBn","abcXyZvBn,<EOF>",3))
    def test_interger(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("123abc123","123,abc123,<EOF>",4))
    def test_float(self):
        """test float number"""
        self.assertTrue(TestLexer.checkLexeme("1.99","1.99,<EOF>",5))
    def test_float_bigE(self):
        """test float number"""
        self.assertTrue(TestLexer.checkLexeme(".1E-12",".1E-12,<EOF>",6))
    def test_float_smallE(self):
        """test float number"""
        self.assertTrue(TestLexer.checkLexeme("1.e20","1.e20,<EOF>",7))
    def test_float_no_decimal_point(self):
        """test float have no decimal point"""
        self.assertTrue(TestLexer.checkLexeme("12E99","12E99,<EOF>",8))
    def test_wrong_float_bigE(self):
        """test float number with wrong syntax"""
        self.assertTrue(TestLexer.checkLexeme("122E","122,E,<EOF>",9))
    def test_wrong_float_smallE(self):
        """test wrong syntax float number"""
        self.assertTrue(TestLexer.checkLexeme("e-12","e,-,12,<EOF>",10))
    def test_wrong_float(self):
        """test wrong syntax float number"""
        self.assertTrue(TestLexer.checkLexeme("122e","122,e,<EOF>",11))
    def test_float_decimal_number_only(self):
        """test special syntax float number"""
        self.assertTrue(TestLexer.checkLexeme(".0",".0,<EOF>",12))
    def test_float_int_number_only(self):
        """test special syntax float number"""
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",13))
    def test_white_space_tab(self):
        """test tab"""
        self.assertTrue(TestLexer.checkLexeme("\t","<EOF>",14))
    def test_white_space_newline(self):
        """test newline"""
        self.assertTrue(TestLexer.checkLexeme("\n","<EOF>",15))
    def test_white_space_formfeed(self):
        """test formfeed"""
        self.assertTrue(TestLexer.checkLexeme("\f","<EOF>",16))
    def test_white_space_return(self):
        """test return escape"""
        self.assertTrue(TestLexer.checkLexeme("\r","<EOF>",17))
    def test_bank_space(self):
        """test no token in the file"""
        self.assertTrue(TestLexer.checkLexeme("","<EOF>",18))
    def test_inline_comment(self):
        """test line commment"""
        self.assertTrue(TestLexer.checkLexeme("//This is a comment","<EOF>",19))
    def test_inline_comment_with_newline(self):
        """test newline in line comment"""
        self.assertTrue(TestLexer.checkLexeme("//This is a comment with new line \n alo","alo,<EOF>",20))
    def test_block_comment(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme("/*This is a block comment*/","<EOF>",21))
    def test_block_comment_escape_inside(self):
        """test block comment with legal escape"""
        self.assertTrue(TestLexer.checkLexeme("/* \n\f\b\r\t > <*/","<EOF>",22))
    def test_keyword_type(self):
        """test keyword type"""
        self.assertTrue(TestLexer.checkLexeme("int float string boolean intfloat","int,float,string,boolean,intfloat,<EOF>",23))
    def test_keyword(self):
        """test other keyword"""
        self.assertTrue(TestLexer.checkLexeme("continue else for return void do while true false","continue,else,for,return,void,do,while,true,false,<EOF>",24))
    def test_arithmetic_operator(self):
        """test arithmetic operator"""
        self.assertTrue(TestLexer.checkLexeme("+-*/","+,-,*,/,<EOF>",25))
    def test_logical_operator(self):
        """test logical operator"""
        self.assertTrue(TestLexer.checkLexeme("!===||<==&&>==","!=,==,||,<=,=,&&,>=,=,<EOF>",26))
    def test_separator(self):
        """test bracker"""
        self.assertTrue(TestLexer.checkLexeme("[]{}()","[,],{,},(,),<EOF>",27))
    def test_exp_operator_int(self):
        """test expression"""
        self.assertTrue(TestLexer.checkLexeme("1+1=2","1,+,1,=,2,<EOF>",28))
    def test_exp_operator_int_separator(self):
        """test expression with bracket"""
        self.assertTrue(TestLexer.checkLexeme("(1+2=3)","(,1,+,2,=,3,),<EOF>",29))
    def test_exp_operators(self):
        """test arithmetic expression with bracket"""
        self.assertTrue(TestLexer.checkLexeme("(1+2)*3=9","(,1,+,2,),*,3,=,9,<EOF>",30))
    def test_logical_exp(self):
        """test compare expression"""
        self.assertTrue(TestLexer.checkLexeme("1<2","1,<,2,<EOF>",31))
    def test_logical_exp_arithmetic(self):
        """test compare expression"""
        self.assertTrue(TestLexer.checkLexeme("(1+2)<3*4","(,1,+,2,),<,3,*,4,<EOF>",32))
    def test_expression(self):
        """test logical expression"""
        self.assertTrue(TestLexer.checkLexeme("(1+2=3)&&(2+1=3)","(,1,+,2,=,3,),&&,(,2,+,1,=,3,),<EOF>",33))
    def test_complex_logical_expression(self):
        """test logical expression"""
        self.assertTrue(TestLexer.checkLexeme("(1+2=3)||(2+1=3)","(,1,+,2,=,3,),||,(,2,+,1,=,3,),<EOF>",34))
    def test_nested_logical(self):
        """test nested logical expression"""
        self.assertTrue(TestLexer.checkLexeme("((1+2=3)&&(2+1=3))&&true","(,(,1,+,2,=,3,),&&,(,2,+,1,=,3,),),&&,true,<EOF>",35))
    def test_assign_var_float(self):
        """test float number assign statement"""
        self.assertTrue(TestLexer.checkLexeme("var = 12e-7;","var,=,12e-7,;,<EOF>",36))
    def test_assign_var_int(self):
        """test int number assign statement"""
        self.assertTrue(TestLexer.checkLexeme("var = 9;","var,=,9,;,<EOF>",37))
    def test_assign_var_string(self):
        """test string assign statement"""
        self.assertTrue(TestLexer.checkLexeme('var = "String" ;','var,=,String,;,<EOF>',38))
    def test_assign_var_var(self):
        """test assign a variable to a variable statement"""
        self.assertTrue(TestLexer.checkLexeme("var = another_var;","var,=,another_var,;,<EOF>",39))
    def test_assign_var_unclosestring(self):
        """test assign an unclose string to a variable"""
        self.assertTrue(TestLexer.checkLexeme('var = "This is unclose string \n \b"','var,=,Unclosed String: This is unclose string ',40))
    def test_assign_var_illigal_escape_instring(self):
        """test assign a string with an ilegal escape inside"""
        self.assertTrue(TestLexer.checkLexeme('var = "This is \illigal escape"','var,=,Illegal Escape In String: This is \i',41))
    def test_var_declare_integer(self):
        """test integer decleration of variable """
        self.assertTrue(TestLexer.checkLexeme("int var;","int,var,;,<EOF>",42))
    def test_var_declare_string(self):
        """test string declaration of variable"""
        self.assertTrue(TestLexer.checkLexeme("string var;","string,var,;,<EOF>",43))
    def test_var_declare_float(self):
        """test float declaration of variable"""
        self.assertTrue(TestLexer.checkLexeme("float var;","float,var,;,<EOF>",44))
    def test_var_declare_bool(self):
        """test bool declaration of var"""
        self.assertTrue(TestLexer.checkLexeme("boolean var;","boolean,var,;,<EOF>",45))
    def test_array_declare(self):
        """test array declaration"""
        self.assertTrue(TestLexer.checkLexeme("int var[9];","int,var,[,9,],;,<EOF>",46))
    def test_vars_declare(self):
        """test many variables declaration in a line"""
        self.assertTrue(TestLexer.checkLexeme("int var1,var2,var3[9];","int,var1,,,var2,,,var3,[,9,],;,<EOF>",47))
    def test_string(self):
        """test special string with double quotes inside"""
        self.assertTrue(TestLexer.checkLexeme('"abc"abc "','abc,abc,Unclosed String: ',48))
    def test_string_special(self):
        """test special string with special character"""
        self.assertTrue(TestLexer.checkLexeme('"abc \b \f bc"','abc \b \f bc,<EOF>',49))
    def test_backslash_illegal_escape(self):
        """test special string"""
        self.assertTrue(TestLexer.checkLexeme('"abc \\ abc"','Illegal Escape In String: abc \ ',50))
    def test_quote_in_string(self):
        """test special string with legal escape inside"""
        self.assertTrue(TestLexer.checkLexeme('"abc \\" abc"','abc \\" abc,<EOF>',51))
    def test_illegal_escape_in_string(self):
        """test special string"""
        self.assertTrue(TestLexer.checkLexeme('"abc \i"','Illegal Escape In String: abc \i',52))
    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme('"abc \\i"','Illegal Escape In String: abc \i',53))
    def test_one_token_error(self):
        """test token error"""
        self.assertTrue(TestLexer.checkLexeme(".","Error Token .",54))
    def test_void_function_declare_no_parameter(self):
        """test void declaration"""
        self.assertTrue(TestLexer.checkLexeme('void Function(){ string a = "This is a string"; return;}','void,Function,(,),{,string,a,=,This is a string,;,return,;,},<EOF>',55))
    def test_void_function_declare_parameters(self):
        """test void declaration with parameter"""
        self.assertTrue(TestLexer.checkLexeme('void Function(string s){s = "This is a string"; return;}','void,Function,(,string,s,),{,s,=,This is a string,;,return,;,},<EOF>',56))
    def test_void_function_call(self):
        """test void function call"""
        self.assertTrue(TestLexer.checkLexeme("Function(string s);","Function,(,string,s,),;,<EOF>",57))
    def test_float_function_declare(self):
        """test float function declaration"""
        self.assertTrue(TestLexer.checkLexeme("float Function(){return 1.1;}","float,Function,(,),{,return,1.1,;,},<EOF>",58))
    def test_float_function_declare_parameter(self):
        """test float function declaration with parameters"""
        self.assertTrue(TestLexer.checkLexeme("float Function(float a){a = 1.1;returna;}","float,Function,(,float,a,),{,a,=,1.1,;,returna,;,},<EOF>",59))
    def test_float_function_call(self):
        """test float function call"""
        self.assertTrue(TestLexer.checkLexeme("Function(1.2);","Function,(,1.2,),;,<EOF>",60))
    def test_int_function_declare(self):
        """test integer function declaration"""
        self.assertTrue(TestLexer.checkLexeme("int Function(){return 0;}","int,Function,(,),{,return,0,;,},<EOF>",61))
    def test_int_function_declare_paremeter(self):
        """test integer function declaration with parameter"""
        self.assertTrue(TestLexer.checkLexeme("int Function(int b){return b;}","int,Function,(,int,b,),{,return,b,;,},<EOF>",62))
    def test_int_function_call(self):
        """test int function call"""
        self.assertTrue(TestLexer.checkLexeme("Function(0);","Function,(,0,),;,<EOF>",63))
    def test_string_function_declare(self):
        """test string function declaration"""
        self.assertTrue(TestLexer.checkLexeme('string Function(){return "String";}','string,Function,(,),{,return,String,;,},<EOF>',64))
    def test_string_function_declare_parameter(self):
        """test string function with parameter declaration"""
        self.assertTrue(TestLexer.checkLexeme('string Function(string "String"){return "String";}','string,Function,(,string,String,),{,return,String,;,},<EOF>',65))
    def test_string_function_call(self):
        """test string function call"""
        self.assertTrue(TestLexer.checkLexeme('Function("string");','Function,(,string,),;,<EOF>',66))
    def test_bool_function_declare(self):
        """test boolean function declaration"""
        self.assertTrue(TestLexer.checkLexeme("bool Function(){return false;}","bool,Function,(,),{,return,false,;,},<EOF>",67))
    def test_bool_function_declare_parameters(self):
        """test boolean function with parameter declaration"""
        self.assertTrue(TestLexer.checkLexeme("boolean Function(boolean a){return a;}","boolean,Function,(,boolean,a,),{,return,a,;,},<EOF>",68))
    def test_bool_function_call(self):
        """test boolean function call and bool variable declare"""
        self.assertTrue(TestLexer.checkLexeme("a = true; Function(a);","a,=,true,;,Function,(,a,),;,<EOF>",69))
    def test_int_array_pointer_type_func(self):
        """test int poiter type function """
        self.assertTrue(TestLexer.checkLexeme("int[] Function(){}","int,[,],Function,(,),{,},<EOF>",70))
    def test_float_array_pointer_type_func(self):
        """test float pointer type function"""
        self.assertTrue(TestLexer.checkLexeme("float[] Function(){}","float,[,],Function,(,),{,},<EOF>",71))
    def test_string_array_pointer_type_func(self):
        """test string poiter type function"""
        self.assertTrue(TestLexer.checkLexeme("string[] Function(){}","string,[,],Function,(,),{,},<EOF>",72))
    def test_bool_array_pointer_type_func(self):
        """test bool pointer type function"""
        self.assertTrue(TestLexer.checkLexeme("bool[] Function(){}","bool,[,],Function,(,),{,},<EOF>",73))
    def test_many_assign(self):
        """test assign expression"""
        self.assertTrue(TestLexer.checkLexeme("a=b=c=d=e=f=g","a,=,b,=,c,=,d,=,e,=,f,=,g,<EOF>",74))
    def test_many_assign_value(self):
        """test assign expression with a value"""
        self.assertTrue(TestLexer.checkLexeme("a=b=c=d=e=f=g=1.669","a,=,b,=,c,=,d,=,e,=,f,=,g,=,1.669,<EOF>",75))
    def test_if_statement(self):
        """test if statement"""
        self.assertTrue(TestLexer.checkLexeme("if(a==b) b=c;","if,(,a,==,b,),b,=,c,;,<EOF>",76))
    def test_if_else_statement(self):
        """test if else statement"""
        self.assertTrue(TestLexer.checkLexeme("if(a==b) b=c; else c=b;","if,(,a,==,b,),b,=,c,;,else,c,=,b,;,<EOF>",77))
    def test_do_while_statement(self):
        """test do while statement"""
        self.assertTrue(TestLexer.checkLexeme("do{} while(a=0)","do,{,},while,(,a,=,0,),<EOF>",78))
    def test_for_statement(self):
        """test for statement"""
        self.assertTrue(TestLexer.checkLexeme("for(i=0;i<10;i=i+1){}","for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,},<EOF>",79))
    def test_for_nested_statement_if(self):
        """test for statement nested inside if statement"""
        self.assertTrue(TestLexer.checkLexeme("if(a==b) for(i=0;i<9;i=i+1)a=b+1;","if,(,a,==,b,),for,(,i,=,0,;,i,<,9,;,i,=,i,+,1,),a,=,b,+,1,;,<EOF>",80))
    def test_for_nested_if_else(self):
        """test for statement nested inside if else statement"""
        self.assertTrue(TestLexer.checkLexeme("if(a==b) for(i=0;i<9;i=i+1)a=b+1; else break;","if,(,a,==,b,),for,(,i,=,0,;,i,<,9,;,i,=,i,+,1,),a,=,b,+,1,;,else,break,;,<EOF>",81))
    def test_do_while_nested_if(self):
        """test do while statement nested inside if statement"""
        self.assertTrue(TestLexer.checkLexeme("if(a==b) do{} while (a!=b);","if,(,a,==,b,),do,{,},while,(,a,!=,b,),;,<EOF>",82))
    def test_do_while_nested_if_else(self):
        """test do while statement nested in if else statement"""
        self.assertTrue(TestLexer.checkLexeme("if(a==b) do{} while (a!=b); else do{} while(a==b)","if,(,a,==,b,),do,{,},while,(,a,!=,b,),;,else,do,{,},while,(,a,==,b,),<EOF>",83))
    def test_if_nested_do_while(self):
        """test if statement nested in do while statement"""
        self.assertTrue(TestLexer.checkLexeme("do{if(a==b) break;} while(a==0)","do,{,if,(,a,==,b,),break,;,},while,(,a,==,0,),<EOF>",84))
    def test_if_else_nested_do_while(self):
        """test if else statement nested in do while statement"""
        self.assertTrue(TestLexer.checkLexeme("do{if(a==b) break; else continue;} while(a==0)","do,{,if,(,a,==,b,),break,;,else,continue,;,},while,(,a,==,0,),<EOF>",85))
    def test_for_nested_do_while(self):
        """test for statement nested in do while statement"""
        self.assertTrue(TestLexer.checkLexeme("do{for(i=0;i<10;i=i+1)i=a+1;}while(a==0)","do,{,for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),i,=,a,+,1,;,},while,(,a,==,0,),<EOF>",86))
    def test_do_while_nested_for(self):
        """test do while statement nested in for statement"""
        self.assertTrue(TestLexer.checkLexeme("for(i =0;i<9;i=i+1){do {i=i-1} while(true)}","for,(,i,=,0,;,i,<,9,;,i,=,i,+,1,),{,do,{,i,=,i,-,1,},while,(,true,),},<EOF>",87))
    def test_if_nested_for(self):
        """test if statement nested in for statement"""
        self.assertTrue(TestLexer.checkLexeme("for(i =0;i<9;i=i+1){if(i!=0) break;","for,(,i,=,0,;,i,<,9,;,i,=,i,+,1,),{,if,(,i,!=,0,),break,;,<EOF>",88))
    def test_index_expression(self):
        """test index expression"""
        self.assertTrue(TestLexer.checkLexeme("foo(2)[3+x] = a[b[2]] +3;","foo,(,2,),[,3,+,x,],=,a,[,b,[,2,],],+,3,;,<EOF>",89))
    def test_initialization(self):
        """test variable initialiation"""
        self.assertTrue(TestLexer.checkLexeme("boolean boo[2]={true,false};","boolean,boo,[,2,],=,{,true,,,false,},;,<EOF>",90))
    def test_id_content_error_char(self):
        """test error token in an identify"""
        self.assertTrue(TestLexer.checkLexeme("this is an id$ntify","this,is,an,id,Error Token $",91))
    def test_error_token_inside_linecomment(self):
        """test token error in a newline comment"""
        self.assertTrue(TestLexer.checkLexeme("// !@#$%^&*?","<EOF>",92))
    def test_error_token_inside_blockcomment(self):
        """test token error in the block comment"""
        self.assertTrue(TestLexer.checkLexeme("/*!@#$%^&*?*/","<EOF>",93))
    def test_line_comment_block(self):
        """test block comment in the newline comment"""
        self.assertTrue(TestLexer.checkLexeme("// /* block comment */","<EOF>",94))
    def test_linecomment_in_blockcomment(self):
        """test newline comment in the block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* // */","<EOF>",95))
    def test_closeblock_in_blockcomment(self):
        """test nested block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* */ */","*,/,<EOF>",96))
    def test_openblock_in_blockcomment(self):
        """test nested block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* /* */","<EOF>",97))
    def test_blockcomment_in_blockcomment(self):
        """test nested block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* /* */ */","*,/,<EOF>",98))
    def test_many_white_space(self):
        """test blank space"""
        self.assertTrue(TestLexer.checkLexeme("        ","<EOF>",99))
    def test_tokens_error(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme("??","Error Token ?",100))
    