# Gerador de Senhas Seguras

## Descrição
Este projeto é um gerador de senhas seguras desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica. O objetivo é permitir que os usuários gerem senhas com diferentes níveis de segurança, personalizando a composição das senhas de acordo com suas preferências.

## Funcionalidades
- **Geração de Senhas**: Cria senhas com base nas preferências do usuário (comprimento, inclusão de letras maiúsculas, minúsculas, números e símbolos).
- **Avaliação da Força da Senha**: Analisa a força da senha gerada e fornece uma classificação (Fraca, Moderada, Forte).
- **Copiar Senha**: Permite que o usuário copie a senha gerada para a área de transferência.
- **Salvar Senha**: Salva a senha gerada em um arquivo de texto com uma descrição opcional.
- **Dicas de Segurança**: Oferece dicas para a criação de senhas seguras.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para desenvolver o gerador de senhas.
- **Tkinter**: Biblioteca para construção da interface gráfica do usuário.

## Como Usar
1. **Instalação**: Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
2. **Executar o Código**: Salve o código em um arquivo `.py` e execute-o utilizando o terminal ou um ambiente de desenvolvimento integrado (IDE).
3. **Configurações**:
   - Insira o comprimento desejado da senha.
   - Selecione as opções para incluir letras maiúsculas, minúsculas, números e símbolos.
   - Escolha se deseja uma senha memorizável.
4. **Gerar Senha**: Clique no botão "Gerar Senha" para criar uma nova senha.
5. **Avaliar a Força**: A força da senha gerada será exibida automaticamente.
6. **Copiar ou Salvar**: Use os botões para copiar a senha para a área de transferência ou salvá-la em um arquivo de texto.

## Exemplo de Uso
```python
senha = gerar_senha(comprimento=16, maiusculas=True, minusculas=True, numeros=True, simbolos=True)
print(senha)
```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.

## Licença
Este projeto é licenciado sob a MIT License.

## Contato
Para dúvidas ou sugestões, entre em contato pelo e-mail: anderson_moegel@hotmail.com 
