# Find the cube root of a perfect cube

x = int(input('Enter an integer: '))
for ans in range(0, abs(x)+1):
  # for loop iterates until it either reaches the int or ans if higher than integer
  if ans**3 >= abs(x):
    break

# if its not equal to the int
if ans**3 != abs(x):
  print(x, 'is not a perfect cube')
else:
  if x < 0:
    # if input was negative, change to negative
    ans = -ans
  
  print('Cube root of ', x, 'is', ans)