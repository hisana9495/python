from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year
    def account_age(self):
        current_year = 2025
        return current_year - self.account_year
    @abstractmethod
    def get_role(self):
        pass
class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"Admin User: {self.name}, Account created in {self.account_year}"
class Guest(User):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return f"Guest User: {self.name}, Account created in {self.account_year}"
admin_user = Admin("haya", 2020)
guest_user = Guest("luvan", 2023)
print("Role:", admin_user.get_role())
print("Account Age:", admin_user.account_age(), "years")
print(admin_user)
print("\nRole:", guest_user.get_role())
print("Account Age:", guest_user.account_age(), "years")
print(guest_user)