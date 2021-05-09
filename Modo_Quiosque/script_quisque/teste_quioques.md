/* Esse script será responsável por iniciar o Chromium e simular o acionamento das teclas. Para criar o script foi executado o seguinte comando:*/

```nano /home/pi/kiosk.sh```

/*define como o interpretador de comandos vai executar o arquivo*/

#!/bin/bash

# Essa três linhas impedem que o gerenciador de energia desligue ou apague a tela.

xset s noblank
xset s off
xset -dpms

#Essa linha executa o programa unclutter, anteriormente instalado. Essa aplicação esconde o mouse da tela sempre que o mesmo estiver ocioso por mais de 0,5 segundos. 
#Você pode ajustar a tempo conforme deseja ou, se deseja esconder o mouse imediatamente, remova o -idle 0.5 do comando

unclutter -idle 0.5 -root &

#Essas duas linhas de script são responsáveis por limpar qualquer mensagem que aparecer na barra de aviso do Chromium.

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

#Esta linha entrega ao Chromium nossos parâmetros.

/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk https://www.filipeflop.com https://www.raspberrypi.org

#Esse comando informa ao Chromium que ele não deve exibir nenhuma mensagem de erro para o usuário final

--noerrdialogs

#Esse comando impede que o Chromium exiba sua barra de informações para o usuário final.

--disable-infobars


#Essa opção coloca o Chromium em modo quiosque, fazendo assim que o acesso fique limitado

--kiosk

#Estas são as duas páginas web que o script abrirá, cada uma será aberta em uma nova guia. 
#Você pode adicionar outras páginas web, basta separar cada uma delas com um espaço.

https://www.filipeflop.com https://www.raspberrypi.org

#Essas linhas repetem o comando usando xdotool, também instalado anteriormente. 
#No caso o loop imita o pressionamento das teclas ctrl+tab, fazendo o Chromium mudar para a próxima guia. 
#Depois que o xdotool executa o pressionamento das teclas, ele coloca o loop em suspensão por 20 segundos.

while true; do
xdotool keydown ctrl+Tab; xdotool keyup ctrl+Tab;
sleep 20
done

#O Script final será mostrado abaixo

```#!/bin/bash
 
xset s noblank
xset s off
xset -dpms
 
unclutter -idle 0.5 -root &
 
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences
 
/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk https://www.filipeflop.com https://www.raspberrypi.org &
 
while true; do
xdotool keydown ctrl+Tab; xdotool keyup ctrl+Tab;
sleep 20
done ```

#Salve o arquivo pressionando as teclas crtl+x, em seguida y e depois enter.

###Iniciando o Raspberry Pi Quiosque

#Para que o nosso Raspberry Pi Quiosque inicie na inicialização, precisaremos criar um arquivo de serviço executando o comando abaixo. 
#Este arquivo de serviço informará ao sistema operacional qual arquivo queremos que seja executado e também  informará como queremos que a interface gráfica esteja disponível antes de iniciar o software.


```sudo nano /lib/systemd/system/kiosk.service```

#Dentro do nosso arquivo de serviço de kiosk, insira as seguintes linhas de texto. 
#Essas linhas definem nosso serviço de kiosk e também indicam que queremos executar nosso script kiosk.sh.


```[Unit]
Description=Chromium Kiosk
Wants=graphical.target
After=graphical.target
 
[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/pi/.Xauthority
Type=simple
ExecStart=/bin/bash /home/pi/kiosk.sh
Restart=on-abort
User=pi
Group=pi
 
[Install]
WantedBy=graphical.target```


#Salve o arquivo pressionando as teclas crtl+x, em seguida y e depois enter. 
#Agora que criamos o arquivo de serviço para o nosso Raspberry Pi Quiosque, podemos ativá-lo executando o seguinte comando:

```sudo systemctl enable kiosk.service```

#Para iniciar o Modo Quiosque use o seguinte comando:

```sudo systemctl start kiosk.service```


















































