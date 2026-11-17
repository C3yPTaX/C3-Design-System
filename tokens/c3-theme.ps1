# Generiert aus tokens/tokens.json mit scripts/build-tokens.py. Nicht von Hand bearbeiten.
#
# Verwendung:  . "$PSScriptRoot\c3-theme.ps1"
#              $form.BackColor = $C3.Color.Bg.Canvas
#              $font = New-Object System.Drawing.Font($C3.Font.Family.Ui, $C3.Font.SizePt.Md)
# Schriftgrößen in Punkt, Maße in Pixel bei 96 dpi, Dauer in Millisekunden.

Add-Type -AssemblyName System.Drawing

$C3 = @{
    'Color' = @{
        'Brand' = @{
            'Cyan' = [System.Drawing.Color]::FromArgb(255, 7, 252, 253)
            'Teal' = [System.Drawing.Color]::FromArgb(255, 6, 208, 196)
            'Green' = [System.Drawing.Color]::FromArgb(255, 72, 247, 98)
            'Ice' = [System.Drawing.Color]::FromArgb(255, 213, 253, 254)
            'Deep' = [System.Drawing.Color]::FromArgb(255, 1, 7, 12)
            'Glow' = [System.Drawing.Color]::FromArgb(255, 6, 59, 61)
        }
        'Bg' = @{
            'Canvas' = [System.Drawing.Color]::FromArgb(255, 10, 13, 16)
            'Subtle' = [System.Drawing.Color]::FromArgb(255, 14, 18, 21)
            'Overlay' = [System.Drawing.Color]::FromArgb(184, 3, 5, 7)
        }
        'Surface' = @{
            'Card' = [System.Drawing.Color]::FromArgb(255, 20, 24, 29)
            'Input' = [System.Drawing.Color]::FromArgb(255, 26, 31, 37)
            'Popover' = [System.Drawing.Color]::FromArgb(255, 28, 33, 39)
            'Control' = [System.Drawing.Color]::FromArgb(255, 32, 38, 45)
            'ControlHover' = [System.Drawing.Color]::FromArgb(255, 41, 48, 58)
            'ControlPressed' = [System.Drawing.Color]::FromArgb(255, 28, 33, 40)
            'Disabled' = [System.Drawing.Color]::FromArgb(255, 23, 27, 32)
        }
        'Border' = @{
            'Subtle' = [System.Drawing.Color]::FromArgb(255, 35, 42, 49)
            'Default' = [System.Drawing.Color]::FromArgb(255, 46, 54, 63)
            'Strong' = [System.Drawing.Color]::FromArgb(255, 61, 71, 82)
            'Control' = [System.Drawing.Color]::FromArgb(255, 75, 86, 97)
            'Focus' = [System.Drawing.Color]::FromArgb(255, 77, 226, 232)
        }
        'Text' = @{
            'Primary' = [System.Drawing.Color]::FromArgb(255, 230, 235, 239)
            'Secondary' = [System.Drawing.Color]::FromArgb(255, 168, 178, 188)
            'Muted' = [System.Drawing.Color]::FromArgb(255, 138, 148, 158)
            'Disabled' = [System.Drawing.Color]::FromArgb(255, 94, 102, 112)
            'OnAccent' = [System.Drawing.Color]::FromArgb(255, 4, 24, 26)
            'Link' = [System.Drawing.Color]::FromArgb(255, 77, 226, 232)
        }
        'Accent' = @{
            'Default' = [System.Drawing.Color]::FromArgb(255, 25, 212, 220)
            'Hover' = [System.Drawing.Color]::FromArgb(255, 77, 226, 232)
            'Pressed' = [System.Drawing.Color]::FromArgb(255, 18, 179, 186)
            'Text' = [System.Drawing.Color]::FromArgb(255, 95, 230, 236)
            'Subtle' = [System.Drawing.Color]::FromArgb(255, 14, 42, 46)
            'SubtleHover' = [System.Drawing.Color]::FromArgb(255, 18, 54, 59)
            'Border' = [System.Drawing.Color]::FromArgb(255, 29, 106, 112)
        }
        'Secondary' = @{
            'Default' = [System.Drawing.Color]::FromArgb(255, 31, 199, 182)
            'Subtle' = [System.Drawing.Color]::FromArgb(255, 13, 42, 39)
        }
        'Status' = @{
            'Success' = [System.Drawing.Color]::FromArgb(255, 63, 217, 122)
            'SuccessSubtle' = [System.Drawing.Color]::FromArgb(255, 15, 42, 26)
            'SuccessBorder' = [System.Drawing.Color]::FromArgb(255, 31, 92, 54)
            'Warning' = [System.Drawing.Color]::FromArgb(255, 245, 165, 36)
            'WarningSubtle' = [System.Drawing.Color]::FromArgb(255, 46, 34, 12)
            'WarningBorder' = [System.Drawing.Color]::FromArgb(255, 107, 74, 18)
            'Danger' = [System.Drawing.Color]::FromArgb(255, 255, 107, 112)
            'DangerSolid' = [System.Drawing.Color]::FromArgb(255, 200, 55, 62)
            'DangerSolidHover' = [System.Drawing.Color]::FromArgb(255, 176, 46, 53)
            'DangerSubtle' = [System.Drawing.Color]::FromArgb(255, 46, 19, 22)
            'DangerBorder' = [System.Drawing.Color]::FromArgb(255, 110, 42, 46)
            'Info' = [System.Drawing.Color]::FromArgb(255, 25, 212, 220)
            'InfoSubtle' = [System.Drawing.Color]::FromArgb(255, 14, 42, 46)
            'InfoBorder' = [System.Drawing.Color]::FromArgb(255, 29, 106, 112)
        }
    }
    'Font' = @{
        'Family' = @{
            'Ui' = 'Segoe UI'
            'Mono' = 'Consolas'
        }
        'Weight' = @{
            'Regular' = 400
            'Semibold' = 600
        }
        'SizePt' = @{
            'Xs' = 9
            'Sm' = 9.75
            'Md' = 10.5
            'Lg' = 12
            'Xl' = 15
            '2xl' = 18
            '3xl' = 21
        }
    }
    'Space' = @{
        '0' = 0
        '1' = 4
        '2' = 8
        '3' = 12
        '4' = 16
        '5' = 20
        '6' = 24
        '8' = 32
        '10' = 40
        '12' = 48
    }
    'Radius' = @{
        'Xs' = 4
        'Sm' = 6
        'Md' = 8
        'Lg' = 10
        'Xl' = 14
        'Full' = 9999
    }
    'Size' = @{
        'Control' = @{
            'Sm' = 28
            'Md' = 32
            'Lg' = 40
        }
        'Icon' = @{
            'Sm' = 16
            'Md' = 20
        }
        'Row' = @{
            'Compact' = 32
            'Default' = 40
        }
        'Sidebar' = 232
        'Titlebar' = 44
        'FocusRing' = 2
    }
    'Motion' = @{
        'DurationMs' = @{
            'Instant' = 80
            'Fast' = 120
            'Normal' = 180
            'Slow' = 250
            'Loop' = 1400
            'Spin' = 900
        }
        'Easing' = @{
            'Standard' = @(0.2, 0, 0, 1)
            'Enter' = @(0.16, 1, 0.3, 1)
            'Exit' = @(0.4, 0, 1, 1)
            'Linear' = @(0, 0, 1, 1)
        }
        'DistancePx' = @{
            'Lift' = 2
            'Shift' = 4
            'Enter' = 8
        }
        'Scale' = @{
            'Press' = 0.98
            'Enter' = 0.97
        }
    }
}
