FROM python:3.11-slim
WORKDIR /app
COPY server.py /app/
RUN pip install flask requests
EXPOSE 7860
CMD ["python", "server.py"]
