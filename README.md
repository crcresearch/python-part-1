# Introuction to Python: Part I

This repository is intended to provide examples of the basics of Python with working examples.  Follow the topics below and their related example python files for demosntrations!

## Topic 1: The Python Interpreter

The Python interpreter is a sort of virtual machine (Python Virtual Machine, or PVM) that allows the user to enter Python commands.  The command are then executed one at a time, being translated from Python code to machine-compiled routines.

There are two ways to interact with the Python interpreter, but they are both the same at their core.

### Python Interactive Interpreter:

The first way is to simply type `python` in the terminal.  This brings up an interactive Python shell where you can start entering Python commands.  To exit the Python interpreter, type `exit()` and press enter.

### Python Scripts:

The second way is to write Python scripts and send the entire script to the interpreter.  This is done so we can automate our commands without having to type them out individually.  These commands are executed in the exact same way, except when one command completes, the interpreter will automatically start the next command.

This can be done with: `python some_script.py`  Once Python reaches the end of the script, it will automatically exit.



## Topic 2: General Logic

The most basic logic can be described with the following bitwise operators:

* AND
* OR
* NOT

These logic operators can be manufactured as simple hardware components, and are the foundation of all computer programming logic.  Everything we do with software can be boiled down to the use of these three basic operators functioning on computer signals represented as 1's and 0's.  `1` being where there is voltage on the line, and `0` where there is no voltage.

In Python, we use these values as the keywords `True` and `False`, and we can generate an exhaustive list of possible outcomes by following the below _Truth Tables_:

### AND Operator - _both_ inputs must be true for the result to be true

|  Input A | Input B | Result |
| -------- | ------- | ------ |
| True     | True    | True   |
| True     | False   | False  |
| False    | True    | False  |
| False    | False   | False  |

### OR Operator - _either_ input must be true for the result to be true

|  Input A | Input B | Result |
| -------- | ------- | ------ |
| True     | True    | True   |
| True     | False   | True   |
| False    | True    | True   |
| False    | False   | False  |

### NOT Operator - _negates_ the input

|  Input  |  Result |
| ------- |  ------ |
| True    |  False  |
| False   |  True   |


We can combine these values using the `and`, `or`, and `not` keywords in Python (see lines 8-28 of `general_logic.py`).

We can also chain these together in infinately long logic by combining the logic operators.  The logic flows from left &rarr; right.  See lines 30-34 of `general_logic.py`, and think about why they give different results.

