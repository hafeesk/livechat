# -*- coding: utf-8 -*-
# Copyright (c) 2015, Semilimes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe.model.document import Document
from frappe.desk.notifications import clear_doctype_notifications

class LivechatMessage(Document):

	'''def validate(self):
		#Establish the current date
		self.date_sent = getdate(now())

	def on_update(self):
		if not self.date_sent:
			self.date_sent = getdate(now())'''

	# Realtime Update
	def after_insert(self):
		if not (self and self.name):
			return

		# Obtains the conversation linked to this Livechat Message
		conversation = frappe.get_doc('Chat Conversation', self.parent)
		# Sends new comment to listening clients so they get a realtime update
		frappe.publish_realtime('new_message', self.as_dict(),
				doctype= 'Chat Conversation', docname = conversation.name,
				after_commit=True)
		frappe.publish_realtime(event='livechat_update', message='''{u'doctype': u'Livechat Message'}''')

	# Clear the notifications of the doctype after update them
	def on_update(self):
		clear_doctype_notifications(self)


@frappe.whitelist()
def add_message(doc):
	'''
	Add a message to the database
	:param doc: json with the required data to create a doctype Livechat Message
	:return:
	'''
	# Loads the json
	json_doc = json.loads(doc)

	# Extracts the conversation to obtain the id of the last message from the database
	conversation = json_doc['parent']
	last_id = get_last_id(conversation)

	# Adds one to the id to set the following message
	json_doc['idx'] = last_id + 1
	#print  json.dumps(json_doc, indent=4, sort_keys=True)

	# Creates the doctype from the json data
	doc = frappe.get_doc(json_doc)

	# Checks that the doctype is a Livechat Message
	if not (doc.doctype=="Livechat Message"):
		frappe.throw(_("This method can only be used to create a Livechat Message"), frappe.PermissionError)

	# Insert the doctype on the database
	doc.insert(ignore_permissions=True)

	return doc.as_dict()


@frappe.whitelist()
def get_last_id(conversation):
	'''
	Obtains the id of the last message added to the database in the conversation
	:param conversation: conversation where we want to add the message
	:return: id of the last message added
	'''
	last_id = frappe.db.sql(
		'''select idx from `tabLivechat Message`
			where parent = "''' + conversation +
		'''" order by idx desc limit 1'''
	)

	if last_id:
		return int(last_id[0][0])
	else:
		return 0

@frappe.whitelist()
def mark_messages_as_seen(conversation):
	'''
	Marks the messages of an opened conversation as seen.
	:param conversation: name of the conversation
	:return: --
	'''
	frappe.db.sql("""update `tabLivechat Message` set seen=1
		where seen=0 and parent = %s""", (conversation,))

@frappe.whitelist(allow_guest=True)
def echo(text):
    frappe.msgprint(text)






