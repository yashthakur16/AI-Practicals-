def dijk(graph,start):

    vertices=int(len(graph))
    visited=[False]*vertices
    dist=[float('inf')]*vertices
    dist[start]=0

    for _ in range(vertices):
        min_dist=float('inf')
        for v in range(vertices):

            if not visited[v] and dist[v]<min_dist:
                min_dist=dist[v]
                u=v
                
            visited[u]=True

    for v in range(vertices):
        if not visited[v] and graph[u][v]>0:
            if dist[u]+graph[u][v]<dist[v]:
                dist[v]=dist[u]+graph[u][v]

    return dist

n=int(input("Enter the number of vertices : "))
graph=[]
print("Enter the adjacency matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

for i in range (n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()

print()
start=int(input("Enter the starting vertex : "))

shortest=dijk(graph,start)

for i,distance in enumerate(shortest):
    print("vertex {} : {} ".format(i,distance))



