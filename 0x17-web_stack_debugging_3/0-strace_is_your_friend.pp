# Use strace for debug a server
exec { 'changeTypo':
  command  => 'sudo mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  provider => shell,
}
