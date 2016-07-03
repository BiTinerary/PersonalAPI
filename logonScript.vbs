bElevate = False
if WScript.Arguments.Count > 0 Then If WScript.Arguments(WScript.Arguments.Count-1) <> "|" then bElevate = True
if bElevate Or WScript.Arguments.Count = 0 Then ElevateUAC
REM run the following script with admin privilages. start point.
 
Set fso = CreateObject("Scripting.FileSystemObject")
GetTheParent = fso.GetParentFolderName(Wscript.ScriptFullName)
 
Set WshShell = WScript.CreateObject ("WScript.Shell")
WshShell.Run chr(34) & GetTheParent & ("./logon.bat")  & chr(34), 0
WScript.Sleep 500
 
REM the above script will be run with admin privilages. end point.
Sub ElevateUAC
    sParms = " |"
    If WScript.Arguments.Count > 0 Then
            For i = WScript.Arguments.Count-1 To 0 Step -1
            sParms = " " & WScript.Arguments(i) & sParms
        Next
    End If
    Set oShell = CreateObject("Shell.Application")
    oShell.ShellExecute "wscript.exe", WScript.ScriptFullName & sParms, , "runas", 1
    WScript.Quit
End Sub