#Write a Python program to reverse a word after accepting the input from the user.
#Sample Output:
#Input word: AcadGild
#Output: dilGdacA

x=input('enter a word:')
l=[]
print(x[::-1])
y=x[::-1]
for e in y:
    l.append(e)
z=l[2]
a=l[1]
l[1]=z
l[2]=a
print(l)
print("".join(l))