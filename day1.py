#Task A
#first  non repeating character

def non_repeating():
    freq = {}
    text = "aabcdef"
 
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for char in text:
        if freq[char] == 1: 
            return char
    return None    
print(non_repeating())     





#Task B

# List : list stores multiple values and does allow duplicate values and this is mutable
students =[ 20,330,4665,23432]
print(students)

#tuple : it is almost similar to list but tuple is immutable and is represented in ()

employee = (101,"abhishek",21)
print(employee)


#set : set stores only unique values it doesnt allow duplicates and it doesnt have any particular order

student={1,2,3,1}
print(student)

#dictionary: it stores data in key value pairs here key must always be unique ,dict is mutable

employee ={"name":"abhishek" ,"age":22}
print(employee)



#unique student id
#for storing unique id we have to use set as it doesnt allows duplicates
students={111,112,113,111}
print(students)

#student profile field
# for this i will  use dict as because it stores values in key value pairs and is easy for retrving data and we can access by giving the key name ,key name should always be unique
students={"name":"abhi","age":21,"city":"hyderabad"}
print("student details",students)


