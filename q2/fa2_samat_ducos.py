"""
#21 - Ducos, Janine Chrisha M.                                                              10/23/2026                              
9 - Samat                                                                                    CS FA 2
"""

class Patient:
    
    def __init__ (self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
        
    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self._name = name
        
    def get_bill_amount(self):
        return self.bill_amount
        
    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount
        
    def calculate_bill(self):
        return self.bill_amount
        
class SeniorPatient(Patient):
    
    def calculate_bill(self):
        original_bill = self.get_bill_amount()
        return original_bill * 0.80
        
class PhilHealthPatient(Patient):
    
    def calculate_bill(self):
        original_bill = self.get_bill_amount()
        return original_bill * 0.85    
    
patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = SeniorPatient("Maria Santos", 15000)
patient3 = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-" * 30)
print(f"Patient Name:  {patient1.get_name()}")
print(f"Original Bill: ₱{patient1.get_bill_amount():,.2f}")
print(f"Final Bill:    ₱{patient1.calculate_bill():,.2f}")
print()
print(f"Patient Name:  {patient2.get_name()}")
print(f"Original Bill: ₱{patient2.get_bill_amount():,.2f}")
print(f"Final Bill:    ₱{patient2.calculate_bill():,.2f}")
print()
print(f"Patient Name:  {patient3.get_name()}")
print(f"Original Bill: ₱{patient3.get_bill_amount():,.2f}")
print(f"Final Bill:    ₱{patient3.calculate_bill():,.2f}")
