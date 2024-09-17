# Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):

    # ON SUBMIT EVENT
    def on_submit(self):
        # CALL FUNCTION UPDATE THE STATUS OF DOC TO COMPLETED ON SUBMIT
        self.update_status_to_completed()

    def after_insert(self):
        self.update_gate_number_to_tickets()

    def on_update(self):
        self.update_gate_number_to_tickets()

    def update_gate_number_to_tickets(self):
        tickets = frappe.get_all("Airplane Ticket", filters={"flight": self.name}, fields=["name", "gate_number"])

        for ticket in tickets:
            ticket_doc = frappe.get_doc("Airplane Ticket", ticket.name)

            if ticket_doc.gate_number != self.gate_number:
                ticket_doc.gate_number = self.gate_number
                ticket_doc.save(ignore_permissions=True)
                frappe.db.commit()

    # UPDATE THE STATUS OF DOC TO COMPLETED ON SUBMIT
    def update_status_to_completed(self):
        self.status = "Completed"