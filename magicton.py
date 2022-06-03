import time
from telethon import TelegramClient, events, sync

ip_id=input("API_id kodini kiritingn:")
ip_hash=input("API_hash kodini kiriting:")

api_id = 17875639
api_hash = "bee197361795bd8008a991df21dd4408"



client = TelegramClient('anon', api_id, api_hash)


 
 


@client.on(events.NewMessage)
async def my_event_handler(event):
    if '.d' in event.raw_text:
     d = ['🌏', '🌎', '🌍', '👋', '🤚', '🖖', '👌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👈', '👉', '👆', '👏', '🤔', '😈', '🖕']
     time.sleep(0.5)
     for i in range(5):
      time.sleep(0.5)
      for j in d:
       time.sleep(0.5)
       await event.edit(j)
       
@client.on(events.NewMessa+13046026598ge(outgoing = True, pattern="\alive"))
async def alivehandler(event):
    client = event.client
    me = await client.get_me()
    username = me.username
    dark = await client.download_profile_photo(username)
    await client.edit_message(event.message,"Salom Biz test rijimidamiz")
    await event.respond("My creator: @{}\nthis is test\nMy channel: @root_COMMANDER_X{}".format(username, '@root_COMMANDER_X'),file = dark)
       
       
       
client.start()
client.run_until_disconnected()
