
def kmt(txt,pat):
    
    #generating the pie table
    pie=[0 for _  in range(len(pat))]
    
    for i in range(1,len(pat)):
        repeated=False
        for j in range(1,i):
            if pat[i]==pat[j]:
                pie[i]=j
                repeated=True
        if not repeated:
            pie[i]=0
    print(pie)
    
    i=1
    j=0
    while(i<=len(txt) and j<=len(pat)-1):
        if j==len(pat)-1:
            print(f"Pattern found at index {i-j}")
            j=0
            i+=1
        
        elif pat[j+1]==txt[i]:
            j+=1
            i+=1
        else:
            if j==0:
                i+=1
            else:
                j=pie[j]
                



if __name__=='__main__':
    # txt=input("Enter the text: ")
    txt="abababababcaaabc"
    txt='_'+txt
    # pat=input("Enter the pat: ")
    pat="ab"
    pat='_'+pat
    print(pat,txt)
    kmt(txt,pat)
    