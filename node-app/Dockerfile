FROM node:18.15.0-alpine

RUN apk add --no-cache openssl

WORKDIR /node-app

# Generate self-signed SSL certificate for HTTP/2
RUN openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=localhost"

COPY . .

EXPOSE 443

CMD ["node", "server.js"]
