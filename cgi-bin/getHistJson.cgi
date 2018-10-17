#!/usr/bin/perl
use warnings;
use strict;
use Data::Dumper;
use File::Copy;
use DBI;
use Time::Piece;

require "createJson_lib.pl";
require "timeDiff_lib.pl";
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
#print "Opened database successfully\n";
my $chId;
if (defined $args[0]) {$chId = $args[0];} else {$chId = 7474;}#7783;
#if ($chId eq "undefined"){ $chId = 7783;}
#print "@args[0]\n";
my $Limit = 100;
my $Address = 0;

#my $stmt = qq(SELECT sample.*, num_metadata.unit FROM sample,num_metadata WHERE sample.channel_id='$chId', sample.channel_id='$chId' ORDER BY sample.smpl_time DESC LIMIT $Limit;);#7783#15167
my $stmt = qq(SELECT S.*, A.* FROM sample S INNER JOIN Array_Val A ON S.smpl_time=A.smpl_time WHERE S.channel_id=A.channel_id AND S.channel_id='$chId' ORDER BY S.smpl_time DESC LIMIT $Limit;);#7783#15167 #AND seq_nbr='1'


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

if ($args[1] ne "undefined") {
  $ftitle = "$args[1]";
}
my $xAxisTitle = "";
my $yAxisTitle = "";
my $NEntries = 0;
my $fName = "$chId";
my $min=0;
my $max=$Limit-1;
my $TimeStamp=0;
my $TimeStamp_oldest=0;
my $TimeStamp_newest=0;

my @val;#= (0,10,20,30,40,50,60,70,80,90,100,110);
my @time;
my $cnt=0;
#################################
# ARRAY?

my @array;
my $arr_cnt = -1;



while(my @row = $sth->fetchrow_array()) {
  
  if ($row[13] == 1) {
    $arr_cnt++;
    $array[$arr_cnt][0] = $row[6];
    #print "TEST\n";
  };
  $array[$arr_cnt][$row[13]] = $row[14];
  $TimeStamp=$row[1];
  $cnt++;
}

if ($cnt >0) {
my $sizeA = @{$array[0]};

if ($Address == 0) {$Address=$array[0][0];}
#print $sizeA."\n";
my $valcnt=0;
for(my $j=0;$j<$arr_cnt;$j++){
  for (my $i=0; $i<($sizeA/2);$i++){
    #printf(" 0x%4x  %f\n",$array[0][$i],$array[0][($sizeA/2)+$i]);
    if ($array[$j][$i] == "$Address"){
      @val[$valcnt]=$array[0][($sizeA/2)+$i];
      $valcnt++;
    }
    #print $i."  ".$array[0][$i]."\n";
  }
}
$min = 0;
$max = $arr_cnt-1.5;
$xNBin = $arr_cnt;
}
##############################
## No Array
if ($cnt==0) {
  $Limit = 100;
  $xNBin = $Limit;
  $max = $Limit-1;
  $stmt = qq(SELECT sample.* FROM sample WHERE sample.channel_id='$chId' AND status_id='5' ORDER BY sample.smpl_time DESC LIMIT $Limit;);#7783#15167
  $sth = $dbh->prepare( $stmt );
  $rv = $sth->execute() or die $DBI::errstr;
  if($rv < 0) {
   #print $DBI::errstr;
  }
  
  my $fZeroEntry = 1;
  while(my @row = $sth->fetchrow_array()) {
  #print @val[$cnt]."\n";
  if (defined $row[5]) {
    @val[$cnt] = $row[5];
    $time[$cnt]= $row[1];
    if ( $row[5]!= 0) { $fZeroEntry=0;}
  } elsif (defined $row[6]) {
    @val[$cnt] = $row[6];
    $time[$cnt]= $row[1];
    $fZeroEntry = 0;
  } else {
    @val[$cnt] = -1;
    $fZeroEntry = 0;
  }
  $TimeStamp_oldest=$row[1];
  if ($cnt == 0) { 
    $TimeStamp_newest=$row[1];
  }
  $cnt++;
}

if ($fZeroEntry == 0) {
@time = reverse @time;
my $TimeArraySize=@time;
for (my $i=($TimeArraySize-1);$i>=0;$i--){
  if ($i == 0) { 
    $time[0]=0;
  } else {
    $time[$i] = TimeDiff($time[$i-1],$time[$i]); # old - new # in Seconds
  }
}


$xNBin= TimeDiff($TimeStamp_oldest,$TimeStamp_newest)+1;

$max = $xNBin;
#print $xNBin."\n";
if ($xNBin > 100000){
my $scale = $xNBin/1000;
#print $scale."\n";
my $size= @time;
  for (my $i=0;$i<$size;$i++){
    $time[$i]= int ($time[$i] / $scale);
  }
  $xNBin = int ($xNBin/1000);
  $stepSize = int $scale;
}

} else {
  $xNBin = 1;
  undef(@time);
  undef(@val);
  $time[0]=0;
  $val[0] =0;
}

$TimeStamp = $TimeStamp_oldest;

}

###############################################
$stmt = qq(SELECT unit FROM num_metadata WHERE channel_id='$chId';);
$sth = $dbh->prepare( $stmt );
$rv = $sth->execute() or die $DBI::errstr;
if($rv < 0){# print $DBI::errstr;
}

while(my @row = $sth->fetchrow_array()) {
  $yAxisTitle =$row[0];
}

@val = reverse @val;
my $sizeVal = @val;

$string .= Start($fName,$ftitle);
$string .= XAxis($xNBin,$xBins,$stepSize,$xAxisTitle,$min,$max,$TimeStamp);
$string .= YAxis($yAxisTitle);
$string .= Values($xNBin,\$NEntries,$sizeVal,@val,@time);
$string .= Legend($NEntries);
$string .= Additional();
$string .= End();

print "$string\n";


$dbh->disconnect();
