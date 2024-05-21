# SQLAlchemy router

Dummy example to show SQLAlchemy's routing capabilities.

The goal is to easily switch db engine whether we are writing (using the master database)
or reading (using read-replicas).

Inspired by Michael Bayer's [blog](https://techspot.zzzeek.org/2012/01/11/django-style-database-routers-in-sqlalchemy/), creator of SQLAlchemy.

## Usage

Assuming you have a Python interpreter available in your `PATH`, with SQLAlchemy installed:

```bash
$ git clone https://github.com/nibbleai/sqlalchemy-router.git
$ cd sqlalchemy-router
$ python main.py
```

Now read the logs: writes are done on `master.db`, reads are done on either one of available replicas.
