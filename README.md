# Example Argus deployment definitions for K8s

This repository contains a (non-working) example of how we deploy Argus to production in our Kubernetes cluster at Sikt.

We use GitLab pipelines to build and deploy the necessary containers to Kubernetes, so the YAML files containing deployment definitions are to be considered templates: They are littered with references to environment variables that ultimately get filled in by our GitLab CI pipelines.

Certain logging customizations that we use have been removed from the examples, and references to internal servers and email addresses have been redacted.


## High level Argus architecture

Any complete Argus instance consists of *two* Deployment objects, and *each* deployment will need Service and Ingress objects to be reachable by users:

1. A backend API server.
2. A front-end (webui) application.


## The backend API server

The API server is the real workhorse of Argus. This is the main database of incidents. It provides the necessary API to create, update, retrieve and resolve incident data. It also provides a registry of known/accepted incident source systems, a user account database and user notification profiles. APIs are also provided to create, update and delete user notification profiles, and it sends the actual notifications for events that match the configured profiles.

### API deployment

The API deployment consists of multiple containers per Pod:

1. One instance of the API application container (django) running in a gunicorn application server, for normal HTTP requests,

2. An other instance of the API application (websockets) running in a daphne application server, for websockets requests.

3. An nginx container that serves as the main web service for the API. It proxies incoming requests to the two application servers, selecting the correct target depending on whether the incoming request is directed to the special websocket URL (/ws) or the normal HTTP API.

4. A redis container for message passing and caching.

See the [api](./api) directory for this deployment definition.

### PostgreSQL

These examples do not show how to deploy a PostgreSQL server for the API backend, as we use a hosted PostgreSQL instance from AWS.  The deployment receives the necessary credentials to connect to this PostgreSQL server from its environment (provided by a secret from the CI pipeline).

## The front-end (webui) application

This is the main user interface to Argus. This is a React application that acts as a bridge between end users and the API server that stores all the information. As such, its K8s deployment is very simple.


### webui deployment

This React application is written in TypeScript: To serve it up to end users, the application and its configuration is compiled into a set of static files that are served through a front-facing web server. I.e. the application runs entirely inside a user's web browser.

The container image is build using a two-stage `Dockerfile`:

1. A stage that builds the application and its configuration into a set of static files
2. A stage that builds an nginx server image, complete with the set of static files to serve.


See the [webui](./webui) directory for this deployment definition.


## Ingress and Service objects

We use an internal toolchain to generate the necessary Service, Ingress and NetworkPolicy objects, so they are not part of this example.

Since this deployment is based on having two separate web services, one for the API and one for serving the front-end static fiels, we typically set up two ingresses:

1. argus.uninett.no for the `webui` deployment (which is what day-to-day users access)
2. api.argus.uninett.no for the `api` deployment. Only API clients and Argus admins would normally access this.

Whenever the example show references to domains like `paas2.uninett.no`, it's because this is normally the domain where our review and staging deployments are served.
