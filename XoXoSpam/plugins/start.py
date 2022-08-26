
import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from XoXoSpam import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID

XoXo_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/b9aac31b258ffce033ffb.jpg"

XoXo_Button = [
        [
        Button.url("🥀 sᴜᴘᴘᴏʀᴛ 🥀", "https://t.me/XoXoSpamtBot")
        ],
        [
        Button.url("❤️ ᴍᴀɪɴᴛᴀɪɴᴇʀ ʙʏ ❤️", "https://t.me/XoXoSpamtBot")
        ]
        ]
               
XoXox_Button = [
        [
        Button.url("🌹 ᴄʜᴀɴɴᴇʟ 🌹", "https://t.me/XoXoSpamtBot"),
        Button.url("💞 sᴜᴘᴘᴏʀᴛ 💞", "https://t.me/XoXoSpamtBot")
        ],
        [
        Button.url("❄️ ʀᴇᴘᴏ ❄️", "https://github.com/TeamLegend77/XoXo-XSpam")
        ]
        ]
        
        
#USERS 


@BOT0.on(events.NewMessage(pattern="/start"))
@BOT1.on(events.NewMessage(pattern="/start"))
@BOT2.on(events.NewMessage(pattern="/start"))
@BOT3.on(events.NewMessage(pattern="/start"))
@BOT4.on(events.NewMessage(pattern="/start"))
@BOT5.on(events.NewMessage(pattern="/start"))
@BOT6.on(events.NewMessage(pattern="/start"))
@BOT7.on(events.NewMessage(pattern="/start"))
@BOT8.on(events.NewMessage(pattern="/start"))
@BOT9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       XoXoBot = await event.client.get_me()
       bot_id = XoXoBot.first_name
       bot_username = XoXoBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheXoXo = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**ʜɪ ᴍᴀsᴛᴇʀ, ɪᴛs ᴍᴇ {bot_id}, ʏᴏᴜʀ sᴘᴀᴍ ʙᴏᴛ !! \n\n ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ ʜᴇʟᴘ 🥀**"
       usermsg = f"**ʜᴇʟʟᴏ, {firstname} ! ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ, ᴡᴇʟʟ ɪ ᴀᴍ {bot_id}, ᴀɴ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ ʙᴏᴛ 🔥!** \n\n**ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ sᴘᴀᴍ ʙᴏᴛs ʏᴏᴜ ᴄᴀɴ ᴅᴇᴘʟᴏʏ ғʀᴏᴍ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ 👇!** \n\n**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheXoXo,
                  XoXo_IMG,
                  caption=ownermsg, 
                  buttons=XoXo_Button)
       else:
            await event.client.send_file(TheXoXo,
                  XoXo_IMG,
                  caption=usermsg, 
                  buttons=XoXox_Button)
                
