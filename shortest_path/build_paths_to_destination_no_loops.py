""""
    Build some paths arriving to destination 5
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
paths_to_destination, path_length = [], 0

while paths_to_destination == []:
    path_length += 1
    # build paths as before
    new_paths = [path + [ngbrs] for path in paths[path_length - 1]
                 for ngbrs in neighboring_cities[path[-1]]
                 if ngbrs not in path]
    # append the paths to the list of paths as before
    paths.append(new_paths)
    # check is the path goes to the destination
    paths_to_destination = [path for path in paths[path_length]
                            if path[-1] == 5]


print(paths_to_destination)
