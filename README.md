## webcms

### Installation direcions

Create the <code>~/envs</code> folder and copy your environment file into it.
If you don't have an environment file, use below contents to create one

<pre>
export WEB_USER="webuser"
export WEB_GROUP="webapps"
export WEB_ROOT_FOLDER="/webserver"
export VENV_NAME="cms_venv"

export REPO_URL="https://github.com/motleytech/webcms.git"
export REPO_NAME="webcms"


export PG_USER="webdbuser"
export PG_PW="pgsqlpassword"
export PG_DB="webcmsdb"
</pre>

Name the file as env_webcms.sh.

#### Bootstrapping the installation

Get the installation bootstrap script and execute it

<pre>
wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap.sh -o bootstrap.sh

bash ./bootstrap.sh
</pre>

That's it.