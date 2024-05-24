## Healing

Este projeto foi desnvolvido durante a PystackWeek 10.0 e se trata de um site de consultas medicas online, criado utilizando a Framework Django. 

Colocando em pratica diversos conceitos de desenvolvimento web e ferramentas do Django para criar um site com sistema de cadastro e login, 
paginas onde os pascientes podem agendar suas consultas e acompanha-las e paginas onde os medicos conseguem gerenciar as consultas marcadas. 
Tudo isso utilizando validações para garantir acesso apenas aos setores que seu usuario tem permissão.
<br>

### Como executar:
<br>

* Clone o repositório utilizando o seguinte comando:

```bash
$ git clone https://github.com/pauloandrecss/healing_psw.git
```

* Vamos entrar em nossa pasta do projeto e criar um ambiente virtual:

```bash
$ cd healing_psw
$ python3 -m venv venv
```

* Agora podemos iniciar nosso ambiente virtual e instalar as bibliotecas necessarias:
  
```bash
$ source venv/bin/activate - Caso utilize linux
$ venv/Scripts/Activate - Caso utilize windows

$ pip install -r requirements.txt
```

* Com tudo instalado podemos criar a estrutura no nosso banco de dados:

```bash
$ python3 manage.py migrate
```

* Caso queira utilizar a sessão de administração do site crie um super usuário com o seguinte comando:

```bash
$ python3 manage.py createsuperuser
```

Siga os passos e preencha as informações do seu super usuário. 

* Agora com tudo pronto inicie o servidor utilizando o comando:

```bash
$ python3 manage.py runserver
```
obs: Caso esteja utilizando windows substitua o comando python3 por apenas python.
<br>
<br>
Acesse http://127.0.0.1:8000/ ou digite localhost:8000 em seu navegador e sinta-se livre para utilizar as funções do site.
