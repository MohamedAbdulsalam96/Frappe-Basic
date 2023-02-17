@frappe.whitelist()
    def Generate_Entries(self):
        acc=frappe.db.get_value("Bank Account", {"name":self.bank_ac},"account")
        details = []
        for tx in self.statement_details:
            if tx.voucher_type == 'Bank Entry':
                dtls={
                    'account':acc,
                    'party_type':'',
                    'party':'',
                    'cost_center':'Main - GO',
                    'debit_in_account_currency':tx.debit,
                    'credit_in_account_currency':tx.credit,
                    'reference_type':'Fetch Bank Statement',
                    'reference_name':self.name,
                    'user_remarks':tx.description
                    }
                dtls1={
                    'account':'Creditors - GWW',
                    'party_type':tx.party_type,
                    'party':tx.party,
                    'cost_center':'Main - GO',
                    'debit_in_account_currency':tx.credit,
                    'credit_in_account_currency':tx.debit,
                    'reference_type':'Fetch Bank Statement',
                    'reference_name':self.name

                    }
                details.append(dtls)
                details.append(dtls1)
            if tx.voucher_type == 'Contra Entry':
                dtls={
                    'account':acc,
                    'party_type':'',
                    'party':'',
                    'cost_center':'Main - GO',
                    'debit_in_account_currency':tx.debit,
                    'credit_in_account_currency':tx.credit,
                    'reference_type':'Fetch Bank Statement',
                    'reference_name':self.name,
                    'user_remarks':tx.description
                    }
                dtls1={
                    'account':'CASH IN HAND JAIPUR WAREHOUSE - GWW',
                    'party_type':tx.party_type,
                    'party':tx.party,
                    'cost_center':'Main - GO',
                    'debit_in_account_currency':tx.credit,
                    'credit_in_account_currency':tx.debit,
                    'reference_type':'Fetch Bank Statement',
                    'reference_name':self.name

                    }
                details.append(dtls)
                details.append(dtls1)

            if tx.voucher_type == 'Payment Entry' and tx.credit != '0' :
                if tx.party_type == 'Supplier':
                    lead = frappe.get_doc({
                        'doctype':'Payment Entry',
                        'company': self.company,
                        'posting_date': frappe.utils.nowdate(),
                        'bank_account':self.bank_ac,
                        'party_type':tx.party_type,
                        'party':tx.party,
                        'remarks':tx.description,
                        'reference_date':tx.date,
                        'reference_no':tx.trans_id,
                        'cheque_date':tx.date,
                        'paid_amount': tx.credit,
                        'payment_type': 'Receive',
                        'paid_to':acc,
                        'paid_to_account_currency':'INR',
                        'paid_from_account_currency':'INR',
                        'received_amount':'INR',
                        'base_received_amount':'INR',
                        'target_exchange_rate':1,
                        'paid_from':'Creditors - GWW'

                        })
                    lead.insert(ignore_permissions=False)
                    frappe.msgprint(("Payment Entry Created"))
                if tx.party_type == 'Customer':
                    lead = frappe.get_doc({
                        'doctype':'Payment Entry',
                        'company': self.company,
                        'posting_date': frappe.utils.nowdate(),
                        'bank_account':self.bank_ac,
                        'party_type':tx.party_type,
                        'party':tx.party,
                        'remarks':tx.description,
                        'reference_date':tx.date,
                        'reference_no':tx.trans_id,
                        'cheque_date':tx.date,
                        'paid_amount': tx.credit,
                        'payment_type': 'Receive',
                        'paid_to':acc,
                        'paid_to_account_currency':'INR',
                        'paid_from_account_currency':'INR',
                        'received_amount':'INR',
                        'base_received_amount':'INR',
                        'target_exchange_rate':1,
                        'paid_from':'Debtors - GWW'
                        })
                    lead.insert(ignore_permissions=False)
                    frappe.msgprint(("Payment Entry Created"))

            if tx.voucher_type == 'Payment Entry' and tx.credit == '0' :
                if tx.party_type == 'Supplier':
                    lead = frappe.get_doc({
                        'doctype':'Payment Entry',
                        'company': self.company,
                        'posting_date': frappe.utils.nowdate(),
                        'bank_account':self.bank_ac,
                        'party_type':tx.party_type,
                        'party':tx.party,
                        'remarks':tx.description,
                        'reference_date':tx.date,
                        'reference_no':tx.trans_id,
                        'cheque_date':tx.date,
                        'paid_amount':tx.debit,
                        'payment_type': 'Pay',
                        'paid_from':acc,
                        'paid_to_account_currency':'INR',
                        'paid_from_account_currency':'INR',
                        'received_amount':'INR',
                        'base_received_amount':'INR',
                        'target_exchange_rate':1,
                        'paid_to':'Creditors - GWW'
                        })

                    lead.insert(ignore_permissions=False)
                    frappe.msgprint(("Payment Entry Created"))
                if tx.party_type == 'Customer':
                    lead = frappe.get_doc({
                        'doctype':'Payment Entry',
                        'company': self.company,
                        'posting_date': frappe.utils.nowdate(),
                        'bank_account':self.bank_ac,
                        'party_type':tx.party_type,
                        'party':tx.party,
                        'remarks':tx.description,
                        'reference_date':tx.date,
                        'reference_no':tx.trans_id,
                        'cheque_date':tx.date,
                        'paid_amount':tx.debit,
                        'payment_type': 'Pay',
                        'paid_from':acc,
                        'paid_to_account_currency':'INR',
                        'paid_from_account_currency':'INR',
                        'received_amount':'INR',
                        'base_received_amount':'INR',
                        'target_exchange_rate':1,
                        'paid_to':'Debtors - GWW'
                        })

                    lead.insert(ignore_permissions=False)
                    frappe.msgprint(("Payment Entry Created"))

            if tx.voucher_type == 'Bank Entry':
                lead = frappe.get_doc({
                    'doctype':'Journal Entry',
                    'company': self.company,
                    'posting_date': frappe.utils.nowdate(),
                    'voucher_type':tx.voucher_type,
                    'cheque_no':tx.trans_id,
                    'cheque_date':tx.date,
                    'total_debit':tx.debit,
                    'total_credit':tx.credit,
                    'accounts':details
                    })

                lead.insert(ignore_permissions=False)
                frappe.msgprint(("Journal Entry Created"))
            if tx.voucher_type == 'Contra Entry':
                lead = frappe.get_doc({
                    'doctype':'Journal Entry',
                    'company': self.company,
                    'posting_date': frappe.utils.nowdate(),
                    'voucher_type':tx.voucher_type,
                    'cheque_no':tx.trans_id,
                    'cheque_date':tx.date,
                    'total_debit':tx.debit,
                    'total_credit':tx.credit,
                    'accounts':details
                    })

                lead.insert(ignore_permissions=False)
                frappe.msgprint(("Journal Entry Created"))


    @frappe.whitelist()
    def on_trash(self):
        for tx in self.statement_details:
            if tx.voucher_type == 'Payment Entry':
                transaction_id,name=frappe.db.get_value("Payment Entry", {"reference_no":tx.trans_id},["reference_no",'name'])
                if tx.trans_id == transaction_id:
                    frappe.delete_doc("Payment Entry", name)
                    frappe.db.commit()
                    frappe.msgprint(("Payment Entry Deleted"))

            if tx.voucher_type != 'Payment Entry':
                transaction_id,name=frappe.db.get_value("Journal Entry", {"cheque_no":tx.trans_id},["cheque_no",'name'])
                if tx.trans_id == transaction_id:
                    frappe.delete_doc("Journal Entry", name)
                    frappe.db.commit()
                    frappe.msgprint(("Journal Entry Deleted"))
