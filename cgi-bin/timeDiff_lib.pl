#!/usr/bin/perl
use strict;

sub TimeDiff{ # name,title
   my $time1 = $_[0];
   my $time2 = $_[1];

   my ($y1,$mon1,$day1,$hour1,$min1,$sec1,$mil1) = ($time1 =~ /(\d*)-(\d*)-(\d*) (\d*):(\d*):(\d*).(\d*)/);
   my ($y2,$mon2,$day2,$hour2,$min2,$sec2,$mil2) = ($time2 =~ /(\d*)-(\d*)-(\d*) (\d*):(\d*):(\d*).(\d*)/);
   
   my $Dy   = $y2   -$y1;
   my $Dmon = $mon2 -$mon1;
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
   my $ret = $Dy*365*24*60*60+$Dmon*30*24*60*60+$Dday*24*60*60+$Dh*60*60+$Dm*60+$Ds;
   return $ret;
}

#print TimeDiff("2018-10-11 15:23:22.123","2018-10-11 15:25:23.122")."\n";

1;
