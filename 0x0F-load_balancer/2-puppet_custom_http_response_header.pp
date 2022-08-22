# This is a line of text
exec { 'update':
  command => '/usr/bin/apt update',
}

package { 'nginx':
    ensure  => present,
	require => Exec['update'],
}

file_line {'header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
    ensure  => running,
	require => Package['nginx'],
}
