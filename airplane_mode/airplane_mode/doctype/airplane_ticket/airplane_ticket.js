// Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
  refresh(frm) {
    frm.add_custom_button(
      "Book Seat",
      () => {
        frappe.prompt("Seat Number", ({ value }) => {
          frm.set_value("seat", value);
          frm.save();
        });
      },
      "Actions"
    );
  },
});
