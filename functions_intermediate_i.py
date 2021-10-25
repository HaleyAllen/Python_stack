# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Byant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)



# Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(some_list):
    for x in range(0,len(some_list),1):
        print("first_name - " + some_list[x]['first_name']+", "
        +"last_name - " +some_list[x]['last_name'])
iterate_dictionary(students)

# Get Values From a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for x in range(0,len(some_list),1):
        print(some_list[x][key_name])
iterateDictionary2('first_name', students)

# Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict.keys():
        print(len(some_dict[key]), key, some_dict[key])
printInfo(dojo)