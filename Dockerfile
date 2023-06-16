FROM python:3.11
COPY . /code
WORKDIR /code
RUN pip install --upgrade pip &&  pip install -r requirements.txt && pip install pyinstaller
CMD python main.py