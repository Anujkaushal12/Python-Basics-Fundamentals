import os
from datetime import datetime

# print(dir(os))

# print(os.getcwd()) #current working directory

# os.chdir()

# print(os.listdir())

# filename="24_datetime_module.py"
# currentworkingdir=os.getcwd()
# print(os.path.join(currentworkingdir,filename))

# with open(filename, "w") as f:
#     f.write("File created using the os module and open().")

# print(os.mkdir("dirname"))
# print(os.makedirs("dirname"))

# print(os.rmdir("dirname"))
# print(os.removedirs("dirname"))

# print(os.rename("from","to"))

# print(os.stat("24_datetime_module.py"))

# print(os.stat("24_datetime_module.py").st_atime)

# modify_time=os.stat("24_datetime_module.py").st_atime
# print(datetime.fromtimestamp(modify_time))

# for dirpath,dirnames,filename in os.walk("/Users/anuj/Python-Basics-Fundamentals/"):
#     print("Current path",dirpath)
#     print("Directories",dirnames)
#     print("Files:",filename)

# print(os.environ.get("PYTHON-BASICS-FUNDAMENTALS"))

# file_path=os.path.join(os.environ.get("PYTHON-BASICS-FUNDAMENTALS"),"file.txt")
# print(file_path)


file_path=os.path.basename("/users/test.txt")
print(file_path)
file_path=os.path.dirname("/users/test.txt")
print(file_path)
file_path=os.path.split("/users/test.txt")
print(file_path)
file_path=os.path.splitext("/users/test.txt")
print(file_path)
