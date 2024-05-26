# QR Code Generator

This project is a QR code generator application built using Python.

## Features

* Generates QR codes from url.
* Returns generated PNG through API endpoint. 

## Installation

### Local Installation (Without Docker):

1. **Clone this repository:**

```
git clone https://github.com/rserry/qr-code-generator.git
```

2. **Install dependencies:**

```
cd qr-code-generator
pip install -r requirements.txt
```

3. **Run the application:**

```
python src/qr_code_generator_api.py
```

This starts the QR code generator API service. You can then interact with it using your programming language of choice (refer to the "Usage" section for an example).

### Installation with Docker Compose:

1. **Prerequisites:** Ensure Docker and Docker Compose are installed on your system.

2. **Build the image (optional):**

   By default, Docker Compose will build the image during the first run. However, you can explicitly build the image beforehand:

   ```
   docker compose build
   ```

3. **Run the application:**

   Start the QR code generator service with Docker Compose:

   ```
   docker compose up -d
   ```

   The `-d` flag runs the container in detached mode, allowing the service to run in the background.

## Usage

The QR code generator API can be used programmatically to generate QR codes from text data. Here's a simple Python example:

```python
import requests

# Replace with the desired URL to encode
url_to_encode = "https://www.example.com/"

# Assuming the API is running locally on port 8080 (adjust if needed)
base_url = "http://localhost:8080"

# Construct the API endpoint with the URL parameter
api_endpoint = f"{base_url}/api/generate?url={url_to_encode}"

# Send a GET request to the constructed endpoint
response = requests.get(api_endpoint)

if response.status_code == 200:
  # QR code image data is returned in the response body
  qr_code_image = response.content

  # Save the QR code image to a file
  with open("qr_code.png", "wb") as f:
    f.write(qr_code_image)
    print("QR code image saved as qr_code.png")
else:
  print("Error generating QR code:", response.text)
```

This script sends a POST request to the API endpoint with the data to encode. The response will contain the QR code image data in a format you can save to a file.

**Note:** This is a basic example. You might need to adapt it based on your specific implementation and data format.

## Project Created with Gemini AI

It's important to acknowledge that this project was created with the assistance of Gemini AI, a large language model from Google AI. Gemini provided guidance for code generation and best practices throughout the development process.

## Contributing

Feel free to fork this repository and contribute your own improvements!

**Additional Notes:**

* The `docker compose.yml` file (assumed to exist in the project root) defines the service configuration for Docker Compose.
* Make sure the port mappings in `docker compose.yml` (if any) match your desired configuration.
