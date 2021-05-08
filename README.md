# Disjoint_set_union_Python_Recipe
Python Recipe for Disjoint Set Union Data Structure

### Dependencies
None

### Usage
* Instantiate an object of DSU simply using ```DSU(size)```, where ```size``` is the number of Sets (see examples).
* ```get(a: int) -> int```: Returns the parent of Set ```a```
* ```find(a: int, b: int) -> int```: Returns a boolean variable denoting whether A and B belong to Same Set
* ```union(a: int, b: int) -> None```: Performs Union Operation on Sets ```A``` and ```B```

### Examples
```
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
```

### Time Complexity
* ```init(N: int) -> Instance: DSU```: O(N)
* ```find(a: int) -> int```: O(log*(N)).
* ```union(a: int, b: int) -> None```: O(log*(N))
    Note that it is not O(log(N)). log*(N) is due to the extremely slow-growing [inverse Ackermann function](https://en.wikipedia.org/wiki/Inverse_Ackermann_function) as a resul of Path - Compression.
    log*(N) signifies the number of times you apply log on N till the result becomes 1. log*(N) doesn't exceed 5 in real-life scenarios. In fact, log*(N) for 2<sup>65536</sup> is 5.

### Space Complexity
* O(N)

### Applications
* Useful for detecting Cycle in a Graph.
* Best useful when only Union and Find operations are performed.