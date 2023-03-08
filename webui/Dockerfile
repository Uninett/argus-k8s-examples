# set ft:dockerfile
FROM node:16-buster as build
WORKDIR /app

COPY helpers/* ./
RUN ./install_packages.sh git ssh

ARG VERSION=master
RUN echo "${VERSION}"
RUN git clone https://github.com/Uninett/Argus-frontend.git
RUN cd Argus-frontend; git checkout ${VERSION}

WORKDIR /app/Argus-frontend
RUN npm ci

# These arguments are needed in the environment to properly configure and build
# Argus-frontend:
ARG REACT_APP_BACKEND_URL=https://api.argus.uninett.no
ARG REACT_APP_ENABLE_WEBSOCKETS_SUPPORT=true
ARG REACT_APP_BACKEND_WS_URL=wss://api.argus.uninett.no/ws
ARG REACT_APP_USE_SECURE_COOKIE=true
ARG REACT_APP_DEBUG=true
ARG REACT_APP_DEFAULT_AUTO_REFRESH_INTERVAL=30
ARG REACT_APP_REALTIME_SERVICE_MAX_RETRIES=5
ARG REACT_APP_COOKIE_DOMAIN=argus.uninett.no

# Now we have everything we need to build
RUN npm run build

# production environment
# FROM: https://mherman.org/blog/dockerizing-a-react-app/
FROM nginx:stable-alpine

COPY --from=build /app/Argus-frontend/build /usr/share/nginx/html

RUN apk add --update tini tree
RUN tree /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
#EXPOSE 80
ENTRYPOINT ["/sbin/tini", "-v", "--"]
CMD ["nginx", "-g", "daemon off;"]
