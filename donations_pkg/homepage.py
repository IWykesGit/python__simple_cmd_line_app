from .database import users, donations
from .users import *

def _show_homepage() -> None:
    print("\n============= DonateMe Homepage =============")
    print("-----------------------------------------------")
    print("| 1. Login               | 2. Register       |")
    print("----------------------------------------------")
    print("| 3. Donate              | 4. Show Donations |")
    print("----------------------------------------------")
    print("| 5. Show User Donations | 6. Exit           |")
    print("----------------------------------------------")
    

def show_unauthorized_message() -> None:
    _show_homepage()
    print("You must be logged in to donate")        
    
def show_authorized_message(user) -> None:
    _show_homepage()
    print("Logged in as: ", user.user_name) 
    
def get_login_user() -> User:
    user_name = input("\nEnter user name: ")
    user_pw = input("Enter password: ")
    
    return User(user_name, user_pw)

def is_login_valid(user: User) -> User:    
    if not users:
        print("\nUser not found. Please register.")
    
    # The returning of an object or none seems bad, but if no user is found it also felt weird to return a blank string
    if (user.user_name in users) and (users[user.user_name].user_pw == user.user_pw):
        users[user.user_name].set_authorized(True)
        print(f"\nWelcome back {user.user_name}!")
        return users[user.user_name]
    elif (user.user_name in users) and (users[user.user_name].user_pw != user.user_pw):
        print("\nIncorrect login details!\n")
        return None
    else:
        print("\nUser not found. Please register.\n")
        return None
        
def register_user() -> None:
    user = get_login_user()
    
    if user.user_name not in users:
        users[user.user_name] = user
        print(f"\nUsername {user.user_name} registered! You may now log in.")
    else:
        print("\nUsername already registered!")

def make_donation(user: User) -> None:
    donation_amount = -1
    while donation_amount <= 0:
        try:
            donation_amount = float(input("\nEnter amount to donate: $").replace(",", ""))
        except ValueError:
            print("Please enter a valid monetary amount")
        else:
            if (donation_amount <= 0):
                print("Please enter a monetary amount greater than zero")
    
    user.add_donation(donation_amount)
    donations.append(f"{user.user_name} donated ${donation_amount}")
    print(f"Thank you for your donation!\n")
    
def show_donations() -> None:
    print("\n--- All Donations ---")
    
    if donations:
        for donation in donations:
            print(donation)
    else:
        print("Currently, there are no donations.")
        