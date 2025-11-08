# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

correct_user_input = (username_input == "user") and (password_input =="pass")
correct_admin_input = (username_input=="admin") and (password_input=="admin")


# TODO: Notify user if credentials are valid or invalid

if correct_user_input:
    print("Access Granted to User")
elif correct_admin_input:
    print("Admin Access Granted")
else:
    print("Access Denied")
