# easyscript

Easyscript is a BASIC based programming language written using PLY parsing tools for Python. It has a simple, straightforward syntax with just enough capabilites for people to use it as a first approach to programming.

## Implementation

### tokrules.py

This module declares the class **MyLexer**. It describes all the tokens and reserved words available in the language. An instance of the MyLexer class is used to build the parser.

### parserules.py

This module delcares the grammar rules for the language within a class called MyParser. The functions declared contain all the translation actions for the instructions in the code. It leverages the tokens processed by the previous module.

### easyscript.py

This module builds the parser for the program by declaring an instance of the MyParser class. A text document with the actual code of the program is passed as argument to this module to begin the execution. Three stages correspond to this process:
- Parsing (identify all the tokens and its semantics in the source code).
- Translating (generating the instructions to execute).
- Execution (run the program).

---
## Syntax

### Program Structure

### Variable Declaration

### Assignment instruction

### Arithmetic operations

### Logic operations

### Procedures

### Conditional Statements

### Loops

### Dimensioned Variables

---
## Code Examples 
### Calculate the factorial of a number:

### Add and Multiply Matrices:
