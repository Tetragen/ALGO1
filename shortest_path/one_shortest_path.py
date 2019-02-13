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


one_shortest_path = [None] * 6
one_shortest_path[0] = [0]


for step in range(1, 6):
    print('---\nstep : ' + str(step) + '\n---')
    for city in range(1, 6):
        if one_shortest_path[city] is None:
            for neighbor in neighboring_cities[city]:
                c = one_shortest_path[neighbor]
                if c is not None and len(c) == step:
                    print('city : ' + str(city))
                    print('neighbor : ' + str(neighbor))
                    print('path to neighbor : ' + str(c))
                    print('build one shortest path to ' + str(city) + ' : ')
                    one_shortest_path[city] = c + [city]
                    print(one_shortest_path[city])


def print_one_shortest_path(destination):
    print('one shortest path to ' + str(destination) + ' is :')
    print(one_shortest_path[destination])


print_one_shortest_path(1)
print_one_shortest_path(2)
print_one_shortest_path(3)
print_one_shortest_path(4)
print_one_shortest_path(5)
