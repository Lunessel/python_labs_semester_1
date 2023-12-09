class ArtificialTree:
    def __init__(self, name_of_the_manufacturer, height, price, production_material, 
                 islacquered, production_date) -> None:
        
        self.__name_of_the_manufacturer = name_of_the_manufacturer
        self.__height = height
        self.__price = price
        self.__production_material = production_material
        self.islacquered = islacquered
        self.production_date = production_date

    def get_name_of_the_manufacturer(self):
        return self.__name_of_the_manufacturer

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_production_material(self):
        return self.__production_material
    
    def __str__(self):
        return f"{self.__name_of_the_manufacturer}, {self.__height}, {self.__price}, {self.__production_material}, {self.islacquered}, {self.production_date}"

    def __repr__(self):
        return f"{self.__name_of_the_manufacturer}, {self.__height}, {self.__price}, {self.__production_material}, {self.islacquered}, {self.production_date}"

    def __del__(self):
        print("Destructor is called")
