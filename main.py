## code for generating the fibanocii series till 8th term

a = 0
b = 1

## printing first two values

print(a)
print(b)

## generating sequence from 2 to 8 and adding with previous terms to generate fibanocci series and prints the output.

for i in range(2,8):
  c = a + b
  a = b
  b = c
  print(c)
