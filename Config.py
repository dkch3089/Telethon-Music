import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "20666779"))
    API_HASH = os.environ.get("API_HASH", "019030d7b246c687f10f39d857c4df97")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6154311188:AAHQI7OXGEtXZD_XDeEJbszdXOG4TFBhVak")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBu2LwIkc12qoJ1t_xXyefEf00WL_3Takz5OUfEFX9Pfd3zou0XKLd_gvbi3aYd7UCJdSSaBNlrV2BvHOm_aN5OnlBKbokxKMhMrs5lCNciJPeKzss9uznQFaWqwmyQa2Cx6qavNOY1iZ_dMptD1oQHT98srZv3b29nOsug-VXLYU5f2Ww7zUMkFRN4NRK_EPErXfkS0cIUqSZIzkYx8md-4sgjm3HPSzBgeEiL_iFs8LrFgLrQwkHvyTF_YdtJadZLwg-i458BBqZmHRaIQNXdDA8x0o4NDcqN2Eo-HlKeMtbNZDoCpNQqwf1Ip4e6LaZZcg8SSQ9AEYwcDDRfKa4TcM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "rockylove_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
