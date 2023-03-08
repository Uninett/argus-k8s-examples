# set ft:dockerfile
FROM nginx:stable-alpine
WORKDIR /app

RUN apk add --update tini

COPY nginx.conf /etc/nginx/conf.d/default.conf
ENTRYPOINT ["/sbin/tini", "-v", "--"]
CMD ["nginx", "-g", "daemon off;"]
