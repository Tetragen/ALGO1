""""
    Build all the paths from 0
"""

# import ipdb

neighboring_cities = [[1, 3, 4],  # neighbors of 0
                      [0, 2, 3],  # neighbors of 1
                      [1, 5],	  # neighbors of 2
                      [0, 1, 5],  # neighbors of 3
                      [0],		  # neighbors of 4
                      [2, 3]]	  # neighbors of 5

# paths of length 0
# a path will be coded as a list
paths = [[[0]]]

for path_length in range(1, 6):
    print('building paths of length ' + str(path_length))
    # build paths of length + 1
    new_paths = [path + [ngbrs] for path in paths[path_length - 1]
                 for ngbrs in neighboring_cities[path[-1]]]
    # append the paths to the list of paths
    paths.append(new_paths)


print(paths[1])
print(paths[3])
# ipdb.set_trace()
