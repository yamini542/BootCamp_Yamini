import heapq

def dijkstra(graph, start):
    # Priority queue: (distance, node)
    queue = [(0, start)]
    # Track shortest distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Track path taken
    previous = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous

# Sample Graph (Node: [(Neighbor, Travel Time)])
graph = {
    'Warehouse': [('A', 2), ('B', 5)],
    'A': [('B', 1), ('Customer', 7)],
    'B': [('Customer', 3)],
    'Customer': []
}

distances, previous = dijkstra(graph, 'Warehouse')

print("Minimum time from Warehouse to each node:")
for node in distances:
    print(f"{node}: {distances[node]} mins")

# Optional: Print shortest path to Customer
def get_path(previous, end):
    path = []
    while end:
        path.append(end)
        end = previous[end]
    return path[::-1]

print("\nShortest path to Customer:")
print(" ➡️  ".join(get_path(previous, 'Customer')))
