# Python Maillog

Easily send log messages via mail.

## Install

Download `maillog.py`.

## Configuration

Set environment variables:

* `MAILLOG_HOST`: SMTP host
* `MAILLOG_PORT`: SMTP port
* `MAILLOG_USER`: SMTP user
* `MAILLOG_PASS`: SMTP password
* `MAILLOG_FROM`: `From` header of the mail
* `MAILLOG_TO`: comma-separated list of recipients

## Usage

`maillog(subject, body)`

## Example

```
from maillog import format_exception, maillog
try:
    # failing code, raising exception
    raise ValueError("Error!")
except ValueError as e:
    maillog("An error occured", format_exception(e))
```
