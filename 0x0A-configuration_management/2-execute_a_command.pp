# This is a line of text
exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
}
