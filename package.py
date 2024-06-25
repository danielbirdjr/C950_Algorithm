import csv

# Class that holds the package objects
class Package:

    # Initializes a new package with the WGUPS Package File headers
    # Time Complexity: O(1)
    def __init__(self, package_id, address, city, deadline, zip_code, weight, status):
        self.package_id = package_id 
        self.address = address
        self.city = city
        self.deadline = deadline
        self.zip_code = zip_code
        self.weight = weight 
        self.status = status 
        self.loading_time = None
        self.delivery_time = None
        self.truck_number = None

    # String representation of the package for printing
    # Time Complexity: O(1)
    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, "
                f"Zip code: {self.zip_code}, Weight: {self.weight}, Status: {self.status}")
    
    # String representation of the package for printing
    # Time Complexity: O(1)
    def __repr__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, "
                f"Zip code: {self.zip_code}, Weight: {self.weight}, Status: {self.status}")
    

# Class for the hash table to store package objects
class HashTable:

    # Initialize the size of the hash table
    # Time Complexity: O(n)
    def __init__(self):
        self.size = 40
        self.table = [None] * self.size
        for i in range(self.size):
            self.table[i] = [] 

    # Hash function to determine the index for a given key
    # Time Complexity: O(1)
    def hash(self, key):
        return key % self.size

    # Function to insert a package into the hash table
    # Time Complexity: O(1) on average
    def insert(self, package_id, address, city, deadline, zip_code, weight, status):
        package = Package(package_id, address, city, deadline, zip_code, weight, status)
        index = self.hash(package_id)
        self.table[index].append(package)

    # Function to lookup a package based off the package ID
    # Time Complexity: O(1) on average
    def lookup(self, package_id):
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                return package
        return None
    
    # Function to delete package based off package ID
    # Time Complexity: O(1) on average
    def delete(self, package_id):
        index = self.hash(package_id)
        bucket = self.table[index]
        for i, package in enumerate(bucket):
            if package.package_id == package_id:
                del bucket[i]
                return True 
        return False

# Function to load the packages from the package_file.csv file into the hash table
# Time Complexity: O(n)
def load_packages(filename, hash_table):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            package_id, address, city, state, zip_code, deadline, weight, special_notes = row
            status = "At hub"  # Default status
            # Convert package_id and weight to integers
            package_id = int(package_id)
            weight = int(weight)
            hash_table.insert(package_id, address, city, deadline, zip_code, weight, status)

# Main execution block to load packages and demonstrate functionality
hash_table = HashTable()
load_packages("package_file.csv", hash_table)

