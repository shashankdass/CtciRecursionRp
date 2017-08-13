"""
Suppose we have some input data describing relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

1   2   4
 \ /   / \
  3   5   8
   \ / \   \
    6   7   9

Write a function that, for two given individuals in our dataset, returns true if and only if they share at least one known ancestor.

Sample input and output:
[3, 8] => false
[5, 8] => true
[6, 8] => true

"""
parentChildPairs = [
    [1, 3], [2, 3], [3, 6], [5, 6],
    [5, 7], [4, 5], [4, 8], [8, 9]
]

from collections import defaultdict


def find(parentChildPairs):
    if not parentChildPairs:
        return None
    child_parents_dict = defaultdict(list)
    return_dict = {}
    for parent_child in parentChildPairs:
        child_parents_dict[parent_child[1]].append(parent_child[0])

    return_dict['One parent'] = [k for k, v in child_parents_dict.items() if len(v) == 1]
    child_set = set(child_parents_dict.keys())
    parent_set = set()
    for _, v in child_parents_dict.items():
        for parent in v:
            parent_set.add(parent)
    return_dict['Zero parent'] = list(parent_set.difference(child_set))

    return child_parents_dict


def isAncestor(child_parents_dict, lis_nodes):
    print(child_parents_dict)

    if not lis_nodes:
        return False
    parents1 = set(getAllParents(lis_nodes[0], child_parents_dict))
    print(parents1)
    parents2 = set(getAllParents(lis_nodes[1], child_parents_dict))
    print(parents2)
    return not len(parents1.intersection(parents2)) == 0


def getAllParents(child, child_parents_dict):
    parents = []
    if child not in child_parents_dict:
        return parents
    for parent in child_parents_dict[child]:
        parents.extend(child_parents_dict[child])
        temp_parent = getAllParents(parent, child_parents_dict)
        parents.extend(temp_parent)
    return parents


child_parents_dict = find(parentChildPairs)
print(isAncestor(child_parents_dict, [3, 8]))
