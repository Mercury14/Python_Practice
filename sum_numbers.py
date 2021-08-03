# Finger exercise - total floats in a string

s = '1.23, 2.4, 3.123'
total = 0.0

new_s = s.split(", ")

for x in new_s:
  total = total + float(x)
print(total)