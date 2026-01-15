nums =[3, 6, 9, 12]
print(nums[0], nums[3])

colours =["Blue","Black", "Red"]
colours.append("Pink")
print(colours)

fruits = ["apple", "banana", "cherry"]

pos = -1
for i in range(len(fruits)):
    if fruits[i] == "banana":
        pos = 1
if pos != -1:
    fruits[pos] = "orange"

print(fruits)


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = []

list3.extend(list1)
list3.extend(list2)

print(list3)

list1[1] = 99
list1[2] = 100
list1.remove(5)
print(list1)

list3.pop()
list3.pop()
print(list3)

