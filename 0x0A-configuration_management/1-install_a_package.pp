# Install Flask version 2.1.0 using pip3 provider
# This ensures that Flask is installed with the specific version required

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug version 2.1.1 using pip3 provider
# This ensures that Werkzeug is installed with the specific version required

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
