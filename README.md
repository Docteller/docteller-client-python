# docteller
** docteller ** transcodes from one image format to another

It especially deals with docteller from pdf and base64 into more useful formats (jpg, or raw np array)

```python
>>> import docteller
>>> path = 'path/to/images.pdf'
>>> images = docteller.transcode(path, output_format='jpg')

>>> image_bytestream = ...
>>> images = docteller.transcode(image_bytestream, output_format='numpy')
```

## Installation
nothing special to do except import docteller

## Run tests
```console
$ python -m unittest
```