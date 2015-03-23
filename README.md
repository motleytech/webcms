## webcms

Create your own djangocms and djangocms-blog based personal webserver in minutes featuring...

* Frontend editing
* Bootstrap theme out of bag - supports easy modification.
* Disqus based comments.
* Python and Django based.

### Installation directions

You want the production environment if you want to get your website up and running asap. If you are interested in developing/modifying the site software (you need to know Python and Django), then you should follow the development directions. If you are not sure what you want, then you want the production environment.

#### Directions for the production environment

The installation has 4 easy steps...

* Download and run `bootstrap_prod.py`...
<pre>
cd /tmp
wget https://raw.githubusercontent.com/motleytech/webcms/motleytechnet/setup/bootstrap_prod.py -O bootstrap_prod.py
python bootstrap_prod.py
</pre>

This will create the `/webserver` folder and clone the git repository in `/webserver/webcms`.

* In `/webserver/conf` folder, edit the file `env_webcms.sh` and populate the values for passwords and django_secret. You should create your own values or use `makepasswd`  to generate random passwords (section on makepasswd below). Keep the values in the `env_webcms.sh` file secret... these are  essential to the security of your website.

* Modify the server settings file `/webserver/webcms/setup/ws_settings.py` to configure the server install. You should change the domains that you want to support by changing `SITE_DETAILS`. By default, there is 1 domain defined with 1 django process assigned to handle it. You can have multiple domains with multiple django processes serving each domain.

* After the configuration, run the install script...
<pre>
cd /webserver/webcms/setup;
python install.py
</pre>

The script will install a bunch of stuff and will prompt you to create an admin user for managing your website. Go ahead and create one with a password of your choice. If the install procedure succeeds, your webserver is ready. Point your browser to `http://www.yourwebsite.com/admin` and start adding pages. Remember, `http://localhost/` might not work as nginx is not set to server at the localhost address in the production environment.

#### Directions for creating a dev environment

* Download and run `bootstrap_dev.py`...
<pre>
mkdir -p ~/dev/ws_project
cd ~/dev/ws_project
wget https://raw.githubusercontent.com/motleytech/webcms/motleytechnet/setup/bootstrap_dev.py -O bootstrap_dev.py
wget https://raw.githubusercontent.com/motleytech/webcms/motleytechnet/setup/bootstrap_prod.py -O bootstrap_prod.py
python bootstrap_dev.py
</pre>

You should now have the git repository cloned in `~/dev/ws_project/webcms` folder.

* In `~/dev/ws_project/conf` folder, modify the file `env_webcms.sh` and change the values for passwords and django_secret.

* Modify the server settings file `~/dev/ws_project/webcms/setup/ws_settings.py` to configure the server install. You should change the domains that you want to support by changing `SITE_DETAILS`.

* Now, execute the following commands to installed the prerequisites...
<pre>
cd ~/dev/ws_project/webcms/setup
python install_dev.py
</pre>

* Run your development server
<pre>
cd ~/dev/ws_project/webcms/djcms
source env.sh
python manage.py runserver 0.0.0.0:8000
</pre>

and that's it. Your development webserver is ready. Head over to `http://localhost:8000/` to visit your site.

You can now edit the code in `~/dev/ws_project/webcms/`, commit and push to your git repo and pull changes to your production environment.


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

