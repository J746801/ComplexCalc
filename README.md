# Calculator With Variables
This is a calculator that can work with variables that you can set and some that are built in, like pi, e (Euler's number), tau, and inf (infinity). It can also use built-in python functions and the functions from the python math module.
# Simple Use
For more basic use, 2\*4 means 2 multiplied by 4, 16/4 means 16 divided by 4, 37-13 means 37 minus 13, 29+16 means 29 plus 16, 2^4 means 2 to the power of 4, or 2\*2\*2\*2, and 8%3 returns the remainder of 8/3, which is 2. At any time, pressing Enter adds the current answer to the History window.

There are two ways to add variables: one is to simply type \<variablename> = \<value/expression> directly in the Variables window. The other way is to type the same thing in the main window and then press Enter. Either way you can use a mathematical expression to define the value of the variable.

# Complex Use
If you know anything about the python math library than you can use math.\<function>(\<value(s)>) in the calculator, like math.ceil(2.071), for example. Otherwise, you can find information about it here: https://www.w3schools.com/python/module_math.asp . You can also use the operators <, >, &, and you can make dictionaries and lists.

# Notes
1. ComplexCalc.exe is version 1.0 and only works on Windows, and also has a few bugs. The other versions will be in appropriately named folders when they are released and inside the folders will be Windows, Linux and Mac versions.
2. You cannot use underscores or symbols in variable names.
3. Allowed symbols for use: +, -, *, /, %, ^ (does what ** normally does in python, so the normal function of ^ is unavailable), &, ~, |, =, [ and ], { and }, >, < (although currently you cannot use >=, <=, != or ==).
4. If you know python, you may create lists and dictionaries using [, ], {, and }.
5. Currently, you must use a space before and after [ and ] when referencing lists and dictionaries.
6. If you accidentally change the value of pi, e, tau, or inf, they fix themselves.
7. Currently, ** and // do not work.
8. I plan on eventually having unit conversions and more built-in.
