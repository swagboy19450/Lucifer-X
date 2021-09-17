import glob
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from Lucifer import CMD_HNDLR, bot
from Lucifer.LuciferConfig import Var
from Lucifer.utils import load_module, load_pmbot, start_mybot

LION = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.send_message(
            LION,
            f"**DARK COBRA 𝙱𝙾𝚃 𝙸𝚂 𝙳𝙴𝙿𝙻𝙾𝚈𝙴𝙳.\n𝚂𝙴𝙽𝙳** `{CMD_HNDLR}alive` **𝚃𝙾 𝚂𝙴𝙴 𝙱𝙾𝚃 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙾𝚁 𝙽𝙾𝚃.\n\nAdd** @{BOTNAME} **𝙰𝙳𝙳 𝚃𝙾 𝚃𝙷𝙸𝚂 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙷𝙸𝙼 𝙰𝙳𝙼𝙸𝙽 𝙵𝙾𝚁 𝙴𝙽𝙰𝙱𝙻𝙸𝙽𝙶 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙾𝙵 DARK COBRA 𝙱𝙾𝚃**",
        )
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = "Lucifer/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("DARK COBRA has been deployed! ")

print("Setting up TGBot")
path = "Lucifer/plugins/mybot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_mybot(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "Lucifer/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                   𝐃𝐚𝐫𝐤 𝐜𝐨𝐛𝐫𝐚 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐝𝐞𝐩𝐥𝐨𝐲𝐞𝐝, 𝐃𝐨 𝐯𝐢𝐬𝐢𝐭 @𝐝𝐚𝐫𝐤_𝐜𝐨𝐛𝐫𝐚_𝐮𝐬𝐞𝐫𝐛𝐨𝐭
                    Cobra ᴠᴇʀ: V2.2
                   𓂀 𝕋𝔼𝔸𝕄 ℂ𝕆𝔹ℝ𝔸 𓂀
                ----------------------------------------------------------------------
"""
)
bot.loop.run_until_complete(startup_log_all_done())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
