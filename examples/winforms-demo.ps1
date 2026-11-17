# C3yPTaX Design System: WinForms-Beispiel
#
# Zeigt Tokens, Programmicon, dunkle Titelleiste, eigengezeichnete Buttons mit
# Farbübergang und Karten. Gedacht als Vorlage, nicht als fertige Bibliothek.
#
# Start unter Windows mit Windows PowerShell 5.1:
#   powershell -ExecutionPolicy Bypass -File .\examples\winforms-demo.ps1

Add-Type -AssemblyName System.Windows.Forms, System.Drawing
. "$PSScriptRoot\..\tokens\c3-theme.ps1"

Add-Type -ReferencedAssemblies System.Windows.Forms, System.Drawing -TypeDefinition @'
using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace C3Demo
{
    public static class Motion
    {
        // Windows-Einstellung "Animationseffekte". Aus bedeutet: keine Übergänge.
        public static bool Enabled = SystemInformation.UIEffectsEnabled;

        // Kubische Bézierkurve wie in CSS (motion.easing.*)
        public static double Ease(double t, double x1, double y1, double x2, double y2)
        {
            double lo = 0, hi = 1, s = t;
            for (int i = 0; i < 12; i++)
            {
                s = (lo + hi) / 2;
                double x = 3 * (1 - s) * (1 - s) * s * x1 + 3 * (1 - s) * s * s * x2 + s * s * s;
                if (x < t) lo = s; else hi = s;
            }
            return 3 * (1 - s) * (1 - s) * s * y1 + 3 * (1 - s) * s * s * y2 + s * s * s;
        }

        public static Color Lerp(Color a, Color b, double t)
        {
            return Color.FromArgb(
                (int)(a.A + (b.A - a.A) * t), (int)(a.R + (b.R - a.R) * t),
                (int)(a.G + (b.G - a.G) * t), (int)(a.B + (b.B - a.B) * t));
        }

        public static GraphicsPath Rounded(Rectangle r, int radius)
        {
            int d = radius * 2;
            var p = new GraphicsPath();
            p.AddArc(r.X, r.Y, d, d, 180, 90);
            p.AddArc(r.Right - d, r.Y, d, d, 270, 90);
            p.AddArc(r.Right - d, r.Bottom - d, d, d, 0, 90);
            p.AddArc(r.X, r.Bottom - d, d, d, 90, 90);
            p.CloseFigure();
            return p;
        }

        [DllImport("dwmapi.dll")]
        static extern int DwmSetWindowAttribute(IntPtr hwnd, int attr, ref int value, int size);

        // Dunkle native Titelleiste, unter Windows 11 zusätzlich in Bg.Subtle
        public static void DarkTitleBar(Form f, Color caption)
        {
            int on = 1;
            DwmSetWindowAttribute(f.Handle, 20, ref on, 4);
            int colorRef = caption.R | (caption.G << 8) | (caption.B << 16);
            DwmSetWindowAttribute(f.Handle, 35, ref colorRef, 4);
        }
    }

    public class C3Button : Control
    {
        public Color Fill, FillHover, FillPressed, FillDisabled, TextColor, TextDisabled, FocusColor;
        public int Radius = 6;
        public int HoverMs = 120;
        public int PressMs = 80;

        Color current, from, to;
        DateTime start;
        int duration;
        bool hover;
        readonly Timer timer = new Timer { Interval = 15 };

        public C3Button()
        {
            SetStyle(ControlStyles.AllPaintingInWmPaint | ControlStyles.OptimizedDoubleBuffer |
                     ControlStyles.UserPaint | ControlStyles.ResizeRedraw | ControlStyles.Selectable, true);
            Cursor = Cursors.Hand;
            timer.Tick += Step;
        }

        protected override void OnCreateControl() { base.OnCreateControl(); current = Enabled ? Fill : FillDisabled; }

        void AnimateTo(Color target, int ms)
        {
            from = current; to = target; start = DateTime.Now; duration = ms;
            if (!Motion.Enabled || ms <= 0) { current = target; timer.Stop(); Invalidate(); return; }
            timer.Start();
        }

        void Step(object sender, EventArgs e)
        {
            double t = Math.Min(1.0, (DateTime.Now - start).TotalMilliseconds / duration);
            current = Motion.Lerp(from, to, Motion.Ease(t, 0.2, 0, 0, 1));   // motion.easing.standard
            Invalidate();
            if (t >= 1.0) timer.Stop();
        }

        protected override void OnMouseEnter(EventArgs e) { base.OnMouseEnter(e); hover = true; if (Enabled) AnimateTo(FillHover, HoverMs); }
        protected override void OnMouseLeave(EventArgs e) { base.OnMouseLeave(e); hover = false; if (Enabled) AnimateTo(Fill, HoverMs); }
        protected override void OnMouseDown(MouseEventArgs e) { base.OnMouseDown(e); Focus(); if (Enabled) AnimateTo(FillPressed, PressMs); }
        protected override void OnMouseUp(MouseEventArgs e) { base.OnMouseUp(e); if (Enabled) AnimateTo(hover ? FillHover : Fill, HoverMs); }
        protected override void OnEnabledChanged(EventArgs e) { base.OnEnabledChanged(e); AnimateTo(Enabled ? Fill : FillDisabled, 0); }
        protected override void OnGotFocus(EventArgs e) { base.OnGotFocus(e); Invalidate(); }
        protected override void OnLostFocus(EventArgs e) { base.OnLostFocus(e); Invalidate(); }

        protected override void OnKeyUp(KeyEventArgs e)
        {
            base.OnKeyUp(e);
            if (e.KeyCode == Keys.Space || e.KeyCode == Keys.Enter) OnClick(EventArgs.Empty);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            var g = e.Graphics;
            g.Clear(Parent != null ? Parent.BackColor : BackColor);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            var r = new Rectangle(0, 0, Width - 1, Height - 1);
            using (var path = Motion.Rounded(r, Radius))
            using (var b = new SolidBrush(current)) g.FillPath(b, path);
            if (Focused && ShowFocusCues)
            {
                using (var path = Motion.Rounded(new Rectangle(1, 1, Width - 3, Height - 3), Radius - 1))
                using (var pen = new Pen(FocusColor, 2)) g.DrawPath(pen, path);
            }
            TextRenderer.DrawText(g, Text, Font, ClientRectangle, Enabled ? TextColor : TextDisabled,
                TextFormatFlags.HorizontalCenter | TextFormatFlags.VerticalCenter | TextFormatFlags.NoPadding);
        }

        protected override void Dispose(bool disposing) { if (disposing) timer.Dispose(); base.Dispose(disposing); }
    }

    public class C3Card : Panel
    {
        public Color Fill, Border;
        public int Radius = 10;

        public C3Card()
        {
            SetStyle(ControlStyles.AllPaintingInWmPaint | ControlStyles.OptimizedDoubleBuffer |
                     ControlStyles.UserPaint | ControlStyles.ResizeRedraw, true);
            Padding = new Padding(20);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            var g = e.Graphics;
            g.Clear(Parent != null ? Parent.BackColor : BackColor);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            var r = new Rectangle(0, 0, Width - 1, Height - 1);
            using (var path = Motion.Rounded(r, Radius))
            {
                using (var b = new SolidBrush(Fill)) g.FillPath(b, path);
                using (var p = new Pen(Border)) g.DrawPath(p, path);
            }
        }
    }
}
'@

