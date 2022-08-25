from XoXoSpam import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from XoXoSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/b9aac31b258ffce033ffb.jpg"

XOXO_Help = "🔥 xᴏxᴏ sᴘᴀᴍ ʙᴏᴛ 🔥\n\n"
 
XOXO_Help += f"_ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ xᴏxᴏ ʙᴏᴛ__\n\n"

XOXO_Help += f" ↧ ᴜsᴇʀʙᴏᴛ ᴄᴍᴅs ↧\n\n"

XOXO_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots \n `.addecho` - to addecho \n `.rmecho` - To remove Echo \n `.addsudo` - To add sudo user using spam bot \n\n"
 
XOXO_Help += f" ↧ ʟᴇᴀᴠᴇ ᴄᴍᴅ ↧\n\n"

XOXO_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
XOXO_Help += f" ↧ sᴘᴀᴍ ᴄᴍᴅ ↧\n\n"

XOXO_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"

XOXO_Help += f" .xoxospam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

XOXO_Help += f"© @XoXoSpamtBot\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=XOXO_Help,
                                  buttons=[
        [
        Button.url("💞 ᴄʜᴀɴɴᴇʟ 💞", "https://t.me/XoXoSpamtBot")
        ] 
        ]
        )
