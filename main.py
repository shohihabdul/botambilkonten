from clients import bot, user
from pyrogram import compose


if __name__ == '__main__':
    print("Running")
    compose([bot, user])
