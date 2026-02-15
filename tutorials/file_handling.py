import os
import json

text={
    "name": "Ravi Ranjan",
    "age": 21,
    "isStudent":"yes"
}
path="output.json"

try:
    with open(path,"w") as file:
        json.dump(text,file,indent=4)   ## file.write(data)
        print("File written succesfully")
except Exception:
    print("File cannot be written/created")

finally:
    pass
