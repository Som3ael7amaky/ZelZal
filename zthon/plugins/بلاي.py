from zthon import zedub
from zthon.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "الترفيه"


# بلاي 
M = (
    "**𓆰**   𝑠𝑜𝑢𝑟𝑐𝑒 ✘   **العـاب الاونلايـن** 🎮𓆪 \n"
    "◐━─━─━─━─✘─━─━─━─━◐\n\n"
    "  ❶ **⪼**  [حرب الفضاء 🛸](https://t.me/gamee?game=ATARIAsteroids)   \n"
    "  ❷ **⪼**  [لعبة فلابي بيرد 🐥](https://t.me/awesomebot?game=FlappyBird)   \n"
    "  ❸ **⪼**  [القط المشاكس 🐱](https://t.me/gamee?game=CrazyCat)   \n"
    "  ❹ **⪼**  [صيد الاسماك 🐟](https://t.me/gamee?game=SpikyFish3)   \n"
    "  ❺ **⪼**  [سباق الدراجات 🏍](https://t.me/gamee?game=MotoFX2)   \n"
    "  ❻ **⪼**  [سباق سيارات 🏎](https://t.me/gamee?game=F1Racer)   \n"
    "  ❼ **⪼**  [شطرنج ♟](https://t.me/T4TTTTBOT?game=chess)   \n"
    "  ❽ **⪼**  [كرة القدم ⚽](https://t.me/gamee?game=FootballStar)   \n"
    "  ❾ **⪼**  [كرة السلة 🏀](https://t.me/gamee?game=BasketBoyRush)   \n"
    "  ❿ **⪼**  [سلة 2 🎯](https://t.me/gamee?game=DoozieDunks)   \n"
    "  ⓫ **⪼**  [ضرب الاسهم 🏹](https://t.me/T4TTTTBOT?game=arrow)   \n"
    "  ⓬ **⪼**  [لعبة الالوان 🔵🔴](https://t.me/T4TTTTBOT?game=color)   \n"
    "  ⓭ **⪼**  [كونج فو 🎽](https://t.me/gamee?game=KungFuInc)   \n"
    "  ⓮ **⪼**  [🐍 لعبة الافعى 🐍](https://t.me/T4TTTTBOT?game=snake)   \n"
    "  ⓯ **⪼**  [🚀 لعبة الصواريخ 🚀](https://t.me/T4TTTTBOT?game=rocket)   \n"
    "  ⓰ **⪼**  [كيب اب 🧿](https://t.me/gamee?game=KeepitUP)   \n"
    "  ⓱ **⪼**  [جيت واي 🚨](https://t.me/gamee?game=Getaway)   \n"
    "  ⓲ **⪼**  [الالـوان 🔮](https://t.me/gamee?game=ColorHit)   \n"
    "  ⓳ **⪼**  [مدفع الكرات🏮](https://t.me/gamee?game=NeonBlaster)   \n\n\n"
    "**𓄂-** 𝙎𝙊𝙐𝙍𝘾𝙀 𝘿𝙀𝙑 **⪼**  [𐇮 𝗬ᴇ𝘀𝗼𝗼 آلـۘهہؚيـٰـُ͢ـُ໋۠بـ໋ۘ۠ه 𐇮](t.me/U_U_Q_1)   \n"
    "**𓆰** 𝙎𝙊𝙐𝙍𝘾𝙀 **⪼**  [ 𝑠𝑜𝑢𝑟𝑐𝑒 ✘](https://t.me/C_U_U_1)  "
)


@zedub.zed_cmd(
    pattern="بلاي$",
    command=("بلاي", plugin_category),
    info={
        "header": "العـاب الانـلاين لـ سـورس ايـگ๛",
        "الاستـخـدام": "{tr}بلاي",
    },
)
async def zedrepo(zelp):
    await edit_or_reply(zelp, M)
