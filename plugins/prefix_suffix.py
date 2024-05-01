from pyrogram import Client, filters, enums
from helper.database import AshutoshGoswami24


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Pʀᴇғɪx__\n\nExᴀᴍᴘʟᴇ :- `/set_prefix @PMIOfficials`**")
    prefix = message.text.split(" ", 1)[1]
    SnowDev = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    await AshutoshGoswami24.set_prefix(message.from_user.id, prefix)
    await SnowDev.edit("**Pʀᴇғɪx Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    SnowDev = await message.reply_text("Pʟᴇᴀsᴇ Wᴀɪᴛ...")
    prefix = await AshutoshGoswami24.get_prefix(message.from_user.id)
    if not prefix:
        return await SnowDev.edit("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Pʀᴇғɪx ❌**")
    await AshutoshGoswami24.set_prefix(message.from_user.id, None)
    await SnowDev.edit("**Pʀᴇғɪx Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    SnowDev = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    prefix = await AshutoshGoswami24.get_prefix(message.from_user.id)
    if prefix:
        await SnowDev.edit(f"**Yᴏᴜʀ Pʀᴇғɪx :-**\n\n`{prefix}`")
    else:
        await SnowDev.edit("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Pʀᴇғɪx ❌**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Sᴜғғɪx__\n\nExᴀᴍᴘʟᴇ :- `/set_suffix @PMIOfficials`**")
    suffix = message.text.split(" ", 1)[1]
    SnowDev = await message.reply_text("Pʟᴇᴀsᴇ Wᴀɪᴛ...")
    await AshutoshGoswami24.set_suffix(message.from_user.id, suffix)
    await SnowDev.edit("**Sᴜғғɪx Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    SnowDev = await message.reply_text("Pʟᴇᴀsᴇ Wᴀɪᴛ...")
    suffix = await AshutoshGoswami24.get_suffix(message.from_user.id)
    if not suffix:
        return await SnowDev.edit("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Sᴜғғɪx ❌**")
    await AshutoshGoswami24.set_suffix(message.from_user.id, None)
    await SnowDev.edit("**Sᴜғғɪx Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    SnowDev = await message.reply_text("Pʟᴇᴀsᴇ Wᴀɪᴛ...")
    suffix = await AshutoshGoswami24.get_suffix(message.from_user.id)
    if suffix:
        await SnowDev.edit(f"**Yᴏᴜʀ Sᴜғғɪx :-**\n\n`{suffix}`")
    else:
        await SnowDev.edit("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Sᴜғғɪx ❌**")










#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
