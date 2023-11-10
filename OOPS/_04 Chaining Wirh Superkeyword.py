class whatapp_version1():   
    def chatting(self):
        print('Text Message')
class whatapp_version2(whatapp_version1):
    def chatting(self):
        super().chatting()
        print('Voice Message')
        print('Image Message')
        print('video calling')
    
    def call(self):
        print('Voice call')
class whatapp_version3(whatapp_version2):
    def call(self):
        super().call()
        print('Video Call')
B1=whatapp_version1()
B2=whatapp_version2()
B3=whatapp_version3()

# B1.chatting()
# B2.chatting()
B3.call()