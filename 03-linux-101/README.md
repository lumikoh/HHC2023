# Linux 101

I did this with ChatGPT mainly to see how well it would be able to help.
I originally did this without obviously, but I thought this would at least
measure the usefulness of ChatGPT in case I would forget some commands.

```bash
Type "yes" to begin: yes
```
-----
```
Perform a directory listing of your home directory to find a troll and retrieve a present!
```

![linux01](../images/linux01.png)

```bash
cd ~
ls
```
-----
```
Now find the troll inside the troll.
```

![linux02](../images/linux02.png)

```bash
cat troll_19315479765589239
```
-----
```
Great, now remove the troll in your home directory.
```

![linux03](../images/linux03.png)

```bash
rm troll_19315479765589239
```
-----
```
Print the present working directory using a command.
```

![linux04](../images/linux04.png)

```bash
pwd
```
-----
```
Good job but it looks like another troll hid itself in your home directory. Find the hidden troll!
```
![linux05](../images/linux05.png)

```bash
ls -a
```
-----
```
Excellent, now find the troll in your command history.
```

![linux06](../images/linux06.png)

```bash
history
```
-----
```
Find the troll in your environment variables.
```
![linux07](../images/linux07.png)

```bash
env
```
-----
```
Next, head into the workshop.
```
![linux08](../images/linux08.png)

```bash
cd workshop
```
-----
```
A troll is hiding in one of the workshop toolboxes. Use "grep" while ignoring case to find which toolbox the troll is in.
```
![linux09](../images/linux09.png)

```bash
grep -i "troll" *
```
-----
```
A troll is blocking the present_engine from starting. Run the present_engine binary to retrieve this troll.
```
![linux10](../images/linux10.png)

```bash
chmod +x present_engine
./present_engine
```
-----
```
Trolls have blown the fuses in /home/elf/workshop/electrical. cd into electrical and rename blown_fuse0 to fuse0.
```
![linux11](../images/linux11.png)

```bash
cd electrical
mv blown_fuse0 fuse0
```
-----
```
Now, make a symbolic link (symlink) named fuse1 that points to fuse0
```
![linux12](../images/linux12.png)

```bash
ln -s fuse0 fuse1
```
-----
```
Make a copy of fuse1 named fuse2.
```
![linux13](../images/linux13.png)

```bash
cp fuse1 fuse2
```
-----
```
We need to make sure trolls don't come back. Add the characters "TROLL_REPELLENT" into the file fuse2.
```
![linux14](../images/linux14.png)

```bash
echo "TROLL_REPELLENT" >> fuse2
```
-----
```
Find the troll somewhere in /opt/troll_den.
```
![linux15](../images/linux15.png)

```bash
find /opt/troll_den -type f -iname "*troll*"
```
-----
```
Find the file somewhere in /opt/troll_den that is owned by the user troll.
```
![linux16](../images/linux16.png)

```bash
find /opt/troll_den -type f -user troll
```
-----
```
Find the file created by trolls that is greater than 108 kilobytes and less than 110 kilobytes located somewhere in /opt/troll_den.
```
![linux17](../images/linux17.png)

```bash
find /opt/troll_den -type f -size +108k -size -110k
```
-----
```
List running processes to find another troll.
```
![linux18](../images/linux18.png)

```bash
ps aux
```
-----
```
The 14516_troll process is listening on a TCP port. Use a command to have the only listening port display to the screen.
```
![linux19](../images/linux19.png)

```bash
netstat -tuln | grep 'LISTEN'
```
-----
```
The service listening on port 54321 is an HTTP server. Interact with this server to retrieve the last troll.
```
![linux20](../images/linux20.png)

```bash
curl http://localhost:54321
```
-----
```
Your final task is to stop the 14516_troll process to collect the remaining presents.
```
![linux21](../images/linux21.png)

```bash
pkill 14516_troll
```
-----

![linux22](../images/linux22.png)

I guess this part acts as some kind of statement &#x1F60E;
