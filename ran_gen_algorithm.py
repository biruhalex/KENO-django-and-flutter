import os
import re
from itertools import chain

import django
from randomgenerator.models import RanGenModel, RanNums
from collections import Counter

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kenobackend.settings")

# Initialize Django
django.setup()

from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            # Initialize an empty cart in the session
            cart = self.session['cart'] = {}
        self.cart = cart

    def add_RanGenModel(self, RanGenModel_id, quantity=1):
        """
        Add a RanGenModel to the cart or update its quantity.
        """
        RanGenModel_id = str(RanGenModel_id)
        quantity = int(quantity)

        if RanGenModel_id in self.cart:
            self.cart[RanGenModel_id]['quantity'] += quantity
        else:
            try:
                ranGenModel = RanGenModel.objects.get(id=RanGenModel_id)
                self.cart[RanGenModel_id] = {
                    'quantity': quantity,
                    'price': str(ranGenModel.price),
                    'name': ranGenModel.name,
                }
            except ObjectDoesNotExist:
                pass

        self.save()

    def remove_RanGenModel(self, RanGenModel_id):
        """
        Remove a RanGenModel from the cart.
        """
        RanGenModel_id = str(RanGenModel_id)
        if RanGenModel_id in self.cart:
            del self.cart[RanGenModel_id]
            self.save()

    def update_quantity(self, RanGenModel_id, quantity):
        """
        Update the quantity of a RanGenModel in the cart.
        """
        RanGenModel_id = str(RanGenModel_id)
        quantity = int(quantity)

        if RanGenModel_id in self.cart:
            self.cart[RanGenModel_id]['quantity'] = quantity
            self.save()

    def get_cart_contents(self):
        """
        Get the contents of the cart.
        """
        cart_items = []
        for RanGenModel_id, item in self.cart.items():
            try:
                RanGenModel = RanGenModel.objects.get(id=RanGenModel_id)
                total_price = Decimal(item['price']) * item['quantity']
                cart_items.append({
                    'RanGenModel': RanGenModel,
                    'quantity': item['quantity'],
                    'total_price': total_price,
                })
            except ObjectDoesNotExist:
                pass

        return cart_items

    def get_cart_total(self):
        """
        Calculate the total price of all items in the cart.
        """
        total = Decimal(0)
        for RanGenModel_id, item in self.cart.items():
            total += Decimal(item['price']) * item['quantity']
        return total

    def clear_cart(self):
        """
        Clear the cart.
        """
        self.cart = {}
        self.save()

    def save(self):
        """
        Save the cart in the session.
        """
        self.session['cart'] = self.cart
        self.session.modified = True


class Keno:
    def __init__(self, request):
        self.stake = []
        # self.model = RanGenModel.objects.get()

    def iterate(self):
        filtered_models = RanGenModel.objects.filter(win__gte=1000).filter(game_id=3208)
        for model_instance in filtered_models:
            print(model_instance)
        print(filtered_models.count())

    def extract_and_convert_numbers(self, text_from_database):
        # Define a regular expression pattern to find numbers
        pattern = r'\b(\d+(\.\d+)?)\b'

        # Use re.findall to extract all numeric values from the text
        matches = re.findall(pattern, text_from_database)

        # Convert the extracted strings to numeric values (int or float)
        numeric_values = [int(match[0]) if '.' not in match[0] else float(match[0]) for match in matches]

        return numeric_values

    def lst_iteration(self):
        my_model_instance = RanGenModel.objects.filter(game_id=3208)
        result = []
        for obj in my_model_instance:
            filtered_models = obj.my_list
            extracted_numbers = self.extract_and_convert_numbers(filtered_models)
            result.append(extracted_numbers)

        flat_list = list(chain(*result))

        selection = []
        unselected = []
        count_selected = 0
        count_unselected = 0

        counter = Counter(flat_list)

        duplicates = {item: count for item, count in counter.items() if count > 1}
        sorted_duplicates = dict(sorted(duplicates.items()))

        # # Sort the dictionary by the counts
        # sorted_duplicates = dict(sorted(duplicates.items(), key=lambda item: item[1]))
        #
        # print("Duplicated items and their counts (sorted by count):", sorted_duplicates)

        print("Duplicated items:", sorted_duplicates)

        # Sort the dictionary by the counts in descending order
        sorted_duplicates = dict(sorted(duplicates.items(), key=lambda item: item[1], reverse=True))

        # Get the most duplicated item
        most_duplicated_item, count = next(iter(sorted_duplicates.items()), (None, 0))

        print("Most duplicated item:", most_duplicated_item)
        print("Count:", count)

        # Get the second most duplicated item
        second_most_duplicated_item, count = next(iter(sorted_duplicates.items())[1:], (None, 0))

        print("Second most duplicated item:", second_most_duplicated_item)
        print("Count:", count)

        #     print("result")
        #     print(result)
        # print("selection")
        # print(selection)
        # print("unselected")
        # print(unselected)
        # print("count_selected")
        # print(count_selected)
        # print("count_unselected")
        # print(count_unselected)


    def gt1k(selfs):
        filtered_models = RanGenModel.objects.filter(win__gte=1000).filter(game_id=3208)
        pass

    def gt2k(selfs):
        pass

    def gt3k(selfs):
        pass

    def gt4k(selfs):
        pass

    def gt5k(selfs):
        pass

    def gt10k(selfs):
        pass

    def winner(self, win):
        pass

    def loser(self, win):
        pass

    def admin_odd(self, win):
        pass

    def agent_odd(self, win):
        pass

    def add_item(self, stake):
        self.stake.append(stake)

    def remove_item(self, stake):
        self.stake.remove(stake)

    def get_stake(self):
        return self.stake

    def get_total(self):
        total = 0
        for item in self.stake:
            total += item.price
        return total

    def clear(self):
        self.stake = []
