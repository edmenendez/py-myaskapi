# py-myaskapi

## Description
This library makes it easy to interface with MyAskAPI's [API](https://myaskai.com/api-docs#!).

## Installation
Simplue install using pip or your favorite package management tools.

    pip install py-myaskapi
This will install the [Requests](https://pypi.org/project/requests/) library.

## Usage
You can initialize it like this:

    import py_myaskapi

    ma = py_myaskapi.MyAskAPI(
        api_url='https://myaskai.com/api/1.1/wf/',
        client_id=settings.MYASK_AI_ID,
        api_key=settings.MYASK_AI_API_KEY)
    # Now let's push some content to the API
    ma.content(
        file_url=f'https://example.com/example-page/?version=json',
        meta_title='Example Page 101',
        meta_author='Ed Menendez',
        meta_link=f'https://example.com/example-page/',
    )
*Note*: You should store your API keys outside of the code repository.

The library currently has a helper function for the `ask-ai-content` verb. You can, however, use it for any of the API calls. Additional helper method PRs are welcome! 

Here's an example of using it for the `ask-ai-search` verb.

    # Previously imported and started the MyAskAPI client (see above)

    ma.post('/ask-ai-search', data={'query': 'Example question?'})

## Credits

Thank you to [LearnWPT](https://learnwpt.com/) for permitting publishing of this code.

## License

MIT License

## How to Contribute

Feel free to submit a PR. Test scripts would be nice! Please see [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) for our code of conduct.
