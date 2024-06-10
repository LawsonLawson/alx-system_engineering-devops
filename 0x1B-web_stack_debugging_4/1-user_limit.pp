# Puppet exec resource to change OS security configuration for the holberton user

exec { 'OS security config':
  # The 'command' attribute specifies the command to be executed.
  # This command uses 'sed' to replace occurrences of 'holberton' with 'foo'
  # in the /etc/security/limits.conf file.
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  
  # The 'path' attribute specifies the directories to include in the search path
  # for the command execution. This ensures that 'sed' is found and executed correctly.
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
