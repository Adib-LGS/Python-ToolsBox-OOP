import copy

list = []

#check empty list
if len(list) == 0:
    list.insert(1, 'element 1')
    list.insert(2, 'alement 2')
    list.append('element 3')
    print(len(list), list)
    if len(list) > 1:
        for i in list:
            print(i)
            print(i.count('element'))

"""----------------------------------------------------------"""


#conver list to sring
list_to_string = ['a', 'b', 'c']
string = " ".join(list_to_string)
print(string)

"""----------------------------------------------------------"""

#copy list using  copy module
list_og = [1]
liest2 = copy.deepcopy(list_og)

liest2.append(2)

print(list_og)
print(liest2)


"""----------------------------------------------------------"""

#add list into list CONCATENATE 2 LIST
list3 = ['test1', 'test2', 'test3']
list4 = ['notest1', 'notest2', 'notest3']
list3.extend(list4)
"""extend() = list3 = list3 + list4"""
print(list3)