# Add a list of elements to a set
def add_list():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]

    sample_set.update(sample_list)

    print("Add a list of elements to a set - ")
    print(sample_set,"\n")

# Return a new set of identical items from two sets
def identical():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    new_set = set()

    for i, j in zip(set1, set2):
        if i==j:
            new_set.add(i)

    print("Return new set of identical items from two sets -")
    print(new_set,"\n")

def


if __name__ == '__main__':
    add_list()
    identical()
