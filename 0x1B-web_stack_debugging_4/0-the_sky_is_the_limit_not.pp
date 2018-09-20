# expand nginx user limit
exec { 'expand nginx user limmit':
  command => '/bin/sed -i 's/15/5000/' /etc/default/nginx',
  command => '/usr/bin/service nginx restart',
}
