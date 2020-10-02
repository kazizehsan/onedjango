#!/bin/sh

docker network inspect onedjango-network >/dev/null 2>&1 ||
  docker network create \
    --driver=bridge \
    onedjango-network
