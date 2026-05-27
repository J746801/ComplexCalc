# Calculator With Variables
This is a calculator that can work with variables that you can set, and some that are built in, like pi, e (Euler's number), tau, and inf (infinity). It can also use built-in python functions and the functions from the python math and cmath modules.

# Please star this repository if you find it useful!
Please download the latest version, older versions have less features and may have some bugs. ComplexCalc.exe (not in a folder) is version 1.0, only works on Windows, has less features, and has a few bugs. DO NOT DOWNLOAD IT.

# Download
1. For Windows: Simply download the latest ComplexCalc.exe version, and if you want, pin it to start/desktop/taskbar.
2. For MacOS: I don't really know, but mabye similar to Windows? Also, MacOS versions are unsigned, so your computer may say it might not be safe software and will ask if you still want to open it. Just click "yes" or something (I don't really know anything about Macs because I don't have one).
3. For Linux: Download the latest ComplexCalc.bin file, and if this is the first time downloading it, download the .desktop (the shortcut) and .svg (the icon) files and change the file paths in the .desktop file. I put ComplexCalc.bin in /bin, ComplexCalc.desktop in /usr/share/applications, and CompCalcIcon.svg in /usr/share/icons/hicolor/scalable/apps. You don't have to put them there, but that's where I recommend to put the .desktop and the .svg.

# Simple Use
For more basic use, 2\*4 means 2 multiplied by 4, 16/4 means 16 divided by 4, 37-13 means 37 minus 13, 29+16 means 29 plus 16, 2**4 means 2 to the power of 4, or 2\*2\*2\*2, and 8%3 returns the remainder of 8/3, which is 2. At any time, pressing Enter adds the current answer to the History window. Delete clears the entry window. You can remove variables by simply going to the Variables window and removing them from the list. Also, sqrt(9) returns the square root of 9, or 3, cbrt(8) returns the cubed root of 8, or 2, and roots(256, 4) returns the fourth root of 256, or 4. For roots(a, b), a is the number you want to find the b root of, so roots(9, 2) is the same as sqrt(9), and roots(8, 3) is the same as cbrt(8).

There are two ways to add variables: one is to simply type \<variablename> = \<value/expression> directly in the Variables window. The other way is to type the same thing in the main window and then press Enter. Either way you can use a mathematical expression to define the value of the variable.

# Complex Use
If you know anything about the python math library than you can use math.\<function>(\<value(s)>) in the calculator, like math.ceil(2.071), for example. Otherwise, you can find information about it here: https://www.w3schools.com/python/module_math.asp . You can also use the operators <, >, <=, >=, ^, &, +=, -=, *=, /=, ==, and //, and you can make dictionaries and lists.

# Notes
1. ComplexCalc.exe (not in a folder) is version 1.0 and only works on Windows, and also has a few bugs. The other versions will be in appropriately named folders when they are released, and inside the folders will be Windows, Linux and MacOS versions.
2. You cannot use symbols in variable names.
3. Allowed symbols for use: +, -, *, /, %, ^, &, ~, |, =, [ and ], { and }, >, <, <=, >=, !=, ==, +=, -=, *=, /=, **, //.
4. If you know python, you may create lists and dictionaries using [, ], {, and }.
5. If you accidentally change the value of pi, e, tau, or inf (for example by typing pi=81 and prssing Enter), they fix themselves if you press any key except Delete (though it will still display the correct value in the answer, it will not in the Variables window). If you press Delete just type = and they will fix themselves.
6. I plan on eventually having unit conversions and more built-in.
7. Please note that I do not have a Mac, so the MacOS Version 1.1 is untested, unsigned and not notarized, so (if it works) your computer may say it might not be safe software and will ask if you still want to open it. Just click "yes" or something (I don't really know anything about Macs because I don't have one).
