FROM python:3.10-slim
WORKDIR /usr/src/app
COPY . .
RUN python -m venv env
RUN source /env/bin/activate
RUN pip install -r ./requirements.txt
RUN chmod +x main.py
ENTRYPOINT [ "python", "./main.py" ]