'''     ex-1    '''
# file = open("FileHandling/mycode.txt", "r")
# print(file.read())
# file.seek(0)
# print(file.read(6))
# file.close()

'''     ex-2    '''
# file = open("FileHandling/tiger.txt", "w+")
# file.write("Tiger is our national animal.")
# file.seek(0)
# print(file.read())
# file.close()

'''    ex-3    '''
# file = open("FileHandling/mycode.txt", "r")

# line = file.readlines()
# print(line)
# for i in line:
#     print(i, end="")


# line = file.readline()
# while line:
#     print(line, end="")
#     line = file.readline()

# print()
# file.close()

'''    ex-4    '''
# with open("FileHandling/mycode.txt", "r") as file: 
#     print(file.read())
#     file.seek(9)
#     print(file.read())


'''     ex-5    '''
from pathlib import Path

path = Path('FileHandling/mycde.txt')

if path.exists():
    file = open(path, "r")
    print(file.read())
else:
    print("file doesn't exists")

