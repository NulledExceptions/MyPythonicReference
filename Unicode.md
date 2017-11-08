# Python 2.7. Unicode Errors Simply Explained

> I know I'm late with this article for about 5 years or so, but people are still using Python 2.x, so this subject is relevant I think.

Some facts first:

* Unicode is an international encoding standard for use with different languages and scripts
* In python-2.x, there are two types that deal with text.
  1. `str` is an 8-bit string.
  2. `unicode` is for strings of unicode code points.  
    A code point is a number that maps to a particular abstract character. It is written using the notation U+12ca to mean the character with value 0x12ca (4810 decimal)
* Encoding (noun) is a map of Unicode code points to a sequence of bytes. (Synonyms: character encoding, character set, codeset). Popular encodings: UTF-8, ASCII, Latin-1, etc.
* Encoding (verb) is a process of converting `unicode` to bytes of `str`, and decoding is the reverce operation.
* Python 2.x uses ASCII as a default encoding. (More about this later)

## SyntaxError: Non-ASCII character

When you sees something like this

```
SyntaxError: Non-ASCII character '\xd0' in file /tmp/p.py on line 2, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
```
you just need to define encoding in the first or second line of your file.
All you need is to have string `coding=utf8` or `coding: utf8` somewhere in your comments.
Python doesn't care what goes before or after those string, so the following will work fine too:

```
# -*- encoding: utf-8 -*-
```
Notice the dash in utf-8. Python has many aliases for UTF-8 encoding, so you should not worry about dashes or case sensitivity.

## `UnicodeEncodeError` Explained

```python
>>> str(u'café')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 3: ordinal not in range(128)
```

`str()` function **encodes** a string. We passed a `unicode` string, and it tried to encode it using a default encoding, which is ASCII. Now the error makes sence because ASCII is 7-bit encoding which doesn't know how to represent characters outside of range 0..128.  
Here we called `str()` explicitly, but something in your code may call it implicitly and you will also get `UnicodeEncodeError`.

**How to fix:** encode `unicode` string manually using `.encode('utf8')` before passing to `str()`

## `UnicodeDecodeError` Explained

```python
>>> utf_string = u'café'
>>> byte_string = utf_string.encode('utf8')
>>> unicode(byte_string)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
```
Let's say we somehow obtained a byte string `byte_string` which contains encoded UTF-8 characters. We could get this by simply using a library that returns `str` type.  
Then we passed the string to a function that converts it to `unicode`. In this example we explicitly call `unicode()`, but some functions may call it implicitly and you'll get the same error.  
Now again, Python uses ASCII encoding by default, so it tries to convert bytes to a default encoding ASCII. Since there is no ASCII symbol that converts to `0xc3` (195 decimal) it fails with `UnicodeDecodeError`.

**How to fix:** decode `str` manually using `.decode('utf8')` before passing to your function.

## Rule of Thumb

Make sure your code works only with Unicode strings internally, converting to a particular encoding on output, and decoding `str` on input.
Learn the libraries you are using, and find places where they return `str`. Decode `str` before return value is passed further in your code.

I use this helper function in my code:

```python
def force_to_unicode(text):
    "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding"
    return text if isinstance(text, unicode) else text.decode('utf8')
```

---
Source: <https://docs.python.org/2/howto/unicode.html>
