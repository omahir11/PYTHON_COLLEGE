# h. Implement a function that demonstrates both *args and kwargs usage.

def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, name="Om", age=18)