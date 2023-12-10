from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TARGET_URL = "https://focus.teamleader.eu/backend/client-api/save_timetracking.php"


@app.route("/proxy", methods=["POST"])
def proxy():
    token = request.headers.get("Authorization")

    headers = {
        "Host": "focus.teamleader.eu",
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-TLC": "1",
        "TL-Strategy": "Content-replace",
        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://focus.teamleader.eu",
        "Connection": "keep-alive",
        "Referer": "https://focus.teamleader.eu/timesheets.php",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
    }
    cookies = {
        "teamleader_focus_session": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJzZXJ2aWNlLWF1dGgiLCJhY2NvdW50X2lkIjoxMDQ4MzMsInVzZXJfaWQiOjM4MDM3Niwic2Vzc2lvbl9pZCI6IjY0ODBlZDM1LWEzYTItNDRiZC04YzZjLTljN2I5MGU2OTE2ZiJ9.ImsADXEhRloLOSmx5t7MLQMX5H5Qzyq4dLq0-v9czs2Dz6q0ChlZyXA00RXGLWf7tn-duGA1cmwWAU1hAl_wkg",
        "teamleader_focus_session_id": "6480ed35-a3a2-44bd-8c6c-9c7b90e6916f",
    }

    if not token:
        return jsonify({"status": 400, "message": "token is required"})

    data = request.get_data()
    response = requests.post(TARGET_URL, data=data, headers=headers, cookies=cookies)
    return jsonify(
        {
            "status": response.status_code,
            "message": response.reason,
            "data": "ok",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
