from win32com.client import Dispatch # Python ActiveX Client
import win32com
import time
##Melusine measurement PC
#vipath = 'C:\\Documents and Settings\\Bauerle\\Mes documents\\takada\\Labview\\FPGA_Batch_1_4\\Batch_main Folder\\FileLauncher.vi'
##Melusine analysis PC
#vipath = 'E:\\Takada\\Program\\Labview\\FPGA_Batch_1_4\\Batch_main Folder\\FileLauncher.vi'
#Wodan
#vipath = 'C:\\Users\\manip.batm\\Documents\\takada\\Labview\\FPGA_Batch_1_5\\Batch_main Folder\\FileLauncher.vi'
#Merlin
vipath = 'C:\\Users\\manip.batm\\Desktop\\FPGA_Batch\\FPGA_Batch_1_5\\Batch_main Folder\\FileLauncher.vi'

def sendFiles(vipath=vipath,
              fileList = []):
    ini = time.time()
    print(fileList)
#    try:
#        LabVIEW = Dispatch("Labview.Application")
#    except:
#        print('Error: Python ActiveX Labview Client not loaded')
    try:
        lvApp = win32com.client.Dispatch("Labview.Application")
#        lv = win32com.client.dynamic.Dispatch ("Labview.Application")
        print(lvApp.__module__)
        #VIPath = lvApp.ApplicationDirectory +  r"\Examples\General\Strings.llb\ParseArithmetic Expression.vi"
        try:
            VI=lvApp.getvireference(vipath)
        except:
            print("failed to load vi from path")
        #VI._FlagAsMethod("Call")
    except:
        print('could not open VI reference at')
        print(vipath)
    try:
        #VI.CloseFrontPanel()
        VI.SetControlValue('Files_temp', fileList)
        print(VI.SetControlValue)
    except:
        print('could not load files to VI')
        print(fileList)
    print('sent after seconds:')
    print(time.time()-ini)

testname = ['C:\\Users\\manip.batm\\Desktop\\merlin_exp_config\\201706021149_0.h5']  
sendFiles(vipath, testname)