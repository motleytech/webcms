# if argument is specified, use that as the port number
if [ $# -eq 0 ]
    then
        PORT=8001
    else
        PORT=$1
fi

source env.sh
python manage.py runserver 0.0.0.0:$PORT
