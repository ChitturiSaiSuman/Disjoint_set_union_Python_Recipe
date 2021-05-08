# Python Recipe for Disjoin Set Union
# Supports Union, Find operations on Sets

class DSU:

    def __init__(self, NAX):
        # Initialise the object Variables
        self.NAX = NAX
        self.parent = [i for i in range(NAX)]
        self.weight = [i for i in range(NAX)]


    def get(self, a):
        # Returns the parent of the set
        # Uses Path Compression technique
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return (a)


    def find(self, a, b):
        # Returns a boolean variable
        # True if parent of 'a' and 'b' are same
        # False otherwise
        return (self.get(a) == self.get(b))


    def union(self, a, b):
        # Performs Union Operation on Two Disjoint Sets
        parent_of_a = self.get(a)
        parent_of_b = self.get(b)

        # They Already belong to same set
        if (parent_of_a == parent_of_b):
            return

        # They don't belong to same set

        # If Number of elements in A is less than that of B
        if self.weight[parent_of_a] < self.weight[parent_of_b]:
            self.parent[parent_of_a] = self.parent[parent_of_b]
            self.weight[parent_of_b] += self.weight[parent_of_a]

        # If number of elements in B is less than that of A
        else:
            self.parent[parent_of_b] = self.parent[parent_of_a]
            self.weight[parent_of_a] += self.weight[parent_of_b]


def main():
    # Example to demonstrate DSU

    dsu = DSU(10)
    # Instantiate an object of DSU

    dsu.union(3, 6)
    # Performing union on 3 and 6

    print(dsu.find(3, 6))
    # Check if 3 and 6 belong to same set

    print(dsu.get(3))
    print(dsu.get(6))
    # Find the parent of 3 and 6

    dsu.union(4, 5)
    # Performing union on 4 and 5

    dsu.union(3, 5)
    # Performing union on 3 and 5

    print(dsu.find(4, 6))
    # Check if 4 and 6 belong to same set
    # Prints True because they belong to same set


# Calling Main Function
main()