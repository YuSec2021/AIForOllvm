#!/bin/env python

ENV_LOGGER_FORMATTER = "%(asctime)s %(levelprefix)s %(message)s"

ENV_ACCESS_LOGGER_FORMATTER = (
    '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
)

ENV_TZ = "Asia/Shanghai"