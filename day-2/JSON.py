
import json

x = {
  "name": "warner",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("india","candy"),
  "pets": None,
  "cars": [
    {"model": "BMW ", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert python into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
---------json2------
import json

# JSON to python:
x = '{ "name":"warner", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
