import telethon
import asyncio
import logging
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
#        updates = client(ImportChatInviteRequest('AAAAAEHbEkejzxUjAUCfYg'))
from config import coll_to_do
import datetime
import time
from datetime import datetime, timedelta
from time import strftime
api_id = 1026835
api_hash = 'bc2fbb95a2983a6add248370f6fe7a49'
loop = asyncio.get_event_loop()
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

async def s(chat):

#    channel = await client.get_entity(chat)

    await client(JoinChannelRequest(channel))

while True:
    
    try:
        
        target = coll_to_do.find_one({'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        
        target['type']
        
    except TypeError:
        
        pass
    
    else:
        print(1)
        try:
            
            target['row']
            
        except TypeError:#пишем по сессиям
       
           client = TelegramClient(target['session'], api_id, api_hash)
           
           client.start()
     
           loop.run_until_complete(s(target['channel'])) 
            
           client.disconnect()

        else:#пишем по сплошным целям  
          
          for x in range(1, target['row']):
              
              client = TelegramClient(str(x), api_id, api_hash)
              
              client.start()
              
              loop.run_until_complete(s(target['channel']))   

              client.disconnect()
 



     
