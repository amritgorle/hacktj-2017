import fbchat
import pdb
from random import shuffle
#subclass fbchat.Client and override required methods
class EchoBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message_new(self, mid, author_id, message, metadata, recipient_id, thread_type):
        pdb.set_trace()
        if "hey Rishabh" in message:
        	#pdb.set_trace()
        	pass
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read

        print("%s said: %s"%(author_id, message))

        #if you are not the author, echo
        if str(author_id) != str(self.uid):
        	wordLis=message.split(" ")
        	shuffle(wordLis)
        	s=""
        	for elem in wordLis:
        		s+=elem+" "
        	self.send(recipient_id,s,message_type=thread_type)
password=input("Password: ")
bot = EchoBot("rishabh.krishnan@gmail.com", password)
bot.listen()