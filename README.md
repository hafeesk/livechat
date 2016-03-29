## LiveChat

A live chat inside ERPNext.

This APP is currently under development.

#### License

GNU GENERAL PUBLIC LICENSE (v3)

### Instructions

##### Client

- The livechat client is accessible on the webpage: http://yourerpnextdomain/chat

###### Creating a new Conversation.
- Write an email on the Email box. (If you are logged in on ERPNext this box will be dissabled and
  instead it will appear the name of the user).
- Press the button "Create Conversation".

NOTES: This will create a new conversation on the system, asigned to a chat agent and to the email which the
user has introduced.
The conversation is stored on a cookie, so if the user tries to create another conversation after that,
a message will appear and won't allow the creation.

###### Sending Messages
- Write a message on the Message box.
- Press the button "Send Message"

##### ERPNext

###### Reading a Conversation and Sending new messages
- Access to the module "Livechat" -> "Chat Conversation".
- Select the conversation to send messages (the list of conversations is filtered by the current user).
- Send new messages writing them on the text box "Message Text" and press the button "Send".