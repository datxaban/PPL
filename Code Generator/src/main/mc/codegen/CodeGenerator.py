'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String
        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        e = SubBody(None, self.env)

        globalArrVar = list()
        for x in ast.decl:
            if type(x) is not VarDecl:
                e.sym.insert(0,Symbol(x.name.name,MType([y.varType for y in x.param],x.returnType),CName(self.className)))
                continue
            globalArrVar.append(Symbol(x.variable,x.varType,CName(self.className))) if type(x.varType) is ArrayType else None
            self.emit.printout(self.emit.emitATTRIBUTE(x.variable,x.varType,False,None))
            e.sym.insert(0,Symbol(x.variable,x.varType,CName(self.className)))
        #Generate static constructor for class
        if len(globalArrVar) > 0:
        	self.genMETHOD(FuncDecl(Id("<clinit>"),list(), VoidType(),Block(list())),globalArrVar,Frame("<clinit>", VoidType()))
        for x in ast.decl:
            if type(x) is FuncDecl:
                e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), self.env, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        isNor = not isInit and not isMain
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)  
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        frame.enterScope(True)
        
        glenv = o
        # Generate code for parameter declarations
        if isInit: 
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        paralist = list()
        if isNor == True:
            counter = 0
            for x in consdecl.param:
                paralist.append(Symbol(x.variable,x.varType,Index(frame.getCurrIndex())))
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "arg"+str(counter), x.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
                counter = counter + 1
        body = consdecl.body
    
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        varList = paralist + glenv
        for x in body.member:
            if type(x) is VarDecl:
                var = self.visit(x,SubBody(frame,varList))
                varList.insert(0,var)
            else:
                self.emit.printout(self.visit(x,SubBody(frame,varList))[0] if type(x) is Block else self.visit(x,Access(frame,varList,True,True))[0] if (type(x) is BinaryOp and x.op == "=") else self.visit(x,Access(frame,varList,False,True))[0])
                if frame.getStackSize() > 0:
                    self.emit.printout(self.emit.emitPOP(frame))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        func = self.lookup(ast.name.name,o.sym,lambda x:x.name)
        o.sym.remove(func)
        o.sym.append(func)
        self.genMETHOD(ast, o.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + o.sym)

    def visitCallExpr(self, ast, o):
        call = self.lookup(ast.method.name, o.sym, lambda x: x.name)
        function = call.value.value
        funcalltype = call.mtype
        para = ["", list()]
        counter = 0
        for x in ast.param:
            thispara = self.visit(x, Access(o.frame, o.sym, False, True))
            if type(funcalltype.partype[counter]) is FloatType and type(thispara[1]) is IntType:
                thispara[0] = thispara[0] + self.emit.emitI2F(frame)
            para[0] = para[0] + thispara[0]
            para[1].append(thispara[1])
            counter = counter + 1
        return para[0] + self.emit.emitINVOKESTATIC(function + "/" + ast.method.name, funcalltype, o.frame) , funcalltype.rettype
        
    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()
    
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST('"'+str(ast.value)+'"',StringType(),o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()
        
    def visitBlock(self,ast,o):
        o.frame.enterScope(False)
        blockStmt = list()
        for x in ast.member:
            if type(x) is VarDecl:
                o.sym.insert(0,self.visit(x,o))
            else:
                bodyStmt = self.visit(x,SubBody(o.frame,o.sym)) if type(x) is Block else self.visit(x,Access(o.frame,o.sym,True,True)) if (type(x) is BinaryOp and x.op == "=") else self.visit(x,Access(o.frame,o.sym,False,True))
                blockStmt.append(bodyStmt[0])
                if o.frame.getStackSize() != 0:
                    blockStmt.append(self.emit.emitPOP(o.frame))
        o.frame.exitScope()
        return ''.join(blockStmt) , None

    def visitVarDecl(self, ast, o):
        newlabel = o.frame.getNewLabel()
        newindex = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(newindex,ast.variable,ast.varType,newlabel,o.frame.getEndLabel(), o.frame))
        self.emit.printout(self.emit.emitLABEL(newlabel,o.frame))
        if type(ast.varType) is ArrayType:
            self.emit.printout(self.emit.emitPUSHICONST(ast.varType.dimen,o.frame))
            self.emit.printout(self.emit.emitNEWARRAY(ast.varType.eleType))
            self.emit.printout(self.emit.emitWRITEVAR(ast.variable,ast.varType,newindex,o.frame))
        return Symbol(ast.variable,ast.varType,Index(newindex))

    def visitReturn(self, ast, o):
        if ast.expr is not None:
            returnStmt = self.visit(ast.expr,Access(o.frame,o.sym,False,True))
            o.frame.pop()
            if type(returnStmt[1]) is IntType:
                if type(o.sym[-1].mtype.rettype) is FloatType:
                    returnStmt[0] = returnStmt[0] + self.emit.emitI2F(o.frame)
            return returnStmt[0] + self.emit.emitGOTO(o.frame.endLabel[0],o.frame), None
        else:
            return self.emit.emitGOTO(o.frame.endLabel[0],o.frame) , None

    def visitId(self, ast, o):
        varName = self.lookup(ast.name, o.sym, lambda x: x.name)
        if type(o) is Access and o.isLeft is False:
            if o.isFirst == False:
                return self.emit.emitALOAD(varName.mtype.eleType,o.frame), varName.mtype
            elif o.isFirst == True:
                if type(varName.value) is CName:
                    return self.emit.emitGETSTATIC(varName.value.value + "." + varName.name,varName.mtype, o.frame), varName.mtype
                return self.emit.emitREADVAR(ast.name,varName.mtype,varName.value.value,o.frame), varName.mtype
        elif type(o) is Access and o.isLeft is True:
            if o.isFirst == False:
                return self.emit.emitASTORE(varName.mtype.eleType,o.frame), varName.mtype
            elif o.isFirst == True:
                if type(varName.value) is CName:
                    return self.emit.emitPUTSTATIC(varName.value.value + "." + varName.name,varName.mtype, o.frame), varName.mtype
                return self.emit.emitWRITEVAR(ast.name,varName.mtype,varName.value.value,o.frame), varName.mtype
        
                
    def visitUnaryOp(self, ast, o):
        jcode = self.visit(ast.body,Access(o.frame,o.sym,False,True))
        if ast.op == "-":
            return jcode[0] + self.emit.emitNEGOP(jcode[1],o.frame), jcode[1]
        elif ast.op == "!":
            return jcode[0] + self.emit.emitNOT(jcode[1],o.frame), jcode[1]
    def visitBinaryOp(self, ast, o):
        temp = str(None)
        if ast.op == "=":
            rightcode, righttype = self.visit(ast.right, Access(o.frame,o.sym,False,True))
            leftcode , lefttype = self.visit(ast.left, Access(o.frame,o.sym,True,True))
            if type(ast.left) is ArrayCell:
                temp , lefttype = self.visit(ast.left,Access(o.frame,o.sym,True,False))
        else:
            leftcode , lefttype = self.visit(ast.left,Access(o.frame,o.sym,False,True))
            rightcode , righttype = self.visit(ast.right,Access(o.frame,o.sym,False,True))
        
        if type(lefttype) == type(righttype) == IntType:
            binType = IntType()
        elif type(righttype) == FloatType and type(lefttype) == IntType :
            binType = FloatType()
            leftcode = leftcode + self.emit.emitI2F(o.frame)
        elif type(righttype) == IntType and type(lefttype) == FloatType:
            binType = FloatType()
            rightcode = rightcode + self.emit.emitI2F(o.frame)
        elif type(lefttype) == type(righttype) == FloatType:
            binType = FloatType()
        else:
        	binType = righttype
        if ast.op == "=":
            if o.isLeft:
                if type(ast.left) is ArrayCell:
                    return leftcode + rightcode + temp , binType
                return rightcode + leftcode , binType
            else:
                if type(ast.left) is ArrayCell:
                    return rightcode + self.emit.emitDUP(o.frame) + leftcode + temp , binType       			
                return rightcode + self.emit.emitDUP(o.frame) + leftcode , binType
        elif ast.op == "+" or ast.op == "-":
            return leftcode + rightcode + self.emit.emitADDOP(ast.op, binType, o.frame), binType
        elif ast.op == "*" or ast.op == "/":
            return leftcode + rightcode + self.emit.emitMULOP(ast.op, binType, o.frame), binType
        elif ast.op == "%":
            return leftcode + rightcode + self.emit.emitMOD(o.frame), binType
        elif ast.op == "<=" or ast.op == ">=" or ast.op == ">" or ast.op == "<"  or ast.op == "!="  or ast.op == "==":
            return leftcode + rightcode + self.emit.emitREOP(ast.op,binType,o.frame), BoolType()
        elif ast.op == "&&":
            return leftcode + rightcode + self.emit.emitANDOP(o.frame), BoolType()
        elif ast.op == "||":
            return leftcode + rightcode + self.emit.emitOROP(o.frame), BoolType()
    
    def visitBreak(self ,ast ,o):
    	return self.emit.emitGOTO(o.frame.getBreakLabel(),o.frame)
    def visitContinue(self, ast ,o):
    	return self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame)
    def visitFor(self, ast, o):
        o.frame.enterLoop()
        if type(ast.loop) is BinaryOp and ast.loop.op == "=":
            stmtcode= self.visit(ast.loop,Access(o.frame,o.sym,True,True))
        elif type(ast.loop) is Block:
            stmtcode = self.visit(ast.loop,SubBody(o.frame,o.sym))
        else:
            stmtcode = self.visit(ast.loop,Access(o.frame,o.sym,False,True))
        jcode = self.visit(ast.expr1,Access(o.frame,o.sym,True,True))[0] + self.emit.emitLABEL(o.frame.getContinueLabel(),o.frame) + self.visit(ast.expr2,Access(o.frame, o.sym, False, True)) [0] + self.emit.emitIFFALSE(o.frame.getBreakLabel(),o.frame) + stmtcode[0] + self.visit(ast.expr3,Access(o.frame,o.sym,True,True))[0] + self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame) + self.emit.emitLABEL(o.frame.getBreakLabel(),o.frame)
        o.frame.exitLoop()
        return jcode , None

    def visitIf(self, ast,o):
        Label1 = o.frame.getNewLabel()
        if ast.elseStmt:
            Label2 = o.frame.getNewLabel()
            elseStmt = self.visit(ast.elseStmt,SubBody(o.frame,o.sym)) if type(ast.elseStmt) is Block else self.visit(ast.elseStmt,Access(o.frame,o.sym,True,True)) if (type(ast.elseStmt) is BinaryOp and ast.elseStmt.op == "=") else self.visit(ast.elseStmt,Access(o.frame,o.sym,False,True))
            return self.visit(ast.expr,Access(o.frame,o.sym,False,True))[0] + self.emit.emitIFFALSE(Label1,o.frame) + (self.visit(ast.thenStmt,SubBody(o.frame,o.sym))[0] if type(ast.thenStmt) is Block else self.visit(ast.thenStmt,Access(o.frame,o.sym,True,True))[0] if (type(ast.thenStmt) is BinaryOp and ast.thenStmt.op == "=") else self.visit(ast.thenStmt,Access(o.frame,o.sym,False,True))[0]) + self.emit.emitGOTO(Label2,o.frame) + self.emit.emitLABEL(Label1,o.frame) + elseStmt[0] + self.emit.emitLABEL(Label2,o.frame), None
        else:
            return self.visit(ast.expr,Access(o.frame,o.sym,False,True))[0] + self.emit.emitIFTRUE(Label1,o.frame) + self.visit(ast.thenStmt,SubBody(o.frame,o.sym))[0] if type(ast.thenStmt) is Block else self.visit(ast.thenStmt,Access(o.frame,o.sym,True,True))[0] if (type(ast.thenStmt) is BinaryOp and ast.thenStmt.op == "=") else self.visit(ast.thenStmt,Access(o.frame,o.sym,False,True))[0] + self.emit.emitLABEL(Label1,o.frame), None
    
    def visitDowhile(self ,ast ,o):
        o.frame.enterLoop()
        jcode = self.emit.emitLABEL(o.frame.getContinueLabel(),o.frame)
        for x in ast.sl:
            forcode = self.visit(x,SubBody(o.frame,o.sym)) if type(x) is Block else self.visit(x,Access(o.frame,o.sym,True,True)) if (type(ast.sl) is BinaryOp and ast.sl.op == "=") else self.visit(x,Access(o.frame,o.sym,False,True))
            if type(forcode[0]) is Symbol:
                o.sym.insert(0,forcode[0])
            else:
                jcode = jcode + forcode[0]
                jcode = jcode + self.emit.emitPOP(o.frame) if o.frame.getStackSize() != 0 else jcode
        jcode = jcode + self.visit(ast.exp,Access(o.frame,o.sym,False,True))[0] + self.emit.emitIFTRUE(o.frame.getContinueLabel(),o.frame) + self.emit.emitLABEL(o.frame.getBreakLabel(),o.frame)
        o.frame.exitLoop()
        return jcode, None
    
    def visitArrayCell(self ,ast ,o):    
        if o.isLeft == True:
            if o.isFirst == True:
                arr = self.visit(ast.arr,Access(o.frame,o.sym,False,o.isFirst))
                return arr[0] + self.visit(ast.idx,Access(o.frame,o.sym,False,True))[0] , arr[1]
            else:
                thisarr = self.visit(ast.arr,Access(o.frame,o.sym,o.isLeft,False))
                return thisarr[0], thisarr[1]
        else:
            ar = self.visit(ast.arr,Access(o.frame,o.sym,False,o.isFirst))
            return ar[0] + self.visit(ast.idx,Access(o.frame,o.sym,False,True))[0] + self.visit(ast.arr,Access(o.frame,o.sym,o.isLeft,False))[0] ,ar[1]