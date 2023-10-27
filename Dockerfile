FROM python:3.11-bookworm
LABEL maintainer="andre.rademacher.business@googlemail.com"

ARG GID=1000
ARG UID=1000
ARG UNAME=codewars

ARG PIPCACHE="/.cache/pip"

RUN groupadd \
    --gid ${GID} \
    --non-unique \
    ${UNAME}

RUN useradd \
    --create-home \
    --gid ${GID} \
    --home-dir /home/codewars \
    --shell /bin/bash \
    --uid ${UID} \
    ${UNAME}

RUN pip install --upgrade pip \
    && pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test

USER ${UNAME}
WORKDIR /codewars/python311

# setup
VOLUME "${PIPCACHE}"