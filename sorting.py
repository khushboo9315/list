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
