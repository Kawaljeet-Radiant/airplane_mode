# Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ContractDetails(Document):

    def before_save(self):

        self.update_shop_availability()

    def update_shop_availability(self):

        shop = frappe.get_doc('Shop Details', self.shop_number)

        if shop:
            shop.is_available = '0'
            shop.save()
            frappe.db.commit()

