#!python3

def test(a):
    print(f"a is {a}")
    a = a-1
    return a



a = 2
b = test(a)
print(a,b)