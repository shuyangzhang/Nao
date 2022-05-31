# Nao: a MabiPro information integration bot for KaiHeiLa

FROM python:3.9-buster

MAINTAINER zhangshuyang <zhangshuyang@outlook.com>

ENV PYTHONIOENCODING=utf-8

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /Nao

COPY requirements.txt /Nao
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt && \
    rm -rf /tmp/*

COPY ./app /Nao/app
COPY ./startup.py /Nao

CMD ["python", "startup.py"]