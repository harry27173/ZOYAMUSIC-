from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="𝖧𝖾𝗅𝗉", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="𝐒ҽƚƚιɳɠ𝐒", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="𝖧𝖾𝗅𝗉", callback_data="settings_back_helper")
        ],
    ]
    return buttons
