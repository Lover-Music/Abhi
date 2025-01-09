import uvloop

uvloop.install()

import sys

from pyrogram import Client, errors
from pyrogram.types import BotCommand
from pyrogram.enums import ChatMemberStatus, ParseMode


import config

from ..logging import LOGGER


class LoverMusic(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            "LoverMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,)

     async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
        try:
            await self.send_photo(
                config.LOG_GROUP_ID, photo=config.PING_IMG_URL, caption=f"**💫 Lover ᴍᴜsɪᴄ 💫**\n\n𖢵 ɪᴅ : `{self.id}`\n𖢵 ɴᴀᴍᴇ : {self.name}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
            )
            await self.set_bot_commands([
    BotCommand("start", "Start the bot"),
    BotCommand("help", "Open the bot help menu"),
    BotCommand("ping", "Check that bot is alive or dead"),
    BotCommand("auth", "Add a user to AUTH LIST of the group"),
    BotCommand("unauth", "Remove a user from AUTH LIST of the group"),
    BotCommand("reboot", "Restarts the bot in your chat"),
    BotCommand("stats", "Shows the stats of the bot"),
    BotCommand("play", "Starts playing the requested song"),
    BotCommand("vplay", "Starts playing the requested song as video"),
    BotCommand("skip", "Moves to the next track"),
    BotCommand("pause", "Pause the current playing song"),
    BotCommand("resume", "Resume the paused song"),
    BotCommand("end", "Clear the queue and leave voice chat"),
    BotCommand("lyrics", "Searches Lyrics for the particular Music on web"),
    BotCommand("song", "Download any track from youtube in mp3 or mp4 formats"),
    BotCommand("loop", "Loops the current playing song on voicechat"),
    BotCommand("shuffle", "Randomly shuffles the queued playlist."),
    BotCommand("seek", "Seek the stream to given duration (in seconds)"),
    BotCommand("seekback", "Seek back the stream to given duration (in seconds)")])
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
