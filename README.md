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
    # Examples to demonstrate DSU

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