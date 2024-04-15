import json

class Computer:
    def __init__(self, brand, model, price, specs, in_stock):
        self.brand = brand
        self.model = model
        self.price = price
        self.specs = specs
        self.in_stock = in_stock

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __del__(self):
        print(f'Объект "{self}" удален')

    def __add__(self, amount):
        self.in_stock += amount
        if self.in_stock > 0:
            print(f"в наличии: {self.in_stock} {self.brand} {self.model}")
        else:
            print('Нет в наличии')


class DesktopComputer(Computer):
    def __init__(self, brand, model, price, specs, in_stock, case_type, power_supply, warranty_years):
        super().__init__(brand, model, price, specs, in_stock)
        self.case_type = case_type
        self.power_supply = power_supply
        self.warranty_years = warranty_years
        self.GPU_TDP = None
        self.CPU_TDP = None
        self.SSD_count = None
        self.have_rgb = None

    def configure(self, GPU_TDP, CPU_TDP, SSD_count, have_rgb):
        self.GPU_TDP = GPU_TDP
        self.CPU_TDP = CPU_TDP
        self.SSD_count = SSD_count
        self.have_rgb = have_rgb

    def get_overall_TDP(self):
        if self.GPU_TDP is None or self.CPU_TDP is None or self.SSD_count is None or self.have_rgb is None:
            return "Невозможно посчитать TDP, вызовите функцию configure()"
        return self.GPU_TDP + self.GPU_TDP + 50 * self.SSD_count + 100 * int(self.have_rgb) + 100


class LaptopComputer(Computer):
    def __init__(self, brand, model, price, specs, in_stock, screen_size, battery_life):
        super().__init__(brand, model, price, specs, in_stock)
        self.screen_size = screen_size
        self.battery_life = battery_life


class MultimediaDevice:
    def __init__(self, multimedia_features):
        self.multimedia_features = multimedia_features

    def play_media(self):
        print(f"Проигрываю медиа с использованием {self.multimedia_features}...")


class MultimediaLaptop(LaptopComputer, MultimediaDevice):
    def __init__(self, brand, model, price, specs, in_stock, screen_size, battery_life, multimedia_features):
        LaptopComputer.__init__(self, brand, model, price, specs, in_stock, screen_size, battery_life)
        MultimediaDevice.__init__(self, multimedia_features)



class Serializer:
    @staticmethod
    def serialize(obj):
        return json.dumps(
            {
                "brand": obj.brand,
                "model": obj.model,
                "price": obj.price,
                "specs": obj.specs,
                "in_stock": obj.in_stock
            }
        )


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def make_purchase(self, item):
        self.purchases.append(item)


if __name__ == "__main__":
    desktop_computer = DesktopComputer("Ardor", "Gaming", 160000, "Ryzen 5 7500f, RTX 4070, 32GB DDR5", False,
                                       "Mid-Tower",
                                       "1000W", 3)
    laptop_computer = LaptopComputer("HP", "Pavilion", 79900.9, "AMD Ryzen 7, 16GB RAM, 512GB SSD", True, 15.6, 8)

    multimedia_laptop = MultimediaLaptop("Lenovo", "Yoga", 80990.99, "Intel i7, 16GB RAM, 1TB SSD", True, 14, 10,
                                         "Dolby Audio")

    print(desktop_computer)
    print(laptop_computer)
    print(multimedia_laptop)

    serialized_desktop = Serializer.serialize(desktop_computer) #
    print("Сериализованный компьютер:", serialized_desktop)

    desktop_computer.configure(200, 300, 2, True)
    print(f"Общий TDP компьютера: {desktop_computer.get_overall_TDP()}Вт.\n")

    customer = Customer("John Doe", "john@example.com")
    customer.make_purchase(desktop_computer)
    customer.make_purchase(laptop_computer)
    desktop_computer.__add__(0)
    laptop_computer.__add__(5)

    print(f"\nПокупки покупателя {customer.name}:")
    for purchase in customer.purchases:
        print(purchase)

    multimedia_laptop.play_media()