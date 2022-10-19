"""
Docteller Python Client Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docteller reads an image and turns it into meaningful JSON data.

Basic usage:
    >>> from docteller import DoctellerClient

    >>> image_path = "path/to/image.jpg"
    >>> api_key = "copy-it-from-your-account-on-docteller.com"

    >>> docteller_client = DoctellerClient(api_key=api_key)
    >>> docteller_client.read(image_path)
    {} # TODO JSON example
"""

from ._client import DoctellerClient  # NOQA: F401
