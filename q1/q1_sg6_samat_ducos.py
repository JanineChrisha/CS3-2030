9 - Samat
21 - Ducos, Janine Chrisha M.

class Lab:
    def __init__(self, room_number):
        self.room_number = room_number

class Technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None  

    def assign_lab(self, lab_obj):
        """Passes a Lab object reference to the technician's keycard slot."""
        self.assigned_lab = lab_obj


chem_lab = Lab("Room 302")

mr_cruz = Technician("Mr. Cruz")

mr_cruz.assign_lab(chem_lab)

print(f"Technician {mr_cruz.name} is unlocking {mr_cruz.assigned_lab.room_number}.")
