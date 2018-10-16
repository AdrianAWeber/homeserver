sub Start{ # name,title
   my $string;
   my $fName  = $_[0];
   my $ftitle = $_[1];
   $string .= "{\n";
   $string .= "\"_typename\" : \"TH1F\",\n";
   $string .= "\"fBits\" : 0,\n";
   $string .= "\"fName\" : \"$fName\",\n";
   $string .= "\"fTitle\" : \"$ftitle\",\n";
   $string .= "\"fLineColor\" : 602,\n";
   $string .= "\"fFillColor\" : 20,\n";
   $string .= "\"fFillStyle\" : 1001,\n";
   $string .= "\"fMarkerColor\" : 1,\n";
   $string .= "\"fMarkerStyle\" : 1,\n";  
   $string .= "\"fMarkerSize\" : 5,\n";
   return $string;
}

sub XAxis{ # xNBINS,xBins,stepsize,AxisTITLE
   my $string;
   my $xNBin = $_[0];
   my $xBins = $_[1];
   my $stepSize = $_[2];
   my $xAxisTitle = $_[3];
   my $min = $_[4];
   my $max = $_[5];
   my $TimeStamp = $_[6];
   $string .= "\"fXaxis\" : { \n";
   $string .= "\"_typename\" : \"TAxis\",\n";
   $string .= "\"fBits\" : 0,\n";
   $string .= "\"fName\" : \"xaxis\",\n";
   $string .= "\"fTitle\" : \"$xAxisTitle\",\n",
   $string .= "\"fNdivisions\" : 512,\n";
   $string .= "\"fAxisColor\" : 1,\n";
   $string .= "\"fLabelColor\" : 1,\n";
   $string .= "\"fLabelFont\" : 42,\n";
   $string .= "\"fLabelOffset\" : 2.000000e-03,\n";
   $string .= "\"fLabelSize\" : 2.000000e-02,\n";
   $string .= "\"fTickLength\" : 3.000000e-02,\n";
   $string .= "\"fTitleOffset\" : 1.000000e+00,\n";
   $string .= "\"fTitleSize\" : 2.500000e-02,\n";
   $string .= "\"fTitleColor\" : 1,\n";
   $string .= "\"fTitleFont\" : 42,\n";
   $string .= "\"fNbins\" : ". $xNBin .",\n";
   $string .= "\"fXmin\" : $min,\n";
   $string .= "\"fXmax\" : $max,\n";
   $string .= "\"fXbins\" : [";
   for (my $i=0;$i<=$xNBin;$i++){
     $string .= "," if ($i!=0);
     $string .= $xBins +$stepSize*$i;
   }
   $string .= "],\n";
   $string .= "\"fFirst\" : 0,\n";
   $string .= "\"fLast\" : 0,\n";
   $string .= "\"fBits2\" : 0,\n";
   $string .= "\"fTimeDisplay\" : true,\n";
   $string .= "\"fTimeFormat\" : \"\%Y-\%m-\%d \%H:\%M:\%S\%F".$TimeStamp."\",\n";
   $string .= "\"fLabels\" : null\n";
   $string .= "},\n";
   return $string;
}

sub YAxis{
   my $string;
   my $yAxisTitle = $_[0];
   $string .= "\"fYaxis\" : { \n";
   $string .= "\"_typename\" : \"TAxis\",\n";
   $string .= "\"fBits\" : 0,\n";
   $string .= "\"fName\" : \"yaxis\",\n";
   $string .= "\"fTitle\" : \"$yAxisTitle\",\n";
   $string .= "\"fNdivisions\" : 512,\n";
   $string .= "\"fAxisColor\" : 1,\n";
   $string .= "\"fLabelColor\" : 1,\n";
   $string .= "\"fLabelFont\" : 42,\n";
   $string .= "\"fLabelOffset\" : 5.000000e-03,\n";
   $string .= "\"fLabelSize\" : 3.500000e-02,\n";
   $string .= "\"fTitleOffset\" : 1.000000e+00,\n";
   $string .= "\"fTitleSize\" : 3.500000e-02,\n";
   $string .= "\"fTitleColor\" : 1,\n";
   $string .= "\"fTitleFont\" : 42,\n";
   $string .= "\"fNbins\" : 1,\n";
   $string .= "\"fXbins\" : [],\n";
   $string .= "\"fFirst\" : 0,\n";
   $string .= "\"fLast\" : 0,\n";
   $string .= "\"fBits2\" : 0,\n";
   $string .= "\"fTimeDisplay\" : false,\n";
   $string .= "\"fTimeFormat\" : \"\",\n";
   $string .= "\"fLabels\" : null\n";
   $string .= "},\n";
   return $string;
}

sub Additional{
  my $string;
  $string .= "\"fBufferSize\" : 0,\n";
  $string .= "\"fBuffer\" : [],\n";
  $string .= "\"fBinStatErrOpt\" : 0\n";
  return $string;
}

