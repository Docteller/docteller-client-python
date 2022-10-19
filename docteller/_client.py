import json
import logging
import os

import requests


logging.basicConfig()
docteller_log = logging.getLogger(__name__).setLevel(logging.DEBUG)
docteller_log.propagate = True


class DoctellerClient(object):
    def __init__(self, api_key: str = None, use_session: bool = True) -> None:

        self.api_key = api_key
        self.request_class = requests.session() if self.use_session else requests
        if self.api_key:
            self.docteller_read_endpoint = "https://docteller.com/mlapi/v1/documentteller/read"
        else:
            self.docteller_read_endpoint = "https://docteller.com/mlapi/v1/documentteller/read-demo"
            docteller_log.info(
                "Without an API Key, you are rate-limited to 1 request every 10 seconds.\n"
                + "Get your API Key now by registering at https://docteller.com ❤️ (start with 250 free credits per month)"
            )

    def read(self, file_path: str, **kwargs) -> dict:
        """Sends an HTTP request to the docteller.com API to read the image.

        :param file_path: A valid path to a file (not to a directory).
        :return: :class:`dict` object
        :rtype: dict

        Usage::
            >>> from docteller import DoctellerClient

            >>> image_path = "path/to/image.jpg"
            >>> api_key = "copy-it-from-your-account-on-docteller.com"

            >>> docteller_client = DoctellerClient(api_key)
            >>> docteller_client.read(image_path)
            {} # TODO JSON example
        """

        if not os.path.isfile(file_path):
            raise ValueError(f"file_path '{file_path}' must be a valid path to a file (not a directory).")

        options = kwargs
        data_dict = {
            "options": (None, json.dumps(options), "application/json"),
            "image": (os.path.basename(file_path), open(file_path, "rb"), "application/octet-stream"),
        }

        response = self.request_class.post(
            self.docteller_read_endpoint,
            headers={"access_token": self.api_key},
            files=data_dict,
        )

        response.raise_for_status()
        response_json = response.json()

        return response_json
