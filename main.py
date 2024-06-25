# Student ID: 011582607

from datetime import datetime
from package import Package, load_packages
from algorithm import delivered_packages_truck1, delivered_packages_truck2, delivered_packages_truck3, total_combined_distance, exported_hash_table

# Use the exported hash table from algorithm.py
hash_table = exported_hash_table

# Combine delivered packages from all trucks for easy lookup
all_delivered_packages = delivered_packages_truck1 + delivered_packages_truck2 + delivered_packages_truck3

# Time Complexity: O(1)
def get_package_status(package, query_time):
    if package.package_id == 9:
        if query_time < datetime(year=2024, month=1, day=1, hour=10, minute=20):
            package.address = "300 State St"
            package.city = "Salt Lake City"
            package.zip_code = "84103"
        else:
            package.address = "410 S. State St"
            package.city = "Salt Lake City"
            package.zip_code = "84111"

    if package.loading_time is None:
        return "Unknown"
    if package.delivery_time is None:
        return "Unknown"
    
    if query_time < package.loading_time:
        return "At hub"
    elif query_time > package.delivery_time:
        return "Delivered"
    else:
        return "En Route"

# Time Complexity: O(n)
def display_all_packages(query_time):
    for package in all_delivered_packages:
        status = get_package_status(package, query_time)
        print(f"Package ID: {package.package_id}, "
              f"Truck Number: {package.truck_number if package.truck_number else 'N/A'}, "
              f"Address: {package.address}, City: {package.city}, "
              f"Zip code: {package.zip_code}, Weight: {package.weight}, Status: {status}, "
              f"Loading Time: {package.loading_time.strftime('%Y-%m-%d %H:%M:%S') if package.loading_time else 'N/A'}, "
              f"Delivery Time: {package.delivery_time.strftime('%Y-%m-%d %H:%M:%S') if package.delivery_time else 'N/A'}")

# Time Complexity: O(1)
def display_one_package(query_time, package_id):
    package = hash_table.lookup(package_id)
    if package:
        status = get_package_status(package, query_time)
        print(f"Package ID: {package.package_id}, "
              f"Truck Number: {package.truck_number if package.truck_number else 'N/A'}, "
              f"Address: {package.address}, City: {package.city}, "
              f"Zip code: {package.zip_code}, Weight: {package.weight}, Status: {status}, "
              f"Loading Time: {package.loading_time.strftime('%Y-%m-%d %H:%M:%S') if package.loading_time else 'N/A'}, "
              f"Delivery Time: {package.delivery_time.strftime('%Y-%m-%d %H:%M:%S') if package.delivery_time else 'N/A'}")
    else:
        print(f"Package with ID {package_id} not found.")

# Time Complexity: O(1)
def display_total_distance():
    print(f"Total combined distance traveled by all trucks: {total_combined_distance:.2f} miles")

# Time Complexity: O(1)
def valid_time_format(time_str):
    try:
        datetime.strptime(f"2024-01-01 {time_str}", '%Y-%m-%d %I:%M%p')
        return True
    except ValueError:
        try:
            datetime.strptime(f"2024-01-01 {time_str}", '%Y-%m-%d %I:%M %p')
            return True
        except ValueError:
            return False

# Time Complexity: O(1)
def get_valid_time():
    while True:
        time_str = input("\nEnter the time (HH:MM AM/PM): ")
        if valid_time_format(time_str):
            return datetime.strptime(f"2024-01-01 {time_str.strip()}", '%Y-%m-%d %I:%M%p' if len(time_str) <= 6 else '%Y-%m-%d %I:%M %p')
        else:
            print("Invalid time format. Please enter the time in HH:MM AM/PM format.")

# Time Complexity: O(1)
def get_valid_package_id():
    while True:
        try:
            package_id = int(input("Enter the package ID: "))
            return package_id
        except ValueError:
            print("Invalid package ID. Please enter a valid numeric package ID.")

# Time Complexity: O(n)
def user_menu():
    while True:
        print("\nPackage Tracking System")
        print("1. Display all packages at a certain time")
        print("2. Display one package at a certain time")
        print("3. Display total combined distance traveled by all trucks")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            query_time = get_valid_time()
            display_all_packages(query_time)
        elif choice == '2':
            query_time = get_valid_time()
            package_id = get_valid_package_id()
            display_one_package(query_time, package_id)
        elif choice == '3':
            print()
            display_total_distance()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the user menu
if __name__ == "__main__":
    user_menu()

