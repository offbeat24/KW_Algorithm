
graph = {0: [1, 2, 3], 1: [4], 2: [4, 5], 3: [], 4:[6], 5:[1], 6: []}

def topology_sort(graph):
    N = len(graph)
    stack = []
    visited = [False for _ in range(N)]

    for i in graph:
        if visited[i] == False:
            dfs(i, stack, visited)
    
    answer = []
    while len(stack) != 0:
        answer.append(stack.pop())
    print("Output : ", answer)

def dfs(v, stack, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0: dfs(i, stack, visited)
    stack.append(v)
topology_sort(graph)