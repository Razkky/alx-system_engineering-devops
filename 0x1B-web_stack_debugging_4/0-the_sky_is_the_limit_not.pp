# Fix the failed request by increase the number of trafic handled by server

# Increase trafic limit in default file
exec { 'increase-traffic':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
