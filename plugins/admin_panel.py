
import os, sys, time, asyncio, logging, datetime
from config import Config
from pyrogram import Client, filters
from helper.database import AshutoshGoswami24
from pyrogram.types import Message
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
 




@Client.on_message(filters.command(["stats", "status", "s"]) & filters.user(Config.ADMIN))
async def get_stats(bot, message):
    total_users = await AshutoshGoswami24.total_users_count()
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - bot.uptime))    
    start_t = time.time()
    st = await message.reply('**Pʀᴏᴄᴇssɪɴɢ Tʜᴇ Dᴇᴛᴀɪʟs.....**')    
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await st.edit(text=f"**--Bᴏᴛ Sᴛᴀᴛᴜs--** \n\n**⌚ Bᴏᴛ UᴘTɪᴍᴇ :** `{uptime}` \n**🐌 Cᴜʀʀᴇɴᴛ Pɪɴɢ :** `{time_taken_s:.3f} ms` \n**👭 Tᴏᴛᴀʟ Usᴇʀs :** `{total_users}`")



@Client.on_message(filters.command(["restart", "r"]) & filters.user(Config.ADMIN))
async def restart_bot(bot, message):
    msg = await bot.send_message(text="🔄 Pʀᴏᴄᴇssᴇs Sᴛᴏᴘᴇᴅ. Bᴏᴛ Is Rᴇsᴛᴀʀᴛɪɴɢ...", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("✅️ Bᴏᴛ Is Rᴇsᴛᴀʀᴛᴇᴅ. Nᴏᴡ Yᴏᴜ Cᴀɴ Usᴇ Mᴇ")
    os.execl(sys.executable, sys.executable, *sys.argv)



@Client.on_message(filters.private & filters.command(["ping", "p"]))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pinging....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ 🔥!\n{time_taken_s:.3f} ms")
    return time_taken_s



@Client.on_message(filters.command(["Bʀᴏᴀᴅᴄᴀsᴛ", "b"]) & filters.user(Config.ADMIN) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    await bot.send_message(Config.LOG_CHANNEL, f"{m.from_user.mention} or {m.from_user.id} Is Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bʀᴏᴀᴅᴄᴀsᴛ......")
    all_users = await AshutoshGoswami24.get_all_users()
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text("Bʀᴏᴀᴅᴄᴀsᴛ Sᴛᴀʀᴛᴇᴅ..!") 
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_users = await AshutoshGoswami24.total_users_count()
    async for user in all_users:
        sts = await send_msg(user['_id'], broadcast_msg)
        if sts == 200:
           success += 1
        else:
           failed += 1
        if sts == 400:
           await AshutoshGoswami24.delete_user(user['_id'])
        done += 1
        if not done % 20:
           await sts_msg.edit(f"**Bʀᴏᴀᴅᴄᴀsᴛ Iɴ Pʀᴏɢʀᴇss :** \n\nTᴏᴛᴀʟ Usᴇʀs {total_users} \nCᴏᴍᴘʟᴇᴛᴇᴅ : {done} / {total_users}\nSᴜᴄᴄᴇss : {success}\nFᴀɪʟᴇᴅ : {failed}")
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(f"**Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ :** \n\nCᴏᴍᴘʟᴇᴛᴇᴅ Iɴ `{completed_in}`.\n\nTᴏᴛᴀʟ Usᴇʀs {total_users}\nCᴏᴍᴘʟᴇᴛᴇᴅ : {done} / {total_users}\nSᴜᴄᴄᴇss : {success}\nFᴀɪʟᴇᴅ : {failed}")
           
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        logger.info(f"{user_id} : Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ")
        return 400
    except UserIsBlocked:
        logger.info(f"{user_id} : Bʟᴏᴄᴋᴇᴅ Tʜᴇ Bᴏᴛ")
        return 400
    except PeerIdInvalid:
        logger.info(f"{user_id} : Usᴇʀ ɪᴅ Iɴᴠᴀʟɪᴅ")
        return 400
    except Exception as e:
        logger.error(f"{user_id} : {e}")
        return 500
 







#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot

