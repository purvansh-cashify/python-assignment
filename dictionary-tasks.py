'''
Tasks given under dictionary section in the assignment
'''

# Converting two lists into dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {}

for i, j in zip(keys, values):
    dict1[i] = j

print("Converting lists to dictionary -")
print(dict1, "\n")

# merging two python dictionaries

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 3, "e": 2, "f": 1}

dict3 = dict1 | dict2
print("Merging two dictionaries -")
print(dict3, "\n")

# Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print("Print the value of key history - ")
print(sampleDict['class']['student']['marks']['history'], "\n")

# initialise dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict1 = dict.fromkeys(employees, defaults)

print("Initialise dictionary with default values - ")
print(dict1, "\n")

# create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]
dict1 = {}

for i in sample_dict:
    if i in keys:
        dict1[i] = sample_dict[i]

print("Creating dictionary by extracting keys from given dictionary -")
print(dict1, "\n")

# delete a list of keys
