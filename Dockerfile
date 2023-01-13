FROM python:3.8-slim
COPY main.py /apps/
COPY requirements.txt /apps/
RUN pip install -r /apps/requirements.txt
EXPOSE 5000
CMD ["python3", "/apps/main.py"]