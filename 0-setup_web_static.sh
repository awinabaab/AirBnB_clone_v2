#!/usr/bin/env bash
# Sets up a web server for deployment of web_static

if ! which nginx > /dev/null; then
	apt-get update -y
	apt-get install -y nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared

echo "<html>
	<head>
	</head>
	<body>
	  ALX
	</body>
</html" | tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/

CONFIG_FILE=/etc/nginx/sites-available/default
SEARCH_STRING="server_name _;"
CONFIG_STRING="$SEARCH_STRING\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}"

cp --backup=numbered "$CONFIG_FILE" "$CONFIG_FILE".bak

if ! grep -qw "location /hbnb_static" "$CONFIG_FILE"; then
	sed -i "s/$SEARCH_STRING/$CONFIG_STRING/" "$CONFIG_FILE"
fi

if nginx -t; then
	service nginx restart
fi
