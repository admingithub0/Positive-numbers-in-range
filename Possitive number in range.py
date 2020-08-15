input_list1,input_list2 =[12,-7,5,64,-14],[12,14,-95,3]
print('Original Values in Input_list1 is :',input_list1)
print('Original vaues in Input_list2 is :',input_list2)
new1= list(filter(lambda x: x>0,input_list1))
print('Positive numbers in list1 :',new1)
new2= list(filter(lambda x: x>0,input_list2))
print('Positive numbers in list2 :',new2)
