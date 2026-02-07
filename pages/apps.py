from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'


'''
1. Em qual arquivo está definida a classe do formulário?
A classe do formulário está definida no arquivo forms.py.

2. Qual classe do Django ela estende?
A classe do formulário estende a classe forms.Form do Django.

3. Onde ocorre a validação dos dados?
A validação dos dados ocorre dentro da classe do formulário em forms.py, nos métodos clean_<campo>: clean_nome, clean_mensagem.

4. Em que momento clean_mensagem é executado?
O método clean_mensagem é executado quando o formulário é validado com o método is_valid().

5. O que acontece quando a requisição é GET?
Quando a requisição é GET, significa que o usuário acessou a página do formulário pela primeira vez.

6. O que acontece quando a requisição é POST?
Quando a requisição é POST, significa que o formulário foi enviado.

7. Por que usamos form.is_valid()?
Usamos form.is_valid() para verificar se os dados preenchidos pelo usuário são válidos. Ele executa todas as validações:
Verifica se os campos obrigatórios foram preenchidos. Valida o formato dos campos, com o e-mail.
Executa as validações personalizadas.

8. Por que usamos cleaned_data?
O cleaned_data contém os dados do formulário após a validação. Ele só é preenchido se o formulário for válido (quando form.is_valid() retorna True).
'''
