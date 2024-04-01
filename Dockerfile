FROM python:3.9-alpine

# Alpine apk
RUN apk update && \
    apk add --no-cache \
        build-base \
        libffi-dev \
        libx11-dev \
        libjpeg-turbo-dev \
        libpng-dev \
        freetype-dev \
        openjpeg-dev \
        lcms2-dev \
        zlib-dev \
        tiff-dev \
        python3-dev

# Python requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir python-dotenv==1.0.1
RUN pip install --no-cache-dir PyMuPDF==1.24.0

# Workdir
WORKDIR /app

# Copy only the source code
COPY app/main.py .

# Default command
CMD ["python", "main.py"]
