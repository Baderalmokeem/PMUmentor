import json

# File to store user data
DATABASE_FILE = "pmumentor_data.json"

# Load data from file or initialize
try:
    with open(DATABASE_FILE, "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

# User class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.events = []
        self.resources = []

    def update_info(self, new_username=None, new_email=None):
        if new_username:
            self.username = new_username
        if new_email:
            self.email = new_email

    def create_event(self, event_name, event_type, event_details):
        event = {
            "name": event_name,
            "type": event_type,
            "details": event_details
        }
        self.events.append(event)

    def share_resource(self, resource_name, resource_type, resource_details):
        resource = {
            "name": resource_name,
            "type": resource_type,
            "details": resource_details
        }
        self.resources.append(resource)

# Helper functions
def save_data():
    with open(DATABASE_FILE, "w") as f:
        json.dump(users, f)

def create_account(username, email):
    if username in users:
        return "Username already exists!"
    users[username] = vars(User(username, email))
    save_data()
    return "Account created successfully!"

def update_account(username, new_username=None, new_email=None):
    if username not in users:
        return "User not found!"
    user_data = users[username]
    user = User(**user_data)
    user.update_info(new_username, new_email)
    users[username] = vars(user)
    if new_username:
        users[new_username] = users.pop(username)
    save_data()
    return "Account updated successfully!"

def create_event(username, event_name, event_type, event_details):
    if username not in users:
        return "User not found!"
    user_data = users[username]
    user = User(**user_data)
    user.create_event(event_name, event_type, event_details)
    users[username] = vars(user)
    save_data()
    return "Event created successfully!"

def share_resource(username, resource_name, resource_type, resource_details):
    if username not in users:
        return "User not found!"
    user_data = users[username]
    user = User(**user_data)
    user.share_resource(resource_name, resource_type, resource_details)
    users[username] = vars(user)
    save_data()
    return "Resource shared successfully!"

# Main program
if __name__ == "__main__":
    while True:
        print("\n--- PmuMentor Platform ---")
        print("1. Create Account")
        print("2. Update Account Information")
        print("3. Create Event")
        print("4. Share Resource")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            print(create_account(username, email))

        elif choice == "2":
            username = input("Enter your username: ")
            new_username = input("Enter new username (or press Enter to skip): ")
            new_email = input("Enter new email (or press Enter to skip): ")
            print(update_account(username, new_username, new_email))

        elif choice == "3":
            username = input("Enter your username: ")
            event_name = input("Enter event name: ")
            event_type = input("Enter event type (virtual/in-person): ")
            event_details = input("Enter event details: ")
            print(create_event(username, event_name, event_type, event_details))

        elif choice == "4":
            username = input("Enter your username: ")
            resource_name = input("Enter resource name: ")
            resource_type = input("Enter resource type (e.g., study guide, tutorial): ")
            resource_details = input("Enter resource details: ")
            print(share_resource(username, resource_name, resource_type, resource_details))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
