FROM weblate/weblate

USER root

COPY weblate_customization /usr/src/weblate_customization
RUN /app/venv/bin/uv pip install --no-cache-dir /usr/src/weblate_customization
ENV DJANGO_SETTINGS_MODULE=weblate_customization.settings

USER 1000
