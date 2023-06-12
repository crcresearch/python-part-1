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

An `if` statment will execute the tabbed code under it if the condition is `True`:

```python
x = 10
y = False

if x > 5:
    y = True

```

Using the `else` statement we can tell it to do something `else` if the statement is `False`:

```python
x = 10
y = 0

if x > 5:
    y = 'Yes'
else:
    y = 'No'
```

You can also combine logic using `and`, `or`, and `not` as seen before:

```python
shirt = 'red'
pants = 'red'
is_all_red = None

if shirt == 'red' and pants == 'red':
    is_all_red = True
else:
    is_all_red = False
```

### while

A `while` loop will repeatedly execute the code under it until the condition becomes `False`.  IMPORTANT: always make sure there is code within the `while` loop that modifies the check, otherwise you will end up stuck in an `infinite loop`:

```python
x = 0

while x < 10:
    x = x + 1
    print(x)
```

An example of an infinite loop:

```python
x = 0
y = 0

while y < 10:
    x = x + 1
    print(x)
```

Can you spot why?  If you're stuck in an infinite loop, press `Ctrl+C` to exit the loop.

### for

A `for` loop allows you to iterate over a list, where each element of the list is assigned to a designated variable on each iteration:

```python
l = [1, 2, 3, 4, 5]

for i in l:
    print("The next item in the list is:", i)
```

Note how `i` was the new variable, and each iteration (or round) of the loop, `i` was assigned the next element in the list.

## Topic 7: Input and Output

### Screen and Keyboard

You can send things to the terminal with the `print` function:

```python
print("Hello world!")
```

And you can format strings to inject variables with:

```python
x = 10

print(f"The value of x is: {x}")
```

And use special characters such as `\n` and `\t`:

```python
print("Here is a new line:\n...and the second line!")

print("Here is a tab:\twith some text after it")
```

And you can grab values from the user with the `input` command:

```python
x = input("What is your name?")

y = input("What is your age?")
```

Note that the `input` command will always return a string!  So if you want to use the input as an integer or float, you'll need to type-cast it by wrapping it in either `int()` or `float()`:

```python
x = input("What is your name?")

y = int(input("What is your age?"))
```


### File Access

File Input/Output (I/O) is very easy using the `open` function:

```python
# to read a file (read-only), pass in the 'r' parameter:
file_in = open('test.txt', 'r')

# then loop over the lines in the file:
for line in file_in.readlines():
    print(line)

# close the file with:
file_in.close()
```


You can also write to new files:
```python
# to write a file (either new file or replace the file), pass in the 'w' parameter:
file_out = open('test2.txt', 'w')

# write your text:
file_out.write("This is some sample text!")

# close the file with:
file_out.close()
```

Lastly, you can append to an existing file:
```python
# to write a file in APPEND mode, pass in the 'a' parameter:
file_out = open('test2.txt', 'a')

# write your text:
file_out.write("This is some MORE text!")

# close the file with:
file_out.close()
```

## Topic 8: Importing Libraries

A python library is a pre-written collection of functions with a specific purpose to bring new features to your script.  Python has many libraries installed by default, but others can be downloaded and installed using `pip` that are published at: https://pypi.org/

For now, let's import a built-in library for generating random numbers:

```python
import random

# generate a random float number between 0 and 1:
x = random.random()

# generate a random integer between 1 and 1000
y = random.randint(1, 1000)
```


## PROJECT:

Using what we learned, write a script that generates a random number between 0 and 100, and have the user guess!
