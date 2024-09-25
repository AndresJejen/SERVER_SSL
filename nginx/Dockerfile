FROM nginx:latest
ADD ./unalcriptografia.local.ext /etc/ssl/unalcriptografia.local.ext
RUN apt-get update
RUN apt-get install -y openssl \
    && NAME=unalcriptografia.local \
    && openssl genrsa -out /etc/ssl/myCA.key 2048 \
    && openssl req -x509 -new -nodes -key /etc/ssl/myCA.key -sha256 -days 3650 -out /etc/ssl/myCA.pem -subj "/C=PT/ST=Lisbon/L=Lisbon/O=MyCompany/OU=IT Department/CN=$NAME" \
    && openssl genrsa -out /etc/ssl/$NAME.key 2048 \
    && openssl req -new -key /etc/ssl/$NAME.key -out /etc/ssl/$NAME.csr -subj "/C=PT/ST=Lisbon/L=Lisbon/O=MyCompany/OU=IT Department/CN=$NAME" \
    && openssl x509 -req -in /etc/ssl/$NAME.csr -CA /etc/ssl/myCA.pem -CAkey /etc/ssl/myCA.key -CAcreateserial -out /etc/ssl/$NAME.crt -days 3650 -sha256 -extfile /etc/ssl/$NAME.ext