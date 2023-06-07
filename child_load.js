frappe.call({
                    method: "frappe.frappe.client.get_estimate_purchase_items",
                    args: { "date":frm.doc.load_date },
                    callback: function(r) {
                        if(!r.exc && r.message) {
                            var company = r.message[0];
                            for (var i = 0; i < r.message.length; i++) {
                                var d = frm.add_child("details");
                                var item = r.message[i];
                                for (var key in item) {
                                    if (!is_null(item[key])) {
                                        // alert(item['item'])
                                        if (key === 'item') d.item = item[key];
                                        if (key === 'qty') d.qty = item[key];
                                        if (key === 'rate')d.rate = item[key];
                                       if (key === 'warehouse') d.warehouse = item[key];
                                        d.amount =Number(d.qty)*Number(d.rate);
                                        
                                    }
                                }
                            }
                            frm.refresh_field('details');
                            // frm.set_value("total_taxes_and_charges", total_tax_amount);
                        }
                    }
                });
