# expand nginx user limit
exec { 'expand nginx user limit':
  command => '/bin/sed -i "s/15/4000/g" /etc/default/nginx',
}

exec { 'restart webserver':
  command => 'service nginx restart',
}
