9 - Samat
21 - Ducos, Janine Chrisha M.

class Glassware:
    def __init__(self, material="Borosilicate Glass"):
        self.material = material

class Beaker(Glassware):
    def __init__(self, capacity_ml=250, material="Borosilicate Glass"):
        super().__init__(material)
        self.capacity_ml = capacity_ml

    def __del__(self):
        print("A Beaker has been destroyed")

class Tray:
    def __init__(self, beaker_capacity=250):
        self.beakers = [Beaker(beaker_capacity) for _ in range(5)]
        print(f"Tray Created containing {len(self.beakers)} beakers")

    def __del__(self):
        self.beakers.clear()
        print("Tray Destroyed")

if __name__ == "__main__":
    my_tray = Tray(250)
    print(f"The tray contains {len(my_tray.beakers)} beakers made of {my_tray.beakers[0].material}")
    del my_tray
