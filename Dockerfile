FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-openbsd libffi-dev libssl-dev musl
RUN apt-get install --fix-broken

RUN mkdir /code
WORKDIR /code
COPY . /code/

# Make .sh scripts executable
RUN dir

COPY requirements.txt /code/requirements.txt

# PIP INSTALL
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 cache purge
RUN pip3 install gunicorn

#ENTRYPOINT ["./scripts/wait-for-it.sh"]
CMD ["gunicorn", "--bind", "unix:/code/socket/sample.sock", "sample.wsgi:application"]
