FROM python:3.10-slim-bullseye
WORKDIR /app

COPY helpers/* ./
RUN ./install_packages.sh software-properties-common \
    git ssh tini tree wget unzip postgresql-client gnupg2 \
    vim less \
    build-essential libpq-dev libssl-dev libffi-dev

# Fix TLS with postgres image
RUN sed -i 's/MinProtocol = TLSv1.2/MinProtocol = TLSv1.0/' /etc/ssl/openssl.cnf
RUN sed -i 's/^CipherString/# &/' /etc/ssl/openssl.cnf; exit 0

# Backend, python/Django
ARG VERSION=master
RUN echo "${VERSION}"
RUN git clone https://github.com/Uninett/Argus.git
RUN cd ./Argus; git checkout ${VERSION}
RUN cd ./Argus; pip install -e .

# Remove dotenv, django-extensions when in final production
RUN echo "Get newer dependency versions"
RUN LC_ALL=C.UTF-8 pip install "gunicorn>=20" argus-ticket-rt "humiologging>1.0.2" -r ./Argus/requirements-django32.txt && pip freeze
RUN echo '##########\n### DEBUG INFO:' && uname -n && tree && which python3 && echo $PYTHONPATH

COPY kubernetes ./kubernetes

ENV EMAIL_HOST 'REDACTED'
ENV EMAIL_PORT 25
ENV DJANGO_SETTINGS_MODULE 'kubernetes.settings'
ENV LOGLEVEL 'info'

ENTRYPOINT ["/usr/bin/tini", "-v", "--"]
