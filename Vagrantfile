# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
   # https://docs.vagrantup.com.

  config.vm.hostname = "app"
  config.vm.box = "jesuejunior/centos7"
  config.vm.network "public_network", bridge: [
  # "en1: Wi-Fi (AirPort)",
  "en6: Broadcom NetXtreme Gigabit Ethernet Controller",
  ]
  # accessing "localhost:8000" will access port 8000 on the guest machine.
  config.vm.network "forwarded_port", guest: 8000, host: 9000
  #config.vm.network "forwarded_port", guest: 3306, host: 3306
  #config.vm.network "forwarded_port", guest: 5672, host: 5672
  #config.vm.network "forwarded_port", guest: 15672, host: 15672
  config.vm.network "forwarded_port", guest: 27017, host: 27005

  config.vm.synced_folder ".", "/app",  type: "virtualbox"
  config.vm.synced_folder "../", "/code",  type: "virtualbox"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "512"
   end

  config.vm.provision "shell", inline: <<-SHELL
    sudo yum install sshpass net-tools dos2unix
  SHELL
end
