# functions.py
def is_user_admin(user):
    return user["admin"]

def append_usertype(old_user_id, user_type):
    return f"{old_user_id}_{user_type}"


def regenerate_userid(user_param):
    new_userid = user_param["id"]
    if is_user_admin(user_param):
        new_userid = append_usertype(new_userid,"ADM")
    else:
        new_userid = append_usertype(new_userid,"USR")

    user_param["id"] = new_userid
    return user_param


user = {
    "name": "John",
    "id": 100,
    "admin": False
}
print(user)
print(regenerate_userid(user))