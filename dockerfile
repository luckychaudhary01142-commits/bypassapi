FROM python:3.11-slim

# OS dependencies jo Chromium ke liye chahiye
RUN apt-get update && \
    apt-get install -y wget gnupg curl libnss3 libatk-bridge2.0-0 \
    libxkbcommon0 libgtk-3-0 libasound2 libxcomposite1 libxdamage1 \
    libxrandr2 libgbm1 libpango-1.0-0 libcups2 libdrm2 \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Playwright browser install
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
RUN python -m playwright install --with-deps

# Code copy
WORKDIR /opt/render/project/src
COPY . .

EXPOSE 10000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
