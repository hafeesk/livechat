import frappe

def get_notification_config():
    return { "for_doctype":
        {
            "Chat Conversation": "livechat.notifications.get_unread_chats"
        }
    }

def get_unread_chats():
    user = frappe.session.user
    return frappe.db.sql('''
        select count(*)
        from `tabChat Conversation`
        where (chat_user = %s
        OR chat_agent = %s)
        AND name IN (select distinct parent from `tabLivechat Message` where seen = 0);
    ''', (user,user))[0][0]
