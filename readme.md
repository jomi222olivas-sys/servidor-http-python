# Multi-threaded HTTP Server in Python (Pure Sockets)

This project is an educational implementation of a web server built from scratch using **Python 3** and its native `socket` module. It avoids external frameworks (like Flask or Django) to demonstrate the low-level workings of the HTTP protocol and TCP/IP communications.

## 🚀 Technical Features

* **Object-Oriented Architecture (OOP):** The server is encapsulated within the `HTTPWebServer` class, ensuring modularity and scalability.
* **Concurrency (Multi-threading):** Uses the `threading` module to handle multiple clients simultaneously without blocking the server.
* **Logging System:** Implements professional console logging with timestamps and severity levels (`INFO`, `ERROR`) to monitor traffic and debug issues.
* **Static File Handling:** Serves HTML, CSS, and images by automatically detecting the correct MIME type (using `mimetypes`).
* **Basic HTTP/1.1 Protocol:**
    * `200 OK` responses for found files.
    * `404 Not Found` responses for missing resources.
    * Basic handling of `GET` and `POST` methods.

## 📋 Requirements

* Python 3.x installed.
* Web browser (Chrome, Firefox, Edge, etc.).

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jomi222olivas-sys/servidor-http-python.git](https://github.com/jomi222olivas-sys/servidor-http-python.git)
    cd servidor-http-python
    ```

2.  **Run the server:**
    ```bash
    py server.py
    ```
    *(Or `python server.py` depending on your system).*

3.  **Access in browser:**
    Open your web browser and go to: `http://127.0.0.1:8080`

## 📂 Project Structure

```text
servidor-http-python/
│
├── public/              # Public assets directory
│   ├── index.html       # Homepage (Welcome card)
│   └── style.css        # Stylesheets
│
├── server.py            # Main logic (Sockets + Threading + OOP)
├── README.md            # Project documentation
└── LICENSE              # MIT License