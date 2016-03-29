# -*- coding: utf-8 -*-
# Copyright (c) 2015, Semilimes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime
import random

class ChatConversation(Document):

	def validate(self):
		# Sets the starting date of the conversation
		if not self.starting_date:
			self.starting_date = now_datetime()
		# Sets an random hash for the communication. It is truncated because it will be used for events
		if not self.random_id:
			self.random_id = frappe.generate_hash()[:10]
		if not self.chat_user:
			return frappe.msgprint("Please, insert a chat user.", raise_exception=1)


@frappe.whitelist()
def get_chat_users():
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
def create_chat_conversation(user):
	'''
	Creates a new chat conversation and inserts it into the database.
	:param user: chat user
	:return: name of the conversation + hash of the conversation
	'''
	# Creates a new conversation and adds the attributes
	conversation = frappe.new_doc("Chat Conversation")
	# Selects a random chat agent
	chat_agents = get_chat_agents("","","","","","")
	agents = []
	for agent in chat_agents:
		if(agent[0] != 'Administrator'):
			agents.append(agent[0])
	conversation.chat_agent = random.choice(agents)
	# Sets the conversation user
	conversation.chat_user = user
	# Inserts the conversation
	conversation.flags.ignore_permissions = True
	conversation.insert()

	return conversation.name + "." + conversation.random_id




