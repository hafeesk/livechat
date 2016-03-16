frappe.ready(function(){

    $('.btn-send-message').off("click").on("click", function(){
        var message = $('[name="message"]').val()

        if(!message) {
            frappe.msgprint(__("Please, enter a message."));
            return false;
        } else {
            return frappe.call({
                method: "livechat.livechat.doctype.livechat_message.livechat_message.echo",
                args: { text: message }
            });
        }

        return false;
    });


     $('.btn-create-conversation').off("click").on("click", function(){


     });
});
