## code for generating the fibanocii series till 8th term.


## declares two variables 'a' and 'b' and assigns 0 and 1 to them.

a = 0
b = 1

## printing first values of a and b.

print(a)
print(b)

## generating sequence from 2 to 8.

for i in range(2,8):

## declares a new variable 'c' and assign the sum of 'a' and 'b' to 'c'.

  c = a + b

## swapping the values
## assigning previous value of 'b' to 'a' and 'c' to 'b' and prints the value of 'c'.

  a = b
  b = c

  print(c)
  
  
  
