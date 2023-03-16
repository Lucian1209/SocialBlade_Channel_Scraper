#!/bin/bash

docker build -t scraper .
docker run --rm scraper python main.py --proxy $(cat proxy_list.txt | shuf -n 1)
