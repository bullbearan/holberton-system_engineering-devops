# This is a line of text
exec { 'hard':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 65535/" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}
exec { 'soft':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 65535/" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
