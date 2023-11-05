class graph:
    
    def __init__(self) :
        self.graph={}

    def add_edge(self,vertex,edge):
        if vertex not in self.graph:
            self.graph[vertex]=[]
        self.graph[vertex].append(edge)

    def bfs(self,start_vertex):
        visited=set()
        queue=[]
        visited.add(start_vertex)
        queue.append(start_vertex)

        while queue:
            vertex=queue.pop(0)
            print(vertex,end=" ")

            for n in self.graph.get(vertex,[]):
                if n not in visited:
                    visited.add(n)
                    queue.append(n)

    def dfs(self, start_vertex):
        visited=set()

        def dfs_recursive(vertex):
            visited.add(vertex)
            print(vertex,end=" ")

            for n in self.graph.get(vertex,[]):
                if n not in visited:
                    dfs_recursive(n)

        dfs_recursive(start_vertex)
        print()
g=graph()

while True:
    vertex=input("Enter the vertex or -1 when done ")
    if vertex=='-1':
        break
    else:
        edge=input("Enter the edge for vertex "+vertex+" ")
    
    g.add_edge(vertex,edge)

# print("Graph:")
# for vertex, edge in g.graph.items():
#   print(f"{vertex}: {edge}")

print("BFS")
start_vertex=input("Enter the starting vertex : ")
g.dfs(start_vertex)
