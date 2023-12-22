# Define the package name and version
$package_name = 'Flask'
$desired_version = '2.1.0'

# Ensure pip is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask with the specific version using pip
exec { "install_flask_${desired_version}":
  command => "/usr/bin/pip3 install ${package_name}==${desired_version}",
  path    => ['/usr/bin'],
  unless  => "/usr/bin/python3 -m flask --version | grep ${desired_version}",
}

