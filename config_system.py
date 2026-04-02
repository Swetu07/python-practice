import json
import os

# Default settings
default_config = {
    "theme": "light",
    "language": "English",
    "font_size": 14
}

# Load config from file
def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as file:
            return json.load(file)
    else:
        return default_config


# Save config to file
def save_config(config):
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)


# Update config
def update_config(config):
    print("\nCurrent Settings:", config)

    key = input("Enter setting (theme/language/font_size): ")

    if key in config:
        value = input("Enter new value: ")

        if key == "font_size":
            value = int(value)

        config[key] = value
        print("Updated successfully!")
    else:
        print("Invalid setting!")

    return config


# Main program
config = load_config()

while True:
    print("\n1. View Config")
    print("2. Update Config")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(config)

    elif choice == "2":
        config = update_config(config)
        save_config(config)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")