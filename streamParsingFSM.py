# You are receiving a continuous byte stream from a Bluetooth sensor. 
# A valid packet always starts with a 0xAA header, followed by 1 byte representing the payload length N, 
# followed by N bytes of data, and ending with a 1-byte checksum. 
# Write a function to parse this stream and return valid payloads, dropping corrupted data

# 0XAA, 
# 0xN
# 0....N bytes (payload)
# Checksum

class FSM():
    def __init__(self):
        self.state="WAIT_HEADER"
        self.payload=[]
        self.expected_length=0
    
    def parseStream(self, chunks):

        valid_payloads=[]

        for byte in chunks:
            
            if(self.state=="WAIT_HEADER"):
                if(byte==0xAA):
                    self.state="READ_LENGTH"
            elif self.state=="READ_LENGTH":
                self.expected_length=int(byte)
                self.payload=[]
                self.state="READ_PAYLOAD_CHUNK"
            elif self.state=="READ_PAYLOAD_CHUNK":
                
                self.payload.append(byte)
                if(len(self.payload)==self.expected_length):
                    self.state="CHECK_CHECKSUM"
            elif self.state=="CHECK_CHECKSUM":
                checksum=byte
                if(self.checkChecksum(self.payload)==checksum):
                    valid_payloads.append(list[self.payload])
                self.state="WAIT_HEADER"
    
        return valid_payloads

    def checkChecksum(self, payload):
        return sum(byte for byte in payload)&0xFF

            

