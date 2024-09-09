# Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from frappe.query_builder.functions import Sum


def execute(filters=None):
    columns = get_columns()
    data = get_data()
    chart_data = get_chart_data(data)

    return columns, data, None, chart_data

def get_columns():
    return [
        {"label": "Airline", "fieldname": "airline", "fieldType": "Link", "width": 150},
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldType": "Currency",
            "width": 100,
            "options": "INR",
        },
    ]

def get_data():
    airplane = frappe.qb.DocType("Airplane")
    airplane_ticket = frappe.qb.DocType("Airplane Ticket")
    airplane_flight = frappe.qb.DocType("Airplane Flight")

    query = (
        frappe.qb.from_(airplane)
        .join(airplane_flight)
        .on(airplane.name == airplane_flight.airplane)
        .join(airplane_ticket)
        .on(airplane_ticket.flight == airplane_flight.name)
        .select(
            airplane.airline.as_("airline"),
            Sum(airplane_ticket.total_amount).as_("revenue"),
        )
        .groupby(airplane.airline)
    )

    results = query.run(as_dict=True)

    return results

def get_chart_data(data):
    labels = []
    values = []

    for d in data:
        labels.append(d.airline)
        values.append(d.revenue)

    return {
        "data": {
            "labels": labels,
            "datasets": [{"values": values}],
        },
        "type": "donut",
    }
