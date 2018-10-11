#!/usr/bin/perl

use DBI;
use strict;

my $driver  = "Pg"; 
my $database = "postgres";
my $dsn = "DBI:$driver:dbname = $database;host = 127.0.0.1;port = 5432";
my $userid = "postgres";
my $password = "\$postgres";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 }) 
   or die $DBI::errstr;

print "Opened database successfully\n";

my $stmt = qq(SELECT * FROM role;);
my $sth = $dbh->prepare( $stmt );
my $rv = $sth->execute() or die $DBI::errstr;
if($rv < 0) {
   print $DBI::errstr;
}
while(my @row = $sth->fetchrow_array()) {
      print "ID = ". $row[0] . "\n";
      print "NAME = ". $row[1] ."\n\n";
}


print "Operation done successfully\n";
$dbh->disconnect();
