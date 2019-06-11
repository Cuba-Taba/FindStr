
import sys

print("Number of arguments: ", len(sys.argv))
print("This is the name of the script: ", sys.argv[0])
print("The arguments are: " , str(sys.argv))

if (len(sys.argv) < 3):
    exit("arguments not found")

str1 = sys.argv[2]
str2 = sys.argv[1]

if (str1.find(str2) >= 0):
    print("строка нашлась")
    exit(0)
elif (str2.find(str1) >= 0):
    print("строка нашлась")
    exit(0)
elif str1==str2:
    print("строка нашлась")
    exit(0)
else:
    print("строка не нашлась")
    exit(1)