[System.Windows.Forms.Application]::EnableVisualStyles()

function New-C3Font([string]$style) {
    $semibold = @{ Title = 'Xl'; Heading = 'Lg'; Label = 'Sm' }
    $regular  = @{ Body = 'Md'; Small = 'Sm'; Caption = 'Xs' }
    if ($semibold.ContainsKey($style)) { return New-Object System.Drawing.Font('Segoe UI Semibold', $C3.Font.SizePt[$semibold[$style]]) }
    return New-Object System.Drawing.Font($C3.Font.Family.Ui, $C3.Font.SizePt[$regular[$style]])
}

function New-C3Label([string]$text, [string]$style, $color, [int]$x, [int]$y) {
    $l = New-Object System.Windows.Forms.Label
    $l.Text = $text; $l.Font = New-C3Font $style; $l.ForeColor = $color
    $l.AutoSize = $true; $l.Location = New-Object System.Drawing.Point($x, $y)
    return $l
}

function New-C3Button([string]$text, [string]$variant, [int]$x, [int]$y, [int]$w) {
    $b = New-Object C3Demo.C3Button
    $b.Text = $text; $b.Font = New-C3Font 'Label'
    $b.Size = New-Object System.Drawing.Size($w, $C3.Size.Control.Md)
    $b.Location = New-Object System.Drawing.Point($x, $y)
    $b.Radius = $C3.Radius.Sm
    $b.HoverMs = $C3.Motion.DurationMs.Fast
    $b.PressMs = $C3.Motion.DurationMs.Instant
    $b.FillDisabled = $C3.Color.Surface.Disabled
    $b.TextDisabled = $C3.Color.Text.Disabled
    $b.FocusColor = $C3.Color.Border.Focus
    if ($variant -eq 'Primary') {
        $b.Fill = $C3.Color.Accent.Default; $b.FillHover = $C3.Color.Accent.Hover; $b.FillPressed = $C3.Color.Accent.Pressed
        $b.TextColor = $C3.Color.Text.OnAccent
    } else {
        $b.Fill = $C3.Color.Surface.Control; $b.FillHover = $C3.Color.Surface.ControlHover; $b.FillPressed = $C3.Color.Surface.ControlPressed
        $b.TextColor = $C3.Color.Text.Primary
    }
    return $b
}

