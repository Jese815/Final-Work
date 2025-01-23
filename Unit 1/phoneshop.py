def calculate_cost():
    print("Welcome to the Phone Shop!")
    
    packages = {
        "1": {"name": "McBasic Package", "phone_cost": 50, "storage": "2 GB", "options": []},
        "2": {"name": "Average Joe Package", "phone_cost": 150, "storage": "8 GB", "options": [
            {"description": "Additional 64 GB storage (+$200)", "cost": 200},
            {"description": "Additional 128 GB storage (+$350)", "cost": 350}
        ]},
        "3": {"name": "Rich Kid Pro Package", "phone_cost": 800, "storage": "32 GB", "options": [
            {"description": "Extra diamonds (+$200)", "cost": 200}
        ]}
    }

    print("Available packages:")
    for key, package in packages.items():
        print(f"{key}. {package['name']} - ${package['phone_cost']} (Included storage: {package['storage']})")

    package_choice = input("Please select a package (1, 2, or 3): ")

    if package_choice not in packages:
        print("Invalid package selection. Please restart the program.")
        return

    selected_package = packages[package_choice]
    total_cost = selected_package['phone_cost']

    if selected_package['options']:
        print("Available options for your package:")
        for idx, option in enumerate(selected_package['options'], start=1):
            print(f"{idx}. {option['description']}")

        option_choice = input("Please select an option (or press Enter to skip): ")
        if option_choice.isdigit() and 1 <= int(option_choice) <= len(selected_package['options']):
            selected_option = selected_package['options'][int(option_choice) - 1]
            total_cost += selected_option['cost']

    print("Cloud data backup options:")
    print("1. 1 year (+$20)")
    print("2. 2 years (+$35)")
    cloud_choice = input("Would you like to add cloud data backup? (1, 2, or press Enter to skip): ")

    if cloud_choice == "1":
        total_cost += 20
        email = input("Please enter your email address for cloud backup: ")
    elif cloud_choice == "2":
        total_cost += 35
        email = input("Please enter your email address for cloud backup: ")

    print("Protective case options:")
    print("1. Rubber case (+$20)")
    print("2. Carbon Fibre case (+$100)")
    case_choice = input("Would you like to add a protective case? (1, 2, or press Enter to skip): ")

    if case_choice == "1":
        total_cost += 20
    elif case_choice == "2":
        total_cost += 100

    charger_choice = input("Would you like to add an extra fast battery charger for $100? (yes/no): ")
    if charger_choice.lower() == "yes":
        total_cost += 100

    print(f"\nThank you for your purchase! Your total cost is: ${total_cost}")

if __name__ == "__main__":
    calculate_cost()