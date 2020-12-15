#Assignment Day 3
#Q.2 Write a function which can return of factorial of a any number given in the argument as INT
def factorial(a):
  fact = 1
  for p in range(a,0,-1):
    fact=fact*p
    return fact

n = int(input("Enter any number"))
result = factorial(n)
print("factorial of",n,"is",result)
