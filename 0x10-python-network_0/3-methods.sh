#!/bin/bash
# this script show the allowed methods
curl -sI "$1" | grep Allow | cut -d " " -f 2-10
