list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
num1 = 0
num2 = 0

print("list1 = ", end = " ")
print(list1)
while(num1 < len(list1)):
    if list1[num1] >= 0:
        print(list1[num1], end = " ")
    num1 += 1
print("\n")
print("list2 = ", end = " ")
print(list2)
while(num2 < len(list2)):
    if list2[num2] >= 0:
        print(list2[num2], end = " ")
    num2 += 1
