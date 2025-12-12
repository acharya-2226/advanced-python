# Variable and input
# 1
my_age = 20
print("My age is", my_age)

# 2
food = input("Enter your favourite food: ")
print("Your favourite food is", food)

# Type conversion
# 3
num_str = "42"
num = int(num_str)
print("The number is", num)
print(type(num))

# 4
float_num = 3.14159
str_num = str(float_num)
print("The string number is", str_num)
print(type(str_num))

# Strings
# 5 Concatenation
a = "Hello"
b = "World!"
c = a + " " + b
print(c)

# 6 String indexing
s = "Python"
print(s[2])

# 7 Print first five words
sentence = input("Enter a sentence: ")
words = sentence.split()
first_five = " ".join(words[:5])
print(first_five)
