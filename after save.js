frappe.ui.form.on('Fetch Bank Statement', {
	after_save: (frm) =>{
		// alert(123)
			frappe.call({
					method:"Generate_Entries",
					doc: frm.doc,
					callback: function(r) {
            if (r.message) {
                // prepare the xml file for download
                console.log(r.message.content);

            }
        }
		    })


	}
	,
	after_delete: (frm) =>{
			frappe.call({
					method:"on_trash",
					doc: frm.doc,
					callback: function(r) {
            if (r.message) {
                console.log(r.message.content);

            }
        }
		    })


	}
});
