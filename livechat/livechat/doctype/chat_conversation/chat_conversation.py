# -*- coding: utf-8 -*-
# Copyright (c) 2015, Semilimes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime

class ChatConversation(Document):

	def validate(self):
		if not self.starting_date:
			self.starting_date = now_datetime()

def get_chat_users(doctype, txt, searchfield, start, page_len, filters):
	'''
	Obtains the name of the users who have a role 'Chat User'
	:return: name of the user
	'''
	return frappe.db.sql('''
		select name from `tabUser` where name in (select parent from `tabUserRole` where role = 'Chat User')
	''')

def get_chat_agents(doctype, txt, searchfield, start, page_len, filters):
	'''
	Obtains the name of the users who have a role 'Agent User'
	:return: name of the user
	'''
	return frappe.db.sql('''
		select name from `tabUser` where name in (select parent from `tabUserRole` where role = 'Agent User')
	''')

@frappe.whitelist(allow_guest=True)
def create_chat_conversation(user, ip):
	# FIXME: The ip should be passed
	ip = frappe.local.request_ip

	return




