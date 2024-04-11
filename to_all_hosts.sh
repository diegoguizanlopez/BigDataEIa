sudo rm /home/cesgaxuser/.ssh/known_hosts

for servidor in $(cat /etc/hosts|grep Xuwir); 
	do ssh-keyscan -H $servidor; 
done >> /home/cesgaxuser/.ssh/known_hosts

clush -l cesgaxuser -bw Xuwira05-[2-4] --copy /etc/hosts --dest /home/cesgaxuser
clush -l cesgaxuser -bw Xuwira05-[2-4] sudo -S mv /home/cesgaxuser/hosts /etc/hosts

clush -l cesgaxuser -bw Xuwira05-[1-4] sudo reboot
reboot
