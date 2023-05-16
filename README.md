# taller_airflow

En este repositorio puedes encontrar una máquina Vagrant para virtualbox con Docker instalado.

También existe un fichero "docker-compose" en la carpeta "docker" para desplegar Apache Airflow. 

Si no dispones de Vagrant puedes encontrar instrucciones en https://developer.hashicorp.com/vagrant/downloads.

Si no dispones de VirtualBox puedes encontrar instrucciones de instalación en https://www.virtualbox.org/wiki/Downloads

Con los anteriores recursos instalados solo deberías ejecutar:

    $ git clone https://github.com/jmaransay/taller_airflow.git

    $ cd taller_airflow

    $ vagrant up

Con los anteriores pasos la máquina virtual ya estaría creada y en funcionamiento.

Antes de acceder a las misma, para poder usar Apache Airflow, creamos las carpetas compartidas en las que los contenedores van a almacenar los datos generados:

    $ cd docker
    
    $ mkdir -p ./dags ./logs ./plugins
 
    $ mkdir -p ./postgresql/data
    
    $ echo -e "AIRFLOW_UID=$(id -u)" > .env

Después accedemos a la máquina:

    $ vagrant ssh

Y en la misma ejecutamos:

    $ cd /vagrant/docker

Creamos las componentes necesarias de la base de datos:

    $ docker compose up airflow-init

Y después "levantamos" toda la infraestructura:

    $ docker compose up

En principio, con los anteriores pasos completados, en http://192.168.56.11:8080 encontrarás la interfaz web de Airflow, cuyas credenciales son "airflow", "airflow". En https://192.168.56.11:9443 podrás encontrar la interfaz web de portainer.

Si tienes cualquier duda puedes ponerte en contacto con jesus-maria.aransay@unirioja.es
