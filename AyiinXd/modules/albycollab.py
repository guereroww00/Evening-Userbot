# Ayiin - Userbot
# Credits (C) 2022-2023 @AyiinXd
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


import asyncio
from secrets import choice
from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import BLACKLIST_CHAT, CMD_HELP
from AyiinXd.ayiin import asupan_sagapung, exolink
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply


exorcist = "https://telegra.ph/file/fccecf320b30088410dcd.jpg"
asupung = "https://telegra.ph/file/82598bc741e3010339d4c.jpg"
exorcist2 = "https://telegra.ph/file/1002a84a022bd13663742.jpg"


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="exo(?: |$)(.*)")
async def _(yins):
    if yins.chat_id in BLACKLIST_CHAT:
        return await yins.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok...")
    await edit_or_reply(yins, "`Exorcist Nih Boss...`")
    sleep(2)
    text = str(yins.pattern_match.group(1).split(" ", 1)[0])
    link = str(yins.pattern_match.group(1).split(" ", 2)[0])
    ayiin = text.replace(".", " ")
    user = await yins.client.get_me()
    link_2 = choice(exolink)
    thumb = exorcist
    output = (
        f"**ʀᴇǫᴜᴇsᴛ ʙʏ :** @{user.username}\n\n"
        f"**{ayiin}**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**               𝙴𝚇𝙾𝚁𝙲𝙸𝚂𝚃**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝙻𝙸𝙽𝙺**\n"
        f"**⌲ {link_2} {link}**\n\n"
        f"**       𝙆𝙊𝙉𝙏𝙀𝙉 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @premiumexor**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 💦**\n\n"
        f"**❖ᴠᴠɪᴩ ᴠɪᴅɪᴏ ʙᴏᴋᴇᴩ ᴛᴀɴᴩᴀ ʟɪɴᴋ❖**\n\n"
        f"**ɪɴғᴏ : @IamAkashii**\n"
        f"**ᴛᴇsᴛɪ : @vvipexor**\n"
    )
    if thumb:
        try:
            logo = thumb
            await yins.delete()
            msg = await yins.client.send_file(yins.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await yins.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await yins.delete()
    else:
        await edit_or_reply(yins, output)


@ayiin_cmd(pattern="as(?: |$)(.*)")
async def _(asupng):
    if asupng.chat_id in BLACKLIST_CHAT:
        return await asupng.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok...")
    await edit_or_reply(asupng, "`Asupan Sagapung...`")
    sleep(1)
    text = str(asupng.pattern_match.group(1).split(" ", 1)[0])
    link = str(asupng.pattern_match.group(1).split(" ", 2)[0])
    ayiin = text.replace(".", " ")
    user = await asupng.client.get_me()
    link_2 = choice(asupan_sagapung)
    image = asupung
    output = (
        f"**ʀᴇǫᴜᴇsᴛ ʙʏ:** @{user.username}\n\n"
        f"**{ayiin}**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**       Asᴜᴘᴀɴ Sᴀɢᴀᴘᴜɴɢ**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝙻𝙸𝙽𝙺**\n"
        f"**⌲ {link_2} {link}**\n\n"
        f"**       𝙆𝙊𝙉𝙏𝙀𝙉 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @PussyTubeCh**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 💦**\n\n"
        f"**❖𝚂𝚄𝙿𝙿𝙾𝚁𝚃❖**\n"
        f"**♕︎ @MovieSagapung**\n"
        f"**♕︎ @PussyTubeCh**"
    )
    if image:
        try:
            logo = image
            await asupng.delete()
            msg = await asupng.client.send_file(asupng.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await asupng.edit(
                output + "\n\n **Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await asupng.delete()
    else:
        await edit_or_reply(asupng, output)

# ========================×========================
#               For Admin Collaborator
# ========================×========================


@ayiin_cmd(pattern="^Exo(?: |$)(.*)")
async def yinscollab(exor):
    if exor.chat_id in BLACKLIST_CHAT:
        return await exor.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok...")
    await edit_or_reply(exor, "`Exorcist Nih Boss...`")
    sleep(1)
    if exor.pattern_match.group(1):
        text, link = exor.pattern_match.group(1).split()
    ayiin = text.replace(".", " ")
    thumbnail = exorcist2
    output = (
        f"**{ayiin}**\n\n"
        f"**⌲ 𝙻𝙸𝙽𝙺**\n"
        f"**⌲ {link}**\n\n"
        f"**❖ᴠᴠɪᴩ ᴠɪᴅɪᴏ ʙᴏᴋᴇᴩ ᴛᴀɴᴩᴀ ʟɪɴᴋ❖**\n\n"
        f"**ɪɴғᴏ : @zereefff**\n"
        f"**ᴛᴇsᴛɪ : @vvipexor**\n"
    )
    if thumbnail:
        try:
            logo = thumbnail
            await exor.delete()
            msg = await exor.client.send_file(exor.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await exor.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await exor.delete()
    else:
        await edit_or_reply(exor, output)


@ayiin_cmd(pattern="^As(?: |$)(.*)")
async def _(asupng):
    if asupng.chat_id in BLACKLIST_CHAT:
        return await asupng.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok...")
    await edit_or_reply(asupng, "`Asupan Sagapung...`")
    sleep(1)
    link = asupng.pattern_match.group(1)
    image = asupung
    output = (
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**       Asᴜᴘᴀɴ Sᴀɢᴀᴘᴜɴɢ**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝙻𝙸𝙽𝙺**\n"
        f"**⌲ {link}**\n\n"
        f"**       𝙆𝙊𝙉𝙏𝙀𝙉 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @PussyTubeCh**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 💦**\n\n"
        f"**❖𝚂𝚄𝙿𝙿𝙾𝚁𝚃❖**\n"
        f"**♕︎ @MovieSagapung**\n"
        f"**♕︎ @PussyTubeCh**"
    )
    if image:
        try:
            logo = image
            await asupng.delete()
            msg = await asupng.client.send_file(asupng.chat_id, logo, caption=output)
            await asyncio.sleep(800)
            await msg.delete()
        except BaseException:
            await asupng.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await asupng.delete()
    else:
        await edit_or_reply(asupng, output)


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "collab": f"**Plugin:** `collab`\
        \n\n  »  **Perintah :** `{cmd}exo`\
        \n  »  **Kegunaan :** Untuk Mendapatkan Link Bokp Dari Ch Exorcist.\
        \n\n  »  **Perintah :** `{cmd}as`\
        \n  »  **Kegunaan :** Untuk Mendapatkan Link Bokp Dari Ch Asupan Sagapung.\
    "
    }
)


CMD_HELP.update(
    {
        "albyexo": f"**Plugin : **`albyexo`\
        \n\n  »  **Perintah:** `Ini Khusus Admin Exorcist Tod Bukan Publik.`\
        \n  »  **Silahkan Ketik** `{cmd}help yinscollab` **Untuk Mendapatkan Konten.**\
    "
    }
)
