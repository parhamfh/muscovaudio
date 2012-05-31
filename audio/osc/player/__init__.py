'''
Created on May 26, 2012

@author: parhamfh
'''
import OSC 

class OSCPlayer(object):
    def __init__(self, ip_address, port, osc_address):
        self.ip_address = ip_address
        self.port = port
        self.base_osc_address = osc_address
        self.client = OSC.OSCClient()

    def open_connection(self):
        try:
            self.client.connect((self.ip_address,self.port))
        except OSC.OSCClientError, o:
            print o
    
    def close_connection(self):
        self.send_message(0, '/stop')
        self.client.close()
    
    def send_message(self, message, osc_address):
        
        osc_message = OSC.OSCMessage("{0}{1}".format(self.base_osc_address, osc_address))
        osc_message.append(message)
        try:
            self.client.send(osc_message, 3)
        except OSC.OSCClientError, o:
            print o
        
    def send_bundle(self, bundle):
        raise NotImplementedError
    
    def set_address(self, address):
        self.osc_address = address
