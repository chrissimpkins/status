================
 status
================
----------
 HTTP status codes for GET and POST requests
----------

Install
=============
You can install from PyPI with pip using the following command::

    pip install status

or download the source repository and run the following command in the top level source directory::

    python setup.py install


Usage
=============
status will report the returned status code with a GET or POST request.  The general syntax is::

    status [option] <url>

GET Request Status Codes
-------------
GET is the default request type. Simply enter the full URL as an argument to status::

    status <url>


POST Request Status Codes
-------------
To use a POST request, add the ``-p`` or ``--post`` option::

    status -p <url>

