def knapsack(s_items,s_values,s_weights,M,n):
    curr_p=curr_w=0
    selected=[]
    for i in range(n):
        if(curr_w+s_weights[i]<=M):
            curr_p+=s_values[i]
            curr_w+=s_weights[i]
            selected.append(s_items[i])
        else:
            fract=(M-curr_w)/s_weights[i]
            curr_p+=s_values[i]*fract
            curr_w+=s_weights[i]*fract
            selected.append([round(fract,2),"part of ",s_items[i]])
            break
    
    print(selected,curr_p)

if __name__ == '__main__':
    n=int(input("Enter number of items: "))
    items=[i for i in range(0,n)]
    M=int(input("Enter the max capacity of the knapsack: "))
    print("Enter the values/profits of items: ")
    values=list(map(int,input().split()))
    print("Enter the weights of items: ")
    weights=list(map(int,input().split()))
    print(values,weights)
    
    
    
    ratio=[]
    for i in range(n):
        r=values[i]/weights[i]
        ratio.append(r)
    print(ratio)
    temp=sorted(zip(ratio,items,values,weights),reverse=True)
    s_ratio,s_items,s_values,s_weights=list(zip(*temp))
    print(s_values,s_weights,s_ratio,s_items)
    knapsack(s_items,s_values,s_weights,M,n)