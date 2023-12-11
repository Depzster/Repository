class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def display_info(self):
        return f"Property: {self.area} sq. m, {self.rooms} rooms, {self.price} PLN, Address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def display_info(self):
        return f"House: {super().display_info()}, Plot size: {self.plot} sq. m"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def display_info(self):
        return f"Flat: {super().display_info()}, Floor: {self.floor}"


house = House(area=150, rooms=4, price=500000, address="123 Main St", plot=300)
flat = Flat(area=80, rooms=2, price=250000, address="456 Oak St", floor=2)

print(house.display_info())
print("\n----------------\n")
print(flat.display_info())
