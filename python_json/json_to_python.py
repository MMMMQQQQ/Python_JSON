# -*- coding: utf-8 -*-

"""
Reading JSON means converting JSON into a Python value(object).
As mentioned above, the json library parses JSON into a dictionary 
or list in Python. In order to do that, we use loads() function (load from a string)
"""
import json
jsonData='{"name":"Frank","age":39}'
jsonToPython=json.loads(jsonData)

# see the output
print(jsonToPython)

##
#comments:
##
"""
the data is returned as a Python dictionary(JSON object data structure)
"""
print(jsonToPython['name'])