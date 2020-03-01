"""
    recursive function to see if a certain value is contained in a sublist
"""


def exists_sublist(values_list, target_value, depth):
    padding = "---"*depth
    print(padding + f" depth {depth}")
    print(padding + f" values : {values_list}")
    print(padding + f" target : {target_value}")
    depth += 1
    # __import__('ipdb').set_trace()
    if len(values_list) == 0:
        print(padding+f" empty list, target value {target_value}")
        if not target_value == 0:
            print(padding+" go back\n")
        return target_value == 0
    else:
        return (exists_sublist(values_list[1:], target_value, depth) or
                exists_sublist(values_list[1:], target_value - values_list[0],
                               depth))


def test_list_target(values, target_value):
    if exists_sublist(values, target_value, 0):
        print(f"{values_1} contains a sublist of value {target_value}")
    else:
        print(f"{values_1} noes NOT a sublist of value {target_value}")


values_1 = [2, 7, -1, 9]
target_value_1 = 16
target_value_2 = 4
values_2 = [1, 23, 14, 7, -17, 3, 5, 179, 358, 25, 11, 2, -36, 17, 34, 23, -76]
target_value_3 = 65
target_value_4 = -31
target_value_5 = 1980

# test_list_target(values_1, target_value_1)
test_list_target(values_1, target_value_2)
# test_list_target(values_2, target_value_3)
# test_list_target(values_2, target_value_4)
# test_list_target(values_2, target_value_5)
