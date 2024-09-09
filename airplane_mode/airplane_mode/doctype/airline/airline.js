// Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
    refresh(frm) {
      if (frm.doc.website !== undefined) {
        frm.add_web_link(frm.doc.website, "View Website");
      }
    },
  });