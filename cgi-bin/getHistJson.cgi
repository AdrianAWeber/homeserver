#!/usr/bin/perl
use warnings;
use strict;
use Data::Dumper;
use File::Copy;
use DBI;

require "/home/adrian/jsroot/demo/createJson_lib.pl";

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
my $chId  = 15168;#7783;
my $Limit = 1001;

#my $stmt = qq(SELECT * FROM Array_Val WHERE channel_id='$chId' ORDER BY smpl_time DESC LIMIT $Limit;);#7783#15167
my $stmt = qq(SELECT S.*, A.* FROM sample S INNER JOIN Array_Val A ON S.smpl_time=A.smpl_time WHERE S.channel_id=A.channel_id AND S.channel_id='$chId' ORDER BY S.smpl_time DESC LIMIT $Limit;);

my $sth = $dbh->prepare( $stmt );
my $rv = $sth->execute() or die $DBI::errstr;
if($rv < 0) {
   #print $DBI::errstr;
}

my $string;
my $xBins = -0.5;
my $xNBin = $Limit;
my $stepSize = 1;
my $ftitle = "$chId";
my $xAxisTitle = "";
my $yAxisTitle = "";
my $NEntries = 0;
my $fName = "$chId";
my $min=0;
my $max=$Limit-1;

my @val ;#= (0,10,20,30,40,50,60,70,80,90,100,110);
my $cnt=0;
#while(my @row = $sth->fetchrow_array()) {
#  #print $row[1]. "  ". $row[6]  ."\n";
#  my $test = $row[6];
#  if (length $test > 0 ) {
#    @val[$cnt] = $test;
#  } else {
#    @val[$cnt] = 0;
#  }
#  $cnt++;
#}

my @array;
my $arr_cnt = -1;
while(my @row = $sth->fetchrow_array()) {
  if ($row[13] == 1) {
    $arr_cnt++;
    $array[$arr_cnt][0] = $row[6];
    print "TEST\n";
  };
  $array[$arr_cnt][$row[13]] = $row[14];
  
  $cnt++;
}

my $sizeA = @{$array[0]};

#print $sizeA."\n";
for (my $i=0; $i<($sizeA/2);$i++){
  printf(" 0x%4x  %f\n",$array[0][$i],$array[0][($sizeA/2)+$i]);
  #print $i."  ".$array[0][$i]."\n";
  
}


$string .= Start($fName,$ftitle);
$string .= XAxis($xNBin,$xBins,$stepSize,$xAxisTitle,$min,$max);
$string .= YAxis($yAxisTitle);
$string .= Values($xNBin,\$NEntries,@val);
$string .= Legend($NEntries);
$string .= Additional();
$string .= End();

#print "$string\n";

#open(my $fh, '>', '/home/adrian/jsroot/demo/test_perl.json');
#print $fh "$string";
#close $fh;



#print "Operation done successfully\n";
$dbh->disconnect();
