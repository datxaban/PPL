# Micro C Language

# Contents
1. [Introduction](#section1)
2. [2 Program Structure](#section2)
    1. [Variable declaration](#subsection2.1)
    2. [Function declaration](#subsection2.2)
3. [Lexical Specification](#section3)
   1. [Character Set](#subsection3.1)
   2. [Comments](#subsection3.2)
   3. [Token Set](#subsection3.3)
   4. [Separators](#subsection3.4)
   5. [Literals](#subsection3.5)
4. [Types and Values](#section4)
   1. [The void Type and Values](#subsection4.1)
   2. [The boolean Type and Values](#subsection4.2)
   3. [The int Type and Values](#subsection4.3)
   4. [The float Type and Values](#subsection4.4)
   5. [The string Type and Values](#subsection4.5)
   6. [Array Types and Their Values](#subsection4.6)
   7. [Array Pointer Type](#subsection4.7)
5. [Variables](#section5)
  1. [Global Variables](#section5.1)
  2. [Local Variables](#section5.2)
6. [Expressions](#section7)
  1. [The if Statement](#subsection7.1)
  2. [The do while Statement](#subsection7.2)
  3. [The for Statement](#subsection7.3)
  4. [The break Statement](#subsection7.4)
  5. [The continue Statement](#subsection7.5)
  6. [The return Statement](#subsection7.6)
  7. [The expression Statement](#subsection7.7)
  8. [The block State](#subsection7.8)
7. [Statements and Control Flow](#section7)
  1. [The if Statement](#subsection7.1)
  2. [The do while Statement](#subsection7.2)
  3. [The for Statement](#subsection7.3)
  4. [The break Statement](#subsection7.4)
  5. [The continue Statement](#subsection7.5)
  6. [The return Statement](#subsection7.6)
  7. [The expression Statement](#subsection7.7)
  8. [The block Statement](#subsection7.8)
8. [Built-in Functions](#section8)
9. [Scope Rules](#section9)
10. [The main function](#section10)
## This is the introduction <a name="introduction"></a>
Some introduction text, formatted in heading 2 style

## 1. Introduction <a name="section1"></a>
MC (Micro C) is a language which consists of a subset of C plus some Java language fea- tures.
The C features of this language are (details will be discussed later): a few primitive types, one-dimensional arrays, control structures, expressions, compound statements (i.e., blocks) and functions.
The Java features of this language are as follows:

1. MC has type boolean, borrowed from Java. In MC, therefore, all boolean expressions must be evaluated to a value of type boolean, which is either true or false. (That is, boolean variables have numerical values, like those in C++).
2. In MC, like Java, the operands of an operator are guaranteed to be evaluated in a specific evaluation order, particularly, from left to right. In C and C++, the evaluation order is left unspecified. In the case of f() + g(), for example, MC dictates that f is always evaluated before g.

For simplicity reason:

1. MC does not support variable initialization.
```
float f = 1.0; // ERROR
float f; //CORRECT
``` 
2. In an array declaration, the size of array must be known explicitly.
```
int i[]; //ERROR
int i[5]; //CORRECT
```
Conventionally, the sequence ’\n’ must be used as a new line character in MC.

## Program Structure <a name="section2"></a>
MC does not support separate compilation so all declarations (variable and function) must be resided in one single file.

An MC program consists of many declarations which include variable declarations and function declarations.

### Variable declaration
- Not support variable initialization
- Array size must be known during declaration.
- Syntax: There are two types of variable declaration:
  - <primitive type> <variable> ’;’
  - where a <primitive type> is a primitive type which is described in Section 4; a <variable> can be an identifier alone or an identifier followed by a ‘[‘, an integer literal, and then a ‘]’.
For example: int i; float j[5];
### Function declaration



## Lexical Specigication <a name="section3"></a>
The second paragraph text

### Character Set
### Comments
### Token Set
### Separators
### Literals

## Types and Values <a name="section4"></a>

### The void Type and Values
### The boolean Type and Values
### The int Type and Values
### The float Type and Values
### The string Type and Values
### Array Types and Their valeus
### Array Pointer Type

## Variables <a name="section5"></a>

### 5.1 Global Variables
### 5.2 Local Variables


## Expression <a name="section6"></a>

### 6.1 Precedence and Associativity
### 6.2 Type Coercions
### 6.3 Index Pression
### 6.4 Invocation Expression
### 6.5 Evaluation Order


## 7. Statements and Control Flow <a name="section7></a>
MC supports these statements: if, for, do. . . while, break, continue, return, expression, and block. All statements except if, for and the block one must be followed by a semi-colon.

### The if Statement
### The do while Statement
### The for Statement
### The break Statement
### The continue Statement
### The return Statement
### The expression Statement
### The block statement

## 8.Built-in Functions <a name="section8"></a>
MC has some following built-in functions:

<em>int getInt()</em>: reads and returns an integer value from the standard input

<em>void putInt(int i)</em>: prints the value of the integer i to the standard output

<em>void putIntLn(int i)</em>: same as putInt except that it also prints a newline

<em>float getFloat()</em>: reads and returns a floating-point value from the standard input void putFloat(float f): prints the value of the float f to the standard output

<em>void putFloatLn(float f)</em>: same as putFloat except that it also prints a newline

<em>void putBool(boolean b)</em>: prints the value of the boolean b to the standard output void putBoolLn(boolean b): same as putBoolLn except that it also prints a new line void 

<em>putString(string s)</em>: prints the value of the string to the standard output

<em>void putStringLn(string s)</em>: same as putStringLn except that it also prints a new line void putLn(): prints a newline to the standard output

## 9.Scope Rules <a name="section9"></a>
Scope rules govern declarations (defining occurrences of identifiers) and their uses (i.e., applied occurrences of identifiers).

The scope of a declaration is the region of the program over which the declaration can be referred to. A declaration is said to be in scope at a point in the program if its scope includes that point.

A block is a language construct that can contain declarations. There are two types of blocks in the MC language:
- The outermost block is the entire program.
- Each block statement forms a block by itself. A special case is that a function has its
block from ’(’ (before the parameter list) to ’}’ (the end of its body).

MC exhibits nested block structure since blocks may be nested one within another. Therefore, there may be many scope levels:
1. All declarations in global scope are effective in the entire progran.
2. All declarations in local scope are effective from the place of the declaration to the end of its scope.
3. No identifier can be defined more than once in the same scope. This implies that no identifier represents both a global variable and a function name simultaneously.
4. Most closed nested rule: For every applied occurrence of an identifier in a block, there must be a corresponding declaration, which is in the smallest enclosing block that contains any declaration of that identifier.



## 10. The main function <a name="section10"></a>
A special function, i.e. main function, is an entry of a MC program where the program starts:
```
void main() { // no parameters are allowed
  ...
}
```
