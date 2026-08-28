import os
import gradio as gradio
import requests

BACKEND_URL = os.getenv(
    "BACKEND_URL","http://backend-service:8080"
)

def processa_audio(audio_path):
    if audio_path is None:
        return "Nenhum áudio recebido"

    with open(audio_path, "rb") as f:
        files = ("file": ("audio.wav",
                        f, "audio/wav"))

        try:
            r = requests.post(
                f"{BACKEND_URL}/transcrever",
                files = files, timeout = 600
            )
            except request.RequestException as e:
                return f"Erro de conexão: {e}"

    if r.status_code != 200:
        return f"Erro no servidor: {r.status_code}"
    return r.json().get("texto","Sem texto.")
