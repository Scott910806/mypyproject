def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        replay = input(prompt)
        if replay in {'y', 'ye', 'yes'}:
            return True
        if replay in {'n', 'no', 'nop', 'nope'}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response!')
        
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

def f(ham:str, eggs:str = 'eggs') -> str:
    print("Annotations:" , f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

if __name__ == '__main__':
    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
    print(my_function.__doc__)
    f('spam')