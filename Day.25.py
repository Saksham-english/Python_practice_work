# wap to create to lists and generate a dictionary with keys from list1 and list2 . 
Dict = {}
list1 = ["a","b","c"]
list2 = [1 ,2 ,3]      # zip make pairs .
Dict = dict(zip(list1,list2))
print(Dict)    # dict convert them into dictionary .
