#!/bin/bash
set -e
apt-get update
RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends $@
rm -rf /var/lib/apt/lists/*
apt-get clean
