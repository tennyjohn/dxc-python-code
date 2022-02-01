## code for generating the fibanocii series till 8th term

a = 0
b = 1
print(a)
print(b)
for i in range(2,8):
  c = a + b
  a = b
  b = c
  print(c)
