**Please note: This project is not suitable for production use.**

This project demonstrates how to use the Heroku pgbouncer buildpack together
 with Django for client-side connection pooling.
 
To get up and running, clone this repo and `cd` into the folder containing this file.

Then:

´´´
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
´´´

Open https://${HEROKU_APP_NAME}/blocking-transaction?sleep=2 in your browser.