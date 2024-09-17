import frappe

def create_payment_schedule(doc, method):
    payment_schedule = frappe.get_doc({
        "doctype": "Payment Schedule",
        "name1": doc.passenger,
        "flight": doc.flight,
        "ticket": doc.name,
        "due_date": doc.payment_due_date,
        "amount": doc.total_amount,
        "status": "Pending"
    })
    payment_schedule.insert(ignore_permissions=True)
    frappe.db.commit()