frappe.listview_settings['Chat Conversation'] = {
    onload: function() {
		this.setup_filters();
	},

	refresh: function() {
	    this.setup_filters();
	},

	setup_filters: function(){
	    if (user != "Administrator"){
            // Default Filters
            var agent = $.inArray("Agent User", user_roles)
            // If the user is an agent, then we apply to filter the conversations by agent
            if(agent != -1){
                frappe.route_options = {
                    "chat_agent": user
                };
            // If the user is not an agent, then we filter the conversations by user
            } else {
                frappe.route_options = {
                    "chat_user": user
                };
            }
    	}
	}

}