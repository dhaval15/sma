airflow db init
airflow users create \
	--username	$USERNAME \
	--firstname $FIRSTNAME \
	--lastname $LASTNAME \
	--role admin \
	--email $EMAILID
airflow webserver --port 8080
airflow scheduler
