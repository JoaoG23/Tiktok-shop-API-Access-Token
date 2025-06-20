# Tiktok shop API Access Token

Este repositório contém um exemplo de integração com a API OAuth do Tiktok Shop. Inclui um servidor Flask para autenticação e obtenção do token de acesso. Certifique-se de configurar corretamente as credenciais (App Key, App Secret) e a URL de redirecionamento antes de executar.

Como usar:
Crie um .env
```
TIKTOK_CLIENT_KEY=seu_app_key
TIKTOK_CLIENT_SECRET=seu_app_secret
TIKTOK_REDIRECT_URI=seu_redirect_uri
```

Configure as credenciais no código:

App Key: Identificador único da aplicação.
App Secret: Chave secreta usada para autenticação.

Execute o servidor Flask com **python tutorial.py**

Acesse a URL gerada pelo servidor e siga o fluxo de autenticação:

Você será redirecionado para a página de login do Tiktok Shop.
Após autenticar, será redirecionado para a URL configurada com o código de autorização.
O servidor trocará o código pelo token de acesso.
O token de acesso pode ser usado para realizar chamadas autenticadas à API do Tiktok Shop.
