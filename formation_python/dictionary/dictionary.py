#Access to Value by Key
dictionary = {1 : 'ALOOOOOOOO', 2 : 'MOOOOOTOOOO'}
print(dictionary[2])

#add key value in dictionary
dic2 = {}
dic2[1] = 'is int ?'
dic2['key'] = 2
print(dic2)

#Delete
dic3 = {'Mobby' : 'Dixxx-Chenay-Reevers', 'Elvis' : 'pressing'}
print(dic3)

get_deleted_value = dic3.pop('Elvis')
print("Deleted value is: ", get_deleted_value)

#Verify existing key
if 'Elvis' in dic3.keys():
    print('Braaaaa-Braaaa')
else:
    print('Blop blop blop...')

#explore key and value
for key in dic2.keys():
    print(key)

for value in dic2.values():
    print(value)

for key, value in dic3.items():
    print("This is the key -> " + key , " |--| This is the value -> " + value)

#Args in func return kind of dictionary
def show_args(**args):
    print(args)

show_args(c='v', d=2)