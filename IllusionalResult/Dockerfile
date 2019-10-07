FROM fedora:31

RUN dnf update -y && dnf install -y python3-devel python3-pip 
RUN pip install bottle
RUN pip install websocket-client
RUN pip install logger

COPY app.py routes.py utils.py /
CMD /app.py
