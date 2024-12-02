import tkinter as tk
from tkinter import messagebox
import json

# File to store user data
DATABASE_FILE = "pmumentor_data.json"

# Load data from file or initialize
try:
    with open(DATABASE_FILE, "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

# Save data to file
def save_data():
    with open(DATABASE_FILE, "w") as f:
        json.dump(users, f)

# Main Application
class PmuMentorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PmuMentor - Peer Mentorship Platform")
        self.root.geometry("500x600")
        
        # Initialize Frames
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.show_main_menu()

    def clear_frame(self):
        """Clears the current frame."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        """Main menu UI."""
        self.clear_frame()

        tk.Label(self.main_frame, text="Welcome to PmuMentor", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.main_frame, text="Create Account", command=self.create_account_ui, width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Update Account", command=self.update_account_ui, width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Create Event", command=self.create_event_ui, width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Share Resource", command=self.share_resource_ui, width=25).pack(pady=10)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, width=25).pack(pady=10)

    def create_account_ui(self):
        """UI for creating an account."""
        self.clear_frame()

        tk.Label(self.main_frame, text="Create Account", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="Username:").pack()
        username_entry = tk.Entry(self.main_frame)
        username_entry.pack()

        tk.Label(self.main_frame, text="Email:").pack()
        email_entry = tk.Entry(self.main_frame)
        email_entry.pack()

        def create_account_action():
            username = username_entry.get().strip()
            email = email_entry.get().strip()
            if not username or not email:
                messagebox.showerror("Error", "Please fill in all fields.")
                return
            if username in users:
                messagebox.showerror("Error", "Username already exists!")
            else:
                users[username] = {"username": username, "email": email, "events": [], "resources": []}
                save_data()
                messagebox.showinfo("Success", "Account created successfully!")
                self.show_main_menu()

        tk.Button(self.main_frame, text="Create Account", command=create_account_action).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.show_main_menu).pack(pady=10)

    def update_account_ui(self):
        """UI for updating an account."""
        self.clear_frame()

        tk.Label(self.main_frame, text="Update Account", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="Username:").pack()
        username_entry = tk.Entry(self.main_frame)
        username_entry.pack()

        tk.Label(self.main_frame, text="New Username (optional):").pack()
        new_username_entry = tk.Entry(self.main_frame)
        new_username_entry.pack()

        tk.Label(self.main_frame, text="New Email (optional):").pack()
        new_email_entry = tk.Entry(self.main_frame)
        new_email_entry.pack()

        def update_account_action():
            username = username_entry.get().strip()
            new_username = new_username_entry.get().strip()
            new_email = new_email_entry.get().strip()
            if username not in users:
                messagebox.showerror("Error", "User not found!")
            else:
                if new_username:
                    users[new_username] = users.pop(username)
                    users[new_username]["username"] = new_username
                if new_email:
                    users[username or new_username]["email"] = new_email
                save_data()
                messagebox.showinfo("Success", "Account updated successfully!")
                self.show_main_menu()

        tk.Button(self.main_frame, text="Update Account", command=update_account_action).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.show_main_menu).pack(pady=10)

    def create_event_ui(self):
        """UI for creating an event."""
        self.clear_frame()

        tk.Label(self.main_frame, text="Create Event", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="Username:").pack()
        username_entry = tk.Entry(self.main_frame)
        username_entry.pack()

        tk.Label(self.main_frame, text="Event Name:").pack()
        event_name_entry = tk.Entry(self.main_frame)
        event_name_entry.pack()

        tk.Label(self.main_frame, text="Event Type (virtual/in-person):").pack()
        event_type_entry = tk.Entry(self.main_frame)
        event_type_entry.pack()

        tk.Label(self.main_frame, text="Event Details:").pack()
        event_details_entry = tk.Entry(self.main_frame)
        event_details_entry.pack()

        def create_event_action():
            username = username_entry.get().strip()
            event_name = event_name_entry.get().strip()
            event_type = event_type_entry.get().strip()
            event_details = event_details_entry.get().strip()
            if username not in users:
                messagebox.showerror("Error", "User not found!")
            else:
                users[username]["events"].append({
                    "name": event_name,
                    "type": event_type,
                    "details": event_details
                })
                save_data()
                messagebox.showinfo("Success", "Event created successfully!")
                self.show_main_menu()

        tk.Button(self.main_frame, text="Create Event", command=create_event_action).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.show_main_menu).pack(pady=10)

    def share_resource_ui(self):
        """UI for sharing a resource."""
        self.clear_frame()

        tk.Label(self.main_frame, text="Share Resource", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="Username:").pack()
        username_entry = tk.Entry(self.main_frame)
        username_entry.pack()

        tk.Label(self.main_frame, text="Resource Name:").pack()
        resource_name_entry = tk.Entry(self.main_frame)
        resource_name_entry.pack()

        tk.Label(self.main_frame, text="Resource Type (e.g., study guide):").pack()
        resource_type_entry = tk.Entry(self.main_frame)
        resource_type_entry.pack()

        tk.Label(self.main_frame, text="Resource Details:").pack()
        resource_details_entry = tk.Entry(self.main_frame)
        resource_details_entry.pack()

        def share_resource_action():
            username = username_entry.get().strip()
            resource_name = resource_name_entry.get().strip()
            resource_type = resource_type_entry.get().strip()
            resource_details = resource_details_entry.get().strip()
            if username not in users:
                messagebox.showerror("Error", "User not found!")
            else:
                users[username]["resources"].append({
                    "name": resource_name,
                    "type": resource_type,
                    "details": resource_details
                })
                save_data()
                messagebox.showinfo("Success", "Resource shared successfully!")
                self.show_main_menu()

        tk.Button(self.main_frame, text="Share Resource", command=share_resource_action).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.show_main_menu).pack(pady=10)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PmuMentorApp(root)
    root.mainloop()
