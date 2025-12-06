list1 = ["carrace"]
list2 = ["racecar"]

copy_list1 = list1.copy()
list1.reverse()
if(copy_list1 == list1):
    print("palindrome")

else:
    print("not")