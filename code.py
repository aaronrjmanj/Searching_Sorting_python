#Linear Search

def liner_search(arr,ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            print(i)
            return i
        else:
            return -1


#Binary Search

def binary_search(arr,ele):
    lower=0
    upper=(len(arr))
    print("Searching element =",ele)
    while (lower<=upper):
        mid=(upper+lower)//2
        if(arr[mid]==ele):
            globals()['pos'] = mid
            #print(mid)
            return True
        else:
            if arr[mid]<ele:
                lower = mid
            else:
                upper = mid
    return False

#bubble sort

def b_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
pos = -1

arr=[2,5,8,10,21,85,48,50,65,6,15,100]#should be sorted
print(arr)
ele = 100
b_sort(arr)
print("New Array sorted using bubble sorting \n",arr)


'''
out=liner_search(arr,ele)
if(out): print("Linear Search: Found")
else: print("NOT FOUND")
'''
if binary_search(arr,ele):
    print("Binary Search: Found at",pos +1)
else: print("Not Found")
