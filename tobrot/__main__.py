#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

import logging
import os
import sys

from pyrogram import Client, filters, idle
from pyrogram.handlers import CallbackQueryHandler, MessageHandler

from tobrot import app
from tobrot import (
    AUTH_CHANNEL,
    CANCEL_COMMAND_G,
    CLEAR_THUMBNAIL,
    CLONE_COMMAND_G,
    DOWNLOAD_LOCATION,
    GET_SIZE_G,
    GLEECH_COMMAND,
    GLEECH_UNZIP_COMMAND,
    GLEECH_ZIP_COMMAND,
    LEECH_COMMAND,
    LEECH_UNZIP_COMMAND,
    LEECH_ZIP_COMMAND,
    LOG_COMMAND,
    PYTDL_COMMAND,
    RENEWME_COMMAND,
    RENAME_COMMAND,
    SAVE_THUMBNAIL,
    STATUS_COMMAND,
    TELEGRAM_LEECH_UNZIP_COMMAND,
    TELEGRAM_LEECH_COMMAND,
    UPLOAD_COMMAND,
    YTDL_COMMAND,
    GYTDL_COMMAND,
    GPYTDL_COMMAND,
    TOGGLE_VID,
    RCLONE_COMMAND,
    TOGGLE_DOC,
    HELP_COMMAND
)
from tobrot.helper_funcs.download import down_load_media_f
from tobrot.plugins.call_back_button_handler import button
from tobrot.plugins.choose_rclone_config import rclone_command_f
from tobrot.plugins.custom_thumbnail import clear_thumb_nail, save_thumb_nail
from tobrot.plugins.incoming_message_fn import (g_clonee, g_yt_playlist,
                                                incoming_message_f,
                                                incoming_purge_message_f,
                                                incoming_youtube_dl_f,
                                                rename_tg_file)
from tobrot.plugins.new_join_fn import help_message_f, new_join_f
from tobrot.plugins.rclone_size import check_size_g, g_clearme
from tobrot.plugins.status_message_fn import (
    cancel_message_f,
    eval_message_f,
    exec_message_f,
    status_message_f,
    upload_document_f,
    upload_log_file,
    upload_as_doc,
    upload_as_video
)

def start_bot():
    try:
        # create download directory, if not exist
        if not os.path.isdir(DOWNLOAD_LOCATION):
            os.makedirs(DOWNLOAD_LOCATION)

        # Starting The Bot
        app.start()

        # Adding message handlers
        add_message_handlers()

        # Logging
        logging.info(f"@{(app.get_me()).username} has started running...🏃💨💨 Now gimme 100$ 🐸")

        # Idle
        idle()

    except Exception as e:
        logging.exception("An error occurred while starting the bot:")
        sys.exit(1)

    finally:
        # Stop the app if it's still running
        if app.is_initialized:
            app.stop()

def add_message_handlers():
    try:
        handlers = [
            MessageHandler(incoming_message_f, filters.command([LEECH_COMMAND, LEECH_UNZIP_COMMAND, LEECH_ZIP_COMMAND, GLEECH_COMMAND, GLEECH_UNZIP_COMMAND, GLEECH_ZIP_COMMAND]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(down_load_media_f, filters.command([TELEGRAM_LEECH_COMMAND, TELEGRAM_LEECH_UNZIP_COMMAND]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(incoming_purge_message_f, filters.command(["purge"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(g_clonee, filters.command([f"{CLONE_COMMAND_G}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(check_size_g, filters.command([f"{GET_SIZE_G}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(g_clearme, filters.command([f"{RENEWME_COMMAND}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(incoming_youtube_dl_f, filters.command([YTDL_COMMAND, GYTDL_COMMAND]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(g_yt_playlist, filters.command([PYTDL_COMMAND, GPYTDL_COMMAND]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(status_message_f, filters.command([f"{STATUS_COMMAND}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(cancel_message_f, filters.command([f"{CANCEL_COMMAND_G}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(exec_message_f, filters.command(["exec"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(eval_message_f, filters.command(["eval"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(rename_tg_file, filters.command([f"{RENAME_COMMAND}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(upload_document_f, filters.command([f"{UPLOAD_COMMAND}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(upload_log_file, filters.command([f"{LOG_COMMAND}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(help_message_f, filters.command([f"{HELP_COMMAND}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(new_join_f, filters=~filters.chat(chats=AUTH_CHANNEL)),
            CallbackQueryHandler(button),
            MessageHandler(save_thumb_nail, filters.command([f"{SAVE_THUMBNAIL}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(clear_thumb_nail, filters.command([f"{CLEAR_THUMBNAIL}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(rclone_command_f, filters.command([f"{RCLONE_COMMAND}"])),
            MessageHandler(upload_as_doc, filters.command([f"{TOGGLE_DOC}"]) & filters.chat(chats=AUTH_CHANNEL)),
            MessageHandler(upload_as_video, filters.command([f"{TOGGLE_VID}"]) & filters.chat(chats=AUTH_CHANNEL)),
        ]

        for handler in handlers:
            app.add_handler(handler)

    except Exception as e:
        logging.exception("An error occurred while adding message handlers:")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        start_bot()
    except KeyboardInterrupt:
        logging.info("Bot stopped by the user.")
    except Exception as e:
        logging.exception("An error occurred while running the bot:")
