#sos means sum so far initally 0
#asf means the subset so far

#youtube link https://www.youtube.com/watch?v=91aMq7HxJB4
def printSubsets(arr,index,asf,sos,target):
    
    #if the sos is > target return
    if(sos>target):
        return

    #if the index is at the last element  that means we have tried all the elements ,if sos is equal to target print the subset 
    if(index==len(arr)):
        if(sos==target):
            print(asf+" .")
            return
        return
    
    #If we include the number at the index in the subset
    printSubsets(arr,index+1,asf+str(arr[index])+" ",sos+arr[index],target)
    
    #if we dont include the number at the index in the subset
    printSubsets(arr,index+1,asf,sos,target)




if __name__=='__main__':
    arr = [10,20,30,40,50]
    target=60
    print("The subsets are: ")
    printSubsets(arr,0,"",0,target)