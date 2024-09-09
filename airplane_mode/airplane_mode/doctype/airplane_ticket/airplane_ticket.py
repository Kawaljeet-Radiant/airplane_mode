# Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):
    def before_save(self):
        if self.status not in ('Boarded'):
            frappe.throw("Cannot book non boarded flights!")
                    
        self.set_total_amount()
        self.assign_seat()

    def validate(self):
        self.validate_addons_unique()
        self.check_ticket_limit()

    def set_total_amount(self):
      total_add_on_amount = 0
      for add_on in self.add_ons:
          total_add_on_amount += add_on.amount

      self.total_amount = total_add_on_amount + self.flight_price

    def assign_seat(self):
        # Generate a random integer (example range from 1 to 100)
        random_integer = random.randint(1, 100)
        # Generate a random capital letter from 'A' to 'E'
        random_letter = random.choice('ABCDEF')

        self.seat = f"{random_integer}{random_letter}"

    def validate_addons_unique(self):
        # Create a set to track add-on IDs
        addon_ids = set()
        for addon in self.add_ons:
            if addon.item in addon_ids:
                frappe.throw("Addon is duplicated")
            addon_ids.add(addon.item)

    def check_ticket_limit(self):
        # Fetch the related flight and airplane
        flight_doc = frappe.get_doc('Airplane Flight', self.flight)
        airplane_doc = frappe.get_doc('Airplane', flight_doc.airplane)
        
        # Get the current number of tickets booked for this flight
        tickets_booked = frappe.db.count('Airplane Ticket', filters={'flight': self.flight})
        
        # Check if the number of tickets booked exceeds the airplane's capacity
        if tickets_booked > airplane_doc.capacity:
            frappe.throw(f"Cannot book more tickets. The capacity of the airplane ({airplane_doc.capacity}) has been reached.")
