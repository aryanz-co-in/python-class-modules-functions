# SpecialOperation class which will perform special operations
class SpecialOperation:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    # concate number is a method inside SpecialOperation class
    # to perform concatenation of two inputs. (Input can be of any type)
    def concatnumber(self):
        return f"{self.val1}{self.val2}"

    def split(self, splitchar):
        return self.concatnumber().split(splitchar)