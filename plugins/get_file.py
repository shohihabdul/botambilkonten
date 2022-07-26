from pyrogram import Client, filters, types
from configs import configs


@Client.on_message(filters.regex('http') & filters.private)
async def get_file(c: Client, m: types.Message):
    if m.from_user.id != configs.owner_id:
        return await m.reply("Bot ini cuma dipake buat owner nya hihi.")
    x = await m.reply("Silakan tunggu")
    link = m.text.split("/")
    chat_id = link[3]
    msg_id = int(link[4])
    if chat_id == "c":
        return await x.edit("Maaf, sekarang masi belum support ch / gc pripat, ntar dibuat")
    await x.delete()
    return await c.copy_message(m.chat.id, chat_id, msg_id)
