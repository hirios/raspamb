# INSTALAÇÃO 

**1) Primeiramente clone o repositório usando:**

$ git clone https://github.com/amaimonrios/raspamb

$ cd raspamb


Obs: Você também pode baixar manualmente e extrair os arquivos para uma pasta


**2) Instale as dependências:**

$ sudo pip install -r requirements.txt


**3) Baixe o driver (que permite a conexão com o navegador) para o Selenium e deixe-o na mesma pasta que o raspamb.py**

Obs: Escolha a versão específica para seu sistema operacional, de prefêrencia uma versão 74 do chromedrive.


**Para Linux User que usam Google Chrome**

$ wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip


**Para Win User**

Baixe manualmente o driver e deixe na mesma pasta que o arquivo raspamb.py

link para download do drive = https://chromedriver.storage.googleapis.com/index.html?path=74.0.3729.6/

Esse driver usará o navegador chrome, mas existem outros drivers para outros navegadores como o Geckodrive  para Firefox, e PhantomJS, para utilizá-los, deverá modificar o código.


# Uso

Dentro da pasta onde está o raspamb.py e o chromedrive de o seguinte comando:

$ python raspamb.py




