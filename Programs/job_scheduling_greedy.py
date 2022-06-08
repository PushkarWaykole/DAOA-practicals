
# def job_schedule(n,profits,deadlines):
#     jobs=[i for i in range(n)]
#     temp=sorted(zip(profits,jobs,deadlines),reverse=True)
#     s_profits,s_jobs,s_deadlines=list(zip(*temp))
#     print(s_profits,s_jobs,s_deadlines)
#     gantt=[0 for _ in range(max(s_deadlines))]
    
#     for i in range(n):
#         currdead=s_deadlines[i]-1
#         print(currdead)
#         while(gantt[currdead]!=0 and currdead>0):
#             currdead-=1
#         print(currdead)
        
#         gantt[currdead]=s_jobs[i]
    
#     print(gantt)
            
        
        


# if __name__=='__main__':
#     # n=int(input("Enter the number of jobs: "))
#     # print("Enter the profits of the jobs: ")
#     # profits=list(map(int,input().split()))
#     # print("Enter the deadlines of the jobs: ")
#     # deadlines=list(map(int,input().split()))
#     n=6
#     profits=[200,180,190,300,120,100]
#     deadlines=[5,3,3,2,4,2]

    
#     job_schedule(n,profits,deadlines)
    
    
max_deadline = 0
P = 0 # profit set to zero initially

# input jobs from the user

# n = int(input("Enter number of jobs: "))
# jobs = []

# for i in range(n):
#     d = int(input(f"Enter deadline of job {i+1}: "))
#     p = int(input(f"Enter profit of job {i+1}: "))
#     print("\n")
#     # sort by value
#     jobs.append( [i+1, d, p] )

#     if d > max_deadline:
#         max_deadline = d


n = 6
jobs = [[1,5,200],
        [2,3,180],
        [3,3,190],
        [4,2,300],
        [5,4,120],
        [6,2,100]]

max_deadline = 5       

# sort by profit
jobs.sort(reverse=True,key=lambda x:x[2])
print(*jobs, sep="\n")

# setting gant chart
gant = [0 for _ in range(max_deadline+1)]
gant[0] = 1 # setting first index as 1 because we donot want to use this position

for i in range(n):
    placed = False
    deadline = jobs[i][1]
    if gant[deadline] == 0:
        gant[deadline] = 1
        P += jobs[i][2]
        print(f"placed job {jobs[i][0]} with deadline {deadline} and profit {jobs[i][2]}")
        placed = True

    else:
        while deadline != 0 and gant[deadline] != 0: 
            deadline-=1

        if gant[deadline] == 0:
            gant[deadline] = 1
            P += jobs[i][2]
            print(f"placed job {jobs[i][0]} with deadline {jobs[i][1]} and profit {jobs[i][2]}")
            placed = True

    if not placed:
        print(f"Cannot place job {jobs[i][0]} with deadline {jobs[i][1]}")

print("Gant Chart: ",gant)  
print(f"Max profit: {P}")