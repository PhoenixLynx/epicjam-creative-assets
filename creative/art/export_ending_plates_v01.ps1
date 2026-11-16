Add-Type -AssemblyName System.Drawing
function Label($g,$text,$x,$y,$size,$color='#EAF3EE') {
 $f=[Drawing.Font]::new('Consolas',$size,[Drawing.FontStyle]::Bold,[Drawing.GraphicsUnit]::Pixel)
 $b=[Drawing.SolidBrush]::new([Drawing.ColorTranslator]::FromHtml($color))
 try {$g.DrawString($text,$f,$b,$x,$y)} finally {$f.Dispose();$b.Dispose()}
}
$items=@(
 @('ART-011_cake_top',1024,1024),@('ART-014_skyline',4096,1024),
 @('ART-012a_desk',1920,1080),@('ART-012b_conference',1920,1080),
 @('ART-012c_corridor',1920,1080),@('ART-012d_ward',1920,1080),@('ART-015_soundstage',2048,1024))
foreach($item in $items){
 $name=$item[0];$w=$item[1];$h=$item[2]
 $src=[Drawing.Image]::FromFile((Join-Path $PSScriptRoot ('source/'+$name+'_original_v01.png')))
 $im=[Drawing.Bitmap]::new($w,$h,[Drawing.Imaging.PixelFormat]::Format32bppArgb)
 $g=[Drawing.Graphics]::FromImage($im)
 try {
  $g.Clear([Drawing.Color]::Transparent);$g.InterpolationMode='HighQualityBicubic';$g.PixelOffsetMode='HighQuality';$g.TextRenderingHint='AntiAliasGridFit'
  $cw=[double]$src.Width;$ch=$cw*$h/$w
  if($ch -gt $src.Height){$ch=[double]$src.Height;$cw=$ch*$w/$h}
  $y=($src.Height-$ch)/2
  if($name -eq 'ART-014_skyline'){$y=$src.Height-$ch}
  $g.DrawImage($src,[Drawing.RectangleF]::new(0,0,$w,$h),[Drawing.RectangleF]::new(($src.Width-$cw)/2,$y,$cw,$ch),[Drawing.GraphicsUnit]::Pixel)
  if($name -like 'ART-012*'){
   $b=[Drawing.SolidBrush]::new([Drawing.Color]::FromArgb(215,12,25,29))
   $g.FillRectangle($b,36,30,1848,72);$g.FillRectangle($b,36,978,1848,72);$b.Dispose()
   $scene=switch($name){'ART-012a_desk'{'DESK / EMPLOYEE 4471'};'ART-012b_conference'{'CONFERENCE / CALL'};'ART-012c_corridor'{'CORRIDOR B'};'ART-012d_ward'{'WARD / OBSERVATION'}}
   Label $g 'HALCYON / DAILIES' 58 45 36
   Label $g 'TAKE 4471' 1575 45 36 '#7FD3C4'
   Label $g $scene 58 993 32
   $tc=switch($name){'ART-012a_desk'{'09:00:14:07'};'ART-012b_conference'{'10:14:00:12'};'ART-012c_corridor'{'14:14:00:00'};'ART-012d_ward'{'02:14:00:00'}}
   Label $g $tc 1590 993 32
  }
  if($name -eq 'ART-015_soundstage'){
   # Labels placed on five blank badge fronts; sixth hook deliberately empty.
   $centers=@(1285,1419,1553,1687,1821)
   for($i=0;$i -lt 5;$i++){Label $g ([string](4466+$i)) ($centers[$i]-40) 505 29 '#17363D'}
  }
  $im.Save((Join-Path $PSScriptRoot ('exports/'+$name+'_'+$w+'x'+$h+'_v01.png')),[Drawing.Imaging.ImageFormat]::Png)
 } finally {$g.Dispose();$im.Dispose();$src.Dispose()}
}
