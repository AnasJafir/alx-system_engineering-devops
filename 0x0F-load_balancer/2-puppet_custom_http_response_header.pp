# Add http response header with puppet

# updating ubuntu server first
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# installing nginx web server on server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# customizing Nginx http response header (X-Served-By HOSTNAME)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# starting service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
