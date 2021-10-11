## dict#!
keys = ('key1', 'key2', 'key3')
values = ('value1', 'value2', 'value3')
dict_ = dict(zip(keys, values))
# print(dict_)

dict_2 = dict()
index = 0
for key in keys:
    dict_2[key] = values[index]
print(dict_2)

lambda_expr = lambda x, y: {x: y}
#create_dict = lambda_expr(keys, values)
#print(create_dict)

create_dict = map(lambda_expr, keys, values)
print(list(create_dict))



def oblik():
    