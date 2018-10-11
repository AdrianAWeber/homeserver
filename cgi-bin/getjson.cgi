#!/usr/bin/perl
use warnings;
use strict;
use Data::Dumper;
use File::Copy;
my @args = split('-',$ENV{'QUERY_STRING'});




if($args[0] eq 'custom') {
  
  my @query = split('-',$ENV{'QUERY_STRING'},2);

  #system("QUERY_STRING=$query[1] /home/hadaq/trbsoft/daqtools/web/htdocs/tools/daq2json.pl");
        

  }
else {  
  print "Cache-Control: no-cache, must-revalidate, max-age=1\r\n";
  print "Expires: Thu, 01 Dec 1994 16:00:00 GMT\r\n";
  print "Content-type: application/json\r\n\r\n";
  unless($args[0] && $args[0] =~ m/\w+/) {exit;}
  system ("cat /var/www/html/files/".$args[0].".json")  if -e "/var/www/html/files/".$args[0].".json";
  }

