import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):   
    def test_main_function(self):
        """Test variable decleration in main function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int main() {
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,101))
    
    def test_int_return_function(self):
        """Test variable decleration in integer return function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int function() {
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,102))
    
    def test_float_return_function(self):
        """Test variable decleration in float return function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        float function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,103))
    def test_string_return_function(self):
        """Test variable decleration in string return type function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        string function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,104))

    def test_bool_return_function(self):
        """Test variable decleration in boolean return type function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        boolean function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,105))

    def test_int_array_pointer_type_function_return(self):
        """Test variable decleration in integer array poiter type return function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,106))

    def test_float_array_pointer_type_function_return(self):
        """Test variable decleration in float array poiter type return function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        float[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,107))

    def test_string_array_pointer_type_function_return(self):
        """Test variable decleration in string array pointer type return function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        string[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,108))
    
    def test_boolean_array_pointer_type_function_return(self):
        """Test variable decleration in boolean array pointer type return function and global declaration"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        boolean[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,109))

    def test_void_function(self):
        """Test variable decleration in void function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        void function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,110))
    
    def test_main_function_funcall(self):
        """Test function call in main function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int main() {
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,111))

    def test_int_return_function_funcall(self):
        """Test function call in integer return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int function() {
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,112))
    
    def test_float_return_function_funcall(self):
        """Test function call in float return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        float function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,113))
    def test_string_return_function_funcall(self):
        """Test function call in string return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        string function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,114))

    def test_bool_return_function_funcall(self):
        """Test function call in boolean return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        boolean function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,115))

    def test_int_array_pointer_type_function_return_funcall(self):
        """Test function call in integer array pointer type return function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,116))

    def test_float_array_pointer_type_function_return_funcall(self):
        """Test function call in float array pointer type return function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        float[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,117))

    def test_string_array_pointer_type_function_return_funcall(self):
        """Test function call in string array pointer type return function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        string[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,118))
    
    def test_boolean_array_pointer_type_function_return_funcall(self):
        """Test function call in boolean array pointer type return function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        boolean[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,119))

    def test_void_function_funcall(self):
        """Test function call in void function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        void function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,120))

    def test_main_function_funcall_buildin_function(self):
        """Test build in function call in main function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int main() {
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,121))

    def test_int_return_function_buildin_function(self):
        """Test build in function call in integer return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int function() {
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,122))
    
    def test_float_return_function_buildin_function(self):
        """Test build in function call in float return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        float function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,123))
    def test_string_return_function_buildin_function(self):
        """Test build in function call in integer return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        string function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return "String";
        }"""
        
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,124))

    def test_bool_return_function_buildin_function(self):
        """Test build in function call in boolean return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        boolean function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,125))

    def test_int_array_pointer_type_function_buildin_function(self):
        """Test build in function call in integer array poiter type return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,126))

    def test_float_array_pointer_type_function_buildin_function(self):
        """Test build in function call in float array poiter type return type function"""
        input = """
        float[] function(){
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,127))

    def test_string_array_pointer_type_function_buildin_function(self):
        """Test build in function call in string array poiter type return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        string[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,128))
    
    def test_boolean_array_pointer_type_function_buildin_function(self):
        """Test build in function call in boolean array poiter type return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        boolean[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,129))

    def test_void_function_buildin_function(self):
        """Test build in function call in void function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        void function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            int_return_function(0);
            float_return_function(0.0);
            string_return_function("String");
            boolean_return_function(true);
            getInt();
            putInt(1);
            putIntLn(1);
            getFloat();
            putFloat(1.1);
            putFloatLn(1.1);
            putBool(a);
            putBoolLn(a);
            putString("String");
            putStringLn("String");
            putLn();
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,130))

    def test_main_function_statements(self):
        """Test complex statement in main function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int main() {
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,131))

    def test_int_return_function_statements(self):
        """Test complex statement in integer return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int function() {
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,132))
    
    def test_float_return_function_statements(self):
        """Test complex statement in float return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        float function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,133))
    def test_string_return_function_statements(self):
        """Test complex statement in string return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        string function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
           
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,134))

    def test_bool_return_function_statements(self):
        """Test complex statement in boolean return type function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        boolean function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,135))

    def test_int_array_pointer_type_function_return_statements(self):
        """Test complex statement in integer array poiter type return function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        int[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,136))

    def test_float_array_pointer_type_function_return_statements(self):
        """Test complex statement in float array poiter type return function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        float[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,137))

    def test_string_array_pointer_type_function_return_statements(self):
        """Test complex statement in string array poiter type return function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        string[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,138))
    
    def test_boolean_array_pointer_type_function_return_statements(self):
        """Test complex statement in boolean array poiter type return function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        boolean[] function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,139))

    def test_void_function_statements(self):
        """Test complex statement in void function"""
        input = """
        int a,b,c[1],d[2];
        float a,b,c[3],d[4];
        string a,b,c[5],d[6];
        boolean a,b,c[7],d[8];
        void function(){
            int a,b,c[1],d[2];
            float a,b,c[3],d[4];
            string a,b,c[5],d[6];
            boolean a,b,c[7],d[8];
            a = b+c;
            a = b-c;
            a = b/c;
            a = b*c;
            boolean e;
            e = true && ((a+1==8)||((b-1!=0)>0));
            var = a[b[2]] +3;
            e = !!!!!true;
            b = ------435;
            a= a+-b;
            foo(2)[3+x] = a[b[2]] +3;
            e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
            x[8] = var%(var&&var)/1996*funcall(funcall());
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,140))
     
    def test_main_function_if_else(self):
        """ test if else statement in main function """
        input = """
        int main() {
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,141))

    def test_int_return_function_if_else(self):
        """ Test if else statement in integer return type function """
        input = """
        int function() {
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,142))
    
    def test_float_return_function_if_else(self):
        """ Test if else statement in float return type function """
        input = """
        float function(){
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,143))
    def test_string_return_function_if_else(self):
        """ Test if else statement in string return type function """
        input = """
        string function(){
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,144))

    def test_bool_return_function_if_else(self):
        """ Test if else statement in boolean return type function """
        input = """
        boolean function(){
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,145))

    def test_int_array_pointer_type_function_return_if_else(self):
        """ Test if else statement in integer array pointer type function """
        input = """
        int[] function(){
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
               
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,146))

    def test_float_array_pointer_type_function_return_if_else(self):
        """ Test if else statement in float array pointer type return function """
        input = """
        float[] function(){
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
               
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,147))

    def test_string_array_pointer_type_function_return_if_else(self):
        """ Test if else statement in string array pointer type return function """
        input = """
        string[] function(){
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,148))
    
    def test_boolean_array_pointer_type_function_return_if_else(self):
        """ Test if else statement in boolean array pointer type return function """
        input = """
        boolean[] function(){
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
               
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,149))

    def test_void_function_if_else(self):
        """ Test if else statement in void function """
        input = """
        void function(){
            if(a==b) {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            else{
               int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,150))
    def test_main_function_do_while(self):
        """ Test do while loop in main function """
        input = """
        int main() {
            do {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,151))

    def test_int_return_function_do_while(self):
        """ Test do while loop in integer type return function """
        input = """
        int function() {
            do{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,152))
    
    def test_float_return_function_do_while(self):
        """ Test do while loop in float type return function """
        input = """
        float function(){
            do{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,153))
    def test_string_return_function_do_while(self):
        """ Test do while loop in string type return function """
        input = """
        string function(){
            do{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,154))

    def test_bool_return_function_do_while(self):
        """ Test do while loop in boolean type return function """
        input = """
        boolean function(){
            do{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,155))

    def test_int_array_pointer_type_function_return_do_while(self):
        """ Test do while loop in integer array pointer type return function """
        input = """
        int[] function(){
            do
            {
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,156))

    def test_float_array_pointer_type_function_return_do_while(self):
        """ Test do while loop in float array pointer type return function """
        input = """
        float[] function(){
            do{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,157))

    def test_string_array_pointer_type_function_return_do_while(self):
        """ Test do while loop in string array pointer type return function """
        input = """
        string[] function(){
            do{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,158))
    
    def test_boolean_array_pointer_type_function_return_do_while(self):
        """ Test do while loop in boolean array poiter type return function """
        input = """
        boolean[] function(){
            do{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,159))

    def test_void_function_do_while(self):
        """ Test do while loop in void function """
        input = """
        void function(){
            do{
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            while(a==0);
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,160))   
    def test_main_function_for(self):
        input = """
        int main() {
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,161))

    def test_int_return_function_for(self):
        """ Test for loop in main function """
        input = """
        int function() {
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,162))
    
    def test_float_return_function_for(self):
        """ Test for loop in float type return function """
        input = """
        float function(){
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,163))
    def test_string_return_function_for(self):
        """ Test for loop in string type return function """
        input = """
        string function(){
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,164))

    def test_bool_return_function_for(self):
        """ Test for loop in boolean type return function """
        input = """
        boolean function(){
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,165))

    def test_int_array_pointer_type_function_return_for(self):
        """ Test for loop in integer array pointer type return function """
        input = """
        int[] function(){
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
               
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,166))

    def test_float_array_pointer_type_function_return_for(self):
        """ Test for loop in float array pointer type return function """
        input = """
        float[] function(){
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,167))

    def test_string_array_pointer_type_function_return_for(self):
        """ Test for loop in string array pointer type return function """
        input = """
        string[] function(){
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
            }
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,168))
    
    def test_boolean_array_pointer_type_function_return_for(self):
        """ Test for loop in boolean array pointer type return function """
        input = """
        boolean[] function(){
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
                sum(3,lab(lab1(lab2(sum(2,x[1])))));
            }
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,169))

    def test_void_function_for(self):
        """ Test for loop in void function """
        input = """
        void function(){
            for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
               
                x[8] = var%(var&&var)/1996*funcall(funcall());
                sum(3,lab(lab1(lab2(sum(2,x[1])))));
            }
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,170))  
    def test_main_function_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in main function"""
        input = """
        int main() {
            if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,171))

    def test_int_return_function_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in integer type return function"""

        input = """
        int function() {
            if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,172))
    
    def test_float_return_function_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in float type return function"""
        input = """
        float function(){
            if(b){
                for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,173))
    def test_string_return_function_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in string type return function"""
        input = """
        string function(){
            if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,174))

    def test_bool_return_function_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in boolean type return function"""
        input = """
        boolean function(){
            if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,175))

    def test_int_array_pointer_type_function_return_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in integer array pointer type return function"""
        input = """
        int[] function(){
            if(b){
                for(i=0;i<10;i=i+1){
                int a,b,c[1],d[2];
                float a,b,c[3],d[4];
                string a,b,c[5],d[6];
                boolean a,b,c[7],d[8];
                boolean e;
                e = true && ((a+1==8)||((b-1!=0)>0));
                var = a[b[2]] +3;
                e = !!!!!true;
                b = ------435;
                a= a+-b;
                foo(2)[3+x] = a[b[2]] +3;
                
                x[8] = var%(var&&var)/1996*funcall(funcall());
                sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,176))

    def test_float_array_pointer_type_function_return_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in float array pointer type return function"""
        input = """
        float[] function(){
            if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,177))

    def test_string_array_pointer_type_function_return_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in string array pointer type return function"""
        input = """
        string[] function(){
            if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,178))
    
    def test_boolean_array_pointer_type_function_return_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in boolean array pointer type return function"""
        input = """
        boolean[] function(){
            if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,179))

    def test_void_function_nested_if_else(self):
        """Test nested for loop and do while loop inside if else in void function"""
        input = """
        void function(){
            if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,180))
    def test_main_function_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in main function"""
        input = """
        int main() {
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,181))

    def test_int_return_function_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in integer return function"""
        input = """
        int function() {
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,182))
    
    def test_float_return_function_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in float return function"""
        input = """
        float function(){
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,183))

    def test_string_return_function_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in string return function"""
        input = """
        string function(){
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,184))

    def test_bool_return_function_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in boolean return type function"""
        input = """
        boolean function(){
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,185))

    def test_int_array_pointer_type_function_return_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in integer array poiter type return function"""
        input = """
        int[] function(){
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,186))

    def test_float_array_pointer_type_function_return_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in float array poiter type return function"""
        input = """
        float[] function(){
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,187))

    def test_string_array_pointer_type_function_return_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in string array poiter type return function"""
        input = """
        string[] function(){
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,188))
    
    def test_boolean_array_pointer_type_function_return_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in boolean array poiter type return function"""
        input = """
        boolean[] function(){
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    e = ((foo(2)[3+x]==a[b[2]] +3) && (z + (so/100%10))) + 19976 <= 5;
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,189))

    def test_void_function_nested_do_while(self):
        """Test if else, do while loop and for loop inside do while loop in void function"""
        input = """
        void function(){
            do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,190))   
    def test_main_function_nested_for(self):
        """Test do while,if else and for loop in for in main function"""
        input = """
        int main() {
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,191))

    def test_int_return_function_nested_for(self):
        """Test do while,if else and for loop inside for loop integer return function"""
        input = """
        int function() {
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,192))
    
    def test_float_return_function_nested_for(self):
        """Test do while,if else and for loop inside for loop in float return function"""
        input = """
        float function(){
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return 0.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,193))
    def test_string_return_function_nested_for(self):
        """Test do while,if else and for loop inside for loop in string return function"""
        input = """
        string function(){
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,194))

    def test_bool_return_function_nested_for(self):
        """Test do while,if else and for loop inside for loop in boolean return function"""
        input = """
        boolean function(){
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,195))

    def test_int_array_pointer_type_function_return_nested_for(self):
        """Test do while,if else and for loop inside for loop in integer array pointer type return function"""
        input = """
        int[] function(){
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,196))

    def test_float_array_pointer_type_function_return_nested_for(self):
        """Test do while,if else and for loop inside for loop in float array pointer type return function"""
        input = """
        float[] function(){
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return 1.1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,197))

    def test_string_array_pointer_type_function_return_nested_for(self):
        """Test do while,if else and for loop inside for loop in string array pointer type return function"""
        input = """
        string[] function(){
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return "String";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,198))
    
    def test_boolean_array_pointer_type_function_return_nested_for(self):
        input = """
        boolean[] function(){
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                   
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,199))

    def test_void_function_nested_for(self):
        """Test do while,if else and for loop inside for loop in void function"""
        input = """
        void foo(int a, int b) 
        {           
            for(i=0;i<9;i=i+1){
                do
                {
                    if(b){
                    for(i=0;i<10;i=i+1){
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall(a,b,c,d,e,f));
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
            }
            else{
                do{
                    int a,b,c[1],d[2];
                    float a,b,c[3],d[4];
                    string a,b,c[5],d[6];
                    boolean a,b,c[7],d[8];
                    boolean e;
                    e = true && ((a+1==8)||((b-1!=0)>0));
                    var = a[b[2]] +3;
                    e = !!!!!true;
                    b = ------435;
                    a= a+-b;
                    foo(2)[3+x] = a[b[2]] +3;
                    
                    x[8] = var%(var&&var)/1996*funcall(funcall());
                    sum(3,lab(lab1(lab2(sum(2,x[1])))));
                }
                while(a==0);
            }
                }
            while(a==0);
            }
            return;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))   

    

