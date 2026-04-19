import openai
from gtts import gTTS
from IPython.display import Audio

# Configuração da API
openai.api_key = "SUA_CHAVE_AQUI"

# 1. Transcrição com Whisper
audio_file = open("audio.m4a", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
user_text = transcript["text"]
print(f"Usuário: {user_text}")

# 2. Resposta com ChatGPT
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": user_text}]
)
ai_response = response.choices[0].message.content
print(f"IA: {ai_response}")

# 3. Conversão para Voz com gTTS
tts = gTTS(ai_response, lang='pt')
tts.save("resposta.mp3")

# Ouvir a resposta
Audio("resposta.mp3")
