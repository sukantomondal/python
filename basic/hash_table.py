dic = {"Apple": 1,"Orange": 2, "Grape": 3 , "Pears": 4}

print(dic)

if("Apple" in dic):
    dic["Apple"] +=1

print(dic)
print(dic.keys())

if("Apple" in dic.keys()):
    print("Apple is there")

print(dic.values())



#set is also a hash table and only difference between dictionary is, it does not contain value


set = {"Apple", "Orange", "Mango", "Pears", "Grape"}

if("Pears" in set):
    print("It is in the set")

set.add("Somthing")

print(set)



