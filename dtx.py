# UseratorOT

from telethon import events
import asyncio
from time import sleep
from userbot.events import register as r
from userbot.cmdhelp import CmdHelp
from userbot import DTO_VERSION

@r(outgoing=True, pattern=".dtx")
async def yabi(e):
    sleep(0.2)
    await e.edit("**NƏ GÜLMƏLİ ZARAFAT İDİ** 😅")
    sleep(1.4)
    await e.edit("**GÜL GÜL OLDÜM HAHA 😂**")
    sleep(1.4)
    await e.edit("**İNDİ GET QAPINI AÇ 🚪**")
    sleep(1.4)
    await e.edit("**YƏQİN Kİ, AZƏRSUDU 🤫**")
    sleep(1.4)
    await e.edit("**GƏL DANIŞARIQ YENƏ 🖐**")
    await e.client.send_file(e.chat_id, "https://telegra.ph/file/88e177ef13c4402859813.mp4",caption='`⚠️WASTED⚠️`')
    sleep(15.3)
    await e.delete()

Help = CmdHelp('dtx')
Help.add_command('dtx', None, 'Birisi siyasi zarafat edərsə işlədin :)')
Help.add_warning('`Sadəcə zarafat məqsədi ilə işlədin !`').add()
Help.add_info(
  '**@ResuI tərəfindən yaradılıb.**'
).add()