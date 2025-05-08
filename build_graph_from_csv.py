import csv
from collections import defaultdict

def build_graph_from_csv(file_path):
    graph = defaultdict(list)

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            source = row["source"]
            destination = row["destination"]
            time = int(row["time_minutes"])
            graph[source].append((destination, time))

    return dict(graph)  # Convert back to normal dict if you want

# Example usage
graph = build_graph_from_csv("routes.csv")

print("Generated Graph from CSV:")
for node in graph:
    print(f"{node} -> {graph[node]}")
