# webpageArchiver
Automatically creates screenshots from webpages

#### Usage:
1. Put your urls inside the `list.txt` file.
2. Call the python script: `python3 webpageArchiver.py` or `./webpageArchiver.py`

Exclude URLs from getting archived by putting a `#` at the beginning.

#### Dependencies:
- Python 3
- python-selenium
- Chromium + Chromedriver (should work with Firefox too after modifications)

#### todo:
- automatically skip already archived webpages / automatically comment archived urls
- parameter to choose browser used to render webpages
- automatically close "we use cookies"-banner (sometimes overlapping contents)
- use add blocker to archive webpage without adds (better compression possible)
