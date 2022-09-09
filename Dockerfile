
FROM arturcorreiajunior/back-pix:latest
WORKDIR /python/src

COPY ./main.py /python/src/main.py
RUN apt update
RUN apt install nano

EXPOSE 80

CMD ["tail","-f","/dev/null"]