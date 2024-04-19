# Define a file resource for /tmp/school

file { '/tmp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
    }
