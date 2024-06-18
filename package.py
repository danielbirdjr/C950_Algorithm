# A.  Develop a hash table, without using any additional libraries or classes,
# that has an insertion function that takes the package ID as input and inserts
# each of the following data components into the hash table:
# •   delivery address
# •   delivery deadline
# •   delivery city
# •   delivery zip code
# •   package weight
# •   delivery status (i.e., at the hub, en route, or delivered), including the delivery time

# Class that holds the package objects
class Package:
    # Initializes a new package with the WGUPS Package File headers
    def __init__(self, package_id, address, deadline, city, zip_code, weight, status):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status

    # String representation of the package for printing
    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, Deadline: {self.deadline}, "
                f"City: {self.city}, Zip code: {self.zip_code}, Weight: {self.weight}, Status: {self.status}")

# Class for the hash table to store package objects
class HashTable:
    def __init__(self):
        self.size = 40
        self.table = [None] * self.size
        for i in range(self.size):
            self.table[i] = []

    def hash(self, key):
        return key % self.size

    def insert(self, package):
        index = self.hash(package.package_id)
        self.table[index].append(package)



# Example Test
# hash_table = HashTable()
# package_example = Package(1, "123 Main St", "10:46", "Washington", "15301", 16, "on its way")
# hash_table.insert(package_example)
# print(hash_table)

