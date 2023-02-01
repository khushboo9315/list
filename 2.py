'''1. Take an array from the user as input and reverse it before printing it to the user. '''
# a=int(input())
# b=[None]*a
# c=[None]*a
# n=0
# while n<a:
#    x=int(input())
#    b[n]=x
#    n+=1
# print(b)
# i=a-1
# j=0
# while i>=0:
#     c[j]=b[i]
#     i-=1
#     j+=1
# print(c)

############################################################
'''' 2. Take an array from the user as input and print the mean, median, and mode of the array 
  '''
# n=int(input())
# a=[None]*n
# print(a)
# b=0
# while b<n:
#     x=int(input())
#         a[b]=x
#     b+=1
# print(a)
# # N=0
# # c=0
# # sum=0
# # while N<n:
# #     c+=1
# #     sum+=a[N]
# #     N+=1
# # mean=sum//n
# # print(mean)
# i=0
# while i<n:
#     min=i
#     j=i
#     while j<n:
#         if a[j]<a[min]:
#             min=j
#         j+=1
#     a[min],a[i]=a[i],a[min]
#     i+=1
# print(a)

# c=n//2
# if n%2==0:
#     median=(a[c-1]+a[c])/2
# else:
#     median=(a[c])
# print(median)

# mode=0
# for m in range(n):
#     x=0
#     for k in range(m+1,n):
#         if a[m]==a[k]:
#             x+=1
#     if x>0:
#         mode=a[m]
# print(mode)

#################################################################

'''ques:3  Print the elements of an array of size N, in a rotated manner with a gap of K. Eg, let us
say the array is - 3, 6, 7, 5, 10. And the value of k = 3. The output should be - 7, 3, 10, 6,
5. If k = 2, the output should be - 6, 5, 3 10, 7  '''

# a=int(input())
# n=[None]*a
# n2=[None]*a
# k=int(input())
# i=0
# while i<a:
#     b=int(input())
#     n[i]=b
#     i+=1
# print(n)
# n2 = [0]*a
# t=0
# j=0
# c=0
# while t<a:
#     if n[j]!="a":
#         c+=1
#     # elif c<k:
#     #     c+=1
#     if c==k:
#         n2[t]=n[j]
#         n[j]="a"
#         c=0
#         t+=1
#     j=(j+1)%a
# print(n2)

####################################################

'''4. Take an array from the user as input and find duplicate elements in an array.  '''

# n=int(input())
# a=[None]*n
# x=0
# while x<n:
#     y=int(input())
#     a[x]=y
#     x+=1
# print(a)
# b=[]
# i=0
# while i<n:
#     c=0
#     if a[i]=="a":
#         i+=1
#         continue
#     j=i+1
#     while j<n:
#         if a[i]==a[j]:
#             a[j]="a"
#             c+=1
#             # j+=1
#         # else:
#         #     c+=1
#         #     continue
#         j+=1
#     if c>0:
#         b.append(a[i])
#         c=0
#     i+=1
# print(b)


################################################################

'''5. Take two sorted arrays from the user as input and Merge them into a single sorted array   '''

# n=int(input())
# arr1=[None]*n
# a=0
# while a<n:
#     b=int(input())
#     arr1[a]=b
#     a+=1
# print(arr1)

# k=0
# while k<n:
#     min=k
#     k1=k
#     while k1<n:
#         if arr1[k1]<arr1[min]:
#             min=k1
#         k1+=1
#     arr1[min],arr1[k]=arr1[k],arr1[min]
#     k+=1
# print(arr1)


# N=int(input())
# arr2=[None]*N
# i=0
# while i<N:
#     x=int(input())
#     arr2[i]=x
#     i+=1
# print(arr2)

# K=0
# while K<N:
#     min1=K
#     K1=K
#     while K1<N:
#         if arr2[K1]<arr2[min1]:
#             min1=K1
#         K1+=1
#     arr2[min1],arr2[K]=arr2[K],arr2[min1]
#     K+=1
# print(arr2)

# n=5
# N=6
# arr1=[1,3,7,9,10]
# arr2=[2,3,3,5,8,9]
# arr=[None]*(n+N)
# m=0
# m1=0
# x1=0
# while m<n and m1<N:
#     if (arr1[m]<arr2[m1]):
#         arr[x1]=arr1[m]
#         m+=1
#         x1+=1
#     else:
#         arr[x1]=arr2[m1]
#         m1+=1
#         x1+=1
# while m<n:
#     arr[x1]=arr1[m]
#     m+=1
#     x1+=1
# while m1<N:
#     arr[x1]=arr2[m1]
#     m1+=1
#     x1+=1
# print(arr)


##############################################################
'''
6. Given an unsorted array of size N that contains only non-negative integers, find a
contiguous subarray which adds to a given number S. In case of multiple subarrays,
return the subarray which comes first on moving from left to right. Eg, let us say the array
is - 3, 6, 7, 5, 10. And the value of S = 12. The output should be - 7 ,5 '''

