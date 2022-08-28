web: gunicorn simple_crm.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=simple_crm worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=simple_crm beat -S redbeat.RedBeatScheduler --loglevel=info
