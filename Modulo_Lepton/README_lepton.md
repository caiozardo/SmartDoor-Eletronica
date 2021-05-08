Biblioteca python para capturar imagens da câmera Lepton com a conexão SPI na Raspbery Pi


Requer módulos cv2 e numpy. Em um sistema baseado em Debian, usamos:

```$ sudo apt-get install python-opencv python-numpy```

Você pode executar os exemplos no diretório de trabalho, mas uma configuração distutils está incluída para instalar em pacotes de sites para distribuição:

```$ sudo python setup.py install```

Lepton pode tomar como argumento opcional o dispositivo SPI no qual encontrar o Lepton. Se em seu sistema esse dispositivo for /dev/spidev0.1, você pode instanciar o Lepton como:

```
...
with Lepton("/dev/spidev0.1") as l:
  ...
  ```
  
  
