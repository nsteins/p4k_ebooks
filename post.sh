#!/bin/bash
sleep ${RANDOM:0:2}m;
. ~/p4k_ebooks/env/bin/activate
python ~/p4k_ebooks/postTweet.py
