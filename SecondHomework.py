import datetime
from typing import List, Union
from unicodedata import name


class FishInfo:

    def __init__(self, fish_name: str, price_in_uah_per_kilo: float, due_date: datetime,
                 origin: str, catch_date: datetime):
        self.fish_name = fish_name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.due_date = due_date
        self.origin = origin
        self.catch_date = catch_date

    pass


class Fish(FishInfo):

    def __init__(self, fish_name: str, price_in_uah_per_kilo: float, due_date: datetime,
                 origin: str, catch_date: datetime, age_in_months: float,
                 single_fish_weight: float):
        FishInfo.__init__(self, fish_name, price_in_uah_per_kilo, due_date,
                          origin, catch_date)
        self.age_in_months = age_in_months
        self.single_fish_weight = single_fish_weight

    pass


class FishBox(FishInfo):

    def __init__(self, fish_name: str, price_in_uah_per_kilo: float, due_date: datetime,
                 origin: str, catch_date: datetime, fish_weight: float, package_date: datetime,
                 height: float, length: float, width: float, is_alive: bool):
        FishInfo.__init__(self, fish_name, price_in_uah_per_kilo,
                          due_date, origin, catch_date,)
        self.fish_weight = fish_weight
        self.package_date = package_date
        self.height = height
        self.length = length
        self.width = width
        self.is_alive = is_alive
    pass


class FishShop(FishBox, Fish,):

    def __init__(self, fish_boxes, fish_list):
        self.fish_boxes = fish_boxes
        self.fish_list = fish_list
        self.full_fish_list = []
        self.full_fish_list.append(self.fish_boxes)
        self.full_fish_list.append(self.fish_list)
        self.frozen_fish = None

    def add_fish_box(self, fish_name: str, price_in_uah_per_kilo: float,
                     due_date: datetime, origin: str, catch_date: datetime,
                     fish_weight: float, package_date: datetime, height: float,
                     length: float, width: float, is_alive: bool):
        FishBox.__init__(self, fish_name, price_in_uah_per_kilo, due_date, origin,
                         catch_date, fish_weight, package_date, height, length, width, is_alive)
        self.fish_boxes[fish_name] = list[price_in_uah_per_kilo, due_date, origin,
                                          catch_date, fish_weight, package_date, height, length,
                                          width, is_alive]

    def add_single_fish(self, fish_name: str, price_in_uah_per_kilo: float, due_date: datetime,
                        origin: str, catch_date: datetime, age_in_months: float,
                        single_fish_weight: float):
        Fish.__init__(self, fish_name, price_in_uah_per_kilo, due_date,
                      origin, catch_date, age_in_months, single_fish_weight)
        self.fish_list[fish_name] = list[price_in_uah_per_kilo, single_fish_weight, due_date,
                                         origin, catch_date, age_in_months, single_fish_weight,
                                         fish_name, age_in_months]

    def get_fish_sorted_by_price(self):
        (sorted(self.full_fish_list, key=lambda x: x[1][0], reverse=True))

    def sell_fish(self, fish_name, fish_weight_sold):
        for x in range(len(self.full_fish_list)):
            if self.full_fish_list[x-1] == fish_name:
                self.full_fish_list[x-1][0] -= fish_weight_sold
                break

    def get_fish_frozen(self, fish_name, fish_weight_frozen):
        for x in range(len(self.full_fish_list)):
            if self.full_fish_list[x - 1] == fish_name:
                self.frozen_fish[self.full_fish_list[x - 1]] = [fish_weight_frozen]

    def get_fresh_fish_sorted_by_price(self):
        pass

    pass
