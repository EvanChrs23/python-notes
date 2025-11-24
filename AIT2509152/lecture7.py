print(set("abac"))
print(set([x for x in range(2)]))

s1 = {1,2,4}
s2 = {1,4,5,2,6}
state = s1.issubset(s2)
state2 = s2.issuperset(s1) #superset is the opposite of subset
print(state)
print(state2)

s1 = {1,2,4}
s2 = {1,4,2}
l1 = list(s1)
l2 = list(s2)
t1 = tuple(s1)
t2 = tuple(s2)
print(s1 == s2)
print(l1 == l2,int(l1 == l2))
print(t1 == t2,str(t1 == t2))

s1 = {1,2,4}
s2 = {1,3,5}
print(s1.union(s2))
print(s1 | s2)
print(s1.intersection(s2))
print(s1&s2)
print(s1.difference(s2))
print(s1 - s2)
print(s1.symmetric_difference(s2))
print(s1^s2)

students = {"111":"John",
            "222":"Jamal"}

print(students)
print(tuple(students.keys()))
print(tuple(students.values()))
print(students["111"])

#{} is for empty dictionary, set() is for empty set

students["333"] = "Smith"

print(students)
for x in range(len(students.values())):
    print(list(students.values())[x],end=" ")
    
print("")

del students["222"]

print(students)
print(len(students))

sigma = {"333":"Smith",
         "111":"John"}

print(students == sigma)

print(students.pop("111"))
print(students)
for x in range(len(students.values())):
    print(list(students.values())[x])

