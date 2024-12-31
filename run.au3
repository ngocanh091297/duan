#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.16.1
 Author:         myName

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here

#include <GUIConstantsEx.au3>
#include <WinAPI.au3>
#include <GDIPlus.au3>
#include <_ImageSearch_UDF.au3>
#include <MsgBoxConstants.au3>
#include <GDIPlus.au3>
#include <FileConstants.au3>
#include <WinHttp.au3>
#include <ScreenCapture.au3>

HotKeySet("{esc}", "_Exit") ; Press ESC for exit
HotKeySet("{p}", "_Pause") ; Press ESC for exit

Func _Exit()
    Exit 0
EndFunc
Func _Pause()
    If MsgBox(1, 'Paused', 'Press ok to resume, or cancel to exit') = 2 Then Exit
EndFunc   ;==>_Pause 292 684

$hWnd = WinGetHandle('SM-G610F') ;ví dụ lấy handle của cửa sổ SciTE đang mở để chụp ảnh của nó


Global $labai1 =""
Global $labai2 =""
Global $dangchoi = False

#Region ### START Koda GUI section ### Form=
$Form1 = GUICreate("Auto Rally League Of Kingdoms", 615, 437, 192, 124)
$Button1 = GUICtrlCreateButton("quet chat", 10, 30, 217, 57)

$Label1 = GUICtrlCreateLabel("TOOL CHƯA CHẠY", 10, 350, 317, 57)
GUICtrlSetFont($Label1, 14, 400, "Strike", "Comic Sans Ms")
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ### A33A37 đến lượt chơi
While  1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		Case $Button1
             xacdinhbai_matboard()

	EndSwitch
WEnd

Func xacdinhbai_matboard()
   $hWnd = WinGetHandle('SM-G610F')
   WinMove($hWnd, "", 0, 0)

EndFunc



