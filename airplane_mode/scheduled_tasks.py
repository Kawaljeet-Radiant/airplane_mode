import frappe
from frappe.utils import getdate, nowdate

@frappe.whitelist()
def send_rent_reminders():
    # Fetch current date
    today = getdate(nowdate())
    
    # Fetch tenants with having shops on lease
    tenants = frappe.get_all('Contract Details', fields=['shop_number', 'shop_rent', 'airport', 'tenant_name', 'tenant_email'])

    for tenant in tenants:
        # Define email subject and message
        subject = "Rent Due Reminder"
        message = f"""
        Dear {tenant.tenant_name},
        
        This is a reminder that your rent of {tenant.shop_rent} towards your shop {tenant.shop_number} inside {tenant.airport} airport is due this month.
        
        Please ensure payment is made on time to avoid any late fees.
        (Ignore if already paid for this month)
        
        Thank you,
        {tenant.airport} Airport Authorities.
        """

        print('recipients::', [tenant.tenant_email])
        print('subject::', subject)
        print('message::', message)

        # Send email
        frappe.sendmail(
            recipients=[tenant.email],
            subject=subject,
            message=message
        )