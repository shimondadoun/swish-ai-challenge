# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /code

# expose port to listen
EXPOSE ${PORT}

# copy project
COPY . /code

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# run app
CMD uvicorn main:app --host 0.0.0.0 --port $PORT