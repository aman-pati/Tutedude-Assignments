# program to read a file and handle errors

try:
    f = open("sample.txt", "r")
    for line in f:
        print(line.strip())
    f.close()
except FileNotFoundError:
    print("File not found")
