# expand nginx user limit
exec { 'expand nginx user limit':
  command => '/bin/sed -i \'s/15/5000/\' /etc/default/nginx',
}

exec { 'restart webserver':
  command => '/usr/bin/service nginx restart',
}
