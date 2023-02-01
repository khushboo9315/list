'''  1. Create an array that stores the names of the four houses in your school in any order.  '''

# a=int(input())
# n=[]
# i=0
# while i<a:
#     b=input()
#     n.append(b)
#     i+=1
# print(n)

'''  2. Create an array that accepts the number of the planet from the user and prints the
name of the planet.'''


# a=9
# i=0
# x=[]
# while i <a:
#     b=input()
#     x.append(b)
#     i+=1
# print(x)
# n=int(input())
# j=0
# while j<a:
#     if (n-1)==j:
#         print(x[j])
#     j+=1

##2nd##


    
'''    3. Print the odd-numbered elements i.e. 1st 3rd 5th(Using loops) in the given list

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]'''

# a=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# b=len(a)
# i=1
# while i<=b:
#     if i%2!=0:
#         print(a[i-1],end=",")
#     i+=1


##2##

#a[1::2]


'''    4. Create an array that stores the first 10 even numbers.   '''

# n=10
# i=1
# x=[]
# while i<=n*2:
#     if i%2==0:
#         x.append(i)
#     i+=1
# print(x)

##2##

# a=[2*i for i in range(1,11)]
# print(a)


'''    5. Create an array that accepts four numbers from the user and stores them in the array. '''

# a=4
# i=1
# x=[]
# while i<=a:
#     b=int(input())
#     x.append(b)
#     i+=1
# print(x)


'''   6. Write a flowchart and a program to find an element(accepted from the user) in any array
and print YES or NO.  '''


# a=int(input())
# i=0
# x=[]
# while i<a:
#     b=int(input())
#     x.append(b)
#     i+=1
# print(x)
# n=int(input())
# j=0
# while j<a:
#     if x[j]==n:
#         print("yes")
#         break
#     j+=1
# else:
#      print("no")



'''   Write a flowchart and a program to find the smallest element in an array accepted from
the user.  '''


# a=int(input())
# b=0
# x=[]
# while b<a:
#     n=int(input())
#     x.append(n)
#     b+=1
# print(x)
# i=0
# min=i
# while i<a:
#     if x[i]<x[min]:
#         min=i
#     i+=1
# print(x[min])


'''    8. Write a flowchart and a program to find the frequency of an element (input from the
user) in an array.
'''

# a=int(input())
# b=0
# x=[]
# while b<a:
#     n=int(input())
#     x.append(n)
#     b+=1
# print(x)
# num=int(input())
# f=0
# i=0
# while i<a:
#     if x[i]==num:
#         f+=1
#     i+=1
# print("freq. of ",num,"is =",f)


'''   . In the given list, find out how many times 3 or more consecutive heads (H) or tails
appears.
['T', 'H', 'T', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'T',
'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'H', 'H',
'H', 'T', 'T', 'H', 'H', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T',
'T', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'H', 'T',
'H', 'T', 'H']  '''


a=['T', 'H', 'T', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'T',
'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'H', 'H',
'H', 'T', 'T', 'H', 'H', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T',
'T', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'H', 'T',
'H', 'T', 'H']


# c=0
# c1=0
# h=0
# h1=0
# for i in range(len(a)):
#     if a[i]=="T" :
#         h=0
#         c+=1
#         if c==3:
#             c1+=1
#     else:
#         c=0
#     if a[i]=="H":
#         h+=1
#         if h==3:
#             h1+=1
# print(c1)
# print(h1)


'''    10. Write a program to fill a 4 X 4 array - using all 1s    '''

# a=4
# l=[]
# x=1
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         l2.append(x)
#     l.append(l2)
# print(l)

##2##
# a=[[1]*4]*4
# print(a)

'''   11. Write a program to fill a 4 X 4 array - using 1 to 16   '''

# a=4
# l=[]
# x=1
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         l2.append(x)
#         x+=1
#     l.append(l2)
# print(l)


'''   12. Write a program to fill a 4 X 4 array - using the user's input   '''

# a=4
# l=[]
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         x=int(input("enter: "))
#         l2.append(x)
#     l.append(l2)
# print(l)

'''13. Print value of the elements in the 2nd row, and 3rd column in an above-initialized array'''
# sum_r=0
# sum_c=0
# a=4
# l=[]
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         x=int(input("enter: "))
#         l2.append(x)
#     l.append(l2)
# print(l)
# x1=[]
# x2=[]
# for k in range(a):
#     for m in range(a):
#         if k==1:
#             x1.append(l2[m])
#         if m==2:
#             x2.append(l2[m])
# print(x1)
# print(x2)

