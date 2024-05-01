from pyrogram import Client, filters 
from helper.database import AshutoshGoswami24


@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await AshutoshGoswami24.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Tʜᴜᴍʙɴᴀɪʟ ❌**") 
		
@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await AshutoshGoswami24.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ 🗑️**")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("**Pʟᴇᴀsᴇ Wᴀɪᴛ...**")
    await AshutoshGoswami24.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("**Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✅️**")








#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
