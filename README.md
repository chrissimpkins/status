# status [![Current Version](https://pypip.in/version/status/badge.svg?text=version&style=flat)](https://pypi.python.org/pypi/status/) [![License](https://pypip.in/license/status/badge.svg?style=flat)](https://github.com/chrissimpkins/status/blob/master/docs/LICENSE)


### HTTP status codes for GET and POST requests

## About
Status is a cross-platform command line application that returns the HTTP response status code for a GET or POST request to a user submitted URL.

It has been tested in cPython 2.7.x, 3.4.x and pypy 2.4.0 (Python v2.7.8)

## Install

You can install status with the Python package manager pip using the following command:

```
pip install status
```

or download the source repository and run the following command in the top level source directory:

```
python setup.py install
```

## Upgrade

You can upgrade to the current release version of status with the Python package manager pip:

```
$ pip install --upgrade status
```

or by downloading the source repository and following the instructions for a new install from source above.


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

v0.2.5 - bug fix : connection error handling modifications, new tests in cPython 2.7.9/3.4.2, pypy 2.4.0

v0.2.4 - updated application dependencies

v0.2.3 - updated application dependencies

v0.2.2 - minor bug fixes, application help documentation clarifications

v0.2.1 - exception handling for HTTP connection errors, help documentation updates

v0.2.0 - initial release


## License

The MIT License (MIT)

Copyright (c) 2015 Christopher Simpkins

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
