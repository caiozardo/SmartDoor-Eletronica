
Para utilizarmos o Modo Quiosque na Raspian, foi utilizado os seguintes passos:

```sudo apt-get install xdotool unclutter sed```

O xdotool permite que o nosso script faça o pressionamento das teclas sem que ninguém esteja usando o dispositivo. E o unclutter permite esconder o mouse da tela.


Para que não seja necessário fazer o login toda vez que a Raspberry Pi Quiosque for iniciada, devemos habilitar a função autologin. 

Digite o seguinte comando:

```sudo raspi-config```

Selecionamos o Boot Options

![Quiosque](https://user-images.githubusercontent.com/55323167/117560521-df081880-b064-11eb-8c57-cd6bca67a2f5.JPG)

Selecione B1 Desktop/CLI

![Quiosque2](https://user-images.githubusercontent.com/55323167/117560534-f47d4280-b064-11eb-8f77-48b1df5f5fb3.JPG)

Selecione B4 Desktop Autologin

![Quiosque3](https://user-images.githubusercontent.com/55323167/117560544-05c64f00-b065-11eb-8854-5354ed5cb349.JPG)

Deste modo o Raspian está preparado para utilizar o Modo Quiosque.

### Escrevendo o script para o Raspberry Pi Quiosque









