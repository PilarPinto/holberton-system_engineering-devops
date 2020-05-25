#Fixing the failed  request
exec { 'Lenght range fix':
    command  => ' sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
    provider => 'shell'
}
