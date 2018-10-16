
import stomp

dest='/queue/ds_remedy' 

class MQListener(stomp.ConnectionListener):
    def __init__(self):
        super(MQListener, self).__init__()
        self.message = []

    def on_connecting(self):
    	print 'connecting'

    def on_connected(self):
    	print 'connected!'

conn = stomp.Connection([('91.216.147.50', 27685)]) 
conn.set_listener('', MQListener()) 
conn.start() 
conn.connect(username='admin', passcode='admin') 
message = 'test'

conn.send(body=message, destination=dest, headers={'transformation' : 
   'jms-map-xml'}, ack='auto') 
conn.disconnect() 