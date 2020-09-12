def getVideoTitle(url_link):
    import urllib.request
    import json
    import urllib
    from StringUtils import format_filename

    params = {"format": "json", "url": url_link}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    title = ""
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            title = data["title"]
    except urllib.error.HTTPError as exception:
        pass
    finally:
        return format_filename(title)
