class script(object):
    START_TXT = """๐ฅ๐๐ฒ ๐ฃ๐ฑ๐ฎ๐ป๐ฎ {}

โจ๏ธ๐๐ฑ๐ฑ ๐ง๐ต๐ถ๐ ๐๐ผ๐ ๐ง๐ผ ๐ฌ๐ผ๐๐ฟ ๐๐ฟ๐ผ๐๐ฝ ๐๐ป๐ฑ ๐๐ถ๐๐ฒ ๐๐ฑ๐บ๐ถ๐ป. ๐๐ฟ๐ผ๐บ ๐ง๐ต๐ฎ๐ ๐ง๐ถ๐บ๐ฒ ๐ง๐ต๐ถ๐ ๐๐ผ๐ ๐ช๐ถ๐น๐น ๐ฃ๐ฟ๐ผ๐๐ถ๐ฑ๐ฒ ๐ ๐ผ๐๐ถ๐ฒ๐ ๐๐ป๐ฑ ๐ฆ๐ฒ๐ฟ๐ถ๐ฒ๐ ๐๐ผ๐ฟ ๐ฅ๐ฒ๐พ๐๐ฒ๐๐๐. ๐ง๐ต๐ถ๐ ๐๐ผ๐ ๐๐ฎ๐๐ฒ ๐ง๐ต๐ฒ ๐๐ฎ๐ฟ๐ด๐ฒ๐๐ ๐ ๐ผ๐๐ถ๐ฒ & ๐ฆ๐ฒ๐ฟ๐ถ๐ฒ๐ ๐๐ฎ๐๐ฎ๐ฏ๐ฎ๐๐ฒ ๐๐ป ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ๐

๐คBy Using Our Service You Must Agree To Our Privacy Policy ๐"""
    HELP_TXT = """๐โโ๏ธ๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐๐"""
    ABOUT_TXT = """<b>๐โโ๏ธ I Aแด </b>: <a href=https://t.me/BorutoAutoFilterRobot>Bแดสแดแดแด</a>
<b>๐จโ๐ป Cสแดแดแดแดส</b>: <a href=https://github.com/KisaraPesanjithPerera>โๅฝกแฒแฉแแถแผ แบแฉแฒแฟแๅฝกโ</a>
<b>๐ถ Pแดแดกแดสแดแด By</b>: @AnonymousBotsInfinity

<b>โโโโโโโโโโโโโโโโโ</b>

๐ฒ <b>Sแดสแด แดส</b> : Hแดสแดแดแด
๐งฉ <b>Lแดษดษขแดแดษขแด</b> : Pyแดสแดษด
๐ <b>Lษชสสแดสy</b> : Pyสแดษขสแดแด
๐ <b>Bแดษชสแด Sแดแดแดแด๊ฑ</b> : V1.0.1 [ Bแดแดแด ]"""
    MANUELFILTER_TXT = """Help: <b>Filters๐งฟ</b>

- Filter is the feature were users can set automated replies for a particular keyword and Boruto will respond whenever a keyword is found the message๐

<b>NOTE๐:</b>
1. Boruto should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands & Usage๐</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons๐งฟ</b>

- Boruto supports both url and alert inline buttons๐

<b>NOTE๐:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Boruto supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>๐URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/AnonymousBotsInfinity)</code>

<b>๐Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter๐งฟ</b>

<b>NOTE๐:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
๐I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections๐งฟ</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE๐:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage๐</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules๐งฟ</b>

<b>NOTE๐:</b>
These are the extra features of Boruto๐น

<b>Commands and Usage๐</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods๐งฟ</b>

<b>NOTE๐:</b>
This module only works for my admins๐

<b>Commands and Usage๐</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>My Sแดแดแดแด๊ฑ</b> ๐ค
    
๐ <b>Tแดแดแดส Mแดแด ษชแด Sแดแด แดแด</b> : <code>{}</code>
๐ค <b>Tแดแดแดส U๊ฑแดส๊ฑ</b> : <code>{}</code>
๐ <b>Tแดแดแดส Gสแดแดแดฉ๊ฑ</b> : <code>{}</code>
๐ฐ <b>U๊ฑแดแด Sแดฉแดแดแด</b> : <code>{}</code> MB
๐๏ธ <b>Fสแดแด Sแดฉแดแดแด</b> : <code>{}</code> MB

<b>โโโโโโโโโโโโโโโโโ</b>

<b>My Sแดสแด แดส Sแดแดแดแด๊ฑ</b> ๐

<b>๐ป Cแดฉแด U๊ฑแดษขแด</b> : {}%
<b>โ๏ธ Rแดแด U๊ฑแดษขแด</b> : {}%"""

    CREDITS = """<b>Credit ๐</b>
    
Bแดสแดแดแด Is A Auto Filter Bot As Well As One Bot In Telegram That Can Download Movies & Series Inline๐

- <b>Developer ๐จโ๐ป</b>
<b>โๅฝกแฒแฉแแถแผ แบแฉแฒแฟแๅฝกโ</b>

- <b>Thanks To ๐</b>
<b>๐ท๏ธ Dan</b> For His Awsome Libary
<b>๐ท๏ธ Mahesh</b> For His Awesome Media-Search-bot
<b>๐ท๏ธ Trojanz</b> for Their Awesome Unlimited Filter Bot And AutoFilterBoT

โ๏ธ๐ฃ๐ผ๐๐ฒ๐ฟ๐ฑ ๐๐ :- @AnonymousBotsInfinity"""
    LOG_TEXT_G = """#NewGroup
๐Group = {}(<code>{}</code>)
๐โโ๏ธTotal Members = <code>{}</code>
๐บAdded By - {}
"""
    LOG_TEXT_P = """#NewUser
โ๏ธID - <code>{}</code>
๐โโ๏ธName - {}
"""
