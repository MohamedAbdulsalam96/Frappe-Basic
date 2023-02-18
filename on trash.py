@frappe.whitelist()
    def on_trash(self):
        for tem in self.employee_details:
            name=frappe.db.get_value("Salary Pay Slip", {"based_on":self.name},['name'])
            # if self.name == name:
            frappe.delete_doc("Salary Pay Slip", name)
            frappe.db.commit()
        frappe.msgprint(("Salary Pay Slip Deleted"))
