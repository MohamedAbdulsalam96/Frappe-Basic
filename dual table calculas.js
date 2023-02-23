	'per':  function(frm, cdt, cdn){
		// calculate_amount(frm, cdt, cdn);
		var dtls = frm.doc.earning
		var child = locals[cdt][cdn];
		var cal_head = 0
		var cal_head2 = 0
		for(var i in dtls){
			if (dtls[i].component == child.calc_head){
				var cal_head = Number(cal_head) + ((child.per/100) * dtls[i].amount).toFixed(2)
				
			}
			else{
				var cal_head = Number(cal_head) + 0
			}
			if (dtls[i].component == child.calc_head2){
				var cal_head2 = Number(cal_head2) + ((child.per/100) * dtls[i].amount).toFixed(2)
				
			}
			else{
				var cal_head2 = Number(cal_head2) + 0
			}
			// alert(Number(cal_head2))
			// alert(Number(cal_head) )
			frappe.model.set_value(cdt, cdn, "amount",  (Number(cal_head) + Number(cal_head2)).toFixed(2));
			
		}
		
		
	}
