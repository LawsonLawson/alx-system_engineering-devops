# Puppet exec resource to modify the max open files limit setting for Nginx

exec { 'modify max open files limit setting':
  # The 'command' attribute specifies the command to be executed.
  # This command uses 'sed' to find and replace the number 15 with 10000
  # in the /etc/default/nginx file. After modifying the file, it restarts the
  # Nginx service to apply the changes.
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',

  # The 'path' attribute ensures that the specified directories are included in the
  # search path for the command execution. This makes sure that 'sed' and 'service'
  # commands are found and executed correctly.
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
