Python Modules
---------------------------

Python modules are .py files that consist of Python code. Any Python file can be referenced as a module.

Some modules are available through the Python Standard Library and are therefore installed with your Python installation.
Others can be installed with Python’s package manager pip.
Additionally, you can create your own Python modules since modules are comprised of Python .py files.

Writing and Importing Modules
----------------------------

### Writing Modules
Writing a module is just like writing any other Python file. Modules can contain definitions of functions, classes, and variables that can then be utilized in other Python programs.

From our Python 3 local programming environment or server-based programming environment, let’s start by creating a file hello.py that we’ll later import into another file.

To begin, we’ll create a function that prints Hello, World!:
```python
# math_operations.py (Located under my-own-modules directory)

# Maths Operation

def add(a, b):
    print(a + b)

 ```
If we run the program on the command line with python math_operations.py nothing will happen since we have not invoked the functions add.


### Importing Modules
Let’s create a second file called main_program.py so that we can import the module we just created, and then call the function.


```python
main_program.py
# Import math_operations module - which is nothing but the math_operations.py file
import math_operations


# Call function
math_operation.add(1, 2)
 ```
Because we are importing a module, we need to call the function by referencing the module name in DOT " . " notation.

We could instead import the module as from hello import world and call the function directly as world(). You can learn more about this method by reading how to using from … import when importing modules.
