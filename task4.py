# 1.
try:
    with open("sample.txt", "r") as  x:
        content = x.read()
        print(content)
except FileNotFoundError as err:
    print("Sorry this file does not exists.")
    
# 2.
data = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(data + "\n")

extra_data = input("Enter some text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(extra_data + "\n")

print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
