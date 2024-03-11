class Shoe:
    def __init__(self, brand, model, size, price):
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price

    def display(self):
        return f"{self.brand} {self.model} - Size: UK{self.size}, Price: ฿{self.price}"

class ADIFOM_shoe(Shoe):
    def __init__(self, brand, model, size, court, price):
        super().__init__(brand, model, size, price)
        self.court = court

    def display(self):
        return f"{self.brand} {self.model} - Size: UK{self.size}, Court: {self.court}, Price: ฿{self.pric
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    shoe1 = Shoe("Nike", "Air Max", 10, 150)

    print(shoe1.display())  # Output: Nike Air Max - Size: 10, Price: $150

    tennis_shoe1 = TennisShoe("Adidas", "Barricade", 9, 120, "Hard")

    print(tennis_shoe1.display())  # Output: Adidas Barricade - Size: 9, Court: Hard, Price: $120