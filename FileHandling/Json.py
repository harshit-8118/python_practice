import json


# with open("FileHandling/jsonFile.json", "r") as file:
#     x = json.load(file)
#     for i in x.keys():
#         print(i, ":", x[i])
        

with open("FileHandling/jsonFile.json", "r") as file:
    strr = file.read()
    print(strr)
    d = json.loads(strr)
    print(type(d))


string = json.dumps(d)
print(string)
print(type(string))
with open("FileHandling/jsonFile2.json", "w") as file:
    json.dump(d, file)

