# Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		if not self.last_name:
			self.full_name = self.first_name
		else:
			self.full_name = f"{self.first_name} {self.last_name}"