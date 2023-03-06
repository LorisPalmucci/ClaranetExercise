#!/bin/sh

crontab -l > /home/user/newCrontabJob

echo "* * * * * tar -czvf /home/user/folder.tar.gz 
    scp -i /percorso della chiave privata /path/to/archive.tar.gz 
    user@remote_host:/path/on/remote_host" >> /home/user/newCrontabJob

crontab /home/user/newCrontabJob

rm /home/user/newCrontabJob