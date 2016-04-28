class Parent(object):
    x = 1

class ChildOne(Parent):
    pass

class ChildTwo(Parent):
    pass

print Parent.x, ChildOne.x, ChildTwo.x

ChildOne.x = 2

print Parent.x, ChildOne.x, ChildTwo.x

Parent.x = 3

print Parent.x, ChildOne.x, ChildTwo.x
