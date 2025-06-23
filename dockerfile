
# FROM registry.gitlab.com/dinamica-clipping/infra/python-base:latest AS testing
FROM python:3.11-slim
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE
WORKDIR /app
COPY ./src/requirements.txt /app/requirements.txt
COPY ./src/apis/v1/tests/requirements.txt /app/requirements-tests.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements-tests.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
