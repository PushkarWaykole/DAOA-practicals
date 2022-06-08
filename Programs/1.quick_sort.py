
#taking first element as pivot
def partition2(arr,left,right):
    i=left+1
    j=right
    pivot=arr[left]
    while(i<j):
        while(i<right and arr[i]<pivot):
            i+=1
        while(j>left and arr[j]>=pivot):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    if(arr[j]<pivot):
        arr[j],arr[left]=arr[left],arr[j]
    
    return j  

#Taking last element as pivot
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while(i<j):
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    if(arr[i]>pivot):                
        arr[i],arr[right]=arr[right],arr[i]
    
    return i


def quicksort(arr,left,right):
    
    if(left<right):
        index=partition(arr,left,right)
        
        quicksort(arr,left,index-1)
        quicksort(arr,index+1,right)
        



if __name__=="__main__":
    arr=[5,4,3,4,1]
    print(arr)
    quicksort(arr,0,len(arr)-1)
    print(arr)
    
    
      