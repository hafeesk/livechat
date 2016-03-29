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
		# Sends notification to listening clients so they get a realtime update
		conv_hash = conversation.name + "." + conversation.random_id;
		frappe.publish_realtime(conv_hash, self.as_dict(),
				after_commit=True)

	# Clear the notifications of the doctype after update them
	def on_update(self):
		clear_doctype_notifications(self)


@frappe.whitelist(allow_guest=True)
def add_message(doc, client_call=False):
	'''
	Adds a message to the database
	:param doc: json with the required data to create a doctype Livechat Message
	:return:
	'''
	# Loads the json
	json_doc = json.loads(doc)

	# Extracts the conversation to obtain the id of the last message from the database
	conversation_name = json_doc['parent']
	last_id = get_last_id(conversation_name)

	# Adds one to the id to set the following message
	json_doc['idx'] = last_id + 1
	#print  json.dumps(json_doc, indent=4, sort_keys=True)

	# If this method is called by the client, the sender is set automatically as the chat user
	if(client_call):
		conversation_doc = frappe.get_doc('Chat Conversation', conversation_name)
		json_doc['sender'] = conversation_doc.chat_user

	# Creates the doctype from the json data
	doc = frappe.get_doc(json_doc)

	# Checks that the doctype is a Livechat Message
	if not (doc.doctype=="Livechat Message"):
		frappe.throw(_("This method can only be used to create a Livechat Message"), frappe.PermissionError)

	# Insert the doctype on the database
	doc.insert(ignore_permissions=True)

	return doc.as_dict()

@frappe.whitelist(allow_guest=True)
def send_client_message(doc, hash):
	'''
	Adds a message to the database from the client app
	:param doc: json with the required data to create a doctype Livechat Message
	:param hash: conversation name + unique hash
	:return:
	'''
	# Checks if the message is legit comparing the unique hash of the conversation
	if not(check_conversation_hash(hash)):
		frappe.msgprint("Your message could not be sent", raise_exception=1)
	# Adds the message
	add_message(doc, True)

def check_conversation_hash(hash):
	'''
	Checks if the unique hash of the conversation is correct
	:param hash: covnersation name + unique hash
	:return:
	'''
	# Divides into conversation name, hash
	conversation_name = hash.split(".")
	# Obtains the conversation doc
	conversation = frappe.get_doc('Chat Conversation', conversation_name[0])
	# Obtains the real hash
	real_hash = conversation_name[0] + "." + conversation.random_id
	# Compares if they are equals
	if(real_hash != hash):
		return False
	else:
		return True

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






