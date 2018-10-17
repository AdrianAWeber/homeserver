#!/usr/bin/perl
use strict;

sub TimeDiff{ # name,title
   my $time1 = $_[0];
   my $time2 = $_[1];

   my ($y1,$mon1,$day1,$hour1,$min1,$sec1,$mil1) = ($time1 =~ /(\d*)-(\d*)-(\d*) (\d*):(\d*):(\d*).(\d*)/);
   my ($y2,$mon2,$day2,$hour2,$min2,$sec2,$mil2) = ($time2 =~ /(\d*)-(\d*)-(\d*) (\d*):(\d*):(\d*).(\d*)/);
   
   my $Dy   = Year2Day($y2) - Year2Day($y1); ## years in days
   my $Dmon = Month2Day($mon2) -Month2Day($mon1);
   my $Dday = $day2 -$day1;
   my $Dh   = $hour2-$hour1;
   my $Dm   = $min2 -$min1;
   my $Ds   = $sec2 -$sec1;
   my $Dmil = $mil2 -$mil1;
   
  # print "Y: ".$Dy."\n";
  # print "Mo:".$Dmon."\n";
  # print "D: ".$Dday."\n\n";
  # print "H: ".$Dh."\n";
  # print "M: ".$Dm."\n";
  # print "S: ".$Ds."\n";
  # print "m: ".$Dmil."\n";
  # print "\n\n";
   my $ret = $Dy*24*60*60+$Dmon*24*60*60+$Dday*24*60*60+$Dh*60*60+$Dm*60+$Ds;
   return $ret;
}

sub Month2Day{
  my $year = $_[1];
  my @month = (0,31,59,90,120,151,181,212,243,273,304,334);
  my $ret = $month[$_[0]-1];#month,year
  if ((($year % 4) == 0) && $ret >59){$ret++;};
  return $ret;
}

sub Year2Day{
  my $yearIn = $_[0];
  my $yearDiff = $yearIn - 2000;
  my $ret = 0;
  for (my $i=0;$i<$yearDiff;$i++){
    if (((2000+$i)%4) ==0) {$ret += 366;} else {$ret += 365;};
  }

  return $ret;
}


#print TimeDiff("2018-10-11 15:23:22.123","2018-10-11 15:25:23.122")."\n";
#print Month2Day("2","2010")."\n";
#print Year2Day("2013")."\n";
#print TimeDiff("2018-10-11 15:23:22.123","2018-10-11 15:25:23.122")."\n";

1;
