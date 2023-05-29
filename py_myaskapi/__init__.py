"""
Interface to the My ASK API. See https://myaskai.com/api-docs

Author: Ed Menendez (ed@menendez.com)
Company: Digital Haiku / LearnWPT
Created: April 26, 2023
Updated: 
"""
import json
import os
import requests
import time


class NotImplemented(Exception):
    pass


class MissingAPIURL(Exception):
    def __str__(self):
        return 'i.e. myaskai_api.MyAskAPI(api_url=settings.MYASK_AI_API_URL ... )'


class MyAskAPI:
    """ You can initialize it like this:

    import py_myaskapi
    ma = py_myaskapi.MyAskAPI(
        api_url='https://myaskai.com/api/1.1/wf/',
        client_id=settings.MYASK_AI_ID,
        api_key=settings.MYASK_AI_API_KEY)
    ma.content(
        file_url=f'https://example.com/example-page/?version=json',
        meta_title='Example Page 101',
        meta_author='Ed Menendez',
        meta_link=f'https://example.com/example-page/',
    )
    """
    def __init__(self, *args, **kwargs):
        try:
            self.api_url = kwargs['api_url']
        except KeyError:
            raise MissingAPIURL()

        self._client_id = kwargs.get('client_id')
        self._api_key = kwargs.get('api_key')

    def _standard_headers(self):
        """ Returns the standard headers
        """
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def _standard_api_data(self):
        return {
            'id': self._client_id,
            'api_key': self._api_key,
        }

    def _get_fq_url(self, url):
        """ Returns the FQ URL for the call.
        """
        fq_url = self.api_url
        if url[0] == '/':
            url = url[1:]  # Remove leading slash because that breaks the os.path.join hack
        return os.path.join(fq_url, url)

    def call(self, url, params=None, headers=None, debug=False):
        """ Makes an API GET Call.
        """
        fq_url = self._get_fq_url(url)
        if not headers:
            headers = self._standard_headers()
        if debug:
            print(f'GET: {fq_url=}\n{headers=}\n{params=}')
        resp = requests.get(fq_url, params=params, headers=headers, timeout=5)
        return resp.json()

    def post(self, url, params={}, data={}, headers=None, json_data=True, debug=False):
        """ Makes an API POST Call.
        """
        fq_url = self._get_fq_url(url)
        if not headers:
            headers = self._standard_headers()
        data.update(self._standard_api_data())
        if debug:
            print(f'POST: {fq_url=}\n{headers=}\n{params=}\n{data=}')
        
        if json_data:
            data = json.dumps(data)

        resp = requests.post(fq_url, params=params, data=data, headers=headers, timeout=5)
        return resp.json()

    def content(self, file_url, meta_title, meta_author=None, meta_link=None, debug=False):
        """ Sends content. Note that this includes a 5 second delay at the end to prevent overloading the API.
        """
        data = {
            'file_url': file_url,
            'meta_title': meta_title,
        }
        if meta_author:
            data['meta_author'] = meta_author
        if meta_link:
            data['meta_link'] = meta_link
        ret = self.post(
            '/ask-ai-content',
            data=data,
            debug=debug,
        )
        time.sleep(5)
        return ret
