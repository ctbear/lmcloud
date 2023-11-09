FROM python:3.11
WORKDIR /lmcloud
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["bash"]