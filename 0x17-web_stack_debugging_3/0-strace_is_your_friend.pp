# Puppet manifest to ensure Apache is configured correctly

# Define the path to the settings file
$settings_file = '/var/www/html/wp-settings.php'

# Ensure the settings file exists
file { $settings_file:
  ensure => file,
}

# Fix the typo in the settings file
exec { 'fix typo in settings config':
  path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
  command => "sed -i 's/phpp/php/g' ${settings_file}",
  require => File[$settings_file],
}
