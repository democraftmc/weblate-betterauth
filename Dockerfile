FROM weblate/weblate:latest

# Switch to root to install packages
USER root

COPY ./weblate_custom /tmp/weblate_custom

RUN pip install --no-cache-dir /tmp/weblate_custom

# Revert to weblate user for the base image
USER weblate
