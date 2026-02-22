import os
from datetime import datetime

print(dir(os))

print(os.getcwd())

# os.chdir()

print(os.listdir())

filename="24_datetime_module.py"
currentworkingdir=os.getcwd()
print(os.path.join(currentworkingdir,filename))

with open(filename, "w") as f:
    f.write("File created using the os module and open().")

# print(os.mkdir("dirname"))
# print(os.makedirs("dirname"))

# print(os.rmdir("dirname"))
# print(os.removedirs("dirname"))

# print(os.rename("from","to"))

# print(os.stat("24_datetime_module.py"))

print(os.stat("24_datetime_module.py").st_atime)

modify_time=os.stat("24_datetime_module.py").st_atime
print(datetime.fromtimestamp(modify_time))