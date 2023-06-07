print('created on Windows')
print('Edit from Linux')
print('Edit from Windows')
def isPrime(number):
    if number < 2:
        return False
    for i in (2,number+1):
        if number % i == 0:
            return False
    return True

range1= int(input("Enter the Starting range : "))
range2= int(input("Enter the Ending range : "))
prime = []
for i in range(range1, range2+1):
    if isPrime(i):
        prime.append(i)
if len(prime)<1:
    print("There is no prime numbers between the range ",range1,"and",range2,".")
else:
    print("There are",len(prime),"in given range")