# Fenster ----------------------------------------------------------------------

$form = New-Object System.Windows.Forms.Form
$form.Text = 'C3 Manager'
$form.ClientSize = New-Object System.Drawing.Size(820, 500)
$form.StartPosition = 'CenterScreen'
$form.BackColor = $C3.Color.Bg.Canvas
$form.ForeColor = $C3.Color.Text.Primary
$form.Font = New-C3Font 'Body'
$form.AutoScaleMode = 'Dpi'
$iconPath = Join-Path $PSScriptRoot '..\assets\icon\c3yptax.ico'
if (Test-Path $iconPath) { $form.Icon = New-Object System.Drawing.Icon($iconPath) }
$form.Add_HandleCreated({ [C3Demo.Motion]::DarkTitleBar($form, $C3.Color.Bg.Subtle) })

# Seitenleiste
$side = New-Object System.Windows.Forms.Panel
$side.Dock = 'Left'; $side.Width = $C3.Size.Sidebar; $side.BackColor = $C3.Color.Bg.Subtle
$side.Add_Paint({ param($s, $e)
    $p = New-Object System.Drawing.Pen($C3.Color.Border.Subtle)
    $e.Graphics.DrawLine($p, $s.Width - 1, 0, $s.Width - 1, $s.Height); $p.Dispose() })
$side.Controls.Add((New-C3Label 'Anwendung' 'Caption' $C3.Color.Text.Muted 24 20))
$navActive = New-Object System.Windows.Forms.Panel
$navActive.Location = New-Object System.Drawing.Point(12, 44); $navActive.Size = New-Object System.Drawing.Size(208, 36)
$navActive.BackColor = $C3.Color.Accent.Subtle
$navBar = New-Object System.Windows.Forms.Panel
$navBar.Location = New-Object System.Drawing.Point(0, 9); $navBar.Size = New-Object System.Drawing.Size(3, 18); $navBar.BackColor = $C3.Color.Accent.Default
$navActive.Controls.Add($navBar)
$navActive.Controls.Add((New-C3Label 'Übersicht' 'Body' $C3.Color.Text.Primary 14 8))
$side.Controls.Add($navActive)
$side.Controls.Add((New-C3Label 'Geräte' 'Body' $C3.Color.Text.Secondary 26 92))
$side.Controls.Add((New-C3Label 'Einstellungen' 'Body' $C3.Color.Text.Secondary 26 128))

# Inhalt
$content = New-Object System.Windows.Forms.Panel
$content.Dock = 'Fill'; $content.BackColor = $C3.Color.Bg.Canvas
$content.Controls.Add((New-C3Label 'Übersicht' 'Title' $C3.Color.Text.Primary 32 28))
$content.Controls.Add((New-C3Label 'Profile, Geräte und letzte Aktivitäten' 'Body' $C3.Color.Text.Muted 33 62))

