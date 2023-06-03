##  Instalar Docker
# sudo apt update
# sudo apt install apt-transport-https ca-certificates curl software-properties-common


# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# sudo apt update
# sudo apt install docker-ce docker-ce-cli containerd.io

# Verificar la instalación de Docker
docker --version
sudo groupadd docker
# otorgar permisos a docker sin reiniciar la maquina
sudo usermod -aG docker $USER


# Instalar Docker Compose
# sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# sudo chmod +x /usr/local/bin/docker-compose

# Verificar la instalación de Docker Compose
# docker-compose --version


luego ir a la raiz del proyecto al nivel del archivo docker-compose.yml

y ejecutar:

docker-compose up -d

esto subira los servicios y lo expondra al puerto 3333 de la IP elastica de EC2 por lo tanto luego de ejecutar este comando


ejecutar docker ps 

y validar que el servicio este activo hacia el puerto 3333 de la maquina


luego ir a la web en la direccion ip elastica de la maquina ec2 en cuestion e ir hacia 

http://ip_elastica:3333/post_file_server

METODO POST 

en los parametros del multipart hacerlo asi

file
case_param
aditional_param

en file se carga el archivo cualquier
case param setearlo con algun valor cualquiera
y aditional_param igual

con el nombre que se envie el archivo asi quedara guardado ,   esta API guarda el archivo enviado en la ruta /mnt del servidor pero puede cambiar esa ruta editando
el archivo main.py

para recrear nuevamente los cambios debe  primero bajar los servicios

docker-compose down

luego ejecutar... 
docker-compose up --force-recreate -d

esto para que tome los cambios de codigo , y esto correra los servicios nuevamente  :)