##2##
# a=[[1]*4]*4
# for i in range(4):
#     print(a[1][i])
#     print[i][2]



'''14. Print the value of the elements in the m row, n column in an already initialized array,
where m and n are given by the user.'''

# sum_r=0
# sum_c=0
# a=4
# l=[]
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         x=int(input("enter: "))
#         l2.append(x)
#     l.append(l2)
# print(l)
# x1=[]
# x2=[]
# z=int(input())
# y=int(input())
# for k in range(a):
#     for m in range(a):
#         if k==z-1:
#             x1.append(l2[m])
#         if m==y-1:
#             x2.append(l2[m])
# print(x1)
# print(x2)


'''Print all the elements in the 2nd row in an already initialized array'''


# a=4
# l=[]
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         x=int(input("enter: "))
#         l2.append(x)
#     l.append(l2)
# print(l)
# for m in range(a):
#     print(l[1][m],end=",")


'''   16. Print all the elements in the 3rd row in an already initialized array   '''

# a=4
# l=[]
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         x=int(input("enter: "))
#         l2.append(x)
#     l.append(l2)
# print(l)
# for m in range(a):
#     print(l[2][m])

'''   17. Print all the elements in the nth row in an already initialized array - n given by the user    '''

# a=4
# l=[]
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         x=int(input("enter: "))
#         l2.append(x)
#     l.append(l2)
# print(l)
# n=int(input())
# for m in range(a):
#     print(l[n][m])


'''    18. Ask them to print all the elements in the mth column in an already initialized array - m
given by the user
    '''


# a=4
# l=[]
# for i in range(a):
#     l2=[]
#     for j in range(a):
#         x=int(input("enter: "))
#         l2.append(x)
#     l.append(l2)
# print(l)
# n=int(input())
# for m in range(a):
#     print(l[m][n])




'''  19. Say you have a list of lists where each value in the inner lists is a one-character string,
like this:
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn
with text characters. The (0, 0) origin is in the upper-left corner, the x-coordinates
increase going right, and the y-coordinates increase going down.
Copy the previous grid value, and write code that uses it to print the image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

'''

# grid = [['.', '.', '.', '.', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['.', 'O', 'O', 'O', 'O', 'O'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.']]


# g=len(grid)
# g1=len(grid[0])
# for i in range(g1):
#     for j in range(g):
#         print(grid[j][i],end=" ")
#     print()



'''      20. Take the input from the user and print the following pattern according to the input.
For example for n = 3 print the following pattern
1 2 3
8 9 4
7 6 5
For n = 4 print the following pattern
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7     '''


# a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# n=len(a)
# top=0
# bottom=n-1
# left=0
# right=n-1
# dir=0
# while (top<=bottom) and (left<=right):
#     if dir==0:
#         for i in range(left,right+1):
#             print(a[top][i])
#         top+=1
#     elif dir==1:
#         for i in range(top,bottom+1):
#             print(a[i][right])
#         right-=1
#     elif dir==2:
#         for i in range(right,left-1,-1):
#             print(a[bottom][i])
#         bottom-=1
#     elif dir==3:
#         for i in range(bottom,top-1,-1):
#             print(a[i][left])
#         left+=1
#     dir=(dir+1)%4


a=1
# n=len(a)
top=0
bottom=4-1
left=0
right=4-1
dir=0
d = [[ 0 for x in range (4)] for y in range(4)]
print(d)
while (top<=bottom) and (left<=right):
    if dir==0:
        for i in range(left,right+1):
            # print(a[top][i])
            d[top][i]=a
            a+=1
        top+=1
    elif dir==1:
        for i in range(top,bottom+1):
            # print(a[i][right])
            # d.append(a[i][right])
            d[i][right]=a
            a+=1
        right-=1
    elif dir==2:
        for i in range(right,left-1,-1):
            # print(a[bottom][i])
            # d.append(a[bottom][i])
            d[bottom][i]=a
            a+=1
        bottom-=1
    elif dir==3:
        for i in range(bottom,top-1,-1):
            # print(a[i][left])
            # d.append(a[i][left])
            d[i][left]=a
            a+=1
        left+=1
    dir=(dir+1)%4
[print(i) for i in d]

