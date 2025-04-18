 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from pixivpy3 import AppPixivAPI, ByPassSniApi

sys.dont_write_bytecode = True


# get your refresh_token, and replace _REFRESH_TOKEN
#  https://github.com/upbit/pixivpy/issues/158#issuecomment-778919084
_REFRESH_TOKEN = "-KSSNRF-XN1jRYPFPom2Hi9i2hzBceQNQgS-A1DKkV0"


def main():
    sni = False
    if not sni:
        api = AppPixivAPI()
    else:
        api = ByPassSniApi()  # Same as AppPixivAPI, but bypass the GFW
        api.require_appapi_hosts()
    api.auth(refresh_token=_REFRESH_TOKEN)

    # get rankings
    json_result = api.illust_recommended()

    directory = "illusts"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # download top3 day rankings to 'illusts' dir
    for idx, illust in enumerate(json_result.illusts):
        image_url = illust.meta_single_page.get(
            "original_image_url", illust.image_urls.large
        )
        print("{}: {}".format(illust.title, image_url))

        # try four args in MR#102
        
        url_basename = os.path.basename(image_url)
        extension = os.path.splitext(url_basename)[1]
        name = f"illust_id_{illust.id}_{illust.title}{extension}"
        api.download(image_url, path=directory, name=name)


if __name__ == "__main__":
    main()
