local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

print(__name__)


if __name__=="__main__": #when we import parent from child.py  __name__ is set to "parent" not "__main__" so the if block the print in child.py   
    print(square(5))
    user = User("Anna")
    print(user.name)
    print(user.say_hello())
    print(user.__dict__)




