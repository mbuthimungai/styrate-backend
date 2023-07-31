#!/bin/bash

set -o errexit
set -o nounset

celery -A app.api.v1.api.celery worker --loglevel=info -Q send_email -P threads