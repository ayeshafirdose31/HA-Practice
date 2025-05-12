"""Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6  to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints
1<

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird."""

"""IF N IS ODD= WEIRD
N IS EVEN 
CASE1= N IS EVEN WHEN RANGE BETYWEEN 2-5 (NOT WEIRD)
CASE2= N IS EVEN 6-20( WEIRD )
Case 3= N IS EVEN AND GREATER THAN 20 NOT weird 
"""
    
n=int(input("Enter the number").strip())

# if n%2!=0:
#     print("Weird")
# elif n in range(2,6):
#     print("Not Weird")
# elif n in range(6,21):
#     print("Weird")
# else:
#     print("Not weird ") Here the test case on Hacckerrank failed since "w" should be in capital 



if n%2!=0:
    print("Weird")
elif n%2==0:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    else:
        print("Not weird ")
    