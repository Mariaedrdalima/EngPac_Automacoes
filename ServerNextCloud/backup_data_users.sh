#! /bin/bash

DATE = "date + %Y%m%d - %H%M%S"

#Diretorio de Origem
dir_origim = " /home/dados/data"

#Diretorio Destino
dir_destino = " /home/Backup"
#Verificando se o diretório existe
if ( !dir_destino ); then
    ação aqui

else
    ação aqui
    echo "Iniciando backup - $DATE" > logsBackup
fi