# a=int(input())
# n=int(input())
# x=[None]*a
# i=0
# while i<a:
#     b=int(input())
#     x[i]=b
#     i+=1
# print(x)
# j=0
# c=0
# while j<a:
#     k=j+1
#     # c=0
#     while k<a:
#         if x[j]+x[k]==n:
#             print(x[j],x[k])
#             c+=1
#         k+=1
#     if c==1:
#         i=n
#         break
#     j+=1


'''  7. Find the Union and Intersection of the two sorted arrays  '''

# a=[1,2,2,3,4]
# a1=len(a)
# insertion=[]
# b=[3,3,4,5,6]
# b1=len(b)
# union=[]
# m=0
# n=0
# while m<a1 and n<b1:
#     if a[m]<b[n]:
#         union.append(a[m])
#         m+=1
#     elif a[m]>b[n]:
#         union.append(b[n])
#         n+=1
#     elif a[m]==b[n]:
#         union.append(a[m])
#         insertion.append(a[m])
#         m+=1
#         n+=1
# while m<a1:
#     union.append(a[m])
#     m+=1 
# while n<b1:
#     union.append(b[n])
#     n+=1
# print(union)
# print(insertion)

########################################################

'''  8. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
median of the two sorted arrays.'''


    
# n=int(input())
# arr1=[None]*n
# a=0
# while a<n:
#     b=int(input())
#     arr1[a]=b
#     a+=1
# print(arr1)

# k=0
# while k<n:
#     min=k
#     k1=k
#     while k1<n:
#         if arr1[k1]<arr1[min]:
#             min=k1
#         k1+=1
#     arr1[min],arr1[k]=arr1[k],arr1[min]
#     k+=1
# print(arr1)


# N=int(input())
# arr2=[None]*N
# i=0
# while i<N:
#     x=int(input())
#     arr2[i]=x
#     i+=1
# print(arr2)

# K=0
# while K<N:
#     min1=K
#     K1=K
#     while K1<N:
#         if arr2[K1]<arr2[min1]:
#             min1=K1
#         K1+=1
#     arr2[min1],arr2[K]=arr2[K],arr2[min1]
#     K+=1
# print(arr2)


# arr=[None]*(n+N)
# m=0
# m1=0
# x1=0
# while m<n and m1<N:
#     if (arr1[m]<arr2[m1]):
#         arr[x1]=arr1[m]
#         m+=1
#         x1+=1
#     else:
#         arr[x1]=arr2[m1]
#         m1+=1
#         x1+=1
# while m<n:
#     arr[x1]=arr1[m]
#     m+=1
#     x1+=1
# while m1<N:
#     arr[x1]=arr2[m1]
#     m1+=1
#     x1+=1
# print(arr)
# if (n+N)%2!=0:
#    median=arr[((n+N)//2)]
# else:
#     median=(arr[((n+N)//2)-1]+arr[((n+N)//2)])//2
# print(median)

#########################################################

'''Take a sorted array from the user as input and find a number using Binary Search the array '''

# a=int(input())
# n=int(input())
# i=0
# l=[None]*a
# while i<a:
#     b=int(input())
#     l[i]=b
#     i+=1
# j=0
# low=j
# up=a-1
# mid=(low+up)//2
# while low<up:
#     if n==l[mid]:
#         print("found",l[mid])
#     else:
#         if n<l[mid]:
#           up=mid-1
#         else:
#             low=mid+1
#     low+=1
# print("found",l[mid],mid)
        


'''selection sort  '''

# n=int(input())
# a=[None]*n
# print(a)
# b=0
# while b<n:
#     c=0
#     x=int(input())
#     while c<=b:
#         a[b]=x
#         c+=1
#     b+=1
# print(a)
# i=0
# while i<n:
#     min=i
#     j=i
#     while j<n:
#         if a[j]<a[min]:
#             min=j
#         j+=1
#     a[min],a[i]=a[i],a[min]
#     i+=1
# print(a)

# ###################################################################




    ###############################################################
    




"""   bubble sort   """
# a=[9,1,50,1000,0,2,-5]
# n=len(a)
# for i in range(b):
#     c=0
#     for j in range(b-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#             c+=1
#     if c==0:
#         break
# print(a)
"""    selection sort    """
# i=0
# while i<n:
#     min=i
#     j=i+1
#     while j<n:
#         if a[j]<a[min]:
#             min=j
#         j+=1
#     a[min],a[i]=a[i],a[min]
#     i+=1
# print(a)

"""    insertion sort   """
# for i in range(1,n):
#     for j in range(i,0,-1):
#         if a[j]<a[j-1]:
#             a[j],a[j-1]=a[j-1],a[j]
# print(a)


