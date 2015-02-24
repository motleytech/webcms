## webcms

Create your own djangocms and djangocms-blog based personal webserver in minutes featuring...

* Frontend editing
* Bootstrap theme out of bag - supports easy modification.
* Disqus based comments.
* Python and Django based.

### Installation directions

#### Directions for the production environment
You want the production environment if you want to get your website up and running asap. If you are interested in developing/modifying the site software (you need to know Python and Django), then you should follow the development directions (below). If you are not sure what you want, then you want the production environment.

The installation has 4 easy steps...

* Download and run `bootstrap_prod.py`...
<pre>
cd /tmp
wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap_prod.py -O bootstrap_prod.py
python bootstrap_prod.py
</pre>

This will create the `/webserver` folder and clone the git repository in `/webserver/webcms`.

* In `/webserver/conf` folder, edit the file `env_webcms.sh` and populate the values for passwords and django_secret. You should create your own values or use `makepasswd`  to generate random passwords (section on makepasswd below). Keep the values in the `env_webcms.sh` file secret... these are  essential to the security of your website.

* Modify the server settings file `/webserver/webcms/setup/ws_settings.py` to configure the server install. You should change the domains that you want to support by changing `SITE_DETAILS`. By default, there are 3 predefined domains with 1 django process assigned to handle each domain (you can assign more than 1).

* Run the install script...
<pre>
cd /webserver/webcms/setup;
python install.py
</pre>

The script will prompt you to create an admin user for managing your website. Go ahead and create one with a password of your choice. If the install procedure succeeds, your webserver is ready. Point your browser to http://www.yourwebsite.com/admin and start adding pages.

#### Directions for creating a dev environment

* Download and run `bootstrap_dev.py`...
<pre>
mkdir -p ~/dev/ws_project
cd ~/dev/ws_project
wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap_dev.py -O bootstrap_dev.py
python bootstrap_dev.py
</pre>

You should now have the git repository cloned in `~/dev/ws_project/webcms` folder.

* In `~/dev/ws_project/conf` folder, modify the file `env_webcms.sh` and populate the values for passwords and django_secret. You should create your own values or use `makepasswd`  to generate random passwords (section on makepasswd below). Keep the values in the `env_webcms.sh` file secret... these are essential to the security of your website. You might also want to set DJANGO_DEBUG="True" in dev mode.

* Modify the server settings file `~/dev/ws_project/webcms/setup/ws_settings.py` to configure the server install. You should change the domains that you want to support by changing `SITE_DETAILS`. By default, there are 3 predefined domains with 1 django process assigned to handle each domain.

* You can now modify the code in `~/dev/ws_project/webcms/`.

* When you are ready to try out your modifications...
<pre>
cd ~/dev/ws_project/webcms/setup
python install_dev.py
</pre>

and that's it. Your personal webserver should be ready.

Head over to `http://www.yourwebsite.com` to visit you page. If you have not registered your domain yet or you are running on a local vm to test things out, you can change your `/etc/hosts` file to fool your browser. Keep in mind that `http://localhost` will not work as nginx is not configured to listen on localhost.

#### Using makepasswd to generate passwords and secrets

`makepasswd` is an excellent tool to generate random passwords of different lengths. You can install it by typing `sudo apt-get -y install makepasswd`. An example usage of makepasswd...

<pre>
$ makepasswd --minchars=14 --maxchars=18 --count=20
F1vLxf56RxuHjjn
3ohQJvfpJQymK3i
iiSS2p2JshbwvfH
...
wQAa3EVEovuEnFz
YuPTudpwNTvTFoBuf
jeCA5saT9SdBDybHU
fCMduR9V4PeYr8rmY
</pre>
