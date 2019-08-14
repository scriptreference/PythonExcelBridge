Sub callPython()
    ' Create Python COM Server object
    Dim PythonBridge As Object
    Set PythonBridge = CreateObject("PythonBridge")
    
    ' Retrieve the data from python
    Dim pythondata
    pythondata = CallByName(PythonBridge, "hello_world", VbMethod)
    
    ' Place data on sheet
    ActiveSheet.Range("A1").Value = pythondata
End Sub
