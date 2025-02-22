# Armarinho TPV Bot
Bot de geração de QR code para uso nos armários do TPV.

## Funcionalidades
- Geração de QR Code a partir de um código ou mensagem recebida.
- Comando `/start` para iniciar a interação com o bot.
- Comando `/help` para obter ajuda sobre como usar o bot.
- Tratamento de erros e mensagens de erro amigáveis.

## Pré-requisitos
- Python 3.12 ou superior
- [Pillow](https://pillow.readthedocs.io/en/stable)
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/)
- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/)
- [qrcode](https://pypi.org/project/qrcode/)
- [ruff](https://docs.astral.sh/ruff/)

## Como configurar
1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione as seguintes variáveis ao arquivo `.env`:
    ```env
    BOTFATHER_TOKEN="seu_token_aqui"
    BOT_USERNAME="@seu_bot_username"
    ```

## Como executar
1. Instale as dependências do projeto:
    ```sh
    pip install -r requirements.txt
    ```
2. Execute o bot:
    ```sh
    python main.py
    ```
## Recomendação
Recomenda-se o uso do [UV](https://docs.astral.sh/uv/) para o gerenciamento das dependências do projeto, garantindo um ambiente isolado e controlado.