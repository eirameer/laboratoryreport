if n == 1:
    print("Move disk 1 from source", source, "to destination", destination)

return TowerOfHanoi(n - 1, source, auxiliary, destination)

print("Move disk", n, "from source", source, "to destination", destination

TowerOfHanoi(auxiliary, n - 1, destination, source)

# Driver code  n = 4 TowerOfHanoi(n,'A','B','C')   # A, C, B are the name of rods

def TowerOfHanoi(n, source, destination, auxiliary):\