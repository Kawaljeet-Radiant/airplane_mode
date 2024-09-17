// Copyright (c) 2024, Kawaljeet Singh Bagga and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contract Details", {
  onload: function (frm) {
    // Function to set the filter on the Shop field
    frm.set_query("shop_number", function () {
      return {
        filters: [
          ["is_available", "=", 1], // Only show shops that are available
        ],
      };
    });
  },
});
