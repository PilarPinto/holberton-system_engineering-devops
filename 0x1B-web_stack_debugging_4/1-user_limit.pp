#Fixing the failed  request
exec { 'Lenght range nofile fix':
    environment => ['ROUTE=/etc/security/limits.conf', 'HAR=hard nofile','SOF=soft nofile'],
    command     => 'sudo sed -i "s/$HAR 5/$HAR 40000/g" $ROUTE; sudo sed -i "s/$SOF 4/$SOF 20000/g" $ROUTE',
    provider    => 'shell'
}
