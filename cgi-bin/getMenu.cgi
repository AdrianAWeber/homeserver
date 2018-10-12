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
my $database = "archive";
my $dsn = "DBI:$driver:dbname = $database;host = 127.0.0.1;port = 5432";
my $userid = "report";
my $password = "\$report";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 })
   or die $DBI::errstr;
print "Opened database successfully\n";


## Display all tables and views in the public schema:
#my $sth = $dbh->table_info('', 'public', undef, undef);
#for my $rel (@{$sth->fetchall_arrayref({})}) {
#  print "$rel->{TABLE_TYPE} name is $rel->{TABLE_NAME}\n";
#}

my $stmt = qq(SELECT * FROM sample WHERE channel_id='7471' ORDER BY smpl_time DESC LIMIT 10;);#7783#15167
#my $stmt = qq(SELECT * FROM (channel INNER JOIN chan_grp ON channel.grp_id = chan_grp.grp_id););

my $sth = $dbh->prepare( $stmt );
my $rv = $sth->execute() or die $DBI::errstr;
if($rv < 0) {
   print $DBI::errstr;
}


#print "\{\n";

my $fields = $sth->{NAME};
print Dumper $fields;


print $sth->{'float_val'}."\n";

while(my @row = $sth->fetchrow_array()) {
my $size = @row;

for (my $i=0;$i<$size;$i++){
     print " |$i: ".$row[$i]."   ";
}
     print "\n";
#print $row[1]. "  ". $row[6]  ."\n";
#my $test = @row;
#print Dumper @row;
}



#print "Operation done successfully\n";
$dbh->disconnect();
