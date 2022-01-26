import datetime
from typing import List, Union
from unicodedata import name

# method
# attributes


class Student:

    group = "IP-11"

    def __init__(self, first_name: str = "", last_name: str = "") -> None:
        self.first_name = first_name  # public
        self.last_name = last_name  # public
        self.__name = "hidden"  # private
        self._another = "another"  # protected

    def print_name(self):
        self.full_name = "Mr/Mrs. " + self.first_name + " " + self.last_name
        print(self.full_name)

    @staticmethod
    def pass_exam() -> None:
        print(Student.group)


class Dean:
    pass


class Fish:

    def __init__(self) -> None:
        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        self.catch_date = datetime("21/01/2022")
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100


class FishShop:

    def __init__(self) -> None:
        self.fish_list = []
        self.casted_out_fish_list = []

    def add_fish(self, fish_name: str, price_for_kilo: float, total_weight:float,  ) -> str:
        self.fish_list.append(Union[fish_name, price_for_kilo, total_weight])
        pass

    def get_fish_names_sorted_by_price(self) -> List[Union[str, float, float]]:
        from operator import itemgetter
        sorted(self.fish_list,  key=itemgetter(1), reverse=True)
        pass

    def sell_fish(self, sold_fish_name: str, sold_weight: float) -> float:

        # cycle which has the same repeats as number of elements in fish_list list
        for number in range(len(self.sold_fish_list)):
            number_of_element: int = 0

            # looking for number of sold fish in the list and changing the weight
            if sold_fish_name == self.fish_list[number_of_element][0]:
                self.fish_list[number_of_element][2] -= sold_weight
                self.revenue += sold_weight*self.fish_list[number_of_element][1]

            number_of_element += 1
            print("revenue from sold  " + sold_fish_name + " is " + self.revenue)
        pass

    def cast_out_old_fish(self, name_of_fish, casted_out_weight) -> List[Union[str, float]]:
        self.casted_out_fish_list.append(Union[name_of_fish, casted_out_weight])
        pass


class Seller:

    def __init__(self):
        self.seller_list = []

    def add_new_seller(self, seller_first_name: str, seller_last_name, seller_total_revenue: float = 0):
        self.seller_list.append(Union[seller_last_name, seller_first_name, seller_total_revenue])
    pass


class Buyer:

    def __init__(self):
        self.buyer_list = []

    def add_new_buyer(self, buyer_first_name: str, buyer_last_name: str, total_money_spent_by_buyer: float = 0):
        self.buyer_list.append(Union[buyer_last_name, buyer_first_name, total_money_spent_by_buyer])
    pass


oleh = Student("oleh", "petrovych")
oleh.print_name()
taras = Student()
taras.print_name()
vasyl = Dean()

C:\Users\homer\PycharmProjects\pythonProject