import datetime

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
        self.status = status # Course Instructor said to get rid of status
        self.departure_time = datetime.datetime.strptime("00:00", '%H:%M')
        self.delivery_time = datetime.datetime.strptime("00:00", '%H:%M')

    # String representation of the package for printing
    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, Deadline: {self.deadline}, "
                f"City: {self.city}, Zip code: {self.zip_code}, Weight: {self.weight}, Status: {self.status}")

# Class for the hash table to store package objects
class HashTable:

    # Initialize the size of the hash table
    def __init__(self):
        self.size = 40
        self.table = [None] * self.size
        for i in range(self.size):
            self.table[i] = [] 
    # CI said to change length to 10 and mod 10

    # Hash function to determine the index for a given key
    def hash(self, key):
        return key % self.size

    # Function to insert a package into the hash table
    def insert(self, package_id, address, deadline, city, zip_code, weight, status):
        package = Package(package_id, address, deadline, city, zip_code, weight, status)
        index = self.hash(package_id)
        self.table[index].append(package)

    # Function to find a package based off the package ID
    def find(self, package_id):
        index = self.hash(package_id)
        for package in self.table[index]:
            if package.package_id == package_id:
                return package
        return None
    
    # Function to delete package based off package ID
    def delete(self, package_id):
        index = self.hash(package_id)
        bucket = self.table[index]
        for i, package in enumerate(bucket):
            if package.package_id == package_id:
                del bucket[i]
                return True 
        return False

