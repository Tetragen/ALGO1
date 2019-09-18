""""
    Check if there is a path of a certain
    length to arrive to a destination
"""

# import ipdb

neighboring_cities = [[1, 3, 4],  # neighbors of 0
                      [0, 2, 3],  # neighbors of 1
                      [1, 5],	  # neighbors of 2
                      [0, 1, 5],  # neighbors of 3
                      [0],		  # neighbors of 4
                      [2, 3]]	  # neighbors of 5


def exists_path(destination, path_length):
    if path_length == 0:
        exists = (destination == 0)
    else:
        exists = any(exists_path(i, path_length - 1) for i in neighboring_cities[destination])
    if exists:
        print(f"destination {destination}, length {path_length}")
    return exists


def test_existence(destination, path_length):
    if exists_path(destination, path_length):
        print(f"there is a path of length {path_length} from 0 to {destination}")
    else:
        print(f"no path of length {path_length} from 0 to {destination}")


# test_existence(5, 5)
# test_existence(5, 4)
# test_existence(5, 3)
test_existence(5, 2)
test_existence(5, 1)
