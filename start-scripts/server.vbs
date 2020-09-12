Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "server.bat" & Chr(34), 0
Set WinScriptHost = Nothing