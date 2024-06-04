# Puppet manifest to ensure Apache is configured correctly

# Ensure the wp-config.php file exists and is correctly configured
file { '/var/www/html/wp-config.php':
  ensure  => file,
  content => template('mymodule/wp-config.php.erb'),
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Ensure Apache service is running
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/wp-config.php'],
}
