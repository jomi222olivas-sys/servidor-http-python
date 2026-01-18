# 🌐 Servidor Web HTTP Multi-hilo en Python (Raw Sockets)

Un servidor web ligero implementado desde cero utilizando Python puro. Este proyecto simula las funcionalidades básicas de servidores como Apache o Nginx, implementando el protocolo HTTP/1.1 manualmente sin el uso de frameworks externos.

## 🚀 Características

* **Sin Frameworks:** Construido puramente con `socket` para entender la comunicación TCP/IP a bajo nivel.
* **Concurrencia:** Utiliza `threading` para manejar múltiples clientes simultáneamente.
* **Protocolo HTTP Manual:** Parseo de peticiones y construcción de encabezados (Headers) HTTP/1.1 artesanales.
* **Soporte de Métodos:**
    * `GET`: Sirve archivos estáticos (HTML, CSS).
    * `POST`: Maneja envío de formularios básicos.
* **Manejo de Errores:** Respuestas 404 personalizadas.

## 📋 Requisitos

* Python 3.x
* Ninguna librería externa requerida (solo librerías estándar).

## 🔧 Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/mi-servidor-http.git](https://github.com/TU_USUARIO/mi-servidor-http.git)
    cd mi-servidor-http
    ```

2.  **Iniciar el servidor:**
    ```bash
    python servidor.py
    ```

3.  **Probar en el navegador:**
    Abre tu navegador y visita: `http://127.0.0.1:8080`

## 🧠 ¿Cómo funciona?

El servidor inicia un socket TCP en el puerto 8080. Al recibir una conexión:
1.  Se crea un nuevo **hilo (thread)** para no bloquear el servidor principal.
2.  Se decodifica la petición cruda (bytes a string).
3.  Se analiza la primera línea del header HTTP (ej. `GET /index.html HTTP/1.1`).
4.  Dependiendo de la ruta y el método, se construye una respuesta byte a byte, incluyendo los **Headers** necesarios (`Content-Type`, `Content-Length`) y el cuerpo del mensaje.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

---
*Proyecto creado con fines educativos para comprender la arquitectura interna de la web.*