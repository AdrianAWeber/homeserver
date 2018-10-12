#!/usr/bin/perl

use warnings;
use strict;

require "createJson_lib.pl";  # assuming it's in the current directory

my $string;
my $xBins = -0.5;
my $xNBin = 12;
my $stepSize = 1;
my $ftitle = "Test Graph";
my $xAxisTitle = "Steps";
my $yAxisTitle = "a.u.";
my $NEntries = 0;
my $fName = "Test";

my @val = (0,10,20,30,40,50,60,70,80,90,100,110);


$string .= Start($fName,$ftitle);
$string .= XAxis($xNBin,$xBins,$stepSize,$xAxisTitle);
$string .= YAxis($yAxisTitle);
$string .= Values($xNBin,\$NEntries,@val);
$string .= Legend($NEntries);
$string .= Additional();
$string .= End();

open(my $fh, '>', 'test_perl.json');
print $fh "$string";
close $fh;
