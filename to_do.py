import telethon
import asyncio
import logging
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, GetMessagesViewsRequest, SendVoteRequest
#        updates = client(ImportChatInviteRequest('AAAAAEHbEkejzxUjAUCfYg'))
from config import coll_to_do, coll_targets
import datetime
import time
from datetime import datetime, timedelta
from time import strftime
api_id = 1026835
api_hash = 'bc2fbb95a2983a6add248370f6fe7a49'
loop = asyncio.get_event_loop()
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
                    
                    
#ПОДПИСКИ
async def s(channel):

 #   channel = await client.get_input_entity(chat)
 
    if ('joinchat' in channel) and ('https' in channel):    
    
        channel = channel[22: ]
        try:

            await client(ImportChatInviteRequest(channel))

        except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:

            pass

    elif ('joinchat' in channel) and (not 'https' in channel):
    
        channel = channel[14: ]
        
        await client(ImportChatInviteRequest(channel))

    elif '@' in channel:
        
        channel = channel[1: ]
       
        await client(JoinChannelRequest(channel))

    else:
       
        await client(JoinChannelRequest(channel))

    coll_targets.update_one(
        {
        '#': target['#'],
        'owner': target['owner']
        },
        {
        '$set':
            {
            'status': 'Complete'
            }
        }
        )

#ПРОСМОТРЫ ПОСТОВ
async def v_p(channel, msg_id):
    
    await client(GetMessagesViewsRequest(
        peer = channel,
        id = [msg_id],
        increment = True
        )
        )
    coll_targets.update_one(
        {
        '#': target['#'],
        'owner': target['owner']
        },
        {
        '$set':
            {
            'status': 'Complete'
            }
        }
        )


#ПРОСМОТРЫ КАНАЛОВ
async def v_c(channel):
    
    messages = await client.get_messages(channel)
    
    messages_id = []
    
    for x in range(0, len(messages)):
        
        messages_id.add(messages[x].id)
    
    await client(GetMessagesViewsRequest(
        peer = channel,
        id = [messages_id],
        increment = True
        )
        )

    coll_targets.update_one(
        {
        '#': target['#'],
        'owner': target['owner']
        },
        {
        '$set':
            {
            'status': 'Complete'
            }
        }
        )



async def v(client, channel, msg_id):  
 
                msg = await client.get_messages(channel, ids = msg_id)            
    
                answers = msg.media.poll.answers
    
                w = 2
                
                print(len(answers))

                for z in range(1, len(answers)+1):
        
                    for y in range(int(target[str(z)]*target['row']*0.01)):
            
                        clients = TelegramClient(str(w), api_id, api_hash)
                  
                        await clients.start()

                        print(msg.media.poll.answers[z-1].option)

                        await clients(SendVoteRequest(
                            peer=channel,
                            msg_id=msg_id,         
                            options = [msg.media.poll.answers[z-1].option]
                            ))    
                        await client.disconnect()

                        w += 1

                coll_targets.update_one(
                    {
                    '#': target['#'],
                    'owner': target['owner']
                    },
                    {
                    '$set':
                        {
                        'status': 'Complete'
                        }
                    }
                    )


#----------------------------------------------------------------------------------
while True:    
    try:        
        target = coll_to_do.find_one({'date': ( datetime.now()+timedelta(minutes = 120) ).strftime('%Y-%m-%d %H:%M:%S')})     
        
        target['type']    
           
    except TypeError:        
        pass
    
    else:
           
        if target['type'] == 'subscribtion':            
            try:                
                target['row']   
                print('£') 
          
            except (KeyError, TypeError):#пишем по сессиям     
                  
               client = TelegramClient(str(target['session']), api_id, api_hash)
               client.start()        
               loop.run_until_complete(s(target['channel']))                
               client.disconnect()    
               
            else:#пишем по сплошным целям     
                      
              for x in range(1, target['row']+1):    
                  print(x)         
                  client = TelegramClient(str(x), api_id, api_hash)                 
                  client.start()                  
                  loop.run_until_complete(s(target['channel']))
                  client.disconnect()
    
            coll_to_do.delete_one({'date': target['date']})











        elif target['type'] == 'view_posts':            
            try:                
                target['row']                
            except (KeyError, TypeError):#пишем по сессиям     
                              
            
               client = TelegramClient(str(target['session']), api_id, api_hash)               
               client.start()         
               loop.run_until_complete(v_p(target['channel'], target['message_id']))                 
               client.disconnect()
                   
            else:#пишем по сплошным целям  
                          
              for x in range(1, target['row']+1):                  
                  client = TelegramClient(str(x), api_id, api_hash)                  
                  client.start() 
                 
                  loop.run_until_complete(v_p(target['channel'], target['post']))                                                    
                  client.disconnect()
    
            coll_to_do.delete_one({'date': target['date']})
      
        
                    
                                
                                            
                                                        
                                                                    
   
                                                                                            
                                                                                                                                                                                                                                                                              
        elif target['type'] == 'view_channel':            
            try:                
                target['row']                
            except (KeyError, TypeError):#пишем по сессиям     
                                         
               client = TelegramClient(str(target['session']), api_id, api_hash)              
               client.start()
         
               loop.run_until_complete(v_c(target['channel']))                 
               client.disconnect()
    
            else:#пишем по сплошным целям  
              
              for x in range(1, target['row']+1):                  
                  client = TelegramClient(str(x), api_id, api_hash)                  
                  client.start()             
                  loop.run_until_complete(v_c(target['channel']))                  
                  client.disconnect()
    
            coll_to_do.delete_one({'date': target['date']})

                                                                               
                                                                                                                                                              
                                                                                                                                                                                                                                             
  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        elif target['type'] == 'vote':
#            
#            try:
#                
#                target['row']
#                
#            except (KeyError, TypeError):#пишем по сессиям     
                  #           
#               client = TelegramClient(target['session'], api_id, api_hash)
#               
#               client.start()
#         
#               loop.run_until_complete(v_p(target['channel'], target['message_id'])) 
#                
#               client.disconnect()
#    
#            else:#пишем по сплошным целям               
               
                client = TelegramClient('1', api_id, api_hash)
                client.start()

                loop.run_until_complete(v(client, target['channel'], target['message_id']))
                client.disconnect()
                coll_to_do.delete_one({'date': target['date']})
                                                                                                              
