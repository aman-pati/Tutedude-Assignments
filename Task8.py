# program to write and append data to a file

# writing data to output.txt
data = input("Enter some text: ")
f = open("output.txt", "w")
f.write(data + "\n")
f.close()

# appending more data
extra = input("Enter more text to append: ")
f = open("output.txt", "a")
f.write(extra + "\n")
f.close()

# reading the final content
f = open("output.txt", "r")
print("Final file content:")
print(f.read())
f.close()
