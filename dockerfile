# image base
FROM python:3

# declare workdir
WORKDIR /home/manhas/Desktop/Upload_your_image/Web-app-take-picture

# copy source from other dir to image
COPY . .

# Install requirements
RUN pip3 install -r requirements.txt

# run
CMD ["python","./app.py"]
