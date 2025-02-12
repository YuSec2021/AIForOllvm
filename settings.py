#!/bin/env python

ENV_LOGGER_FORMATTER = "%(asctime)s %(levelprefix)s %(message)s"

ENV_ACCESS_LOGGER_FORMATTER = (
    '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
)

ENV_TZ = "Asia/Shanghai"

ENV_DEEPSEEK_API_KEY = "1"
ENV_BASE_DEEPSEEK_URL = "https://api.deepseek.com"