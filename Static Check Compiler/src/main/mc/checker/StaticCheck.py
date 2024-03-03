
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
# class MType:
#     def __init__(self,partype,rettype):
#         self.partype = partype
#         self.rettype = rettype
@dataclass
class MType:
    partype: List[Type]
    rettype: Type


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType())),
        Symbol("putStringLn", MType([StringType()], VoidType())),
        Symbol("putLn", MType([], VoidType()))
    ]

    def __init__(self, ast):
        # print(ast)
        # print(ast)
        # print()
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        flag = True
        built_in_list = ["getInt","putInt","putIntLn","getFloat","putFloat","putFloatLn","putBool","putBoolLn","putString","putStringLn","putLn"]
        glb_list = []
        for x in ast.decl:
            if type(x) is VarDecl:
                if x.variable in built_in_list:
                    raise Redeclared(Variable(),x.variable)
                glb_list.append(Symbol(x.variable, x.varType))
                if self.lookup(x.variable, glb_list[:-1], lambda x: x.name):
                    raise Redeclared(Variable(), x.variable)
            if type(x) is FuncDecl:
                if x.name.name in built_in_list:
                    raise Redeclared(Function(),x.name.name)
                if x.name.name == "main":
                    flag = False
                    glb_list.append(Symbol(x.name.name, MType([y.varType for y in x.param], x.returnType)))
                    if self.lookup(x.name.name, glb_list[:-1], lambda x: x.name):
                        raise Redeclared(Function(), x.name.name)
                else:
                    glb_list.append(Symbol(x.name.name, MType([y.varType for y in x.param], x.returnType)))
                    if self.lookup(x.name.name, glb_list[:-1], lambda x: x.name):
                        raise Redeclared(Function(), x.name.name)
        if flag == True:
            raise NoEntryPoint()
        glb_list.extend(c);
        
        for x in ast.decl:
            if type(x) is FuncDecl: 
                if x.name.name in built_in_list:
                    raise Redeclared(Function(),x.name.name)
                self.visit(x, [glb_list])

       
        a = list(filter(lambda x:type(x.mtype) is MType,glb_list))
        unreachset = set([x for x in a if a.count(x) == 1])

        for x in unreachset:
            if x.name != "main" and x.name not in built_in_list:
                raise UnreachableFunction(x.name)
        return "8====D"

    def visitFuncDecl(self, ast, c):
        try:
            param = reduce(lambda env, decl: [
                           env[0]+self.visit(decl, env)], ast.param, [[]])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)

        nam = [Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType))]
        c[-1].insert(0, nam)
        reduce(lambda env, x: [env[0] + self.visit(x, env)]+(param+c)[1:], ast.body.member, param + c)
        if not "return" in c[-1]:
            if str(c[-1][0][0].mtype.rettype) is not "VoidType":
                raise FunctionNotReturn(ast.name.name)
        else:
            n = c[-1].count("return")
            for x in range(n):
                c[-1].remove("return")
            m = c[-1].count("breakcon")
            for x in range(m):
                c[-1].remove("breakcon")
        c[-1].remove(nam)
        return []

    def visitVarDecl(self, ast, c):
        flatten = [x for x in c[0] if type(x) is Symbol]
        if self.lookup(ast.variable, flatten, lambda x: x.name):
            raise Redeclared(Variable(), ast.variable)

        return [Symbol(ast.variable, ast.varType)]

    def visitBlock(self, ast, c):
        reduce(lambda env, x: [
               env[0] + self.visit(x, env)] + c, ast.member, [[]]+c)
        return []

    def visitId(self, ast, c):
        flatten = [
            val for sublist in c for val in sublist if type(val) is Symbol]
        for x in flatten:
            if type(x) is not Symbol:
                flatten.remove(x)
        temp = self.lookup(ast.name, flatten, lambda x: x.name)
        if temp is None:
            raise Undeclared(Identifier(), ast.name)
        elif type(temp.mtype) is ArrayType:
            return[temp.mtype]
        else:
            return[temp.mtype]

    def visitUnaryOp(self, ast, c):
        if ast.op == "!":
            if str(self.visit(ast.body, c)[0]) == "BoolType":
                return [BoolType()]
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "-":
            if str(self.visit(ast.body, c)[0]) == "IntType":
                return [IntType()]
            elif str(self.visit(ast.body, c)[0]) == "FloatType":
                return [FloatType()]
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitBinaryOp(self, ast, c):
        if ast.op == "%":
            if str(self.visit(ast.left, c)[0]) == "IntType"and str(self.visit(ast.right, c)[0]) == "IntType":
                return [IntType()]
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "&&" or ast.op == "||":
            if str(self.visit(ast.left, c)[0]) == "BoolType"and str(self.visit(ast.right, c)[0]) == "BoolType":
                return [BoolType()]
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "==" or ast.op == "!=": 
            if str(self.visit(ast.left, c)[0]) == "BoolType" and str(self.visit(ast.right, c)[0]) == "BoolType":
                return [BoolType()]
            elif str(self.visit(ast.left, c)[0]) == "IntType" and str(self.visit(ast.right, c)[0]) == "IntType":
                return [BoolType()]
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "<" or ast.op == "<=" or ast.op == ">" or ast.op == ">=":
            if str(self.visit(ast.left, c)[0]) == "IntType":
                if str(self.visit(ast.right, c)[0]) == "IntType" or str(self.visit(ast.right, c)[0]) == "FloatType":
                    return [BoolType()]
                else:
                    raise TypeMismatchInExpression(ast)
            elif str(self.visit(ast.left, c)[0]) == "FloatType":
                if str(self.visit(ast.right, c)[0]) == "IntType" or str(self.visit(ast.right, c)[0]) == "FloatType":
                    return [BoolType()]
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "+" or ast.op == "-"  or ast.op == "*" or ast.op == "/":
            if str(self.visit(ast.left, c)[0]) == "IntType":
                if str(self.visit(ast.right, c)[0]) == "IntType":
                    return [IntType()]
                elif str(self.visit(ast.right, c)[0]) == "FloatType":
                    return [FloatType()]
                else:
                    raise TypeMismatchInExpression(ast)
            elif str(self.visit(ast.left, c)[0]) == "FloatType":
                if str(self.visit(ast.right, c)[0]) == "IntType" or str(self.visit(ast.right, c)[0]) == "FloatType":
                    return [FloatType()]
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "=":
            if not (type(ast.left) is Id or type(ast.left) is ArrayCell or type(ast.left) is ArrayPointerType):
                raise NotLeftValue(ast.left)
            self.visit(ast.right,c)
            if str(self.visit(ast.right, c)[0]) == "FloatType" and str(self.visit(ast.left, c)[0]) == "FloatType":
                return [FloatType()]
            elif str(self.visit(ast.right, c)[0]) == "IntType":
                if str(self.visit(ast.left, c)[0]) == "IntType":
                    return [IntType()]
                elif str(self.visit(ast.left, c)[0]) == "FloatType":
                    return [FloatType()]
                else:
                    raise TypeMismatchInExpression(ast)
            elif str(self.visit(ast.right, c)[0]) == "StringType" and str(self.visit(ast.left, c)[0]) == "StringType":
                return [StringType()]
            elif str(self.visit(ast.right, c)[0]) == "BoolType" and str(self.visit(ast.left, c)[0]) == "BoolType":
                return [BoolType()]
            else:
                raise TypeMismatchInExpression(ast)
            
        else:
            raise TypeMismatchInExpression(ast)

    def visitIf(self, ast, c):
        if type(self.visit(ast.expr, c)[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        a = ["a"]
        b = ["a"]
        self.visit(ast.thenStmt, [a]+c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, [b]+c)
        counter = 0
        counter1 = 0
        if (a == ['c']) and (b == ['c']):
            for x in c:
                for y in x:
                    if y is 'a':
                        counter = 1
                        num = x.index('a')
                        x.remove('a')
                        x.insert(num, 'c')
                        break
                if counter == 1:
                    break
            for x in c:
                for y in x:
                    if y is 'z':
                        counter1 = 1
                        num = x.index('z')
                        x.remove('z')
                        x.insert(num, 'y')
                        break
                if counter1 == 1:
                    break
        if (a != ["a"]) and (b != ["a"]) and (["c"] not in c) and (["a"] not in c) and (["z"] not in c):
            c[-1].append("return")
        return[]

    def visitFor(self, ast, c):
        c[-1].insert(-1, "breakcon")
        c[-1].insert(-1, "for")
        if str(self.visit(ast.expr1, c)[0]) != "IntType":
            raise TypeMismatchInStatement(ast)
        if str(self.visit(ast.expr2, c)[0]) != "BoolType":
            raise TypeMismatchInStatement(ast)
        if str(self.visit(ast.expr3, c)[0]) != "IntType":
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, c)
        c[-1].remove("breakcon")
        c[-1].remove("for")
        return []

    def visitDowhile(self, ast, c):
   
        c[-1].insert(-1, "breakcon")
        if str(self.visit(ast.exp, c)[0]) != "BoolType":
            raise TypeMismatchInStatement(ast)
        z = ['z']
        for x in ast.sl:
            # self.visit(x, [[z]] + c)
            self.visit(x, [z] + c)
        counter = 0
        counter1 = 0
        if z != "z":
            for x in c:
                for y in x:
                    if y is "z":
                        counter = 1
                        num = x.index("z")
                        x.remove("z")
                        x.insert(num, "y")
                        break
                if counter == 1:
                    break
            for x in c:
                for y in x:
                    if y is "a":
                        counter1 = 1
                        num = x.index("a")
                        x.remove("a")
                        x.insert(num, "c")
                        break
                if counter1 == 1:
                    break
            # flatten = [val for sublist in c for val in sublist]
           
            # if (z!=['z']) and (z not in flatten):
            # if (z!=['z']) and (['z'] not in flatten):
            if (z!=['z']) and (["c"] not in c) and (["a"] not in c) and (["z"] not in c):
                c[-1].append("return")
        if "breakcon" in c[-1]:
            c[-1].remove("breakcon")
        return []

    def visitReturn(self, ast, c):
        if not "for" in c[-1]:
            count = 0
            counter = 0
            for x in c:
                for y in x:
                    if y is "a":
                        counter = 1
                        num = x.index("a")
                        x.remove("a")
                        x.insert(num, "c")
                        count = count + 1
                        break
                    elif y is "z":
                        counter = 1
                        num = x.index("z")
                        x.remove("z")
                        x.insert(num,"y")
                        count = count + 1
                if counter == 1:
                    break
            if count == 0:
                c[-1].append("return")
        if ast.expr == None and str(c[-1][0][0].mtype.rettype) is not "VoidType":
            raise TypeMismatchInStatement(ast)
        elif ast.expr != None:
            if self.visit(ast.expr,c)[0]:
                if type(c[-1][0][0].mtype.rettype) is VoidType:
                    raise TypeMismatchInStatement(ast)
            if type(c[-1][0][0].mtype.rettype) is ArrayPointerType:
                if type(self.visit(ast.expr,c)[0]) is not ArrayType and type(self.visit(ast.expr,c)[0]) is not ArrayPointerType:
                    raise TypeMismatchInStatement(ast)
                elif type(self.visit(ast.expr,c)[0].eleType) != type(c[-1][0][0].mtype.rettype.eleType):
                    raise TypeMismatchInStatement(ast)
            # elif type(self.visit(ast.expr,c)[0]) is ArrayCell:
                # return []
            elif type(self.visit(ast.expr,c)[0]) != type(c[-1][0][0].mtype.rettype):
                # if type(c[-1][0][0].mtype.rettype) is FloatType and type(self.visit(ast.expr,c)[0]) is IntType:
                #     return []
                # else:
                raise TypeMismatchInStatement(ast)
        return []

    def visitArrayType(self,ast,c):
        return [ast.eleType,ast.dimen]
    def visitArrayPointerType(self,ast,c):
        return [ast.eleType]
    def visitArrayCell(self, ast, c):
        if type(self.visit(ast.idx, c)[0]) is not IntType:
            raise TypeMismatchInExpression(ast)
        if not (type(self.visit(ast.arr,c)[0]) is ArrayType or type(self.visit(ast.arr,c)[0]) is ArrayPointerType):
            raise TypeMismatchInExpression(ast)
        if "IntType" in str(self.visit(ast.arr, c)):
            return [IntType(), "ArrayType"]
        elif "FloatType" in str(self.visit(ast.arr, c)):
            return [FloatType(), "ArrayType"]
        elif "StringType" in str(self.visit(ast.arr, c)):
            return [StringType(), "ArrayType"]
        elif "BoolType" in str(self.visit(ast.arr, c)):
            return [BoolType(), "ArrayType"]

    def visitArrayPointerType(self, param, c):
        return [ast.eleType]

    def visitCallExpr(self, ast, c):
        flatten = [val for sublist in c for val in sublist if type(val) is Symbol]
        a = self.lookup(ast.method.name, flatten, lambda x: x.name)
        if a is None:
            raise Undeclared(Function(), ast.method.name)
        if type(a.mtype) is not MType:
            raise TypeMismatchInExpression(ast)
        count = 0
        if len(a.mtype.partype) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        for x in ast.param:
            if (type(self.visit(x, c)[0]) != type(a.mtype.partype[count])) and type(a.mtype.partype[count]) is ArrayPointerType:
                if type(a.mtype.partype[count]) is ArrayPointerType:
                    if type(self.visit(x, c)[0]) is ArrayType:
                        if type(self.visit(x, c)[0].eleType) is not type(a.mtype.partype[count].eleType):
                            raise TypeMismatchInExpression(ast)
                        else:
                            count = count + 1
                            continue
                    else:
                        raise TypeMismatchInExpression(ast)
            elif type(self.visit(x, c)[0]) is ArrayPointerType and type(a.mtype.partype[count]) is ArrayPointerType:
                if type(a.mtype.partype[count].eleType) is not type(self.visit(x, c)[0].eleType):
                    raise TypeMismatchInExpression(ast)
                else:
                    count = count + 1
                    continue
            elif (type(self.visit(x, c)[0]) != type(a.mtype.partype[count])) and type(a.mtype.partype[count]) is not ArrayPointerType:
                if type(a.mtype.partype[count]) is FloatType and type(self.visit(x, c)[0]) is IntType:
                    count = count + 1
                    continue
                else:
                    raise TypeMismatchInExpression(ast)
            count = count + 1
        if c[-1][0][0].name != a.name:
            c[-1].append(a)
        return [a.mtype.rettype]

    def visitBreak(self, ast, c):
        if "breakcon" not in c[-1]:
            raise BreakNotInLoop()
        return []

    def visitContinue(self, ast, c):
        if "breakcon" not in c[-1]:
            raise ContinueNotInLoop()
        return []

    def visitIntLiteral(self, ast, c):
        return [IntType()]

    def visitFloatLiteral(self, ast, c):
        return [FloatType()]

    def visitBooleanLiteral(self, ast, c):
        return [BoolType()]

    def visitStringLiteral(self, ast, c):
        return [StringType()]

    def visitVoidLiteral(self, ast, c):
        return [VoidType()]

    def visitStringLiteral(self, ast, c):
        return [StringType()]

