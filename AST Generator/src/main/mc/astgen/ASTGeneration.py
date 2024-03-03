#1752159
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from antlr4 import *

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        make_list = []
        for declare in ctx.declaration():
            x = self.visitDeclaration(declare)
            if type(x) is list:
                make_list.extend(x)
            else:
                make_list.append(x)
        return Program(make_list)

        
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visitChildren(ctx)

    def visitVardeclare(self, ctx:MCParser.VardeclareContext):
        var_list = []
        for x in ctx.var():
            b = x.ID()
            if x.getChildCount() == 1:
                var_list.append(VarDecl(b.getText(),self.visit(ctx.primitivetype())))
            else:
                var_list.append(VarDecl(b.getText(),ArrayType(int(x.INTLIT().getText()),self.visit(ctx.primitivetype()))))
        return var_list


    def visitVar(self,ctx:MCParser.VarContext):
        pass

    def visitPrimitivetype(self, ctx:MCParser.PrimitivetypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.BOOLTYPE():
            return BoolType()
        
    def visitFunctiondeclare(self, ctx:MCParser.FunctiondeclareContext):
        if ctx.voidfunctiondeclare():
            return self.visit(ctx.voidfunctiondeclare())
        elif ctx.nonvoidfunctiondeclare():
            return self.visit(ctx.nonvoidfunctiondeclare())
        else:
            return self.visit(ctx.functionpoitertype())
       
    
    def visitNonvoidfunctiondeclare(self,ctx:MCParser.NonvoidfunctiondeclareContext):  
        return FuncDecl(Id(ctx.getChild(1).getText()),self.visit(ctx.parameterlists()),self.visit(ctx.primitivetype()),self.visit(ctx.functionbody()))
    def visitVoidfunctiondeclare(self,ctx:MCParser.VoidfunctiondeclareContext):
        return FuncDecl(Id(ctx.getChild(1).getText()),self.visit(ctx.parameterlists()),self.visit(ctx.functiontype()),self.visit(ctx.functionbody()))
    def visitFunctionpoitertype(self,ctx:MCParser.FunctionpoitertypeContext):
        return FuncDecl(Id(ctx.getChild(3).getText()),self.visit(ctx.parameterlists()),ArrayPointerType(self.visit(ctx.primitivetype())),self.visit(ctx.functionbody()))
    def visitFunctiontype(self,ctx:MCParser.FunctiontypeContext):
        return VoidType()
    def visitParameterlists(self,ctx:MCParser.ParameterlistsContext):
        para_list = []
        for x in ctx.variable():
            para_list.append(self.visit(x))
        return para_list

    def visitVariable(self, ctx:MCParser.VariableContext):
        if ctx.getChildCount() == 2:
            return VarDecl(ctx.ID().getText(),self.visit(ctx.primitivetype()))
        else:
            return VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.primitivetype())))
            
    def visitFunctionbody(self,ctx:MCParser.FunctionbodyContext):
        statementlist = []
        for x in ctx.statement():
            state = self.visit(x)
            if type(state) is list:
                statementlist.extend(state)
            else:
                statementlist.append(state)
        return Block(statementlist)

    def visitStatement(self,ctx:MCParser.StatementContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.blockstatement():
            return self.visit(ctx.blockstatement())
        elif ctx.ifstatement():
            return self.visit(ctx.ifstatement())
        elif ctx.dowhilestatement():
            return self.visit(ctx.dowhilestatement())
        elif ctx.forstatement():
            return self.visit(ctx.forstatement())
        elif ctx.breakstatement():
            return self.visit(ctx.breakstatement())
        elif ctx.continuestatement():
            return self.visit(ctx.continuestatement())
        elif ctx.voidreturnstatement():
            return self.visit(ctx.voidreturnstatement())
        elif ctx.nonvoidreturnstatement():
            return self.visit(ctx.nonvoidreturnstatement())
        elif ctx.vardeclare():
            return self.visit(ctx.vardeclare())

    def visitBlockstatement(self,ctx:MCParser.BlockstatementContext):
        statementlist = []
        for x in ctx.statement():
            state = self.visit(x)
            if type(state) is list:
                statementlist.extend(state)
            else:
                statementlist.append(state)
        return Block(statementlist)
    
    
    
    
    def visitContinuestatement(self,ctx:MCParser.ContinuestatementContext):
        return Continue()
    def visitBreakstatement(self,ctx:MCParser.BreakstatementContext):
        return Break()
    def visitIfstatement(self,ctx:MCParser.IfstatementContext):
        if ctx.ELSE():
            return If(self.visit(ctx.orexpression()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))
        else:
            return If(self.visit(ctx.orexpression()),self.visit(ctx.statement(0)))
    def visitDowhilestatement(self,ctx:MCParser.DowhilestatementContext):
        statement_list = []
        for x in ctx.statement():
            if type(x) is not list:
                statement_list.append(self.visit(x))
            else:
                statement_list.extend(self.visit(x))
        return Dowhile(statement_list,self.visit(ctx.orexpression()))
    def visitForstatement(self,ctx:MCParser.ForstatementContext):
        return For(self.visit(ctx.expression(0)),self.visit(ctx.orexpression()),self.visit(ctx.expression(1)),self.visit(ctx.statement()))
    def visitVoidreturnstatement(self,ctx:MCParser.VoidreturnstatementContext):
        return Return()
    def visitNonvoidreturnstatement(self,ctx:MCParser.NonvoidreturnstatementContext):
        return Return(self.visit(ctx.orexpression()))
    
    
    
    def visitFuncall(self,ctx:MCParser.FuncallContext):
        return CallExpr( Id(ctx.getChild(0).getText()) ,self.visit(ctx.param()))
    def visitParam(self,ctx:MCParser.ParamContext):
        exp_list = []
        for x in ctx.exp():
            exp_list.append(self.visit(x))
        return exp_list
    def visitExp(self,ctx:MCParser.ExpContext):
        if ctx.funcall():
            return self.visit(ctx.funcall())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.BOOLLIT():
            var = True if ctx.BOOLLIT().getText() == "true" else False
            return BooleanLiteral(var)
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        else:
            return self.visit(ctx.orexpression())

    def visitExpression(self,ctx:MCParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.orexpression())
        else:
            return BinaryOp("=",self.visit(ctx.orexpression()),self.visit(ctx.expression()))
    def visitOrexpression(self,ctx:MCParser.OrexpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.andexpression())
        else:
            return BinaryOp("||",self.visit(ctx.orexpression()),self.visit(ctx.andexpression()))
    def visitAndexpression(self,ctx:MCParser.AndexpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        else:
            return BinaryOp("&&",self.visit(ctx.andexpression()),self.visit(ctx.term()))
    def visitTerm(self,ctx:MCParser.TermContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.compareexpression(0))
        else:
            return BinaryOp(self.visit(ctx.termop()),self.visit(ctx.compareexpression(0)),self.visit(ctx.compareexpression(1)))
    def visitCompareexpression(self,ctx:MCParser.CompareexpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arithexpression(0))
        else:
            return BinaryOp(self.visit(ctx.compareop()),self.visit(ctx.arithexpression(0)),self.visit(ctx.arithexpression(1)))
    def visitArithexpression(self,ctx:MCParser.ArithexpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arithmeticexpression())
        else:
            return BinaryOp(self.visit(ctx.arithop()),self.visit(ctx.arithexpression()),self.visit(ctx.arithmeticexpression()))
    def visitArithmeticexpression(self,ctx:MCParser.ArithmeticexpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.negativeexpression())
        else:
            return BinaryOp(self.visit(ctx.arithmeticop()),self.visit(ctx.arithmeticexpression()),self.visit(ctx.negativeexpression()))
    def visitNegativeexpression(self,ctx:MCParser.NegativeexpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.square())
        else:
            return UnaryOp(self.visit(ctx.negativeop()),self.visit(ctx.negativeexpression()))
    def visitSquare(self,ctx:MCParser.SquareContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.ex())
        else:
            return ArrayCell(self.visit(ctx.operand()),self.visit(ctx.expression()))
    def visitEx(self,ctx:MCParser.ExContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.operand())
        else:
            return self.visit(ctx.expression())
    def visitOperand(self,ctx:MCParser.OperandContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        elif ctx.BOOLLIT():
            # return BooleanLiteral((ctx.BOOLLIT().getText()))
            para = True if ctx.BOOLLIT().getText() == 'true' else False
            return BooleanLiteral(para)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.funcall())
    def visitTermop(self,ctx:MCParser.TermContext):
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        else:
            return ctx.NOTEQUAL().getText()
    def visitCompareop(self,ctx:MCParser.CompareopContext):
        if ctx.LESSEQUAL():
            return ctx.LESSEQUAL().getText()
        elif ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.GREATEREQUAL():
            return ctx.GREATEREQUAL().getText()
    def visitArithmeticop(self,ctx:MCParser.ArithmeticopContext):
        if ctx.MULTIPLICATION():
            return ctx.MULTIPLICATION().getText()
        elif ctx.DIV():
            return ctx.DIV().getText()
        else:
            return ctx.MOD().getText()
    def visitArithop(self,ctx:MCParser.ArithopContext):
        if ctx.ADD():
            return ctx.ADD().getText()
        else:
            return ctx.SUB().getText()
    def visitNegativeop(self,ctx:MCParser.NegativeopContext):
        if ctx.SUB():
            return ctx.SUB().getText()
        else:
            return ctx.NOT().getText()
