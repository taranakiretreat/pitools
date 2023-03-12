#!/usr/bin/python3
import time
import socket
import os
import wx

# 
class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.filePosition = 0
        self.modified=0
        self.log = ''
        self.myHostname = socket.gethostname()
        self.purposeFile = '/home/projects/pitools/lib/' + str(self.myHostname)
        self.disoverMyPurpose()
        self.InitUI()
        self.poll()
 
    def InitUI(self):

        pnl = wx.Panel(self)
        font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)
        st1 = wx.StaticText(pnl, label='Device Function: ' + self.myPurpose, style=wx.ALIGN_LEFT,  pos=(20, 20))
        updateButton = wx.Button(pnl, label='Update', pos=(20, 50))
        updateButton.Bind(wx.EVT_BUTTON, self.OnClose)
        setFuncButton = wx.Button(pnl, label='Set Function', pos=(20, 100))
        setFuncButton.Bind(wx.EVT_BUTTON, self.OnClose)
        rebootButton = wx.Button(pnl, label='Reboot', pos=(20, 150))
        rebootButton.Bind(wx.EVT_BUTTON, self.OnClose)
        proceedButton = wx.Button(pnl, label='Proceed', pos=(20, 200))
        proceedButton.Bind(wx.EVT_BUTTON, self.proceed)
        if self.myPurpose == 'Unset': proceedButton.Enable(False)


        self.SetSize((350, 300))
        self.SetTitle('Retreat Team Options:')
        self.Centre()

    def OnClose(self, e):

        self.Close(True)


    def poll(self):
        # waits 1 minute before calling proceed
        wx.CallLater(3000, self.proceed)


    def disoverMyPurpose(self):
        try:    
            with open(self.purposeFile, 'r') as f:
                self.myPurpose = f.read()
        except: self.myPurpose = 'Unset'


    def proceed(self, e=None):
        if self.myPurpose == 'Unset': return
        self.Close(True)
        print("Still here!")




def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
    


if __name__ == '__main__':
    main()

