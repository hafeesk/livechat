# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "livechat"
app_title = "LiveChat"
app_publisher = "Semilimes"
app_description = "A live chat inside ERPNext."
app_icon = "octicon octicon-file-directory"
app_color = "'green'"
app_email = "support@semilimes.com"
app_version = "0.0.1"
app_license = "GNU GENERAL PUBLIC LICENSE v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/livechat/css/livechat.css"
# app_include_js = "/assets/livechat/js/livechat.js"

# include js, css files in header of web template
# web_include_css = "/assets/livechat/css/livechat.css"
# web_include_js = "/assets/livechat/js/livechat.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "livechat.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "livechat.install.before_install"
# after_install = "livechat.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

notification_config = "livechat.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"livechat.tasks.all"
# 	],
# 	"daily": [
# 		"livechat.tasks.daily"
# 	],
# 	"hourly": [
# 		"livechat.tasks.hourly"
# 	],
# 	"weekly": [
# 		"livechat.tasks.weekly"
# 	]
# 	"monthly": [
# 		"livechat.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "livechat.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "livechat.event.get_events"
# }

