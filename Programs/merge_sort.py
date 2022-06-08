def merge_sort(arr):
    if(len(arr)<=1):
        return
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge_list(left,right,arr) 
    
def merge_list(a,b,arr):
    len_a=len(a)   
    len_b=len(b)
    
    l=r=k=0
    
    while( l<len_a and r< len_b):
        if(a[l]<=b[r]):
            arr[k]=a[l]
            l+=1
        else:
            arr[k]=b[r]
            r+=1
        k+=1
        
    while (l<len_a):
        arr[k]=a[l]
        l+=1
        k+=1
    
    while (r<len_b):
        arr[k]=b[r]
        r+=1
        k+=1       
        
print("Enter the array")
arr=list(map(int,input().split()))
print("The entered array is:")
print(arr)
merge_sort(arr)
print("The sorted array using merge_list sort is:")
print(arr)