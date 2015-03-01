
# make sure you change these values for a production server.
export DJANGO_SECRET="any_random_string_will_work_here.Just_make_it_nice_and_long"
export PG_USER_PW="sample_user_pw"
export PG_ADMIN_PW="sample_admin_pw"

# set this to "True" to enable django debug mode.
# only set this to True in development mode
# not recommended in production.
export DJANGO_DEBUG="False"
export PRODUCTION_ENV="True"
