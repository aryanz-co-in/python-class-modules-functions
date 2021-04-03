Python Classes & Objects
---------------------------

Python is an object-oriented programming language. Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.


## Creating Class

```python
class MyClass:
    empid = 1001
    empname = "John"

```


## Creating object for the class

```python
    obj1 = MyClass()
    print(obj1.empid)
    print(obj1.empname)   

```

## The \__init\__() Function

This is kind of Python's standard initialize method which is invoked during object creation of the class.
consider you want to pre-initialize the properties of the class ahead of object creation, then you need to use this method.


```python
class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age

# -------------------------------------------

student1 = Student(100,"Bob", 22)
print(student1.sid)
print(student1.name)
print(student1.age)
```

In the above class we have init method which will initialize with the constructor value passed while creating object,
Also if you noticed we have **self** as our first parameter, which is used for identifying the current/own object. 

**Note: The \__init\__() function is called automatically every time the class is being used to create a new object.**


## The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

```python

class Car:
    def __init__(myownobjectref, carid, carmake):
        myownobjectref.carid = carid
        myownobjectref.carmake = carmake

```

in the above example we have used myownobjectref as first param and it refers the current object.

-------------------------------------------------

## Modify object properties

```python
class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name

# -------------------------------------------

student1 = Student(100,"Bob")
student1.sid = 101

```


## Delete object properties

```python
class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name

# -------------------------------------------

student1 = Student(100,"Bob")
del student1.sid

```


## Delete object

```python
class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name

# -------------------------------------------

student1 = Student(100,"Bob")
del student1

```