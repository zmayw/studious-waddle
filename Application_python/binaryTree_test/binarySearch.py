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


arr = [1,2,3,4,5,6,7,8]
l1 = binarySearch(arr,1)
n = len(arr)
l2 = binarySearchRe(arr,0,n-1,8)
print l1
print l2