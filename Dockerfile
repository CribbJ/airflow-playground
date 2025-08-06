FROM apache/airflow:3.0.3

# root user to perform apt-get commands
USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      vim \
    && apt-get autoremove -yqq --purge \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# airflow user to instal via pip
USER airflow

COPY requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt