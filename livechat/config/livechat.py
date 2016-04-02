from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("History"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Chat Conversation",
					"description": _("View all conversations"),
				},
			]
		},
		{
			"label": _("Agents - TODO"),
			"icon": "icon-star",
			"items": [
				{
					"type": "report",
					"name":"List of agents",
					"doctype": "User",
					"is_query_report": True,
				},
			]
		}
	]
