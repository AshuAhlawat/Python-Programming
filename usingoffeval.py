a1,a2=map(int,input().split())
x=a1
print(a2==eval(input()))

# in the above function a1 is the value of x for any polynomial and a2 is the expected result,

# constrain here is all the polynomial will be written in the power of x as P(x) so we can take the value of x from a1 to put it in the equation. 

# the eval operator will automatically put the value of x in the polynomial input

# we are using a boolean output if the value of a2== P(a1(which is the value of x from the line 1 input))

# (line 1 input) 1 4

# (line 3 input) x**3+x**2+x+1

# output 1**3+1**2+1+1=4

# True