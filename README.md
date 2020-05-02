**Please note: This project is not suitable for production use.**

This project demonstrates how to use the 
[Heroku pgbouncer buildpack](https://github.com/heroku/heroku-buildpack-pgbouncer) 
together with Django for client-side connection pooling.

## Usage

To get up and running, clone this repo and `cd` into the folder containing this
 README-file.

Then:

```
# create app
$ heroku apps:create ${HEROKU_APP_NAME}

# add postgres
$ heroku addons:create heroku-postgresql:hobby-dev --name=${HEROKU_APP_NAME}

# add pgbouncer buildpack
$ heroku buildpacks:add heroku/pgbouncer

# add python buildpack
$ heroku buildpacks:add heroku/python3

# deploy the app
$ git push heroku master

# run Django migrations
$ heroku run python manage.py migrate
```

Open https://${HEROKU_APP_NAME}/blocking-transaction?sleep=2 in your browser.

You should see something like this (but not as nicely formatted):

```
{
    "seconds_delay": 2.0,
    "total_item_count": 120,
    "pgbouncer_stats": [
        {
            "database": "db1",
            "total_xact_count": 24,
            "total_query_count": 288,
            "total_received": 32580,
            "total_sent": 17915,
            "total_xact_time": 14320888,
            "total_query_time": 8179707,
            "total_wait_time": 7903285,
            "avg_xact_count": 0,
            "avg_query_count": 3,
            "avg_recv": 377,
            "avg_sent": 207,
            "avg_xact_time": 661640,
            "avg_query_time": 33823,
            "avg_wait_time": 109654
        },
        {
            "database": "pgbouncer",
            "total_xact_count": 12,
            "total_query_count": 12,
            "total_received": 0,
            "total_sent": 0,
            "total_xact_time": 0,
            "total_query_time": 0,
            "total_wait_time": 0,
            "avg_xact_count": 0,
            "avg_query_count": 0,
            "avg_recv": 0,
            "avg_sent": 0,
            "avg_xact_time": 0,
            "avg_query_time": 0,
            "avg_wait_time": 0
        }
    ]
}
```