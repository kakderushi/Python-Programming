'''
Hybrid aslo known as MRO 
MRP represents how properties (attributes methods ) are searched in inheritance
Rule of MRO:
1) Python first search in child class and then goes to parent class
2) Priority is to child class
3)MRO follows depth first left to right approach
'''
class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B,C):
    pass
class Y(B,C):
    pass
class P(X,Y):
    pass

print(P.mro())