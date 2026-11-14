param([string]$TitleLine1 = 'TAKE', [string]$TitleLine2 = '4471')
Add-Type -AssemblyName System.Drawing
$sourcePath = Join-Path $PSScriptRoot 'source/ART-003_cover_original_v01.png'
$sourceImage = [System.Drawing.Image]::FromFile($sourcePath)
$plate = [System.Drawing.Bitmap]::new(630, 500)
$graphics = [System.Drawing.Graphics]::FromImage($plate)
try {
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $cropWidth = [double]$sourceImage.Width
    $cropHeight = $cropWidth / 1.26
    if ($cropHeight -gt $sourceImage.Height) { $cropHeight = [double]$sourceImage.Height; $cropWidth = $cropHeight * 1.26 }
    $sourceRect = [System.Drawing.RectangleF]::new(($sourceImage.Width-$cropWidth)/2, ($sourceImage.Height-$cropHeight)/2, $cropWidth, $cropHeight)
    $graphics.DrawImage($sourceImage, [System.Drawing.RectangleF]::new(0,0,630,500), $sourceRect, [System.Drawing.GraphicsUnit]::Pixel)
} finally { $graphics.Dispose(); $sourceImage.Dispose() }
try {
    $plate.Save((Join-Path $PSScriptRoot 'exports/itch_cover_art_v01.png'), [System.Drawing.Imaging.ImageFormat]::Png)
    $titled = $plate.Clone()
    try {
        $graphics = [System.Drawing.Graphics]::FromImage($titled)
        $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
        $font1 = [System.Drawing.Font]::new('Arial', 48, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
        $font2 = [System.Drawing.Font]::new('Arial', 74, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
        $white = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(244,248,245))
        $mint = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(127,211,196))
        try {
            $graphics.DrawString($TitleLine1, $font1, $white, 107, 100)
            $graphics.DrawString($TitleLine2, $font2, $mint, 104, 146)
        } finally { $font1.Dispose(); $font2.Dispose(); $white.Dispose(); $mint.Dispose(); $graphics.Dispose() }
        $titled.Save((Join-Path $PSScriptRoot 'exports/itch_cover_working_title_v01.png'), [System.Drawing.Imaging.ImageFormat]::Png)
        foreach ($entry in @(@('art', $plate), @('working_title', $titled))) {
            $thumb = [System.Drawing.Bitmap]::new(315, 250)
            $graphics = [System.Drawing.Graphics]::FromImage($thumb)
            try {
                $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
                $graphics.DrawImage($entry[1], [System.Drawing.Rectangle]::new(0,0,315,250))
                $thumb.Save((Join-Path $PSScriptRoot ('exports/itch_cover_' + $entry[0] + '_315_v01.png')), [System.Drawing.Imaging.ImageFormat]::Png)
            } finally { $graphics.Dispose(); $thumb.Dispose() }
        }
    } finally { $titled.Dispose() }
} finally { $plate.Dispose() }
