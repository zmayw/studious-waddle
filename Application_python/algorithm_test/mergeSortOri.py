#coding=utf-8
import runTime
#callInfo1 = runTime.CallingInfo('mylog1')




#合并闭区间[l...mid]和闭区间[mid...r]的数据
#@callInfo1.info
#@runTime.info
def merge(arr,l,mid,r):
    aux = []
    aux = arr[l:(r+1)]
    i=l
    j=mid+1
    for k in range(l,r+1):
        if(i>mid):
            arr[k]=aux[j-l]
            j=j+1
        elif(j>r):
            arr[k]=aux[i-l]
            i=i+1
        elif(aux[i-l]>aux[j-l]):
            arr[k]=aux[j-l]
            j=j+1
        else:
            arr[k]=aux[i-l]
            i=i+1



#处理[l...r],闭区间
#@callInfo1.info
#@runTime.info
def __mergeSort(arr,l,r):
    if(l>=r):
        return
    mid=l+(r-l)/2
    __mergeSort(arr,l,mid)
    __mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)


#@callInfo1.info
#@runTime.info
def mergeSort(arr):
    n = len(arr)
    __mergeSort(arr,0,n-1)

#a=[9,7,8,3,4,5,2,6,5,1]
#a=[9,7,8,3,4,2,6,5,1]
# a=[10,9,8,7,2,4,2,3,4,3,1]
# mergeSort(a)
# print a
