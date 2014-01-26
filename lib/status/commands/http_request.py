#!/usr/bin/env python
# encoding: utf-8

from Naked.toolshed.network import HTTP
from Naked.toolshed.system import exit_success
from Naked.toolshed.system import stderr
from requests.exceptions import ConnectionError

class Get:
    def __init__(self, url):
        self.url = url

    def get_response(self):
        try:
            the_url = prepare_url(self.url)
            http = HTTP(the_url)
            http.get()
            resp = http.response()
            if len(resp.history) > 0:
                count = len(resp.history)
                for i in range(count):
                    print(str(resp.history[i].status_code) + " : " + str(resp.history[i].url))
            print(str(http.res.status_code) + " : " + http.res.url)
            exit_success()
        except ConnectionError:
            error_string = "Unable to connect to the URL, " + self.url
            stderr(error_string, 1)
        except Exception as e:
            raise e

class Post:
    def __init__(self, url):
        self.url = url

    def post_response(self):
        try:
            the_url = prepare_url(self.url)
            http = HTTP(the_url)
            http.post()
            resp = http.response()
            if len(resp.history) > 0:
                count = len(resp.history)
                for i in range(count):
                    print(str(resp.history[i].status_code) + " : " + str(resp.history[i].url))
            print(str(http.res.status_code) + " : " + the_url)
            exit_success()
        except ConnectionError as ce:
            error_string = "Unable to connect to the URL, " + self.url
            stderr(error_string, 1)
        except Exception as e:
            raise e


def prepare_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    else:
        return 'http://' + url
