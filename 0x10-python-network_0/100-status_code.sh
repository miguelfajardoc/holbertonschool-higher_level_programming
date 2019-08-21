#!/bin/bash
# this script show the status code of the current request
curl -sw %{http_code} "$1" -o /dev/null
