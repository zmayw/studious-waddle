#coding=utf-8

#二分查找法，在有序数组arr中，查找target
#如果找到target，在返回相应的索引index
#如果没有找到target,返回-1

def binarySearch(arr,target):
    # 在arr[l..r]之中查找target
    n = len(arr)
    l = 0
    r = n-1
    while(l<=r):
        mid = l+(r-l)/2
        if(arr[mid] == target):
            return mid
        if target < arr[mid]:
            r = mid-1
        else:
            l = mid +1

    return -1


#递归法实现二分查找法
def binarySearchRe(arr,l,r,target):
    mid = l+(r-l)/2
    targetIndex=-1
    if l <= r:
        if target==arr[mid]:
            targetIndex = mid
        elif target<arr[mid]:
            targetIndex = binarySearchRe(arr,l,mid-1,target)
        else:
            targetIndex = binarySearchRe(arr,mid+1,r,target)
    return targetIndex

#二分查找法，在有序数组arr中，查找target
#如果找到target，且该值有多个，则返回最小的索引
#如果没找到返回信比target小的最大值的索引index，如果这个值有多个，返回最大索引
#如果这个target比整个数组的最小元素值还小，则返回-1
def floor(arr,target):
    n = len(arr)
    l = 0
    r = n-1
    while ( l <= r ) :
        mid = l+(r-l)/2
        if (arr[mid]==target):
            while(mid>0 and arr[mid-1]==target):
                mid = mid -1
            return mid
        elif(arr[mid]>target):
            r = mid - 1
        elif(arr[mid]<target):
            l = mid + 1
    if r < 0:
        return -1
    return r

#二分查找法，在有序数组arr中，查找target
#如果找到target，则有多个，则返回最大的索引
#如果没找到，则返回比target大的最小值的索引index，如果这个值有多个，返回最小的索引
#如果这个target比整个数组的最大元素值还大，则返回-1
def ceil(arr,target):
    n = len(arr)
    l = 0
    r = n-1
    while ( l <= r ) :
        mid = l+(r-l)/2
        if (arr[mid]==target):
            while(mid < (n-1) and arr[mid+1]==target):
                mid = mid + 1
            return mid
        elif(arr[mid]>target):
            r = mid - 1
        elif(arr[mid]<target):
            l = mid + 1
    if (l > n -1):
        return -1
    return l

#arr = [1,1,1,1,2,3,4,5,6,7,8]
#arr = [1,2,3,4,4,5,5,5,6,7,8,9,10]
arr = [1,1,2,3,4,6,6,6,8,8,8,8,9,10,10]
# l1 = binarySearch(arr,1)
# n = len(arr)
# l2 = binarySearchRe(arr,0,n-1,8)
# print l1
# print l2

print "floor....."
l3 = floor(arr,7)
print l3

print "ceil....."
l4 = ceil(arr,10)
print l4
print arr[l4]