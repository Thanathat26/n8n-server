FROM n8nio/n8n:latest

USER root

RUN apk add --no-cache python3 py3-pip poppler-utils

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install typhoon-ocr PyPDF2

USER node

WORKDIR /home/node/project

RUN npm install pdf-lib
