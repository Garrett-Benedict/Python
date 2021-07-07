x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)


students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{'first_name' : 'John', 'last_name' : 'Rosales'}]
students[0]['last_name'] = 'Bryant'
print(students)


sports_directory = {'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],'soccer' : ['Messi', 'Ronaldo', 'Rooney']}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

print('****************************************')

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ] 
# i = 0
# for i in range(0,5):
#     for key in students[i]:
#         print(students[i][key])


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
iterateDictionary2('first_name', students)
print('************************')
iterateDictionary2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_list):
    for i in some_list:
        print(i)
        info_some = some_list[i]
        for j in info_some:
            print(j)
printInfo(dojo)






# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
