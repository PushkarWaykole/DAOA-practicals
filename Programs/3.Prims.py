# Prim's Algorithm in Python
def prims():
    selected=[]
    INF = 9999999
    # number of vertices in graph
    V=int(input("Enter the number of vertices: "))
    # V = 5
  
    
    print("Enter the rows of the adjacency matrix :")
    #creating graph by adjacency matrix method
    G=[[0 for _ in range(V)] for _ in range(V) ]

    for i in range(V):
        row=list(map(int,input().split()))
        G[i]=row
        
    print(G)
    #selected array to check the vertex has been selected or not
    selected_node = [False]*V 

    #number of edges added in the MST
    no_edge = 0

    #by default select the first vertex
    selected_node[0] = True

    # printing for edge and weight
    print("Edge : Weight\n")
    while (no_edge < V - 1):
        
        minimum = INF
        a = 0 #source
        b = 0 #destination
        
        for v in range(V):
            if selected_node[v]: #if the vertex is selected
                for n in range(V): #n means the nearest neighbour vertices of the selected vertex
                    if ((not selected_node[n]) and G[v][n]):  
                        # if the vertex is not in selected and there is an edge
                        if minimum > G[v][n]:
                            minimum = G[v][n]
                            a = v
                            b = n
        print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
        selected.append([a,b])
        selected_node[b] = True
        no_edge += 1
    print(selected)
        
prims()












    
    

