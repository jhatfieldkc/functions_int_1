#1 update values in dictionaries and lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

#1a
# def update_x(num):
#     x[1][0] = num
#     print(x)

# new_x = update_x(15)

#1b
# def sports_ball(lname):
#     students[0]['last_name'] = lname
#     print(students)

# new_sports=sports_ball('Bryant')

#1c
# def sports_dir(update):
#     sports_directory['soccer'][0] = update
#     print(sports_directory)

# update_dir=sports_dir('Andres')

#1d
# def axis_shift(num):
#     z[0]['y'] = num
#     print(z)

# nex_axis=axis_shift(30)

#2
# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def iterateDictionary(list):
#     for x in list:
#         print(x)

# roll_call= iterateDictionary(students)

#3
# def iterateDictionary2(key_name, list_name):
#     for x in list_name:
#         print(x[key_name])

# roll_call2=iterateDictionary2('first_name',students)

#4
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(dict):
#     for x in dict:
#         print(len(dict[x]), x, *dojo[x])

# get_info=printInfo(dojo)