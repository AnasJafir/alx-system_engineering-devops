#!/usr/bin/env bash
# Configuring ssh configuration file using puppet

file { '/etc/ssh/ssh_config':
	ensure => present,

	content => "
	#SSH client configuration
	Host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
