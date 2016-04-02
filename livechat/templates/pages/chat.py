from __future__ import unicode_literals
import frappe
import frappe.website.render

page_title = "Livechat"

def get_context(context):
    user = frappe.session.user
    return {
        "user": user
    }

