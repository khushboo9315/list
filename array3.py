'''      

A = [ 2,4,1
8,0,-1
1,-4,0]
B = [ 8, 0, 3
2,-5 , 7
3, -1,5]

1. Write a Python Program to add two matrices and store them in a separate matrix.    '''
# A = [[2,4,1],[8,0,-1],[1,-4,0]]
# B = [[8, 0, 3],[2,-5 ,7],[3,-1,5]]

# a=len(A)
# s=[]
# for i in range(len(A)):
#     k=[]
#     for j in range(len(B[i])):
#             k.append([A[i][j]+B[i][j]])
#     s.append(k)
# print(s)


'''    2. Write a program to subtract two matrices and store them in a separate matrix.    '''

# l=[]
# for i in range(len(A)):
#     l1=[]
#     for j in range(len(A[i])):
#             l1.append([A[i][j]-B[i][j]])
#     l.append(l1)
# print(l)

'''    3. Write a program to multiply two matrices and store the result in a separate matrix.    '''

# A = [[2,4,1],[8,0,-1],[1,-4,0]]
# B = [[8, 0, 3],[2,-5 ,7],[3,-1,5]]
# # A=[[1,2,3],[4,5,6]]
# # B=[[10,11],[20,21],[30,31]]
# a=[]
# for i in range(len(A)):
#     b=[]
#     for j in range(len(B[0])):
#         sum=0
#         for k in range(len(A[0])):
#             sum+=A[i][k]*B[k][j]
#         b.append(sum)
#     a.append(b)                                                   
# print(a)

'''       4. Write a Python program to transpose matrix A. Store the result in a separate matrix.       '''

# A = [[2,4,1],[8,0,-1],[1,-4,0]]
# a=len(A)
# d=[[0 for m in range(a)] for n in range(a)]
# for i in range(a):
#     for j in range(a):
#         d[i][j]=A[j][i]    
# print(d)


'''     5. Write a program that prompts for a phone number of 10 digits and two dashes, with
dashes after the area code and the next three numbers. For example, 017-555-1212 is a
legal input.     '''


# a=input()
# if a[3]=="-" and a[7]=="-":
#     print("valid")
# else:
#     print("no")






'''      6. Write a program that rotates the elements of a list so that the elements at the first index
moves to the second and element at the second index move to the third and so on. The
last element moves at the first index.     '''

# A=[1,2,3,4,5,6,7]
# B=[0]*len(A)
# for i in range(len(A)):
#     b=((len(A)-1)+i)%len(A)
#     B[i]=A[b]
# print(B)

'''     7. Write a Program to check whether a given matrix is an identity matrix or not.      '''

# n=True
# A=[[1,0,0],[4,1,0],[0,0,1]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         if i==j and A[i][j!=1]:
#             n=False
#         if i!=j and A[i][j]!=0:
#             n=False
# if n==True:
#     print("valid")
# else:
#     print("not")



'''     8. Write a Program to find whether the given matrix is diagonal or not.     '''

# n=True
# A=[[1,0,0],[0,1,0],[0,0,1]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         if i==j and A[i][j]<=0:
#             n=False
#         if i!=j and A[i][j]!=0:
#             n=False
# if n==True:
#     print("valid")
# else:
#     print("not")

'''    9. Write a Program to find the sum of all diagonal elements of a matrix.    '''

# A=[[1,2,3],[6,7,8],[10,11,12]]
# sum=0
# sum1=0
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         if i==j:
#             sum+=A[i][j]
#         if i+j==len(A[0])-1:
#             sum1+=A[i][j]
# print(sum)
# print(sum1)
'''    10. Write a Program to find the maximum element in the matrix.    '''
# A=[[1,2,30,4],[5,6,73,8],[98,10,11,12]]
# max=0
# max1=0
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         if A[i][j]>max:
#             max=A[i][j]
# print(max1)

'''    11. Write a Program to find the minimum element in the matrix.     '''

# A=[[9,2,30,4],[5,6,73,8],[98,10,11,12]]
# min=A[0][0]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         if A[i][j]<min:
#             min=A[i][j]
# print(min)

'''     12. Write a Program to find the position of an element in a 2d array or Matrix.    '''
# a=[[1,2,3,4],[1,2,3,4,5],[3,7,8,9]]
# b=int(input())
# c=1
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i==1:
#             if a[i][j]==b:
#                 print("yes",j)
#                 break
           



"""     symmetric matrix     """
# A=[[8,2,3],[0,-5,-1],[3,7,5]]
# n=False
# a=len(A)
# d=[[0 for m in range(a)] for n in range(a)]
# print(d)
# for i in range(a):
#     for j in range(a):
#         d[i][j]=A[j][i]    
# print(d)
# for x in range(a):
#     if A[i]==d[i]:
#         n=True
# if n==True:
#     print("yes")
# else:
#     print("no")
    
"""    screw - symmetric matrix      """
# A=[[0,1,-2],[-1,0,3],[2,-3,0]]
# n=False
# a=len(A)
# d=[[0 for m in range(a)] for n in range(a)]
# print(d)
# for i in range(a):
#     for j in range(a):
#         d[i][j]=A[j][i]*(-1)    
# print(d)
# for x in range(a):
#     if A[i]==d[i]:
#         n=True
# if n==True:
#     print("yes")
# else:
#     print("no")

# A=[[1,2],[4,6],[9,1],[3,2]]
# B=[[3,2,4],[6,1,5]]
# a=[]
# for i in range(len(A)):
#     b=[]
#     for j in range(len(B[0])):
#         sum=0
#         for k in range(len(A[0])):
#             sum+=A[i][k]*B[k][j]
#         b.append(sum)
#     a.append(b)

            

        