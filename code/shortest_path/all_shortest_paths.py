""""
    return one shortest path
"""

# import ipdb

neighboring_cities = [[1, 3, 4],  # neighbors of 0
                      [0, 2, 3],  # neighbors of 1
                      [1, 5],	  # neighbors of 2
                      [0, 1, 5],  # neighbors of 3
                      [0],		  # neighbors of 4
                      [2, 3]]	  # neighbors of 5


shortest_paths = [[] for i in range(6)]
shortest_paths[0] = [[0]]


for step in range(1, 6):
    print('---\nstep : ' + str(step) + '\n---')
    for city in range(1, 6):
        if shortest_paths[city] == []:
            for neighbor in neighboring_cities[city]:
                c = shortest_paths[neighbor]
                if c != [] and len(c[0]) == step:
                    print(f"city : {city}")
                    print(f"neighbor : {neighbor}")
                    print(f"path to neighbor : {c}")
                    print(f"build one shortest path to {city}")
                    for x in c:
                        new_shortest_path = x + [city]
                        shortest_paths[city].append(new_shortest_path)
                        print('add : ')
                        print(new_shortest_path)


def print_shortest_paths(destination):
    print("the shortest paths to " + str(destination) + " are :")
    print(shortest_paths[destination])


print_shortest_paths(1)
print_shortest_paths(2)
print_shortest_paths(3)
print_shortest_paths(4)
print_shortest_paths(5)
