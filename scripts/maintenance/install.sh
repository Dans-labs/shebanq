#!/bin/bash

# READ THIS FIRST: maintenance.md

# Script to install a server.
# Run it on the server.

source ${0%/*}/config.sh


USAGE="
Usage: ./$(basename $0) [Options] [version]

Without options, it runs the complete installation process for a $APP server.
By means of options, you can select exactly one step to be performed.
The server must have been provisioned.

Options:
    --python: the python programming language
    --emdros: the emdros software
    --mysqlinstall: install mariadb (drop-in replacement of mysql)
    --mysqlconfig: configure mysql
    --static: load static data into mysql
    --dynamic: load dynamic data into mysql
    --$APP: clone $REPO
    --web2py: install web2py
    --apache: setup apache (assume certificates are already in place)

version:
    a valid SHEBANQ data version, such as 4, 4b, c, 2017, 2021
    It will restrict the data provisioning to the databases
    that belong to this version.
    If left out, all versions will be done.
    Especially relevant if --static is passed.

CAUTION
Take care with installing the current production server.
It might damage the current installation.
"

showUsage "$1" "$USAGE"

setSituation "$HOSTNAME" "Installing" "$USAGE"

ensureDir "$SERVER_UNPACK_DIR"

doAll="v"
doPython="x"
doEmdros="x"
doMysqlinstall="x"
doMysqlConfig="x"
doStatic="x"
doDynamic="x"
doShebanq="x"
doWeb2py="x"
doApache="x"

if [[ "$1" == "--python" ]]; then
    doAll="x"
    doPython="v"
    shift
elif [[ "$1" == "--emdros" ]]; then
    doAll="x"
    doEmdros="v"
    shift
elif [[ "$1" == "--mysqlinstall" ]]; then
    doAll="x"
    doMysqlinstall="v"
    shift
elif [[ "$1" == "--mysqlconfig" ]]; then
    doAll="x"
    doMysqlConfig="v"
    shift
elif [[ "$1" == "--static" ]]; then
    doAll="x"
    doStatic="v"
    shift
elif [[ "$1" == "--dynamic" ]]; then
    doAll="x"
    doDynamic="v"
    shift
elif [[ "$1" == "--$APP" ]]; then
    doAll="x"
    doShebanq="v"
    shift
elif [[ "$1" == "--web2py" ]]; then
    doAll="x"
    doWeb2py="v"
    shift
elif [[ "$1" == "--apache" ]]; then
    doAll="x"
    doApache="v"
    shift
fi

if [[ "$1" == "" ]]; then
    versions="$STATIC_VERSIONS"
else
    versions="$1"
    shift
fi

# stuff to get the emdros stuff working

# needed for the mql command
PATH=$PATH:$HOME/.local/bin:$HOME/bin
EMDROS_HOME=/opt/emdros
export EMDROS_HOME
PATH=$EMDROS_HOME/bin:$PATH
export PATH

# Install procedure

# Python
# * install module markdown (probably sudo pip3 install markdown)
# also: mod_wsgi

if [[ "$doAll" == "v" || "$doPython" == "v" ]]; then
    echo "o-o-o    INSTALL PYTHON o-o-o"
    yum -q -y install python36
    yum -q -y install python36-devel
    yum -q -y install python3-markdown
    # we need the python command (for emdros compilation)
    alternatives --set python /usr/bin/python3
    yum -q -y install mod_wsgi
fi

# MariaDB
# * install mariadb
# * configure mariadb
# * (/etc/my.cnf should contain default-character-set=utf8)
# * create users $MYSQL_USER and $MYSQL_ADMIN if needed
# * grant rights on tables to these users if needed

if [[ "$doAll" == "v" || "$doMysqlinstall" == "v" ]]; then
    echo "o-o-o    INSTALL MARIADB    o-o-o"
    yum -q -y install mariadb.x86_64
    yum -q -y install mariadb-devel.x86_64
    yum -q -y install mariadb-server.x86_64

    service mariadb start
fi

# We do Emdros right now, because some cfg files
# end up inside the emdros installation

if [[ "$doAll" == "v" || "$doEmdros" == "v" ]]; then
    echo "o-o-o    INSTALL Emdros    o-o-o"

    cd "$SERVER_INSTALL_DIR"
    tar xvf "$EMDROS_FILE"
    cd "$EMDROS_BARE"

    echo "o-o-o - Emdros CONFIGURE"
    ./configure --prefix=$SERVER_EMDROS_DIR --with-sqlite3=no --with-mysql=yes --with-swig-language-java=no --with-swig-language-python2=no --with-swig-language-python3=yes --with-postgresql=no --with-wx=no --with-swig-language-csharp=no --with-swig-language-php7=no --with-bpt=no --disable-debug

    echo "o-o-o - Emdros MAKE"
    make

    echo "o-o-o - Emdros INSTALL"
    make install

    cp -r "$SERVER_INSTALL_DIR/cfg" "$SERVER_EMDROS_DIR"
    chown -R apache:apache "$SERVER_EMDROS_DIR"
fi

skipUsers="x"
skipGrants="x"

if [[ "$doAll" == "v" || "$doMysqlConfig" == "v" ]]; then
    echo "o-o-o    CONFIGURE MYSQL    o-o-o"

    cd "$SERVER_INSTALL_DIR"

    if [[ "$DB_HOST" == "" ]]; then
        cp shebanq.cnf /etc/my.cnf.d/
        if [[ "$skipUsers" != "v" ]]; then
            echo "o-o-o - create users"
            mysql -u root < "$SERVER_CFG_DIR/user.sql"
        fi
        if [[ "$skipGrants" != "v" ]]; then
            echo "o-o-o - grant privileges"
            mysql -u root < grants.sql
        fi
    fi

    setsebool -P httpd_can_network_connect 1
    setsebool -P httpd_can_network_connect_db 1
fi

# Import dynamic data:
#   user-generated-content databases

if [[ "$DB_HOST" == "" ]]; then
    if [[ "$doAll" == "v" || "$doDynamic" == "v" ]]; then
        echo "o-o-o    LOAD DYNAMIC DATA start    o-o-o"
        for db in $DYNAMIC_NOTE $DYNAMIC_WEB
        do
            echo "o-o-o - DB $db"

            echo "o-o-o - creating fresh $db"
            mysql --defaults-extra-file=$SERVER_CFG_DIR/mysqldumpopt -e "drop database if exists $db;"
            mysql --defaults-extra-file=$SERVER_CFG_DIR/mysqldumpopt -e "create database $db;"

            echo "o-o-o - unzipping $db"
            cp "$SERVER_INSTALL_DIR/$db.sql.gz" "$SERVER_UNPACK_DIR"
            gunzip -f "$SERVER_UNPACK_DIR/$db.sql.gz"

            echo "o-o-o - loading $db"
            echo "use $db" | cat - $SERVER_UNPACK_DIR/$db.sql | mysql --defaults-extra-file=$SERVER_CFG_DIR/mysqldumpopt

            rm "$SERVER_UNPACK_DIR/$db.sql"
        done
        echo "o-o-o    LOAD DYNAMIC DATA end    o-o-o"
    fi
fi

# Import static data:
#   passage databases
#   emdros databases
#   user-generated-content databases

skipPdb="x"
skipEdb="x"

if [[ "$DB_HOST" == "" ]]; then
    if [[ "$doAll" == "v" || "$doStatic" == "v" ]]; then
        echo "o-o-o    LOAD STATIC DATA start    o-o-o"

        mysqlOpt="--defaults-extra-file=$SERVER_CFG_DIR/mysqldumpopt"

        for version in $versions
        do
            if [[ "$skipPdb" != "v" ]]; then
                echo "o-o-o - VERSION $version ${STATIC_PASSAGE}"
                db="$STATIC_PASSAGE$version"
                echo "o-o-o - unzipping $db"
                cp "$SERVER_INSTALL_DIR/$db.sql.gz" "$SERVER_UNPACK_DIR"
                gunzip -f "$SERVER_UNPACK_DIR/$db.sql.gz"
                echo "o-o-o - loading $db"
                mysql $mysqlOpt < "$SERVER_UNPACK_DIR/$db.sql"
                rm "$SERVER_UNPACK_DIR/$db.sql"
            fi

            if [[ "$skipEdb" != "v" ]]; then
                echo "o-o-o - VERSION $version ${STATIC_ETCBC}"
                db="$STATIC_ETCBC$version"
                echo "o-o-o - unzipping $db"
                cp $SERVER_INSTALL_DIR/$db.mql.bz2 $SERVER_UNPACK_DIR
                bunzip2 -f $SERVER_UNPACK_DIR/$db.mql.bz2
                echo "o-o-o - dropping $db"
                mysql $mysqlOpt -e "drop database if exists $db;"
                echo "o-o-o - importing $db"
                mqlPwd=`cat $SERVER_CFG_DIR/mqlimportopt`
                mqlOpt="-e UTF8 -n -b m -u $MYSQL_ADMIN"
                $SERVER_MQL_DIR/mql $mqlOpt -p $mqlPwd < $SERVER_UNPACK_DIR/$db.mql
                rm "$SERVER_UNPACK_DIR/$db.mql"
            fi
        done
        echo "o-o-o    LOAD STATIC DATA end    o-o-o"
    fi
fi

# clone $REPO

if [[ "$doAll" == "v" || "$doShebanq" == "v" ]]; then
    ensureDir "$SERVER_APP_DIR"
    chmod 755 /opt
    chmod 755 "$SERVER_APP_DIR"
    cd "$SERVER_APP_DIR"

    if [[ -d "$SERVER_APP_DIR/$APP" ]]; then
        echo "o-o-o    SHEBANQ pull    o-o-o"
        cd "$SERVER_SHEBANQ_DIR"
        git fetch origin
        git checkout master
        git reset --hard origin/master
    else
        echo "o-o-o    SHEBANQ clone    o-o-o"
        if [[ -e "$APP" ]]; then
            rm -rf "$APP"
        fi
        git clone "$REPO_URL"
    fi

    cd "$SERVER_APP_DIR"
    chown -R apache:apache $APP
    if [[ -e "$SERVER_WEB2PY_DIR" ]]; then
        compileApp $APP
    fi
fi

# install web2py

skipExtradirs="x"

if [[ "$doAll" == "v" || "$doWeb2py" == "v" ]]; then
    echo "o-o-o    WEB2PY START    o-o-o"

    # unpack Web2py

    echo "o-o-o - install"
    ensureDir "$SERVER_APP_DIR"
    chmod 755 /opt
    chmod 755 "$SERVER_APP_DIR"

    cd "$SERVER_APP_DIR"
    cp "$SERVER_INSTALL_DIR/$WEB2PY_FILE" web2py.zip
    if [[ -e web2py ]]; then
        rm -rf web2py
    fi
    unzip web2py.zip
    rm web2py.zip
    mv web2py/handlers/wsgihandler.py web2py/wsgihandler.py

    for pyFile in parameters_443.py routes.py
    do
        cp "$SERVER_INSTALL_DIR/$pyFile" web2py
    done

    compileApp admin

    echo "o-o-o - Removing examples app"
    rm -rf "$SERVER_WEB2PY_DIR/applications/examples"

    setsebool -P httpd_tmp_exec on

    # hook up SHEBANQ

    echo "o-o-o - hookup $APP"
    cd "$SERVER_WEB2PY_DIR/applications"
    if [[ -e $APP ]]; then
        rm -rf $APP
    fi
    ln -s "$SERVER_APP_DIR/$APP" "$APP"
    chown apache:apache "$APP"

    if [[ -e "$APP" ]]; then
        compileApp $APP
    fi

    cd "$SERVER_APP_DIR"
    chown -R apache:apache web2py
    chcon -R -t httpd_user_content_t /opt/web-apps/

    if [[ "$skipExtradirs" != "v" ]]; then
        echo "o-o-o - make writable dirs"
        cd "$SERVER_WEB2PY_DIR/applications"
        for app in welcome admin $APP
        do
            for dir in databases cache errors sessions private uploads
            do
                # if [[ -e ${app}/${dir} ]]; then
                #     rm -rf ${app}/${dir}
                # fi
                if [[ ! -e ${app}/${dir} ]]; then
                    mkdir ${app}/${dir}
                fi
                chown -R apache:apache ${app}/${dir}
                chcon -R -t tmp_t ${app}/${dir}
            done
        done
    fi

fi

# configure apache

if [[ "$doAll" == "v" || "$doApache" == "v" ]]; then
    echo "o-o-o    APACHE setup    o-o-o"

    if [[ -e "$APACHE_DIR/welcome.conf" ]]; then
        mv "$APACHE_DIR/welcome.conf" "$APACHE_DIR/welcome.conf.disabled"
    fi
    cp $SERVER_INSTALL_DIR/apache/*.conf "$APACHE_DIR"
    cp "$SERVER_INSTALL_DIR/wsgi.conf" "$APACHE_DIR"

    service httpd restart
fi

eraseDir "$SERVER_UNPACK_DIR"

# Todo after install
#
# Let DNS resolve the server name to the IP address of the newly
# installed server
