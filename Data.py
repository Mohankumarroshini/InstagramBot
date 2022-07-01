from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ✨ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ɪ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇs ғʀᴏᴍ ɪɴsᴛᴀɢʀᴀᴍ ᴀʟᴏɴɢ ᴡɪᴛʜ ᴘᴏsᴛ ᴄᴀᴘᴛɪᴏɴs.

ʏᴏᴜs ᴄᴀɴ ᴀᴜᴛʜᴏʀɪsᴇ ᴍᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀɪᴠᴀᴛᴇ ᴘᴏsᴛs 🧚.

ɪ ᴀᴍ ᴏɴʟʏ ᴘʀᴏғɪʟᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ sᴏ ᴅᴏɴ'ᴛ ᴜʀʟ ʟɪɴᴋs ᴀɴᴅ sᴘᴀᴍ ᴍᴇ.

ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ 🌟.

ʙʏ @TamilBots [🤖](https://telegra.ph/file/57873ee2279555866f4c9.jpg)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ🌟", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("ғᴏʀ ᴍᴏʀᴇ ʙᴏᴛs🤖", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ❔", callback_data="help"),
            InlineKeyboardButton("🎪ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs🧚", url="https://t.me/StarkBots")],
    ]

    # Help Message
    HELP = """
1) **Images, Videos and Reels**
Send the link here to get the post contents including caption.

2) **Profile Pictures**
Use the command `/profile_pic` or `/dp` along with instagram username to get its profile picture.
Example : `/dp StarkProgrammer`

3) **Private Posts**
Authorize the bot to download private posts. Use /auth

**Note** : Stories and IGTV are not supported.

Use /auth to authorize and /unauth to unauthorize.
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴsᴛᴀɢʀᴀᴍ ᴄᴏɴᴛᴇɴᴛ ʙʏ @TamilBots

ɴᴀᴍᴇ : [ɪɴsᴛᴀ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ](https://t.me/instadownloadprobot)

ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

ᴅᴇᴠʟᴏᴘᴇʀ : [.♪.எம்.எஸ்.டி.♪.](https://t.me/my_dear_lightbright)

sᴇʀᴠᴇʀ : [ʜᴇʀᴏᴋᴜ](https://heroku.com/)

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴀᴍɪʟ ʙᴏᴛs](https://t.me/tamilbots)
    """
