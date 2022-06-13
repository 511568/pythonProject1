filepath = '/Users/abinbin/Desktop/源代码文件/chapter_10/pi_million_digits.txt'

with open(filepath) as file_object:
    lines = file_object.readline()

print(lines)

filename = '/Users/abinbin/Desktop/InPythonyoucan.txt'
with open(filename) as LP:
    contents = LP.readlines()
for i in range(3):
    print(f"\n{contents}")
filename = '/Users/abinbin/Desktop/InPythonyoucan.txt'
with open(filename) as LP:
    contents = LP.readlines()
for content in contents:
    print(f"{content}")
    print('\n')
