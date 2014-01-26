# status [![PyPI version](https://badge.fury.io/py/status.png)](https://pypi.python.org/pypi/status)


### HTTP status codes for GET and POST requests

## About
Status is a command line application that returns the HTTP response status code for a GET or POST request to a user submitted URL.  It has been tested in cPython 2.7, 3.2, 3.3 and pypy 2.2.1 (Python v2.7.3)

## Install

You can install from PyPI with pip using the following command:

```
pip install status
```

or download the source repository and run the following command in the top level source directory:

```
python setup.py install
```

## Usage

status will report the returned status code with a GET or POST request.  The general syntax is:

```
status [option] <url>
```

It is not necessary to include the protocol (http://) in your URL.  If you enter a URL without the protocol, status will prefix it with http://.  If you intend to test with the secure HTTP protocol (https://), then make this explicit in your URL.

### GET Request Status Codes

GET is the default request type. Enter the URL as an argument to status without an option:

```
status <url>
```


### POST Request Status Codes

To use a POST request, add the `-p` or `--post` option:

```
status -p <url>
```

## Versions

v0.2.1 - exception handling for HTTP connection errors, help documentation updates

v0.2.0 - first production release

v0.1.x - testing releases

## License

The MIT License (MIT)

Copyright (c) 2014 Christopher Simpkins

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
