import types
def left(e):
  return e[0]
def op(e):
  return e[1]
def right(e):
  return e[2]
def isInside(v,e):
    if v == e:
        return True
    elif type(e) == tuple:
        if isInside(v,left(e)) or isInside(v,right(e)):
            return True
        else:
            return False
    else:
        return False
def solve(v,q):
    if isInside(v,left(q))==True:
        return solving(v,q)
    else:
        q2=(right(q),op(q),left(q))
        return solving(v,q2)
#tests if the operation is +,-,*,/, or =
def solving(v,q):
    if v == q[0]:
        return q
    else:
        x=left(q)
        if op(x) == '+':
           return solvingAdd(v,q)
        if op(x) == '-':
            return solvingSub(v,q)
        if op(x)=='*':
            return solvingMult(v,q)
        if op(x)=='/':
            return solvingDiv(v,q)
        if op(q)=='=':
            return solvingEqual(v,q)
#solves is second index of q is +
def solvingAdd(v,q):
    x=left(q)
    if left(x)==v:
        y=(right(q),'-',right(x))
        q2=(v,'=',y)
        return solving(v,q2)
    else:
        y=(right(q),'-',left(x))
        q2=(v,'=',y)
        return solving(v,q2)
#solves is second index of q is -
def solvingSub(v,q):
    x=left(q)
    if left(x)==v:
        y=(right(q),'+',right(x))
        q2=(v,'=',y)
        return solving(v,q2)
    else:
        y=(left(x),'-',right(q))
        q2=(v,'=',y)
        return solving(v,q2)
#solves is second index of q is *
def solvingMult(v,q):
    x=left(q)
    if left(x)==v:
        y=(right(q),'/',right(x))
        q2=(v,'=',y)
        return solving(v,q2)
    else:
        y=(right(q),'/',left(x))
        q2 = (v, '=', y)
        return solving(v, q2)
#solves is second index of q is /
def solvingDiv(v,q):
    x=left(q)
    if v == right(x):
        y=(left(x),'/',right(q))
        q2=(v,'=',y)
        return solving(v,q2)
    else:
        y=(right(q),'*',right(x))
        q2=(v,'=',y)
        return solving(v,q2)
#solves is second index of q is =
def solvingEqual(v,q):
    x=right(q)
    y=left(q)
    z=left(x)
    l=right(x)
    m=left(l)
    if v==right(z):
       # p=(y,'-',right(x))
        #o=((y,'-',right(x)),'/',left(z))
        q2=(v,'=',((y,'-',right(x)),'/',left(z)))
        return solving(v,q2)
    else:
        i=(left(q),'/',left(x))
        u=(i,'+',right(l))
        t=(u,'*',right(m))
        q2=(v,'=',t)
        return solving(v,q2)
print(isInside('x','x'))
print(isInside('x','y'))
print(isInside('x',('x','+','y')))
print(isInside('x',('a','+','b')))
print(isInside('+',('a','+','b')))
print(isInside('x',(('m','*','x'),'+','b')))

print(solve('x', (('a', '+', 'x'), '=', 'c')))
print(solve('x', (('x', '+', 'b'), '=', 'c')))
print(solve('x', (('a', '-', 'x'), '=', 'c')))
print(solve('x', (('x', '-', 'b'), '=', 'c')))
print(solve('x', (('a', '*', 'x'), '=', 'c')))
print(solve('x', (('x', '*', 'b'), '=', 'c')))
print(solve('x', (('a', '/', 'x'), '=', 'c')))
print(solve('x', (('x', '/', 'b'), '=', 'c')))
print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))