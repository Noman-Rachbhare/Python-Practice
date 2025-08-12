# List in Python

bike=["burgman","Splender","Herohonda","Activa","Suzuki"];

# Simple Print List
print(bike);
# How to acces List Elements

print(bike[2]);

# change Element
bike[3]="HFDLX";
print(bike)

# list Methods
# Append  it is used to add Element in List at end

bike.append("TVS");
print(bike);

# insert Method it is ued to add at Element At Specific Position
# insert(i, x) Syntax

bike.insert(3,"Latestbike");
print(bike)

# Remove Method it is used to remove element from list
bike.remove("TVS");
print(bike)

# Pop Method is used to delet the Elment from List
bike.pop(3);
print(bike)

# Sort Method is used to Sort the List
bike.sort()
print(bike);

# Display elment from a particular Postion to another Postion
print(bike[1:3]);