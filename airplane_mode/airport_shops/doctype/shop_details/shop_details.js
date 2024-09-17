// Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Details", {
  onload: function (frm) {
    frappe.call({
      method: "frappe.client.get_list",
      args: {
        doctype: "Shop Settings",
        fields: ["default_rent_amount", "enable_rent_reminder"],
      },
      callback: function (response) {
        if (response.message) {
          if (!frm.doc.shop_rent) {
            frm.set_value("shop_rent", response.message[0].default_rent_amount);
          }
          if (!frm.doc.is_available) {
            frm.set_value(
              "is_available",
              response.message[0].enable_rent_reminder
            );
          }
        }
      },
    });
  },
});
