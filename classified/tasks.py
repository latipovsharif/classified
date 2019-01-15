from testproject.celery import app

@app.task(bind=True)
def count_views(self):
    print('Request: {0!r}'.format(self.request))