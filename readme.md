# selectn-py [![Build Status](http://img.shields.io/travis/srn/selectn-py.svg?style=flat-square)](https://travis-ci.org/srn/selectn-py)

> Resolves deeply-nested dictionary properties via dot-notation

Inspired by the node library [selectn](https://github.com/wilmoore/selectn.js)

So you can do:

```python
selectn('info.name.full', person);
```

instead of:

```python
person and person['info'] and person['info']['name'] and person['info']['name']['full']
```

## Install

```sh
$ pip install selectn-python
```

## Usage

```python
>>> from selectn import selectn
>>>
>>> dic = {'info': {'name': {'full': 'selectn'}}}
>>>
>>> selectn('info.name.full', dic)
'selectn'
```

## License

MIT © [Søren Brokær](http://srn.io)