$card = New-Object C3Demo.C3Card
$card.Fill = $C3.Color.Surface.Card; $card.Border = $C3.Color.Border.Subtle; $card.Radius = $C3.Radius.Lg
$card.Location = New-Object System.Drawing.Point(32, 104); $card.Size = New-Object System.Drawing.Size(520, 240)
$card.BackColor = $C3.Color.Surface.Card   # Ecken werden in der Farbe des Elternelements gezeichnet
$card.Controls.Add((New-C3Label 'Neues Profil' 'Heading' $C3.Color.Text.Primary 20 18))
$card.Controls.Add((New-C3Label 'Profilname' 'Label' $C3.Color.Text.Secondary 20 62))

# Eingabefeld: native TextBox in einem Rahmen-Panel
$inputFrame = New-Object System.Windows.Forms.Panel
$inputFrame.Location = New-Object System.Drawing.Point(20, 84); $inputFrame.Size = New-Object System.Drawing.Size(480, $C3.Size.Control.Md)
$inputFrame.BackColor = $C3.Color.Surface.Input
$inputFrame.Padding = New-Object System.Windows.Forms.Padding(12, 7, 12, 0)
$script:inputBorder = $C3.Color.Border.Control
$inputFrame.Add_Paint({ param($s, $e)
    $p = New-Object System.Drawing.Pen($script:inputBorder)
    $e.Graphics.DrawRectangle($p, 0, 0, $s.Width - 1, $s.Height - 1); $p.Dispose() })
$tb = New-Object System.Windows.Forms.TextBox
$tb.BorderStyle = 'None'; $tb.Dock = 'Fill'; $tb.BackColor = $C3.Color.Surface.Input; $tb.ForeColor = $C3.Color.Text.Primary
$tb.Font = New-C3Font 'Body'
$tb.Add_GotFocus({ $script:inputBorder = $C3.Color.Accent.Default; $inputFrame.Invalidate() })
$tb.Add_LostFocus({ $script:inputBorder = $C3.Color.Border.Control; $inputFrame.Invalidate() })
$inputFrame.Controls.Add($tb)
$card.Controls.Add($inputFrame)

$hint = New-C3Label 'Das Profil kann später jederzeit geändert werden.' 'Caption' $C3.Color.Text.Muted 20 124
$card.Controls.Add($hint)

$btnCancel = New-C3Button 'Abbrechen' 'Secondary' 288 184 100
$btnSave = New-C3Button 'Profil anlegen' 'Primary' 396 184 104
$card.Controls.AddRange(@($btnCancel, $btnSave))

$btnSave.Add_Click({
    if ([string]::IsNullOrWhiteSpace($tb.Text)) {
        $script:inputBorder = $C3.Color.Status.Danger; $inputFrame.Invalidate()
        $hint.Text = 'Bitte einen Namen eingeben.'; $hint.ForeColor = $C3.Color.Status.Danger
        return
    }
    $script:inputBorder = $C3.Color.Border.Control; $inputFrame.Invalidate()
    $hint.Text = "$($tb.Text.Trim()) wurde angelegt."; $hint.ForeColor = $C3.Color.Status.Success
    $tb.Clear()
})
$btnCancel.Add_Click({ $tb.Clear(); $hint.Text = 'Das Profil kann später jederzeit geändert werden.'; $hint.ForeColor = $C3.Color.Text.Muted })

$content.Controls.Add($card)
$form.Controls.Add($content)
$form.Controls.Add($side)

# Fenster weich einblenden (motion.duration.slow, motion.easing.enter)
if ([C3Demo.Motion]::Enabled) {
    $form.Opacity = 0
    $fade = New-Object System.Windows.Forms.Timer
    $fade.Interval = 15
    $script:fadeStart = $null
    $fade.Add_Tick({
        if (-not $script:fadeStart) { $script:fadeStart = Get-Date }
        $t = [Math]::Min(1.0, ((Get-Date) - $script:fadeStart).TotalMilliseconds / $C3.Motion.DurationMs.Slow)
        $e = $C3.Motion.Easing.Enter
        $form.Opacity = [C3Demo.Motion]::Ease($t, $e[0], $e[1], $e[2], $e[3])
        if ($t -ge 1.0) { $fade.Stop(); $fade.Dispose() }
    })
    $form.Add_Shown({ $fade.Start() })
}

[void]$form.ShowDialog()
$form.Dispose()
