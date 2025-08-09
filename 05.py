# operator

# Arithmetic  Operator
# +,-,*,/,%

a=2;
b=4;
a+b;
print(a+b);
print(a-b);
print(a*b);
print(a/b);

# Assignment Operator
a=2;
a+=3;
print(a);

b=4;
b-=2;
print(b);

# Comparison operator

a=4;
b=8;

print(b<a);

d= a==b;
print(d);

# Logical Operator

a=10;
b=20;
c=40;

d= a>b and b>c;

e=c>b or b<a;

print(not(True));
print(not(False));


# Ternery Operator
#  syntax value_if_true if condition else value_if_false
age=18;

status="adult" if age>16 else "child"
print(status);

#  Membership Operators

# Check karte hain ki koi value list, string, tuple ya set me present hai ya nahi.
fruits=["apple","mango","banana"]
print("apple" in fruits);
print("watermelon" in fruits);


print("After Membership Operators");
#  Identity Operators
# Check karte hain ki do variables same object ko point karte hain ya nahi.
x=[2,4,5,8]
y=x
z=8,4,6
print( x is y);
print(z is y)

