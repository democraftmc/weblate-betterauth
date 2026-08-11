FROM weblate/weblate

USER root

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN source /app/venv/bin/activate && uv pip install --no-cache-dir .
ENV DJANGO_SETTINGS_MODULE=weblate_customization.settings

USER 1000
