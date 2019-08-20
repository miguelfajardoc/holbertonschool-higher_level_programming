#!/bin/bash
# this script show the size of the body response
curl -s $1 | wc -m
