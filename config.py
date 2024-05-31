import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "24482734")
    API_HASH  = os.environ.get("API_HASH", "5ccf6a58166cc047a7eba01c5dbc930c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6714999304:AAEs25BnMlirc15upe9FD0852c9lmZt-kS0") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","rename")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Tn69Links:epiIlhWaO1B0FG71@cluster0.ldwpogq.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/dbf07ce0f70a6cea7b7d7.jpg")
    ADMIN = int(os.environ.get("ADMIN", "1790775725"))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "TN69Links") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001891110437"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))

#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot

class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴇʟʟᴏ {} 👋 

➻ Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀғᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ.

➻ Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ Aɴᴅ Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oғ Yᴏᴜʀ Fɪʟᴇs.

➻ Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ Aɴᴅ Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ.

➻ Tʜɪs Bᴏᴛ Aʟsᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.</b>

<b>Bᴏᴛ Is Mᴀᴅᴇ Bʏ : <a href=https://t.me/Cute_Boy_Saravana>Ƭɴ69 ×͜× Sᴀʀᴀᴠᴀɴᴀ࿐</a></b>"""
#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 Mʏ Nᴀᴍᴇ : {}</b>
├<b>🖥️ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Cute_Boy_Saravana>Ƭɴ69 ×͜× Sᴀʀᴀᴠᴀɴᴀ࿐</a></b>
├<b>👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/RoyalxMovies>RᴏʏᴀʟxMᴏᴠɪᴇs</a></b>
├<b>📕 Lɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a></b>
├<b>✏️ Lᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>Pʏᴛʜᴏɴ 𝟹</a></b>
├<b>💾 Dᴀᴛᴀʙᴀsᴇ : <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ Dʙ</a></b>
├<b>📊 Bᴜɪʟᴅ Vᴇʀsɪᴏɴ : <a href=https://t.me/PMIOfficials>Rᴇɴᴀᴍᴇ v4.5.0</a></b>  
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ</u></b>
  
<b>➪ /start - Sᴛᴀʀᴛ Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴʏ Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ.
➪ /del_thumb - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴᴀɪʟ.
➪ /view_thumb - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ.

📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ</u></b>

➪ /set_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ A Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ /see_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ /del_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ Exᴀᴍᴘʟᴇ - <code>/set_caption 📕 Nᴀᴍᴇ ➠ : {filename}

🔗 Sɪᴢᴇ ➠ : {filesize} 

⏰ Dᴜʀᴀᴛɪᴏɴ ➠ : {duration}</code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>

➪ Sᴇɴᴅ Aɴʏ Fɪʟᴇ Aɴᴅ Tʏᴘᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ Aɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ Dᴏᴄᴜᴍᴇɴᴛ, Vɪᴅᴇᴏ, Aᴜᴅɪᴏ ].           

Aɴʏ Oᴛʜᴇʀ Hᴇʟᴘ Cᴏɴᴛᴀᴄᴛ :- <a href=https://t.me/Cute_Boy_Saravana>Cʀᴇᴀᴛᴏʀ</a></b>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ Pʀᴏɢʀᴇss Bᴀʀ ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 Pʟᴇᴀsᴇ Jᴏɪɴ : @TN69_Links
╰━━━━━━━━━━━━━━━➣ </b>"""
#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
    DONATE_TXT = """
<b>Tʜᴀɴᴋs Fᴏʀ Sʜᴏᴡɪɴɢ Iɴᴛᴇʀᴇsᴛ Iɴ Dᴏɴᴀᴛɪᴏɴ! ❤️</b>

<b>Iғ Yᴏᴜ I Lɪᴋᴇ Mʏ Bᴏᴛs Yᴏᴜ Cᴀɴ Pʟᴇᴀsᴇ Sᴜᴘᴘᴏʀᴛ Tʜɪs Cʜᴀɴɴᴇʟ Aɴᴅ Sʜᴀʀᴇ Wɪᴛʜ Yᴏᴜʀ Fʀɪᴇɴᴅs & Fᴀᴍɪʟʏ.</b>

<b>🔗 Cʜᴀɴɴᴇʟ Lɪɴᴋ : @TN69_Links, @UltraQualityMovies, @RoyalxMovies, @UHD4K_Movies, @PMIOfficials</b>
"""

#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
