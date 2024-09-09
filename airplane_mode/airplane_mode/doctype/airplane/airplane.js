// Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane", {
  onload(frm) {
    // Check if the user has the 'Airport Authority Personnel' role
    if (frappe.user.has_role("Airport Authority Personnel")) {
      // Show the field and make it editable
      frm.set_df_property("initial_audit_completed", "hidden", 0);
      frm.set_df_property("initial_audit_completed", "read_only", 0);
    } else {
      // Hide the field and make it read-only
      frm.set_df_property("initial_audit_completed", "hidden", 1);
      frm.set_df_property("initial_audit_completed", "read_only", 1);
    }
    frm.refresh_field("initial_audit_completed");
  },
});
