 var dtls = frm.doc.details;
        var totamount = 0
        for(var i in dtls) {
    		if (dtls[i].amount)
    		{
    		totamount = totamount + Number(dtls[i].amount)
    		}
    	}
    	var totqty = 0
        for(var i in dtls) {
    		if (dtls[i].qty)
    		{
    		totqty = totqty + Number(dtls[i].qty)
    		}
    	}
    
    	frm.set_value("total_amount",totamount)
    	frm.set_value("total_qty",totqty)
