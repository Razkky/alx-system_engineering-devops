# Fix the failed request by increase the number of trafic handled by server

# Increase trafic limit in default file
exec { 'increase-trafic':
    command => 'sed -i s"/15/4099/" /etc/default/nginx'
    path    => '/usr/local/bin/:/bin/'
}   ->

# Restart nginx
exec { 'restart-nginx':
    command => 'nginx restart'
    path    => '/etc/init.d/'
}