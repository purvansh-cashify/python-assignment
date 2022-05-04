# Add a list of elements to a set
def add_list():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]

    sample_set.update(sample_list)

    print("Add a list of elements to a set - ")
    print(sample_set, "\n")


# Return a new set of identical items from two sets
def identical():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    new_set = set()

    for i, j in zip(set1, set2):
        if i == j:
            new_set.add(i)

    print("Return new set of identical items from two sets -")
    print(new_set, "\n")


# Get Only unique items from two sets
def unique():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    new_set = set1.union(set2)

    print("Unique items from two sets - ")
    print(new_set, "\n")


# Update the first set with items that don’t exist in the second set
def update():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}

    set1.difference_update(set2)

    print("Update the first set with items that don’t exist in the second set - ")
    print(set1, "\n")


def remove():
    set1 = {10, 20, 30, 40, 50}

    set1.difference_update(set([10, 20, 30]))

    print("Remove items from the set at once - ")
    print(set1, "\n")


def not_both():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    new_set = set1.symmetric_difference(set2)

    print("Return a set of elements present in Set A or B, but not both - ")
    print(new_set, "\n")


def common():
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}

    if set1.isdisjoint(set2) is False:
        new_set = set1.intersection(set2)

    print("Check if two sets have any elements in common. If yes, display the common elements - ")
    print(new_set, "\n")


def add():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    set1.symmetric_difference_update(set2)

    print("Update set1 by adding items from set2, except common items - ")
    print(set1, '\n')


if __name__ == '__main__':
    add_list()
    identical()
    unique()
    update()
    remove()
    not_both()
    common()
    add()
