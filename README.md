# docteller

**Docteller** reads an image and turns it into meaningful JSON data.

Basic usage:

```python
>>> from docteller import DoctellerClient

>>> image_path = "path/to/image.jpg"
>>> api_key = "copy-it-from-your-account-on-docteller.com"

>>> docteller_client = DoctellerClient(api_key)
>>> docteller_client.read(image_path)
{} # TODO JSON example
```

## Installation

```bash
pip install docteller
```
