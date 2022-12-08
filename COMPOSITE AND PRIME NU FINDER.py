'''In this project you have to enter a positive integer range [A, B] and system will find out the
status (Prime or composite) of each number available in the given range. At the end print the
count also.
Note: Make use of efficient approach to check prime status of the number.
For example:
Range is (7,10)
Then the status of each number in the range is:
7 is prime
8 is composite or not prime
9 is composite
10 is composite
Count: 1 prime and 3 composite numbers in the range.'''

print("\nWelcome :)\n")
print("_______________________________")
x=int(input("\n>>>Enter the lower limit⏬: "))
y=int(input(">>>Enter the upper limit⏫: "))
print("_______________________________\n")
s=0
g=0
if x>y:
    c=input("\nThe lower limit cannot be more than the upper limit\nIf you wish to interchange the values type 'Yes' else 'No': ").lower()
    print()
    if c=="yes":
    	temp=y
    	y=x
    	x=temp
for i in range(x,y+1):
        a=i
        c=0
        for j in range(2,a):
            if a%j==0:
                c=1
                s+=1
                print(f"{a} is Composite.")
                break
        if c==0:
            print(f"{a} is Prime.")
            g+=1
if c=="no":
	pass
else:
	print(f"\nThere are total of {g} prime numbers, and {s} composite numbers in the given range.")
