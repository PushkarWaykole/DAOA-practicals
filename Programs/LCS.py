def lcs(s1,s2):
    len_a=len(s1)
    len_b=len(s2)
    
    dp=[[0 for _ in range(len_b+1)] for _ in range(len_a+1)]
    print(dp)

    for i in range(len_a+1):
        for j in range(len_b+1):
            
            if(i==0 or j==0):
                dp[i][j]=0
            
            elif(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    print(dp)
    print("The length of longest common substring is: ",dp[len_a][len_b])

    common=[]*dp[len_a][len_b]
    i=len_a
    j=len_b
    while(i>0 and j>0):
        if(s1[i-1]==s2[j-1]):
            common.insert(0,s1[i-1])
            i-=1
            j-=1
        elif (dp[i-1][j]>dp[i-1][j-1]):
            i-=1
        else:
            j-=1
    
    common_str=' '.join(map(str, common))
    if(dp[len_a][len_b]!=0):
        
        print("The longest common subsequence is : ",common_str)
            
        

if __name__=='__main__':
    s1=input("Enter the first string: ")
    s2=input("Enter the second string: ")
    # s1="stone"
    # s2="longest"
    
    lcs(s1,s2)