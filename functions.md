Python Functions
---------------------------

Python functions are written inside .py files which performs the instruction or action written in Python.
each method/function performs set of instruction or operations we wanted to perform. like adding two numbers, checking if the user is admin or not etc.,

## Creating Function

In order to create python functions/methods you need to use def key word prefixed. lets see the below example.

```python
# functions.py
# def -> key word tells us this is a method.
# display_app_name(): this is our method name with no parameters, because with in the brackets we have not passes any variable.
def display_app_name():
    print("My App Name")
```

## Calling Function

Calling a medhod in Python is easy, just need to use the method name with the brackets. (If method has any parameters, we need to just pass it inside the brackets.)

```python
# calling the function
display_app_name()
```


## Returning data from Function

```python
# functions.py
def get_current_username(user):
    return user["name"]

userobj = {
    "name": "John",
    "id": 100}

print(get_current_username(userobj))

```


## Calling function inside another function.

```python
# functions.py
def is_admin(user_param):
    return user_param["admin"]

def append_usertype(old_user_id, user_type):
    return f"{old_user_id}_{user_type}"


def regenerate_userid(user_param):
    new_userid = user_param["id"]
    if is_admin(user_param):
        new_userid = append_usertype(new_userid,"ADM")
    else:
        new_userid = append_usertype(new_userid,"USR")

    user_param["id"] = new_userid
    return user_param

#-----------------------------------------

user = {
    "name": "John",
    "id": 100,
    "admin": False
}
print(user)
print(regenerate_userid(user))


```