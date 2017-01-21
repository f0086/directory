#!/usr/bin/env python
from __future__ import print_function, division, absolute_import, unicode_literals

import requests
import json
import collections

# Get spaces list
directory_file = './directory.json'
directory = open(directory_file, 'r')
spaces = json.loads(directory.read())
spaces_new = {}
has_error = False

# Check spaces
for name, url in spaces.items():
    if 'spaceapi.net' in url:
        continue
    try:
        print('+ %s %s' % (name, url))
        response = requests.get(url, verify=False, timeout=10)
        if response.status_code == 200:
            spaces_new[name] = url
        else:
            print('  \033[0;31m-> Status: %s: %s\033[0m' \
                % (response.status_code, response.reason))
    except Exception as e:
        print('  \033[0;31m-> Error: %s\033[0m' % e)
        has_error = True

directory.close()

# Save new spaces
directory = open(directory_file, 'w+')
json_str = json.dumps(spaces_new, indent=2, sort_keys=True, separators=(',', ':'))
directory.write(json_str)
directory.close()
exit(int(has_error))
