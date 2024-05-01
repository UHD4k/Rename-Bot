from pyrogram import Client, filters 
from helper.database import AshutoshGoswami24

@Client.on_message(filters.private & filters.command(['set_caption', "sc"]))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Gɪᴠᴇ Tʜᴇ Cᴀᴘᴛɪᴏɴ\n\nExᴀᴍᴘʟᴇ :- `/set_caption 📕 Nᴀᴍᴇ ➠ : {filename} \n\n🔗 Sɪᴢᴇ ➠ : {filesize} \n\n⏰ Dᴜʀᴀᴛɪᴏɴ ➠ : {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await AshutoshGoswami24.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Aᴅᴅᴇᴅ ✅**")
   
@Client.on_message(filters.private & filters.command(['del_caption', "dc"]))
async def delete_caption(client, message):
    caption = await AshutoshGoswami24.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Cᴀᴘᴛɪᴏɴ ❌**")
    await AshutoshGoswami24.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ 🗑️**")
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption', "vc"]))
async def see_caption(client, message):
    caption = await AshutoshGoswami24.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ :**\n\n`{caption}`")
    else:
       await message.reply_text("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Cᴀᴘᴛɪᴏɴ ❌**")









#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
