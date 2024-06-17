
class User:
    
    def __init__(self, user_name: str, user_pw: str):
        self.user_name = user_name
        self.user_pw = user_pw
        self.is_authorized = False
        self.donations = 0
    
    def set_authorized(self, is_authorized: bool) -> None:
        self.is_authorized = is_authorized
        
    def add_donation(self, donation_amount: float) -> None:
        self.donations += donation_amount
        
    def print_donation_amount(self) -> None:
        print(f"{self.user_name} has donated: ${self.donations}")
    
    