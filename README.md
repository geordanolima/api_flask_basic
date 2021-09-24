# api_flask_basic
api para consumo de usuário simples para desenvolvimento de front end (login)
> cruds disponíveis:
> * usuarios
>  ``` json
>  {
>     "id": int,
>     "nome": str,
>     "usuario": str,
>     "senha": str,
>     "email": str,
>     "telefone": str,
>     "celular": str,
>     "foto": str
>  }
>  ```
> * permissoes-usuario
>  ``` json
>  {
>     "id": int,
>     "usuario_id": int,
>     "descricao": str,
>     "icone": str,
>     "habilita": bool
>  }
>  ```
