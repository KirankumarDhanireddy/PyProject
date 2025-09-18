''' 
# 1. volume of sphere
def vol(rad):
    return (rad**3)*(4/3)*3.14

print(vol(2))

'''
'''
# 2. number in given range
def num(no,low,high):
    return no in range(low,high)
    # if low < no < high:
      #   print(f"{no} is in betwween {low} and {high}")
    # else:
      #   print(f"{no} is not in the range")

num(11,1,9)
'''

'''
# 3. unique list
def unique_list(lst):
    x = []
    for i in lst:
        if i not in x:
            x.append(i)
    return x
        

unique_list([1,1,1,2,2,2,3,4,5])
'''


# 4. multiply all in a list
def multiply(num):
    for i in num:
        return i*i+1
        continue
    
print(multiply([1,2,2,3,3,3,4,8]))

'''
# palindrome
def palindrome(str):
    n = 0
    m = n+1
    for i in str:
      if str[n] == str[-m]:
          print("given word is a palindrome!")
      else:
          print("given word is not a palindrome")
        
palindrome('kiran')

'''

