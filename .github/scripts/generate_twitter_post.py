#!/usr/env python3

import re
from pathlib import Path

changelog = Path('./CHANGELOG.md')

POST_TEMPLATE = """New Release: {tag}
{highlight_content}
{url}
"""


if not changelog.exists():
    print('No Changelog found..')
    exit(1)


with open(changelog, mode='r') as file:
    content = file.read()


regex = r'(?<=## Highlights)(.*)(?=## Commits)'
match = re.search(regex, content, re.DOTALL)

if not match:
    print('Could not find "Highlights" content.')
    exit(1)


highlight_content = match.group(1).strip()

if len(highlight_content) > 200:
    # We only have 280 characters to play with, so lets reserve 80 for our own use, then use the rest for the highlight message.
    shortend_content = highlight_content[:200]
    shortend_content = shortend_content.split('\n\n')[:-1]
    highlight_content = '\n\n'.join(shortend_content)


print(highlight_content)




# print(changelog)