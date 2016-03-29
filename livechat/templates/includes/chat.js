frappe.ready(function(){

    // Gets the current user
    var user = getCookie("user_id");
    // If there is an user logged (not guest), it sets the email field and disables it.
    if(user != "Guest"){
        $('[name="email"]').val(user);
        $('[name="email"').prop('disabled', true);
    }

    // Gets the conversation if it is established and sets the listener ( in case of refreshing webpage )
    var convCookie = getCookie("livechat_conversation");
    if(convCookie){
        document.getElementById("history").value += "\nListening messages from Conversation: "
            + get_conversation_name(convCookie);
        setListener(convCookie);
    }

    // Button "Create a conversation"
    $('.btn-create-conversation').off("click").on("click", function(){
        // Obtains the email from the field
        var chat_user = $('[name=email').val();
        if(!chat_user){
            frappe.msgprint("Please, insert your email.");
            return;
        }
        // Check if the user already created a conversation
        var conversation = getCookie("livechat_conversation");
        if(!conversation){
            // Creates a new conversation
            return frappe.call({
                method: "livechat.livechat.doctype.chat_conversation.chat_conversation.create_chat_conversation",
                args: {
                    user: chat_user
                },
                callback: function(r){
                    if(!r.exc) {
                        document.cookie = "livechat_conversation=" + r.message;
                        document.getElementById("history").value += "\nConversation created! "
                            + get_conversation_name(r.message);
                        setListener(r.message);
                    }
                }
            });
        } else {
            frappe.msgprint("You have already created a conversation: " + get_conversation_name(conversation));
        }
     });

    // Button "Send Message"
    $('.btn-send-message').off("click").on("click", function(){
        var date_sent = new Date().toISOString().slice(0, 19).replace('T', ' ');
        var conv_hash = getCookie("livechat_conversation");
        var conversation_name = conv_hash.split(".");
        var message = $('[name="message"]').val();

        if(!parent){
            frappe.msgprint(__("Please, create a new conversation."));
            return false;
        } else {
            if(!message) {
                frappe.msgprint(__("Please, enter a message."));
                return false;
            } else {
                return frappe.call({
                    method: "livechat.livechat.doctype.livechat_message.livechat_message.send_client_message",
		            args: {
			            doc:{
				            doctype: "Livechat Message",
				            date_sent: date_sent,
				            text: message,
				            parent: conversation_name[0],
				            parenttype: "Chat Conversation",
				            parentfield: "messages"
			            },
			            hash: conv_hash
		            },
		            callback: function(r) {
			            if(!r.exc) {
			                $('[name="message"]').val("");
			            }
			        }
                });
            }
        }
        return false;
    });

});


function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}

function get_conversation_name(conversation_id){
    return conversation_id.split(".")[0];
}

