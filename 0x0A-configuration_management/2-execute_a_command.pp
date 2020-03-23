# Resources in puppet
exec {'killp':
  command  => 'pkill killmenow',
  provider => 'shell'
}