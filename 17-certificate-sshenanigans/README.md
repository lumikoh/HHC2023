# Certificate SSHenanigans

Most of this challenge was learning how the CA signing actually works. At first
I used a few hours just toying with the commands that were used in the video 
tutorial to have a little bit better picture of how they work.

After a little bit of figuring out, I managed to create myself a key pair 
and got the token from 
[the azure function app](https://northpole-ssh-certs-fa.azurewebsites.net/api/create-cert?code=candy-cane-twirl).
With the correct key, I was able to SSH to the machine. The instructions told
to use the monitor role.

```bash
ssh -i lumi-ssh-key -i lumi-ssh-key-cert.pub monitor@ssh-server-vm.santaworkshopgeeseislands.org
```

I actually think the process of discovery can be best shown with my terminal
output:

```bash
monitor@ssh-server-vm:~$ ls
monitor@ssh-server-vm:~$ ls -la
total 20
drwx------ 1 monitor monitor 4096 Nov  3 16:50 .
drwxr-xr-x 1 root    root    4096 Nov  3 16:50 ..
-rw-r--r-- 1 monitor monitor  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 monitor monitor 3649 Nov  9 17:05 .bashrc
-rw-r--r-- 1 monitor monitor  807 Apr 23  2023 .profile
monitor@ssh-server-vm:~$ cd ..
monitor@ssh-server-vm:/home$ ls
alabaster  monitor
monitor@ssh-server-vm:/home$ cd alabaster/
bash: cd: alabaster/: Permission denied
monitor@ssh-server-vm:/home$ ls
alabaster  monitor
monitor@ssh-server-vm:/home$ ls -la
total 16
drwxr-xr-x 1 root      root      4096 Nov  3 16:50 .
drwxr-xr-x 1 root      root      4096 Dec 20 21:37 ..
drwx------ 1 alabaster alabaster 4096 Nov  9 14:07 alabaster
drwx------ 1 monitor   monitor   4096 Nov  3 16:50 monitor
monitor@ssh-server-vm:/home$ cd monitor/
monitor@ssh-server-vm:~$ ls -la
total 20
drwx------ 1 monitor monitor 4096 Nov  3 16:50 .
drwxr-xr-x 1 root    root    4096 Nov  3 16:50 ..
-rw-r--r-- 1 monitor monitor  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 monitor monitor 3649 Nov  9 17:05 .bashrc
-rw-r--r-- 1 monitor monitor  807 Apr 23  2023 .profile
monitor@ssh-server-vm:~$ cat .profile
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
monitor@ssh-server-vm:~$ cd /etc
monitor@ssh-server-vm:/etc$ ls
X11                     deluser.conf  hostname       logcheck        pam.d       rcS.d        subuid
adduser.conf            dhcp          hosts          login.defs      passwd      resolv.conf  subuid-
alternatives            dpkg          hosts.allow    logrotate.d     passwd-     rmt          sv
apache2                 e2scrub.conf  hosts.deny     machine-id      perl        rpc          sysctl.conf
apt                     environment   init.d         mime.types      profile     runit        sysctl.d
bash.bashrc             ethertypes    inputrc        mke2fs.conf     profile.d   security     systemd
bindresvport.blacklist  fonts         issue          modules-load.d  protocols   selinux      terminfo
binfmt.d                fstab         issue.net      motd            python3     services     timezone
ca-certificates         gai.conf      kernel         mtab            python3.11  shadow       tmpfiles.d
ca-certificates.conf    gprofng.rc    ld.so.cache    nanorc          rc0.d       shadow-      ucf.conf
cron.d                  group         ld.so.conf     netconfig       rc1.d       shells       ufw
cron.daily              group-        ld.so.conf.d   networks        rc2.d       skel         update-motd.d
dbus-1                  gshadow       ldap           nsswitch.conf   rc3.d       ssh          vim
debconf.conf            gshadow-      libaudit.conf  opt             rc4.d       ssl          wgetrc
debian_version          gss           lighttpd       os-release      rc5.d       subgid       xattr.conf
default                 host.conf     localtime      pam.conf        rc6.d       subgid-      xdg
monitor@ssh-server-vm:/etc$ ls
X11                     deluser.conf  hostname       logcheck        pam.d       rcS.d        subuid
adduser.conf            dhcp          hosts          login.defs      passwd      resolv.conf  subuid-
alternatives            dpkg          hosts.allow    logrotate.d     passwd-     rmt          sv
apache2                 e2scrub.conf  hosts.deny     machine-id      perl        rpc          sysctl.conf
apt                     environment   init.d         mime.types      profile     runit        sysctl.d
bash.bashrc             ethertypes    inputrc        mke2fs.conf     profile.d   security     systemd
bindresvport.blacklist  fonts         issue          modules-load.d  protocols   selinux      terminfo
binfmt.d                fstab         issue.net      motd            python3     services     timezone
ca-certificates         gai.conf      kernel         mtab            python3.11  shadow       tmpfiles.d
ca-certificates.conf    gprofng.rc    ld.so.cache    nanorc          rc0.d       shadow-      ucf.conf
cron.d                  group         ld.so.conf     netconfig       rc1.d       shells       ufw
cron.daily              group-        ld.so.conf.d   networks        rc2.d       skel         update-motd.d
dbus-1                  gshadow       ldap           nsswitch.conf   rc3.d       ssh          vim
debconf.conf            gshadow-      libaudit.conf  opt             rc4.d       ssl          wgetrc
debian_version          gss           lighttpd       os-release      rc5.d       subgid       xattr.conf
default                 host.conf     localtime      pam.conf        rc6.d       subgid-      xdg
monitor@ssh-server-vm:/etc$ cd ssh/
monitor@ssh-server-vm:/etc/ssh$ ls
auth_principals  ssh_config            ssh_host_ed25519_key-cert.pub  ssh_host_rsa_key-cert.pub  sshd_config.d
ca.pub           ssh_config.d          ssh_host_ed25519_key.pub       ssh_host_rsa_key.pub
moduli           ssh_host_ed25519_key  ssh_host_rsa_key               sshd_config
monitor@ssh-server-vm:/etc/ssh$ cat ca.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGk2GNMCmJkXPJHHRQH9+TM4CRrsq/7BL0wp+P6rCIWH Elf Certificate Authority
monitor@ssh-server-vm:/etc/ssh$ cat ca
cat: ca: No such file or directory
monitor@ssh-server-vm:/etc/ssh$ cat ssh_host_ed25519_key
cat: ssh_host_ed25519_key: Permission denied
monitor@ssh-server-vm:/etc/ssh$ ls -la
total 620
drwxr-xr-x 1 root root   4096 Nov  9 14:07 .
drwxr-xr-x 1 root root   4096 Dec 20 21:37 ..
drwxr-xr-x 1 root root   4096 Nov  7 21:37 auth_principals
-rw-r--r-- 1 root root    107 Nov  9 14:07 ca.pub
-rw-r--r-- 1 root root 573928 Sep 23 22:11 moduli
-rw-r--r-- 1 root root   1650 Sep 23 22:11 ssh_config
drwxr-xr-x 1 root root   4096 Sep 23 22:11 ssh_config.d
-rw------- 1 root root    411 Nov  7 21:37 ssh_host_ed25519_key
-rw-r--r-- 1 root root    505 Nov  7 21:37 ssh_host_ed25519_key-cert.pub
-rw-r--r-- 1 root root     81 Nov  7 21:37 ssh_host_ed25519_key.pub
-rw------- 1 root root   2610 Nov  7 21:37 ssh_host_rsa_key
-rw-r--r-- 1 root root    973 Nov  7 21:37 ssh_host_rsa_key-cert.pub
-rw-r--r-- 1 root root    553 Nov  7 21:37 ssh_host_rsa_key.pub
-rw-r--r-- 1 root root   3223 Sep 23 22:11 sshd_config
drwxr-xr-x 1 root root   4096 Nov  7 21:37 sshd_config.d
monitor@ssh-server-vm:/etc/ssh$ cd auth_principals/
monitor@ssh-server-vm:/etc/ssh/auth_principals$ ls
alabaster  monitor
monitor@ssh-server-vm:/etc/ssh/auth_principals$ ls -la
total 16
drwxr-xr-x 1 root root 4096 Nov  7 21:37 .
drwxr-xr-x 1 root root 4096 Nov  9 14:07 ..
-rw-r--r-- 1 root root    6 Nov  7 21:37 alabaster
-rw-r--r-- 1 root root    4 Nov  7 21:37 monitor
monitor@ssh-server-vm:/etc/ssh/auth_principals$ cat alabaster
admin
monitor@ssh-server-vm:/etc/ssh/auth_principals$ cat monitor
elf
monitor@ssh-server-vm:/etc/ssh/auth_principals$ exit
logout
```

After toying around a bit, I figured out that the function app does allow me
to specify a principal in the body. Earlier digging showed that alabaster is 
linked to the principal admin. After requesting another key, I was able 
to connect with 

```bash
ssh -i lumi-ssh-key -i lumi-ssh-key-cert.pub alabaster@ssh-server-vm.santaworkshopgeeseislands.org
```

which did give me the access to the requested file:

```
alabaster@ssh-server-vm:~$ cat alabaster_todo.md
# Geese Islands IT & Security Todo List

- [X] Sleigh GPS Upgrade: Integrate the new "Island Hopper" module into Santa's sleigh GPS. Ensure Rudolph's red nose doesn't interfere with the signal.
- [X] Reindeer Wi-Fi Antlers: Test out the new Wi-Fi boosting antler extensions on Dasher and Dancer. Perfect for those beach-side internet browsing sessions.
- [ ] Palm Tree Server Cooling: Make use of the island's natural shade. Relocate servers under palm trees for optimal cooling. Remember to watch out for falling coconuts!
- [ ] Eggnog Firewall: Upgrade the North Pole's firewall to the new EggnogOS version. Ensure it blocks any Grinch-related cyber threats effectively.
- [ ] Gingerbread Cookie Cache: Implement a gingerbread cookie caching mechanism to speed up data retrieval times. Don't let Santa eat the cache!
- [ ] Toy Workshop VPN: Establish a secure VPN tunnel back to the main toy workshop so the elves can securely access to the toy blueprints.
- [ ] Festive 2FA: Roll out the new two-factor authentication system where the second factor is singing a Christmas carol. Jingle Bells is said to be the most secure.
alabaster@ssh-server-vm:~$ exit
```

This gets me the flag gingerbread cookie for the solution.