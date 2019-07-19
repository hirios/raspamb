# INSTALAÇÃO 

**1) Primeiramente clone o repositório usando:**

`<$ git clone https://github.com/hirios/raspamb>`

`<$ cd raspamb>`


Obs: Você também pode baixar manualmente e extrair os arquivos para uma pasta.


**2) Instale as dependências:**

`<$ sudo pip install -r requirements.txt>`


**3) Download e extração do driver para Linux User que usam Google Chrome**

`<$ wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip```

`<$ unzip chromedriver_linux64.zip>`

Obs: O arquivo extraído deve estar na mesma pasta do `raspamb.py` ou na pasta `bin` do `venv`, caso use ambiente virtual.

**Para Win User**

Baixe manualmente o driver e extraia para mesma pasta que o arquivo `raspamb.py` está, ou para pasta `bin` do seu `venv`, caso use ambiente virtual.

link para download do drive = https://chromedriver.storage.googleapis.com/index.html?path=74.0.3729.6/

Esse driver usará o navegador chrome, mas existem outros drivers para outros navegadores como o Geckodrive  para Firefox, e PhantomJS, para utilizá-los, deverá modificar o código.


# Uso

Dentro da pasta onde está o `raspamb.py` e o chromedrive dê o seguinte comando:

`<$ python raspamb.py>`

# Disclaimer
Não somos responsavel por nenhuma das fontes de download utilizadas por esse código. Todas elas pertencendo ao ambient e não tendo nenhuma relação conosco.

