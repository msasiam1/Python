#Variables value can be assigned in many ways

#type1
d=1
print(d)

#type2 (multiple value assigned)
e,f,g=3,4,5
print(e)
print(f)
print(g)

#type 3 (same value in different variable)
x=y=z=14

print(x)
print(y)
print(z)

#multiple variable print

print(x,y,z)

#string and number variable print

m="Hello This is"
n=12
print(m,n)

#global variable

v=14

def my():
    print(v)

my()

#local variable

def my2():
    t="This is local variable"
    print(t)
my2()

#global vs local variable testing

k="This is Global"

def testing():
    k="This is Local"
    print(k)

testing()
print(k)

#global keyword

def testkeyword():
    global r #must be declare first then assign
    r="Hi This Variable is Now Global"
    print(r)

testkeyword()