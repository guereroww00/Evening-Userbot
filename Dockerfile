FROM python:3.10

RUN git clone -b Evening-Userbot https://github.com/guereroww00/Evening-Userbot /home/evening/ && \
    chmod 777 /home/evening && \
    mkdir /home/evening/bin/

COPY ./sample_config.env ./config.env* /home/alby/

WORKDIR /home/evening/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
