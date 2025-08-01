#!/bin/bash
python bot.py &
exec gunicorn webapp:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT