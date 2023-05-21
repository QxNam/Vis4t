#!/usr/bin/env bash

cloudflared tunnel --config .cloudflared/config.yml --url 0.0.0.0:8000 run vis4t