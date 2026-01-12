from abc import ABC, abstractmethod
from datetime import datetime
class User(ABC):
    def __init__(self, name, join_year):
        self.name = name
        self.join_year = join_year
    def years_on_platform(self):
        current_year = 2025
        return current_year - self.join_year
    @abstractmethod
    def role(self):
        """Each subclass must define its role"""
        pass
    def __str__(self):
        return f"{self.name} ({self.role()}) - Using platform for {self.years_on_platform()} years"
class Customer(User):
    def role(self):
        return "Customer"
class Vendor(User):
    def role(self):
        return "Vendor"
c1 = Customer("Riya", 2020)
v1 = Vendor("Adam", 2018)
print(c1) 
print(v1) 