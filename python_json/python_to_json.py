import json

pythonDictionary={'name':'Bob','age':44,'isEmployed':True}

#consider the output as the data representation of the object (Dictionary)
dictionaryToJson=json.dumps(pythonDictionary)

print(dictionaryToJson)


"""
it is important to note at this point that JSON cannot store all types of Python
objects, but only the following types: Lists; Dictionaries; Booleans; Numbers;
Character strings; and None. Thus, any other types need to be converted in order to be stored in JSON
"""

#we have the following class:
class Employee(object):
    def __init__(self,name):
        self.name=name
        
#Let's say that we created a new object abder
abder=Employee('Abder')        

#Now we plan to convert this object to JSON
def jsonDefault(object):
    return object.__dict__

#Then encode the object into JSON 
jsonAbder=json.dumps(abder,default=jsonDefault)    

#print the translated data
print(jsonAbder)