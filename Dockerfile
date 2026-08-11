FROM weblate/weblate

USER root

COPY ./weblate_custom /usr/src/weblate_customization
RUN source /app/venv/bin/activate && uv pip install --no-cache-dir social-auth-core
RUN source /app/venv/bin/activate && uv pip install --no-cache-dir /usr/src/weblate_customization
ENV DJANGO_SETTINGS_MODULE=weblate_custom.settings

USER 1000
