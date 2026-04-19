# Voice Intelligence: Integrando Whisper, ChatGPT e gTTS 

Este projeto demonstra a criação de uma interface de conversação por voz, unindo transcrição de áudio, processamento de linguagem natural e síntese de voz.

##  Objetivo
Desenvolver uma aplicação em Python capaz de ouvir o usuário, processar a pergunta via IA e responder vocalmente, simulando uma interação humana fluida.

##  Tecnologias Utilizadas
* **OpenAI Whisper:** Modelo de S2T (Speech-to-Text) para transcrição de áudio com alta precisão.
* **OpenAI ChatGPT (GPT-3.5/4):** Motor de processamento de texto para gerar respostas inteligentes.
* **gTTS (Google Text-to-Speech):** Biblioteca para converter a resposta de texto em áudio.
* **Python:** Linguagem base para integração das APIs.

##  Fluxo do Sistema
1. **Entrada:** O usuário grava um áudio (ou fornece um arquivo).
2. **Transcrição:** O Whisper converte o áudio em texto.
3. **Processamento:** O texto é enviado ao ChatGPT, que gera uma resposta.
4. **Saída:** O gTTS converte a resposta em um arquivo de áudio (.mp3) e o reproduz.

## Resumo do Funcionamento 
O script segue este fluxo lógico:

Autenticação: Configura a chave da API da OpenAI.

Transcrição (Whisper): O arquivo de áudio (.m4a, .mp3, etc.) é enviado para a OpenAI e transformado em texto.

Inteligência (ChatGPT): O texto transcrito é enviado ao modelo gpt-3.5-turbo para gerar uma resposta coerente.

Sintese de Voz (gTTS): A resposta em texto é convertida em um arquivo de áudio MP3 usando os servidores do Google.
