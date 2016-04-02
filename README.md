## LiveChat

A live chat inside ERPNext.

This APP is currently under development.

#### License

GNU GENERAL PUBLIC LICENSE (v3)


### Installation

1. In the command line

-`home/frappe/frappe-bench/`
-`bench get-app livechat https://github.com/semilimes/livechat`

2. In the ERPNext GUI

- Type "App Installer" in the 'awesome bar' (on the Top right) and open it
- find the "livechat" app & click on 'install'


### Instructions

##### Roles
There are two roles for the Livechat APP that should be configured for the users of the APP in order to use
it from ERPNext. These roles are:

- **Agent User**. The Agents are the workers of the company that should answer the questions that the customers
will make through the Livechat APP. Agents have permissions to Read, Write, Create and Delete Conversations.
Have in mind that in order to start any new Conversation is necessary that you add this role to one or more
users and that this user will be online.

- **Chat User**. The Chat Users are the customers that will have an account created on the company's system. Chat
Users have permissions to Read, Write and Create Conversations.

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

