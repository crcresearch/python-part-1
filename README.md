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


## Topic 3: Variables

Python variables are much like other programming language variables where you can name a variable and update/fetch the variable's value.  However, Python does not require you to declare the variable type, and the type can change throughout your code.  The most basic Python variable types are:

* Boolean (`True` or `False`)
* Integer
* Float
* String
* Class (no covered in this course)

You can assign variables with the `=` operator.

```python
w = True
x = 1
y = 2.5
z = "Hello world!"
```

You can change the variable (and it's type):
```python
w = True
w = 2.5
w = "Yes!"
```

You can see what the type of the variable is with:

```python
w = True
type(w)

w = 2.5
type(w)
```

You can compare two variables to see if they're the same with the `==` operator: note how this is different than `=`

```python
x = True
y = False

x == y

y = True

x == y
```

## Topic 4: Mathematical Operators

### +, -, *, /, %

Operators will perform different actions based on the variable types.

In summary:
- `+` adds numbers, concatonates strings
- `-` subtracts numbers, doesn't support strings
- `*` multiples numbers, doesn't support strings (but DOES support a string and a number!)
- `/` devides numbers (always returns float), doesn't support strings
- `%` returns the remainder of a division (numbers only)

```python
x = 10
y = 2

x + y

x - y

x * y

x / y

x % y
```

```python
x = 10
y = 'hello'
z = 'world'

y + z

x * y
```

What other combinations are there?


## Topic 5: Basic Data Structures

### List

A list is an ordered series of values.  They don't need to be the same type, and the order is preserved.  Lists in Python are `zero-indexed`:

```python
l = [False, 1, 2.5, 'three']

l[0]

l[3]

l[-1]

l[0] = True

x = 100

l[1] = x
```

### Dictionary

A dictionary is a structured data object with `key: value` pairs.  A dictionary's order is not guaranteed to be preserved, but they `key: value` pairs always will be.

```python
d = {'name': 'david', 'age': 10, 'location': 'Notre Dame', 'is_awake': True}

d['name']

d['is_awake'] = False
```

## Topic 6: Logic Flow

### If/else

### while

### for

## Topic 7: Input and Output

### Screen and Keyboard

### File Access

## Topic 8: Importing Libraries


## PROJECT:

Using what we learned, write a script that generates a random number between 0 and 100, and have the user guess!
