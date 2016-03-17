// Copyright (c) 2016, Semilimes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Chat Conversation', {

	refresh: function(frm) {

        // Displays the users with the role Chat User on the select field.
        cur_frm.set_query("chat_user", function() {
            return {
                query: "livechat.livechat.doctype.chat_conversation.chat_conversation.get_chat_users"
            };
        });

        // Displays the users with the role Agent User on the select field.
        cur_frm.set_query("chat_agent", function() {
            return {
                query: "livechat.livechat.doctype.chat_conversation.chat_conversation.get_chat_agents"
            };
        });

        // Hides the current user (name) in the form
        frm.toggle_display("chat_user", frm.doc.chat_user!=user);
        frm.toggle_display("chat_agent", frm.doc.chat_agent!=user);
	},
});

// Set the messages as seen when the user opens the document
cur_frm.cscript.refresh = function(doc, cdt, cdn) {
    set_messages_as_seen(doc);
}

// Listen to the event livechat_update and calls to reload the doc
frappe.realtime.on("livechat_update",function(data){
    reload_doc_form();
});

// Reloads the doc and refresh the form
function reload_doc_form(){
    cur_frm.refresh();
    cur_frm.reload_doc();
}

// Button call
cur_frm.cscript.send_button = function(doc) {
   // Set the fields of the new Livechat Message
   // Message
   var message_text = doc.message_text
   // Date
   var date_sent = new Date()
   // Sender
   var sender = user
   // Conversation
   var parent_conversation = doc.name

   // Call to create a new doctype Livechat Message and refresh the table
   if(message_text){
      add_message(message_text, sender, date_sent, parent_conversation, doc);
      // Refresh the page and reloads the doc to show the message.
      reload_doc_form();
   } else {
      frappe.msgprint('Please, enter a message.');
   }
}

// Add a message to the conversation
function add_message(message_text, sender, date_sent, parent_conversation, doc){
    return frappe.call({
		method: "livechat.livechat.doctype.livechat_message.livechat_message.add_message",
		args: {
			doc:{
				doctype: "Livechat Message",
				date_sent: date_sent,
				sender: sender,
				text: message_text,
				parent: parent_conversation,
				parenttype: "Chat Conversation",
				parentfield: "messages",
			}
		},
		callback: function(r) {
			if(!r.exc) {
				// Delete and refresh the message from the text box
                doc.message_text = ""
                cur_frm.refresh_field("message_text")

                // Play sound
				frappe.utils.play_sound("click");
			}
		}
	});
}

// FIXME: Set the messages as seen (globally)
function set_messages_as_seen(doc){
    return frappe.call({
        method: "livechat.livechat.doctype.livechat_message.livechat_message.mark_messages_as_seen",
        args: { conversation: doc.name }
    });
}

