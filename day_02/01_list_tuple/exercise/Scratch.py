# list1 = [1, 2, 3]
# print (list1 * 4)
#
#
# # item costs
# item_costs = [0] * 10
# print (item_costs)
#
#
# #Sorted Function
# example = [1, 3, 3, 4, 4]
# new_example = sorted(example, reverse=True)
#
# print(new_example)
# print(example)


#Append Function
#
# items = [1, 2, 3, 4]
#
# items.append(5)
# items.remove(5)
# print(items)

# example = [1, 2, 3]
#
# for x in example[:]:
#     example.pop(0)
#     print(example)

# DICTIONARIES - SET DEFINITION

# letters= {'a','b','c','d','e','f','g','h','i'}
# print(letters)

# set1 = {'a','b','c','d'}
# set2 = {'a','b','c','d'}
#
#
# print(set1 | set2)

# student_names = ['a','b','c','d']
# student_scores = [1,2,3,4]
# student_numbers = [1,2,3,4]
#
# student_records = {
#     'a':{'score', 'number'},
#     'b':{'score', 'number'},
#     'c':{'score', 'number'},
#     'd':{'score', 'number'}
# }
#
# for name, info in student_records.items():
#     print(f"Student {name} - Score: {info[0]} - Number: {info[1]}")


# WRITING TEXT FILE (Multiple String)

with open(r"C:\Users\akb_l\PycharmProjects\python-bootcamp\day_02\01_list_tuple\exercise", "r") as file:
    user_input = file.read()
    print(user_input)

