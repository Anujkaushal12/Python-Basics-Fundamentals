try:
    f=open("file.txt")
    if f.name == "file.txt":
        raise Exception

# except FileNotFoundError as e:
#     print(e)

except Exception:
    print("Sorry! file not found")
else:
    print(f.read())
    f.close()

finally:
    print("Program completed")
