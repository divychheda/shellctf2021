FROM ubuntu

RUN  apt-get -y update && \
     apt-get -y install python  && \
     apt-get -y install python3-pip && \
     pip install pymodbus 

ADD server.py /root/server.py

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

RUN chmod +x /root/server.py

CMD ["./start.sh"]

EXPOSE 9999
