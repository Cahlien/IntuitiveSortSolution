FROM python:latest
SHELL ["/bin/bash", "-c"]
COPY . /app
ENV TEST_DATA_FILE /app/instructions/sort_me.txt
RUN chown -R $UID /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "main.py", "/app/instructions/sort_me.txt"]