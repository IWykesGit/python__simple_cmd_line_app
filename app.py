from donations_pkg import homepage
from time import sleep

homepage.show_unauthorized_message()
user = None

while True:
    user_selected = input("Choose an option: ")
    
    match user_selected:
        case "1":
            temp_user = homepage.get_login_user()
            user = homepage.is_login_valid(temp_user)
            # faked loading period
            sleep(1)
            if user:
                homepage.show_authorized_message(user)
        case "2":
            homepage.register_user()
            # faked loading period
            sleep(1)
            
            # if a user was already logged in, do not show unauth screen
            if user is not None and user.is_authorized:
                homepage.show_authorized_message(user)
            else:
                homepage.show_unauthorized_message()
        case "3":
            if user is not None and user.is_authorized:
                homepage.make_donation(user)
            else:
                print("\nYou are not logged in.")
        case "4":
            homepage.show_donations()
        case "5":
            if user is not None and user.is_authorized:
                user.print_donation_amount()
            else:
                print("\nYou are not logged in.")
        case "6":
            exit()
        case _:
            print("Please select a valid option\n")
            
    sleep(1)
        
            

