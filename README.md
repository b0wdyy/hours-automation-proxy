# Proxy hours automation client
This is a proxy server written with Flask. We need this proxy server since the website is blocked with CORS when trying to directly post from the client.

## Install

```bash
python3.x -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```bash
python main.py
```

## .env
Copy `.env.example` to `.env`. Copy the required cookies into the `.env` file. More details to be followed on how to do so. (Probably in the client)
