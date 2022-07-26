from pyrogram import Client, types, filters


@Client.on_message(filters.command("start"))
async def start_handler(_, m: types.Message):
    await m.reply(
        f"Halo {m.from_user.first_name}\nSilakan kirim link nya untuk mengambil file dari channel yang direstrict kontennya."
    )
