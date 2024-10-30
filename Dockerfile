FROM python:3.10-slim
WORKDIR /usr/src/app
COPY . .
# python -m venv env
# source /env/bin/activate
RUN pip install -r ./requirements.txt
RUN chmod +x main.py
ENTRYPOINT [ "python", "./main.py" ]