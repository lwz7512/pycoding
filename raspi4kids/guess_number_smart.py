# Guess Number smart version
# by robin
# @2019/09/09

# Iterative Binary Search Function 
# It returns location of x in given array arr if present, 
# else returns -1 
def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)/2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1

# Test array 
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 10
  
# Function call 
# result = binarySearch(arr, 0, len(arr)-1, x) 
  
# if result != -1: 
#     print "Element is present at index %d" % result 
# else: 
#     print "Element is not present in array"

numbers = range(1, 11) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
location = 0
right_loc= len(numbers)-1 # 9
x = 0

while location <= right_loc: 
  
  mid = location + (right_loc - location)/2
  # print "location: " + str(location)
  str_mid = str(numbers[mid])
  answer = raw_input("your number More than "+ str_mid + "? - yes or no?")
  while answer != "yes" and answer != "no":
    answer = raw_input("your number More than "+ str_mid + "? - yes or no?")

  if answer == "yes":
    if len(numbers[location:right_loc])<=2:
      x = numbers[right_loc]
      break
    location = mid + 1
  else:
    if len(numbers[location:right_loc])<=2:
      x = numbers[location]
      break
    right_loc = mid

  print numbers[location:right_loc]
  
print "you number is: " + str(x)