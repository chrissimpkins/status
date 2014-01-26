#!/usr/bin/env python
# encoding: utf-8

from Naked.toolshed.network import HTTP
from Naked.toolshed.system import exit_success

class Get:
    def __init__(self, url):
        self.url = url

    def get_response(self):
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

class Post:
    def __init__(self, url):
        self.url = url

    def post_response(self):
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


def prepare_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    else:
        return 'http://' + url
