#!/bin/sh

# Grab schema from GitHub repository
wget https://github.com/SuperSonicHub1/twitch-graphql-api/raw/master/schema.json -O /tmp/schema.json

# Run codegen in virtualenv
poetry run sgqlc-codegen schema /tmp/schema.json twitch_sgqlc/schema.py
