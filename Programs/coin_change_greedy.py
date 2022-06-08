def index_of_coin(curr_amount,coins):
    
    index=None
    for i in range(len(coins)):
        if(coins[i]<=curr_amount):
            index=i
            break
    return index
        

def coin_change(coins,amount):
    #sort coins in descending order
    coins.sort(reverse=True)
   
    ans=[]
    can_form=True
    while(amount!=0):
        index=index_of_coin(amount,coins)
        if(index==None):
            can_form=False
            break
        ans.append(coins[index])
        amount-=coins[index]
        
    if(can_form):
        print("The selected coins are: ",ans)
    else:
        print("Amount cannot be formed with the given coins.")
        




if __name__=='__main__':
    n=int(input("Enter number of coins: "))
    print("Enter the coins: ")
    coins=list(map(int,input().split()))
    amount=int(input("Enter the amount to be formed: "))
    # n=8
    # coins=[1,2,5,10,20,50,100,500]
    # amount=93
    coin_change(coins,amount)