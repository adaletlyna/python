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

# Update the values
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30
def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ""
        for key in dictionary:
            output += f"{key} - {dictionary[key]}, "
        print(output[:-2])  # remove last comma and space

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'lyna', 'last_name': 'adalet'},
    {'first_name': 'iheb', 'last_name': 'adalet'}
]

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
        print()  

        
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