sub Legend(){
  my $string;
  $NEntries = $_[0];
  $string .= "\"fBarOffset\" : 0,\n";
  $string .= "\"fBarWidth\" : 1000,\n";
  $string .= "\"fEntries\" : $NEntries,\n";
  #$string .= "\"fTsumw\" : 1.213022e+07,\n";
  #$string .= "\"fTsumw2\" : 1.213022e+07,\n";
  #$string .= "\"fTsumwx\" : -1.140346e+03,\n";
  #$string .= "\"fTsumwx2\" : 1.211905e+07,\n";
  #$string .= "\"fMaximum\" : -1.111000e+03,\n";
  #$string .= "\"fMinimum\" : -1.111000e+03,\n";
  #$string .= "\"fNormFactor\" : 0.000000e+00,\n";
  #$string .= "\"fContour\" : [],\n";
  $string .= "\"fSumw2\" : [],\n";
  $string .= "\"fOption\" : \"\",\n";
  $string .= "\"fFunctions\" : {\n";
  $string .= "\"_typename\" : \"TList\",\n";
  $string .= "\"name\" : \"TList\",\n";
  $string .= "\"arr\" : [{\n";
  $string .= "\"_typename\" : \"TPaveStats\",\n";
#  $string .= "\"fUniqueID\" : 0,\n";
#  $string .= "\"fBits\" : 50331657,\n";
  $string .= "\"fLineColor\" : 1,\n";
  $string .= "\"fLineStyle\" : 1,\n";
  $string .= "\"fLineWidth\" : 1,\n";
  $string .= "\"fFillColor\" : 0,\n";
  $string .= "\"fFillStyle\" : 1001,\n";
#Start of Position
  #$string .= "\"fX1\" : 85.0000025331975,\n";
  #$string .= "\"fY1\" : 907.200013518334,\n";
  #$string .= "\"fX2\" : 110.000003278256,\n";
  #$string .= "\"fY2\" : 1122.24001191616,\n";
  $string .= "\"fX1NDC\" : 0.780000016093254,\n";
  $string .= "\"fY1NDC\" : 0.775000005960464,\n";
  $string .= "\"fX2NDC\" : 0.980000019073486,\n";
  $string .= "\"fY2NDC\" : 0.935000002384186,\n";
#End of Position
  $string .= "\"fBorderSize\" : 1,\n";
  $string .= "\"fInit\" : 1,\n";
  $string .= "\"fShadowColor\" : 1,\n";
  $string .= "\"fCornerRadius\" : 0,\n";
  $string .= "\"fOption\" : \"brNDC\",\n";
  $string .= "\"fName\" : \"stats\",\n";
  $string .= "\"fTextAngle\" : 0,\n";
  $string .= "\"fTextSize\" : 0,\n";
  $string .= "\"fTextAlign\" : 12,\n";
  $string .= "\"fTextColor\" : 1,\n";
  $string .= "\"fTextFont\" : 42,\n";
  $string .= "\"fLabel\" : \"\",\n";
  $string .= "\"fLongest\" : 18,\n";
  $string .= "\"fMargin\" : 0.05,\n";
  $string .= "\"fLines\" : {\n";
  $string .= "\"_typename\" : \"TList\",\n";
  $string .= "\"name\" : \"TList\",\n";
  $string .= "\"opt\" : [\"\", \"\", \"\", \"\"]\n";
  $string .= "},\n";
  $string .= "\"fOptFit\" : 0,\n";
  $string .= "\"fOptStat\" : 1111,\n";
  $string .= "\"fFitFormat\" : \"5.4g\",\n";
  $string .= "\"fStatFormat\" : \"6.4g\",\n";
  $string .= "\"fParent\" : \"\$ref:0\"\n";
  $string .= "\}],\n";
  $string .= "\"opt\" : [\"brNDC\"]\n";
  $string .= "},\n";
  return $string;
}

sub Values(){
  my $string;
  my $xNBin       = shift;
  my $NEntriesRef = shift;
  my $NEntries    = ${$NEntriesRef};
  my $border      = shift;
  my @tmp_a       = @_;
  my @val;
  my @time;
  
  my $arraysize = @tmp_a;
  for(my $i=0;$i<$arraysize;$i++){
    if ($i < $border) {
      $val[$i] = $tmp_a[$i];
    } else {
      $time[$i-$border] = $tmp_a[$i];
    }
  }
  
  #print Dumper @time;
  #print ${$NEntries}."\n";
  
  $string .= "\"fArray\" : {\n";
  my $sizeArray = @val;
  my $EntryCnt = 0;
  my $timeCnt  = 0;
  for (my $i=0;$i<$xNBin;$i++){
    $string .= ",\n" if ($i!=0);
    $string .= "\"".($i+1)."\" : ";
    if ($EntryCnt < $sizeArray) { 
      if ($timeCnt < $time[$EntryCnt+1])  {
        $string   .= $val[$EntryCnt];
        $NEntries += $val[$EntryCnt];
       
        $timeCnt++;
        
      } elsif ($time[$EntryCnt+1] == 0) {
         $string   .= $val[$EntryCnt];
        $NEntries += $val[$EntryCnt];
      } else {
        #$string   .= " ".$EntryCnt."  ".$time[$EntryCnt+1]." ";
        #$string   .= "$timeCnt";
      }#print $timeCnt."\n";
      if ($timeCnt == $time[$EntryCnt+1]){$EntryCnt++;$timeCnt=0;}
    } else {
      $string .= "0";
    }
    
  }
  $string .= "\n},\n";
  ${$NEntriesRef} = $NEntries;
  return $string;
}

sub End() {
  my $string;
  $string .= "}\n";
  return $string;
}

1;
