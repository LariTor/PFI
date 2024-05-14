import struct
import sys
import numpy as np 
    

class gamma_data:
    def __init__(self,filename):
        try:
            self.infile         = open(filename, "rb")
            self.read_chn_binary()
        except ValueError:
            print('Unable to load file ' + filename)

     
    def read_chn_binary(self):       # We start by reading the 32 byte header
        self.version            = struct.unpack('h', self.infile.read(2))[0]
        self.mca_detector_id    = struct.unpack('h', self.infile.read(2))[0]
        self.segment_number     = struct.unpack('h', self.infile.read(2))[0]
        self.start_time_ss      = self.infile.read(2)
        self.real_time          = struct.unpack('I', self.infile.read(4))[0]
        self.live_time          = struct.unpack('I', self.infile.read(4))[0]
        self.start_date         = self.infile.read(8) #Ascii type date in 
                                #DDMMMYY* where * == 1 means 21th century
        self.start_time_hhmm    = self.infile.read(4)
        self.chan_offset        = struct.unpack('h', self.infile.read(2))[0]
        self.no_channels        = struct.unpack('h', self.infile.read(2))[0]    
        self.hist_array         = np.zeros(self.no_channels) #Init hist_array 
        #Read the binary data
        for index in range(len(self.hist_array)):
            self.hist_array[index]= struct.unpack('I', self.infile.read(4))[0]
        assert struct.unpack('h', self.infile.read(2))[0] == -102
        self.infile.read(2)
        self.en_zero_inter = struct.unpack('f', self.infile.read(4))[0]  
        self.en_slope = struct.unpack('f', self.infile.read(4))[0]
        self.en_quad = struct.unpack('f', self.infile.read(4))[0]
        self.infile.close()
    def write_txt(self, fname):
        tf = open(filename[:-4]+'.txt','w')
#        tf.writelines(['# Filename : ' + fname,
#                       '\n# Version: ' + str(self.version),
#                       '\n# MCA detector ID: ' + str(self.mca_detector_id),
#                       '\n# Start time : ' + self.start_time_hhmm[:2].decode('utf-8')+':'+ self.start_time_hhmm[:2].decode('utf-8') + ':'+ str(self.start_time_ss),
#                       '\n# Start date : ' + self.start_date.decode('utf-8'),
#                       '\n# No channels : ' + str(self.no_channels),
#                       '\n# Live time : ' + str(self.live_time),
#                       '\n# Real time : ' + str(self.real_time),
#                       '\n# En cal factors A + B*x + C*x*x',
#                       '\n# A : ' + str(self.en_zero_inter),
#                       '\n# B : ' + str(self.en_slope),
#                       '\n# C : ' + str(self.en_quad)])
        for i in self.hist_array:
            tf.write(str(int(i)) + '\n')
        tf.close()
        
for archivo in sys.argv[2:]:
    if __name__ == '__main__':   
        if len(sys.argv) >1:
            filename = sys.argv[1]
        else: 
            filename = raw_input('Filename of binary, (including .Chn): ')
        gamma_object = gamma_data(filename)
        gamma_object.write_txt(filename)