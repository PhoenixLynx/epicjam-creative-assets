param([ValidateSet('v01', 'v02', 'v03', 'v04', 'v05', 'v06')][string]$Revision = 'v01')
Add-Type -AssemblyName System.Drawing
$sourcePath = Join-Path $PSScriptRoot ('source/ART-002_title_original_' + $Revision + '.png')
$exportPath = Join-Path $PSScriptRoot ('exports/title_keyart_' + $Revision + '.png')
$sourceImage = [System.Drawing.Image]::FromFile($sourcePath)
$outputImage = [System.Drawing.Bitmap]::new(1920, 1080, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$graphics = [System.Drawing.Graphics]::FromImage($outputImage)
try {
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $ratio = 1920.0 / 1080.0
    $cropWidth = [double]$sourceImage.Width
    $cropHeight = $cropWidth / $ratio
    if ($cropHeight -gt $sourceImage.Height) {
        $cropHeight = [double]$sourceImage.Height
        $cropWidth = $cropHeight * $ratio
    }
    $sourceRect = [System.Drawing.RectangleF]::new(($sourceImage.Width - $cropWidth) / 2, ($sourceImage.Height - $cropHeight) / 2, $cropWidth, $cropHeight)
    $graphics.DrawImage($sourceImage, [System.Drawing.RectangleF]::new(0, 0, 1920, 1080), $sourceRect, [System.Drawing.GraphicsUnit]::Pixel)
    $outputImage.Save($exportPath, [System.Drawing.Imaging.ImageFormat]::Png)
} finally {
    $graphics.Dispose()
    $outputImage.Dispose()
    $sourceImage.Dispose()
}
