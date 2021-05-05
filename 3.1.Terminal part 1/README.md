05.05.2021 

1. - 7. 
alexsp@alexsp-530U3C-530U4C:~/vagrant$ vagrant init
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
alexsp@alexsp-530U3C-530U4C:~/vagrant$ nano Vagrantfile
alexsp@alexsp-530U3C-530U4C:~/vagrant$ nano Vagrantfile
alexsp@alexsp-530U3C-530U4C:~/vagrant$ nano Vagrantfile
alexsp@alexsp-530U3C-530U4C:~/vagrant$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'bento/ubuntu-20.04'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'bento/ubuntu-20.04' version '202012.23.0' is up to date...
==> default: Setting the name of the VM: vagrant_default_1620215344928_72493
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Mounting shared folders...
    default: /vagrant => /home/alexsp/vagrant
alexsp@alexsp-530U3C-530U4C:~/vagrant$ vagrant ssh
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 System information disabled due to load higher than 1.0


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento
VBox basic memory is 1024 mbat 
8. Ознакомиться с разделами man bash, почитать о настройках самого bash:

какой переменной можно задать длину журнала history, и на какой строчке manual это описывается?
 что делает директива ignoreboth в bash?
HISTFILESIZE line 1165
Значение ignoreboth является сокращением для ignorespace и ignoredups.
9. В каких сценариях использования применимы скобки {} и на какой строчке man bash это описано?
Parameter Expansion line 1619
10. Основываясь на предыдущем вопросе, как создать однократным вызовом touch 100000 файлов? А получилось ли создать 300000?
touch test--{000..10000} or touch test--{000..30000} 30000 создать получилось13.
11. В man bash поищите по /\[\[. Что делает конструкция [[ -d /tmp ]]
Конструкция [[ -d /tmp ]] проверяет существование каталога, вернет ноль если файл существует и является каталогом.
12. Основываясь на знаниях о просмотре текущих (например, PATH) и установке новых переменных; командах, которые мы рассматривали, добейтесь в выводе type -a bash в виртуальной машине наличия первым пунктом в списке:

bash is /tmp/new_path_directory/bash
bash is /usr/local/bin/bash
bash is /bin/bash
(прочие строки могут отличаться содержимым и порядком)
vagrant@vagrant:~$ mkdir /tmp/new_path_directory
vagrant@vagrant:~$ cp /bin/bash /tmp/new_path_directory/bash
vagrant@vagrant:~$ PATH=/tmp/new_path_directory:$PATH
vagrant@vagrant:~$ type -a bash
bash is /tmp/new_path_directory/bash
bash is /usr/bin/bash
bash is /bin/bash

13. Чем отличается планирование команд с помощью batch и at?
at добавляет таск в заданное время
batch когда уровень загрузки системы ниже 1.5
14. vagrant halt
==> default: Attempting graceful shutdown of VM...
