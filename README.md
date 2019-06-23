# INSTALAÇÃO 

**1) Primeiramente clone o repositório usando:**

$ git clone https://github.com/hirios/raspamb

$ cd raspamb


Obs: Você também pode baixar manualmente e extrair os arquivos para uma pasta.


**2) Instale as dependências:**

$ sudo pip install -r requirements.txt


**3) Baixando o driver (que permite a conexão do selenium com o navegado):

Obs: Escolha a versão específica para seu sistema operacional, de prefêrencia uma versão 74 do chromedrive.

**Download e extração do driver para Linux User que usam Google Chrome**

$ wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip

$ unzip chromedriver_linux64.zip

**Para Win User**

Baixe manualmente o driver extraia para mesma pasta que o arquivo raspamb.py está, ou para pasta bin do seu venv.

link para download do drive = https://chromedriver.storage.googleapis.com/index.html?path=74.0.3729.6/

Esse driver usará o navegador chrome, mas existem outros drivers para outros navegadores como o Geckodrive  para Firefox, e PhantomJS, para utilizá-los, deverá modificar o código.


# Uso

Dentro da pasta onde está o raspamb.py e o chromedrive de o seguinte comando:

$ python raspamb.py




