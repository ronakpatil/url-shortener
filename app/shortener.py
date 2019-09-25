import logging
import json
from pyshorteners import Shortener
LOGGER = logging.getLogger('url_shortener')


class Shorteners:

    def __init__(self, url):
        self.url = url

    def bitly_shortener(self):
        try:
            with open('config/bitly.json') as source:
                data = json.load(source)
                source.close()
            access_token = str(data["token"])
            bitly_plug = Shortener('Bitly', bitly_token=access_token)
            short_url = bitly_plug.short(self.url)
            LOGGER.info("Short URL is %s", str(short_url))
            # actual_url = bitly_plug.expand(short_url)
            return "Short URL is {}".format(short_url)

        except Exception as err:
            raise err
