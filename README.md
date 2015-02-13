## webcms

A djangocms and djangocms-blog based personal webserver.

It has frontend editing, bootstrap themes, disqus based comments and python goodness.

### Installation directions

Installation is a simple 4 step process

1. Use the bootstrap.py file to clone the repo locally.

`wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap.py`

2. Create a shell script `ws_project/conf/env_webcms.sh` to hold your webserver secret keys and passwords. Sample script shown below. Be sure to change these values.

2b. (Optional) Modify the setup/install_settings.py file to configure the installation. You can change the number / names of sites and django processes per site.

3. Run the install script.

```
cd setup;
python install.py
```

and that's it. Your personal webserver is ready.

####Sample shell script 

<pre>
export PG_USER_PW="something random and long here"
export PG_ADMIN_PW="something equally big here"
export DJANGO_SECRET="something perplexing here"
</pre>

You can copy these fields, modify them and save the file as env_webcms.sh.
