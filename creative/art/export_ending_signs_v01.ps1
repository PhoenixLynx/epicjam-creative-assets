Add-Type -AssemblyName System.Drawing
$out = Join-Path $PSScriptRoot 'exports'
function Brush($hex) { [Drawing.SolidBrush]::new([Drawing.ColorTranslator]::FromHtml($hex)) }
function Text($g,$s,$size,$color,$x,$y,$w,$h,$bold=$true) {
 $style = if($bold){[Drawing.FontStyle]::Bold}else{[Drawing.FontStyle]::Regular}
 $font=[Drawing.Font]::new('Arial',$size,$style,[Drawing.GraphicsUnit]::Pixel)
 $b=Brush $color; $format=[Drawing.StringFormat]::new()
 $format.Alignment=[Drawing.StringAlignment]::Center; $format.LineAlignment=[Drawing.StringAlignment]::Center
 try {$g.DrawString($s,$font,$b,[Drawing.RectangleF]::new($x,$y,$w,$h),$format)} finally {$font.Dispose();$b.Dispose();$format.Dispose()}
}
function Logo($g,$cx,$cy,$r,$hex) {
 $b=Brush $hex; $pen=[Drawing.Pen]::new($b,($r*0.09));$pen.StartCap='Round';$pen.EndCap='Round'
 try {
  $g.FillPie($b,($cx-$r),($cy-$r),($r*2),($r*2),180,180)
  $g.DrawLine($pen,($cx-$r*1.55),($cy+$r*0.28),($cx+$r*1.55),($cy+$r*0.28))
  $g.DrawLine($pen,($cx-$r*0.95),($cy+$r*0.62),($cx+$r*0.95),($cy+$r*0.62))
  foreach($deg in @(20,43,66,90,114,137,160)) {
   $a=$deg*[Math]::PI/180
   $g.DrawLine($pen,[single]($cx+[Math]::Cos($a)*$r*1.35),[single]($cy-[Math]::Sin($a)*$r*1.35),[single]($cx+[Math]::Cos($a)*$r*1.75),[single]($cy-[Math]::Sin($a)*$r*1.75))
  }
 } finally {$b.Dispose();$pen.Dispose()}
}
function Canvas($w,$h) {
 $im=[Drawing.Bitmap]::new($w,$h,[Drawing.Imaging.PixelFormat]::Format32bppArgb)
 $g=[Drawing.Graphics]::FromImage($im);$g.SmoothingMode='AntiAlias';$g.TextRenderingHint='AntiAliasGridFit'
 $g.Clear([Drawing.Color]::Transparent)
 return @($im,$g)
}
# Flat banner texture: border and small confetti marks, no painted perspective or hanging ropes.
$pair=Canvas 2048 512; $im=$pair[0];$g=$pair[1]
try {
 $b=Brush '#EAF3EE';$g.FillRectangle($b,24,24,2000,464);$b.Dispose()
 $pen=[Drawing.Pen]::new([Drawing.ColorTranslator]::FromHtml('#7FD3C4'),10);$g.DrawRectangle($pen,44,44,1960,424);$pen.Dispose()
 Logo $g 170 256 48 '#27665E'
 Text $g "THAT'S A WRAP" 132 '#15343C' 320 100 1400 200
 Text $g 'HALCYON CONTINUITY' 32 '#426D70' 420 310 1200 70
 foreach($v in @(@(1870,145,24,10),@(1820,320,12,30),@(1900,280,26,10))) {$b=Brush '#7FD3C4';$g.FillRectangle($b,$v[0],$v[1],$v[2],$v[3]);$b.Dispose()}
 $im.Save((Join-Path $out 'ART-010_wrap_banner_2048x512_v01.png'),[Drawing.Imaging.ImageFormat]::Png)
} finally {$g.Dispose();$im.Dispose()}
# Both chair backs share exactly the same canvas and baseline.
foreach($value in @('blank','4471')) {
 $pair=Canvas 1024 256;$im=$pair[0];$g=$pair[1]
 try {
  $b=Brush '#233238';$g.FillRectangle($b,0,0,1024,256);$b.Dispose()
  $pen=[Drawing.Pen]::new([Drawing.ColorTranslator]::FromHtml('#60736F'),2);$pen.DashStyle='Dash';$g.DrawRectangle($pen,14,14,996,228);$pen.Dispose()
  # Subtle regular weave lines remain quiet at distance.
  $pen=[Drawing.Pen]::new([Drawing.Color]::FromArgb(10,224,239,230),1)
  for($y=20;$y -lt 240;$y+=6){$g.DrawLine($pen,20,$y,1004,$y)};$pen.Dispose()
  $label=if($value -eq 'blank'){'DIRECTOR:'}else{'DIRECTOR: 4471'}
  Text $g $label 88 '#EDF4EF' 45 38 934 180
  $im.Save((Join-Path $out ('ART-013_director_card_'+$value+'_1024x256_v01.png')),[Drawing.Imaging.ImageFormat]::Png)
 } finally {$g.Dispose();$im.Dispose()}
}
# Overtime board: corporate production notice, deliberately different from handwritten lunch specials.
$pair=Canvas 1024 1024;$im=$pair[0];$g=$pair[1]
try {
 $g.Clear([Drawing.ColorTranslator]::FromHtml('#152A31'))
 $b=Brush '#7FD3C4';$g.FillRectangle($b,24,24,976,12);$b.Dispose()
 Text $g 'HALCYON / CRAFT SERVICES' 26 '#A5BDBB' 64 62 896 55
 Text $g 'OVERTIME MENU' 72 '#F2F4EE' 45 133 934 100
 Text $g 'AFTER HOURS. SAME COMMITMENT.' 23 '#7FD3C4' 60 238 904 45
 $pen=[Drawing.Pen]::new([Drawing.ColorTranslator]::FromHtml('#48656A'),2);$g.DrawLine($pen,80,320,944,320);$g.DrawLine($pen,80,495,944,495);$g.DrawLine($pen,80,700,944,700);$pen.Dispose()
 Text $g 'COFFEE' 54 '#7FD3C4' 80 341 864 85
 Text $g 'CAKE' 54 '#7FD3C4' 80 517 864 85
 Text $g "for later, don't touch" 33 '#EDF4EF' 80 605 864 60 $false
 Text $g 'craft services closes when' 35 '#EDF4EF' 65 743 894 60 $false
 Text $g 'the director says it closes' 35 '#EDF4EF' 65 802 894 60 $false
 Text $g 'PLEASE REMAIN AVAILABLE.' 23 '#7FD3C4' 80 924 864 45
 $im.Save((Join-Path $out 'ART-016_overtime_menu_1024_v01.png'),[Drawing.Imaging.ImageFormat]::Png)
} finally {$g.Dispose();$im.Dispose()}
