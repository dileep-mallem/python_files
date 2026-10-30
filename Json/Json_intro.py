# JSon : javaScript Object Notation is independent lang , text foramt for exchanging structederd Data .# A
# API's , congfig Files , DB's , logs , ML pipelines Use it 
#  It grew popular in web APIs because it is compact and maps naturally to objects and arrays.
# XML remains useful for document-heavy and enterprise ecosystems; JSON did not eliminate XML.

# JSOn vs Python dict syntax 
# A dict is an in-memory Python object; JSON is text
# JSON values are object, array, string, number, true, false, or null
# . Object keys and strings use double quotes; arrays use []; objects use {}; no comments or trailing commas
#  Single quotes, Python None/True/False, sets, tuples, and undefined are not JSON syntax. 
# Nested objects and arrays can be combined.

# dict↔object↔dict; list↔array↔list; str↔string↔str; int/float↔number↔int/float;
# bool↔true/false↔bool; None↔null↔None  Tuples serialize as arrays and return as lists
#  Sets, datetime, UUID, Decimal, NumPy arrays, and custom objects require deliberate conversion or a custom encoder
# Avoid relying on non-string dict-key coercion.

import json 
value={"tuple":(1,2),"enabled":True,"missing":None}
text=json.dumps(value)
print(json.loads(text)) # {'tuple': [1, 2], 'enabled': True, 'missing': None} Tuple becomes list 

# Which are valid JSON: {"x":1}, {'x':1}, [1,2,], true, None?
# Valid: {"x":1} and true. Single quotes, trailing commas, and Python None are invalid.

# Why can a tuple serialize but a set fails by default?
# The standard encoder treats tuples as arrays. A set has no default mapping; convert it intentionally, such as to a sorted list.

# Represent a person with name, tags, and two addresses.
# {"name":"Asha","tags":["python","ml"],"addresses":[{"city":"Kadapa","kind":"home"},{"city":"Hyderabad","kind":"college"}]}

# JSON (JavaScript Object Notation) is a text-based format used to store and exchange data. 
# Think of it as a universal language for data: it allows different programming languages (like Python, JavaScript, and Java) 
# to easily talk to one another because it uses a clean, human-readable structure of keys and values