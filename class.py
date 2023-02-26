class Supermarket:
    def __init__(self, location, name, product, customer):
        self.name = name
        self.location = location
        self.product = product
        self.customer = customer

    def stuffname(self):
        print(self.name)

    def stufflocation(self):
        print(self.location)

    def stuffproduct(self):
        print(self.product)

    def stuffcustomer(self):
        print(self.customer)