## webcms

A djangocms and djangocms-blog based personal webserver. Create your own personal webserver in minutes with...

* Frontend editing
* Bootstrap theme out of bag - supports easy modification.
* Disqus based comments.
* Last and the best - Python and Django based.

### Installation directions

#### Directions for the production environment

* Download `bootstrap_prod.py` and run it to create directories and clone repo...
<pre>
cd /tmp
wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap_prod.py -O bootstrap_prod.py
python bootstrap_prod.py
</pre>

This should create the required folders `/webserver`, `/webserver-pip-cache` and  `/webserver-backup`. It will also clone the `webcms` repository in `/webserver/webcms`.

* Copy the `/webserver/webcms/conf/sample_env_webcms.sh` to `/webserver/conf/env_webcms.sh`.
<pre>
cp /webserver/webcms/conf/sample_env_webcms.sh /webserver/conf/env_webcms.sh
</pre>
Now, edit the secrets file in `/webserver/conf/env_webcms.sh`. Make up your own secret passwords.

* Modify the server settings file `/webserver/webcms/setup/ws_settings.py` to configure the server install. You can change the domain names and sites that you want to support here.

* Run the install script.
<pre>
cd /webserver/webcms/setup;
python install.py
</pre>

#### Directions for creating a dev environment

* Download the `bootstrap_dev.py` file and run it to set initial things up.

<pre>
mkdir ~/ws_project
cd ~/ws_project
wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap_dev.py -O bootstrap_dev.py
python bootstrap_dev.py
</pre>

* Modify the shell script `~/ws_project/conf/env_webcms.sh` to hold your webserver secret keys and passwords. Sample script shown below. Be sure to change these values.

* (Optional) Modify the `~/ws_project/setup/ws_settings.py` file to configure the installation. You can change the number / names of sites and django processes per site.

* You can modify the code in `~/ws_project/webcms/`.

* When you are done, try out your changes by running...
<pre>
cd ~/ws_project/webcms/setup
python install_dev.py
</pre>

and that's it. Your personal webserver is ready.


Head over to `http://www.yourwebsite.com` to visit you page. If you have not registered your domain yet (or running in dev mode), you can change your hosts file to fool your browser.
