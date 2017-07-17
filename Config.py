import numpy as np
import h5py
class Variables():
    Melusine = True
    Wodan = False
    Merlin = False
    """ Fridge specific parameters """
    if Melusine == True:
        FPGA_address = '10.0.0.2'
        addressList = {'K2000':'0:17','K34401A':'0:17','DSP_lockIn':'0:12','RS_RF':'0:19','AWG':'10.0.0.4'}
    elif Wodan == True:
        FPGA_address = '192.168.137.11'
        addressList = {'K2000':'0:17','K34401A':'0:17','DSP_lockIn':'0:12','RS_RF':'0:28','AWG':'192.168.0.4', 'ATMDelayLine':'COM3', 'MercuryIPS':'192.168.0.3'}
    elif Merlin == True:
        FPGA_address = '192.168.137.11'
        addressList = {'K2000':'0:17','K34401A':'0:17','DSP_lockIn':'0:12','RS_RF':'0:28','AWG':'192.168.0.4', 'ATMDelayLine':'COM3', 'MercuryIPS':'192.168.0.3'}
    else:
        FPGA_address = '192.168.137.11'
        addressList = {'K2000':'0:17','K34401A':'0:17','DSP_lockIn':'0:12','RS_RF':'0:28','AWG':'192.168.0.4', 'ATMDelayLine':'COM3', 'MercuryIPS':'192.168.0.3'}
    """ parameters """
    compress_sweep = True
    compress_data = True
    compression_level = 9
    save_config2ExpFile = True
    # special data type for structured array in numpy
    init_move_dt = np.dtype({'names':['name','parameter','value'],'formats':['S100','u8','f8']})
    init_position_dt = np.dtype({'names':['Name','kind','Value'],'formats':['S100','u8','f8']})
    # special data type to define array of flexible length strings in HDF5 file
    flexible_str_dt = h5py.special_dtype(vlen=bytes)

    # list of kind for readout instruments and sweep instruments
    readout_kind = [0,1,2,3,12]
    sweep_kind = [4,5,6,7,8,9,10,11,13,14,15,16]
    # list of class name ordered by 'kind' number
    classList = ['ADC','K2000','K34401A','dummy','DAC','DAC_Lock_in','RS_RF','AWG','dummy','FastSequences','FastSequenceSlot']
    classList+= ['CMD','DSP_lockIn','DSP_lockIn_sweep','mswait','ATMDelayLine','MercuryIPS']
    readConfigForExpFile = [False,False,False,False,False,False,True,True,False,True,False]
    readConfigForExpFile+= [False,False,False,False,False,False]