---
rating: ⭐⭐
title: autohotkey-v2-gui
url: https://skills.sh/sarfraznawaz2005/agent-skills-collection/autohotkey-v2-gui
---

# autohotkey-v2-gui

skills/sarfraznawaz2005/agent-skills-collection/autohotkey-v2-gui
autohotkey-v2-gui
Installation
$ npx skills add https://github.com/sarfraznawaz2005/agent-skills-collection --skill autohotkey-v2-gui
SKILL.md
AutoHotkey v2 GUI Applications

Advanced GUI development patterns and optimization techniques for AutoHotkey v2.

When to Apply
Building complex GUI applications with multiple controls
Implementing event-driven user interfaces
Optimizing GUI performance and memory usage
Working with advanced controls like ListView, ComboBox, Tab
Critical Rules

Event Handling: Use OnEvent method, not g-labels

; WRONG - v1 g-label syntax
MyGui.Add("Button", "gButtonClick", "OK")

; RIGHT - v2 OnEvent method
Btn := MyGui.Add("Button", "w80", "OK")
Btn.OnEvent("Click", ButtonClick)


Data Submission: Use Submit() method with variable names

; WRONG - accessing controls directly
EditText := MyGui["MyEdit"].Text

; RIGHT - Submit returns object with named values
MyGui.Add("Edit", "vUserName")
Data := MyGui.Submit()
UserName := Data.UserName


Control Visibility: Use Visible property, not Show/Hide commands

; WRONG - v1 command syntax
GuiControl, Hide, MyButton

; RIGHT - v2 property syntax
MyButton.Visible := false

Key Patterns
Basic GUI Structure
MyGui := Gui("+Resize", "Application Title")
MyGui.OnEvent("Close", AppClose)

; Add controls with variables for data retrieval
NameEdit := MyGui.Add("Edit", "vUserName w200")
SubmitBtn := MyGui.Add("Button", "Default w80", "OK")
SubmitBtn.OnEvent("Click", ProcessForm)

MyGui.Show("w300 h150")

ProcessForm(*) {
    Data := MyGui.Submit()
    MsgBox("Hello " . Data.UserName)
}

AppClose(*) {
    ExitApp
}

ListView with Event Handling
MyGui := Gui()
LV := MyGui.Add("ListView", "r20 w700", ["Name", "Size (KB)"])
LV.OnEvent("DoubleClick", LV_DoubleClick)

; Populate ListView
Loop Files, A_MyDocuments "\*.*"
    LV.Add(, A_LoopFileName, A_LoopFileSizeKB)

LV.ModifyCol()  ; Auto-size columns
LV.ModifyCol(2, "Integer")  ; Enable numeric sorting

LV_DoubleClick(LV, RowNumber) {
    RowText := LV.GetText(RowNumber)
    MsgBox("Selected: " . RowText)
}

Tab Control with Organized Layout
MyGui := Gui()
Tab := MyGui.Add("Tab3",, ["Settings", "Data", "Output"])

; First tab controls
MyGui.Add("CheckBox", "vAutoStart", "Start automatically")
MyGui.Add("ComboBox", "vTheme", ["Light", "Dark", "Auto"])

; Second tab controls  
Tab.UseTab(2)
MyGui.Add("Edit", "vDataPath w200")
MyGui.Add("Button", "x+10 yp", "Browse...")

; Third tab controls
Tab.UseTab(3)
MyGui.Add("Edit", "vOutput r10 w300")

Tab.UseTab()  ; End tab association
MyGui.Add("Button", "Default", "Apply")

Modal Dialog Pattern
MainGui := Gui("+Resize", "Main Window")
MainGui.Opt("+OwnDialogs")  ; Make dialogs modal

ShowSettingsBtn := MainGui.Add("Button", "w100", "Settings")
ShowSettingsBtn.OnEvent("Click", ShowSettings)

ShowSettings(*) {
    ; Modal dialogs prevent interaction with main window
    Result := MsgBox("Save current settings?", "Confirm", "YesNoCancel")
    if (Result = "Yes") {
        ; Save logic here
    }
}

Performance Optimization
Memory Management for Large Data
; Pre-allocate string capacity for concatenation
VarSetStrCapacity(&LargeString, 5120000)  ; ~10 MB

Loop Files, "C:\*.*", "R"
    LargeString .= A_LoopFileFullPath . "`n"

; Free memory when done
LargeString := ""

Object Capacity Tuning
; Pre-allocate array/map capacity for performance
DataArray := []
DataArray.Capacity := 1000  ; Avoid frequent reallocation

DataMap := Map()
DataMap.Capacity := 500

Advanced Control Patterns
ComboBox with Validation
ColorBox := MyGui.Add("ComboBox", "vColor", ["Red", "Green", "Blue"])
ColorBox.OnEvent("Change", ValidateColor)

ValidateColor(Ctrl, *) {
    if (Ctrl.Text = "Red")
        MsgBox("Warning: Red selected!")
}

Dynamic Control Management
; Get control position for dynamic layouts
MyEdit.GetPos(&x, &y, &w, &h)
NewBtn := MyGui.Add("Button", "x" . (x + w + 10) . " y" . y, "Next")

; Retrieve control values without Submit
CurrentText := ControlGetText("Edit1", MyGui.Hwnd)

Common Mistakes
Missing variable names: Controls need "v" prefix for Submit() to retrieve values
Incorrect positioning: Use "xm ym" to reset to margins, "x+m y+m" for relative positioning
Event handler parameters: Modern event handlers receive (Ctrl, Info) parameters, not just (*)
Window activation timing: Use NoActivate option when showing background windows to avoid focus stealing
Weekly Installs
59
Repository
sarfraznawaz200…llection
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass