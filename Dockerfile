FROM python:3.12.11-alpine3.22 AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /workspace

COPY requirements.txt ./
RUN pip install --no-cache-dir --requirement requirements.txt

COPY mkdocs.yml ./
COPY docs ./docs
RUN mkdocs build --strict --site-dir /tmp/site

FROM nginxinc/nginx-unprivileged:1.29.1-alpine3.22 AS runtime

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder --chown=101:101 /tmp/site /usr/share/nginx/html

USER 101:101
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --quiet --spider http://127.0.0.1:8080/healthz || exit 1
