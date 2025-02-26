FROM python:3

RUN apt-get update && \
    apt-get install -y git

WORKDIR /app

COPY requirements.txt process-info.py backend.py entrypoint.sh .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

CMD ["python","backend.py"]


