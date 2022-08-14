# This is a line of text
file_line { 'set_password_authentication_to_no':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}
