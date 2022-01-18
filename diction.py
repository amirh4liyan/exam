import json

with open("input.txt", "r") as f:
    content = f.read()
 
      
js = json.loads(content)
 
print(js)
