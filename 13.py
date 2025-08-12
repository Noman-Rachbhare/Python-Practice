# dictionary
person={
    "name":"Noman",
    "age":23,
    "gender":"male",
    "list":[1,3,4,]
}

# print(person,type(person));
print(person.items());
print(person.keys());

print(person.values()); 
person.update({"age":24})
print(person);

# newdic=__dict__.fromkeys(person,0);
# print(newdic)  error
