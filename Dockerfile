# start by pulling the python image
FROM python:3.10

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY . .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# to run application on horeku
CMD ["python", "app.py"]