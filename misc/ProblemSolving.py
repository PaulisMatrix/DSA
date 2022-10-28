def rot13(message):
    Caps = {}
    Small = {}
    mycaps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mysmall = [str(x.lower()) for x in mycaps]

    for i,v in enumerate(mycaps,1):
        Caps.update({v:i})
    
    for i,v in enumerate(mysmall,1):
        Small.update({v:i})

    for i in range(0,len(message)):
        if message[i].isupper():
            temp = Caps[message[i]] + 13
            if temp > 26 :
                temp = temp - 26
                for key,value in Caps.items():
                    if value == temp:
                        toreplace=key
                        message=message.replace(message[i],toreplace,1)
            else:
                for key,value in Caps.items():
                    if value == temp:
                        toreplace=key
                        message=message.replace(message[i],toreplace,1)
            
        else:
            temp1 = Small[message[i]] + 13
            if temp1 > 26:
                temp1 = temp1 - 26
                for key1,value1 in Small.items():
                    if value1 == temp1:
                        toreplace1=key1
                        message=message.replace(message[i],toreplace1,1) 
            else:
                for key,value in Small.items():
                    if value == temp1:
                        toreplace1=key
                        message=message.replace(message[i],toreplace1,1)
    print(message)        
    
rot13("Test")


