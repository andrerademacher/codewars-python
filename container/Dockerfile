FROM python:3.11-alpine
LABEL maintainer="andre.rademacher.business@googlemail.com"
RUN apk add git \
    && pip install --upgrade pip \
    && pip install git+https://github.com/codewars/python-test-framework.git#egg=codewars_test
USER 1000
WORKDIR /codewars/python311