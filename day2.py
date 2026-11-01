#remove duplicates while preserving the order
#TASK A

def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
    print(remove_duplicates([12,34,12,45]))  


#maximum sum of any contiguous window of size
#TASK B

def max_window_sum(numbers,k):
    if k <= 0 or k > len(numbers):
        return None

    window_sum = sum(numbers[:k])   
    max_sum = window_sum

    for right in range(k,len(numbers)):
        windows_sum += numbers[right] - numbers[right - k]  

        max_sum = max(max_sum ,window_sum)
        

    return max_sum
numbers = [2, 1, 5, 1, 3, 2]
k = 3

print(max_window_sum(numbers, k))
 


#TASK C

nums=[10,18,17,19,102]
target = 19
for num in nums:
    if num == target:
        print("found")
else:
   
   print("not found")    

# the reason is the else block belongs to if inside  the loop so it prints not found for every number that is not 19,the loop checks every number and if the numver is not target it prints not found till we get the target element it prints not found and after we get the target element it prints the target element.and it prints not found for next iterations,so to overcome this we have to do else block of a Python for loop runs only when the loop finishes without encountering a break


#TASK D


#list it maintains a insertion order
#set it removes duplicates 
#dict it stores values in key value pairs here the key must be unique


#example for list
#storing product details
products =["mobile","charger","headphones"]
print(products)

#example for set

student_id = {11,12,13}

new_id = 12
if new_id in student_id:
    print("id already registerd")
else:
    student_id.add(new_id)
    print("Registration successful")


#example for dict
#storing user info

employee ={"name":"abhishek","age":21,"country":"india"}
print(employee["name"])

