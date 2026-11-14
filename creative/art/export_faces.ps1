param([string[]]$Variants = @('calm', 'fear'), [string]$Revision = 'v03')
Add-Type -AssemblyName System.Drawing
$artRoot = $PSScriptRoot
$exportRoot = Join-Path $artRoot 'exports'
New-Item -ItemType Directory -Force -Path $exportRoot | Out-Null
foreach ($variant in $Variants) {
    $sourcePath = Join-Path $artRoot ('source/ART-001_face_' + $variant + '_' + $Revision + '.png')
    $exportPath = Join-Path $exportRoot ('ART-001_face_' + $variant + '_1024_' + $Revision + '.png')
    $sourceImage = [System.Drawing.Image]::FromFile($sourcePath)
    $exportImage = [System.Drawing.Bitmap]::new(1024, 1024, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $graphics = [System.Drawing.Graphics]::FromImage($exportImage)
    try {
        $graphics.Clear([System.Drawing.Color]::Transparent)
        $graphics.CompositingMode = [System.Drawing.Drawing2D.CompositingMode]::SourceCopy
        $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        $graphics.DrawImage($sourceImage, [System.Drawing.Rectangle]::new(0, 0, 1024, 1024))
        $exportImage.Save($exportPath, [System.Drawing.Imaging.ImageFormat]::Png)
    } finally {
        $graphics.Dispose()
        $exportImage.Dispose()
        $sourceImage.Dispose()
    }
}
