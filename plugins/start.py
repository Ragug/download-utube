from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Telegram sticker", url="https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTc2ODU0NzI4Mzk4MjY5?story_media_id=2623219158225116484_45667768285&utm_medium=copy_link")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://www.instagram.com/ragug19?r=nametag")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
