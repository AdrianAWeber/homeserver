#!/usr/bin/perl
use warnings;
use strict;
use Data::Dumper;
use File::Copy;
use DBI;

my @args = split('-',$ENV{'QUERY_STRING'});

  print "Cache-Control: no-cache, must-revalidate, max-age=1\r\n";
  print "Expires: Thu, 01 Dec 1994 16:00:00 GMT\r\n";
  print "Content-type: application/json\r\n\r\n";

my $driver   = "Pg"; 
my $database = "homeserver";
my $dsn = "DBI:$driver:dbname = $database;host = 127.0.0.1;port = 5432";
my $userid = "postgres";
my $password = "\$postgres";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 })
   or die $DBI::errstr;
#print "Opened database successfully\n";

my $stmt = qq(SELECT rooms.Name, sensors.Name FROM ((rooms INNER JOIN boards ON rooms.Id = boards.room_Id) INNER JOIN sensors ON boards.Id = sensors.board_Id) ORDER BY rooms.Name ASC;);
my $sth = $dbh->prepare( $stmt );
my $rv = $sth->execute() or die $DBI::errstr;
if($rv < 0) {
#   print $DBI::errstr;
}
#print "\{\n";
my $curr_Room = "";
print "{\n";
while(my @row = $sth->fetchrow_array()) {
     #print "{\n"; 
     if ($curr_Room ne $row[0]) {
       if ($curr_Room ne "") { 
         print "},\n";
       }
       print "\"$row[0]\" : {\n";
     } else {
       print ",\n";
     }
     print "\"$row[1]\" : \"\"";
#     print "\"sensor\" : \"". $row[1] . "\"\n";
     #print "}\n";
     $curr_Room = $row[0];
}
print "}\n}\n";
#print "Operation done successfully\n";
$dbh->disconnect();
