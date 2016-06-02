# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
   # https://docs.vagrantup.com.

  config.vm.hostname = "app"
  config.vm.box = "jesuejunior/centos7"
  config.vm.network "public_network", bridge: [
  "en6: Broadcom NetXtreme Gigabit Ethernet Controller",
  ]
  # accessing "localhost:8000" will access port 8000 on the guest machine.
  config.vm.network "forwarded_port", guest: 2375, host: 2375
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.synced_folder ".", "/app",  type: "virtualbox"
  config.vm.synced_folder "../", "/code",  type: "virtualbox"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "512"
     vb.name = "rocket"
   end

  config.vm.provision "shell", inline: <<-SHELL
    sudo yum install sshpass net-tools dos2unix -y
  SHELL
end
