frappe.ready(function(){

    // Gets the current user
    var user = getCookie("user_id");
    // If there is an user logged (not guest), it sets the email field and disables it.
    if(user != "Guest"){
        $('[name="email"]').val(user);
        $('[name="email"').prop('disabled', true);
    }


     $('.btn-create-conversation').off("click").on("click", function(){
        var chat_user = $('[name=email').val();
        if(!chat_user){
            frappe.msgprint("Please, insert your email.");
            return;
        }
        var url = 'http://localhost:8000/api/resource/Chat Conversation?data={"chat_agent":"agent1@semilimes.com",';
        url += '"chat_user":"' + chat_user + '"}';
        var conversation = getCookie("livechat_conversation");
        if(!conversation){
            $.ajax({
                url: url,
                type: 'post',
                data: {
                    "chat_agent":"agent1@semilimes.com",
                    "chat_user":"chatuser1@semilimes.com"
                },
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-Frappe-CSRF-Token": frappe.csrf_token
                },
                dataType: 'json',
                success: function(data){
                    document.cookie="livechat_conversation=" + data.data.name;
                    document.getElementById("history").value += "\nConversation created: " + data.data.name;
                }
            });
        } else {
            frappe.msgprint("You have already created a conversation: " + conversation);
        }
     });



    $('.btn-send-message').off("click").on("click", function(){

        var url = 'http://localhost:8000/api/resource/Livechat Message?data={"parenttype":"Chat Conversation", "parentfield":"messages",';
        var date_sent = new Date().toISOString().slice(0, 19).replace('T', ' ');
        var parent = getCookie("livechat_conversation");
        var message = $('[name="message"]').val()

        if(!parent){
            frappe.msgprint(__("Please, create a new conversation."));
            return false;
        } else {
            if(!message) {
                frappe.msgprint(__("Please, enter a message."));
                return false;
            } else {
                url += '"sender":"' + user + '", "date_sent":"' + date_sent + '", "parent":"' + parent +'", "text": "' + message + '"}';
                console.log(url);
                $.ajax({
                url: url,
                type: 'post',
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-Frappe-CSRF-Token": frappe.csrf_token
                },
                dataType: 'json',
                success: function(data){
                    $('[name="message"]').val("");
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





