from datetime import datetime, timedelta
from package import HashTable, Package, load_packages
from distance_data import get_distance, address_dictionary, get_index

# Initialize the hash table and load the packages
hash_table = HashTable()
load_packages("package_file.csv", hash_table)

# Create lists of package ids for each truck
truck1 = [4, 13, 14, 15, 16, 17, 19, 20, 21, 29, 30, 31, 34, 37, 39, 40]
truck2 = [1, 3, 5, 6, 12, 18, 25, 26, 28, 32, 36, 38]
truck3 = [2, 7, 8, 9, 10, 11, 22, 23, 24, 27, 33, 35]

# Create start times for each truck
start_time_truck1 = datetime(year=2024, month=1, day=1, hour=8, minute=0)
start_time_truck2 = datetime(year=2024, month=1, day=1, hour=9, minute=5)
start_time_truck3 = datetime(year=2024, month=1, day=1, hour=10, minute=20)

# Timestamp each package in each list with the corresponding loading time
def timestamp_packages(truck, start_time):
    for package_id in truck:
        package = hash_table.lookup(package_id)
        if package:
            package.loading_time = start_time
            package.status = "Loaded on Truck"
            # print(f"Debug: Package {package_id} loading time set to {package.loading_time}")  # Debug print


# Apply timestamp to each truck
timestamp_packages(truck1, start_time_truck1)
timestamp_packages(truck2, start_time_truck2)
timestamp_packages(truck3, start_time_truck3)

# Print the results to verify
# def print_loaded_packages(truck, truck_number):
#     print(f"\nTruck {truck_number} Loaded Packages:")
#     for package_id in truck:
#         package = hash_table.lookup(package_id)
#         if package:
#             print(f"Package ID: {package.package_id}, Address: {package.address}, "
#                   f"City: {package.city}, Zip code: {package.zip_code}, "
#                   f"Weight: {package.weight}, Status: {package.status}, "
#                   f"Loading Time: {package.loading_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Print the results to verify
# def print_loaded_packages(truck, truck_number):
#     print(f"\nTruck {truck_number} Loaded Packages:")
#     for package_id in truck:
#         package = hash_table.lookup(package_id)
#         if package:
#             print(f"Package ID: {package.package_id}, Address: {package.address}, "
#                   f"City: {package.city}, Zip code: {package.zip_code}, "
#                   f"Weight: {package.weight}, Status: {package.status}, "
#                   f"Loading Time: {package.loading_time.strftime('%Y-%m-%d %H:%M:%S')}")
            
# Set the current truck location to the index location of the hub
hub_address = "HUB"
current_truck_location = get_index(hub_address)

# Print the current truck location to verify
# print(f"Current truck location (index): {current_truck_location}")

# Function to deliver packages using the nearest neighbor algorithm
def deliver_packages(truck, start_time):
    current_time = start_time
    current_location = hub_address
    delivered_packages = []
    total_distance = 0.0  # Initialize the total distance

    # Calculate distance from the HUB to the first delivery location
    if truck:
        first_package_id = truck[0]
        first_package = hash_table.lookup(first_package_id)
        if first_package:
            distance_to_first = get_distance(current_location, first_package.address)
            total_distance += distance_to_first
            travel_time = timedelta(minutes=(distance_to_first / 18) * 60)
            current_time += travel_time
            current_location = first_package.address

    while truck:
        min_distance = float('inf')
        min_package = None

        for package_id in truck:
            package = hash_table.lookup(package_id)
            if package:
                try:
                    distance = get_distance(current_location, package.address)
                except ValueError as e:
                    print(e)
                    continue
                if distance < min_distance:
                    min_distance = distance
                    min_package = package

        if min_package:
            travel_time = timedelta(minutes=(min_distance / 18) * 60)  # Assuming truck speed is 18 miles per hour
            current_time += travel_time
            min_package.delivery_time = current_time
            min_package.status = "Delivered"
            delivered_packages.append(min_package)
            truck.remove(min_package.package_id)
            current_location = min_package.address
            total_distance += min_distance  # Update the total distance
            # print(f"Debug: Package {min_package.package_id} delivered at {min_package.delivery_time}")  # Debug print

    # Calculate distance from the last delivery location back to the hub
    if delivered_packages:
        distance_back_to_hub = get_distance(current_location, hub_address)
        total_distance += distance_back_to_hub

    return delivered_packages, total_distance

# Deliver packages for each truck and calculate the total distance
delivered_packages_truck1, total_distance_truck1 = deliver_packages(truck1, start_time_truck1)
delivered_packages_truck2, total_distance_truck2 = deliver_packages(truck2, start_time_truck2)
delivered_packages_truck3, total_distance_truck3 = deliver_packages(truck3, start_time_truck3)


# Print the delivery results for each truck
# def print_deliveries(truck_deliveries, truck_number, total_distance):
#     print(f"\nTruck {truck_number} Deliveries:")
#     for package in truck_deliveries:
#         print(f"Package ID: {package.package_id}, Address: {package.address}, "
#               f"City: {package.city}, Zip code: {package.zip_code}, "
#               f"Weight: {package.weight}, Status: {package.status}, "
#               f"Delivery Time: {package.delivery_time.strftime('%Y-%m-%d %H:%M:%S')}")
#     print(f"\nTotal distance traveled by Truck {truck_number}: {total_distance:.2f} miles")

# print_deliveries(delivered_packages_truck1, 1, total_distance_truck1)
# print_deliveries(delivered_packages_truck2, 2, total_distance_truck2)
# print_deliveries(delivered_packages_truck3, 3, total_distance_truck3)

# Calculate the total distance traveled by all trucks
total_combined_distance = total_distance_truck1 + total_distance_truck2 + total_distance_truck3
# print(f"\nTotal combined distance traveled by all trucks: {total_combined_distance:.2f} miles\n")

# Verify that all packages are delivered
def verify_deliveries(truck_deliveries, truck_number):
    for package in truck_deliveries:
        if package.status != "Delivered":
            print(f"Truck {truck_number} failed to deliver package {package.package_id}")
        else:
            print(f"Truck {truck_number} successfully delivered package {package.package_id} at {package.delivery_time}")


# verify_deliveries(delivered_packages_truck1, 1)
# verify_deliveries(delivered_packages_truck2, 2)
# verify_deliveries(delivered_packages_truck3, 3)

# Export the hash table and total combined distance
exported_hash_table = hash_table
exported_total_combined_distance = total_combined_distance