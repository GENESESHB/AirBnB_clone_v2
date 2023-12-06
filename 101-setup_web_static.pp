# Manifest that configures an Nginx web server

# install Nginx
package { 'nginx':
  ensure => 'installed',
}

# create directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

# create an index.html file in /data/web_static/releases/test
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Welcome',
}

# create a symbolic link to /data/web_static/releases/test in /data/web_static/current
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# set ownership
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin:/usr/local/bin:/bin',
}

# create directories for Nginx default website
file { ['/var/www', '/var/www/html']:
  ensure => 'directory',
}

# create an index.html file for the default website
file { '/var/www/html/yasin.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# create a symbolic link to the default site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# configure Nginx to serve static files from /data/web_static/current
exec { 'add_lines':
  command  => 'sudo sed -i "s|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|" /etc/nginx/sites-enabled/default',
  provider => shell,
}
# ensure Nginx service is running
service { 'nginx':
  ensure => 'running',
}

