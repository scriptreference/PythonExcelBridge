class PythonBridge(object):
    _reg_clsid_ = '{5E685108-CC97-446C-B079-2204C3FF46DC}'
    _reg_progid_ = 'PythonBridge'
    _public_methods_ = ['hello_world']

    def hello_world(self):
        return 'Hello World!'


if __name__ == '__main__':
    print("Registering COM server...")
    import win32com.server.register
    win32com.server.register.UseCommandLine(PythonBridge)
