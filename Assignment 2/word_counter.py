with open("python.txt", "r") as file:
    text = file.read()


count = text.count("Python")

print("The number of times 'Python' occurred is:", count)