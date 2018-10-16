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

#my $stmt = qq(SELECT * FROM Array_Val WHERE channel_id='7474' LIMIT 1000;);
my $stmt = qq(SELECT * FROM sample WHERE channel_id='7478' AND status_id='5' ORDER BY smpl_time DESC LIMIT 100;);#7783#15167
#my $stmt = qq(SELECT * FROM (channel INNER JOIN chan_grp ON channel.grp_id = chan_grp.grp_id););

#my $stmt = qq(SELECT S.*, A.* FROM sample S INNER JOIN Array_Val A ON S.smpl_time=A.smpl_time WHERE S.channel_id=A.channel_id AND S.channel_id='15168' ORDER BY S.smpl_time DESC LIMIT 1800;);
#my $stmt = qq(SELECT * FROM Array_Val WHERE channel_id='7485' LIMIT 1000;);
my $sth = $dbh->prepare( $stmt );
my $rv = $sth->execute() or die $DBI::errstr;
if($rv < 0) {
   print $DBI::errstr;
}


#print "\{\n";

my $fields = $sth->{NAME};
print Dumper $fields;

my $isArrayVal = 0;
while(my @row = $sth->fetchrow_array()) {
my $size = @row;
$isArrayVal = 1;
for (my $i=0;$i<$size;$i++){
     print " |$i: ".$row[$i]."   ";
}
     print "\n";
#print $row[1]. "  ". $row[6]  ."\n";
#my $test = @row;
#print Dumper @row;
}

print("is Array: $isArrayVal \n");


#print "Operation done successfully\n";
$dbh->disconnect();
