# Gujarati-Compiler
Key words and their functionalities are mentioned in the separate doc files.

Lexer,Parser and function files are written in python language in __pycache__ directory.
In doc directory submitted report as my university project.
## Requirements:
* Python (v3.7+)
* Python ply `pip install ply`

## Use:
You can start using it by using the following commands:
* `python parser.py` for interpreted mode
* `python parser.py file.dr` to compile a file

## Keywords (and equivalent in python):
Keyword	Python
chhapo	print
mahiti	input
jo	if
athva	else
kro	do
jya	while
mate	for
bahar	break
chalu	continue
ane	and
ya	or
khotu	false
sachu	true
nahi	not
banavo	def
moklo	return
prayas	try
sivay	except
kul	len
jodo	append
hatavo	pop

## Features:
* Variables
* Comments
* Control flow statements:
    - loops (while,do-while,for)
    - conditional statements
    - function calls
    
* Operators:
    - arithmetic : `+ - * / % ^`
    - comparison : `> >= < <= == !=`
    - logical : `and or not`
    - assignement : `=`
    - unary : `++ --`

### Identifiers:
Rules for writing identifiers:
1. Identifiers can be a combination of letters in lowercase or uppercase or digits or an underscore _. 
2. An identifier cannot start with a digit.
3. Keywords cannot be used as identifiers.
4. Variables are case sensitive `test` is different than `Test`. 


