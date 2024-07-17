import csv 
import sys
import argparse
import ast
from datetime import date

# File having the pixel sequence for Digital Excitation
##f0 = open("pixelSequence.txt", "r")
##f0 = open("/group/picmic/savePicmicConfi/scripts/pixelSequenceSignalInjection.txt", "r")
f0 = open("K:\savePicmicConfi\scripts\pixelSequenceSignalInjection.txt", "r")

# outro sequence before to close the file
outro = ["38,50",
#"39,0",
"39,40",
"40,45",
"41,128",
#"41,255",
"42,91",
#"42,120",
"43,73",
"44,180",
"45,1",
"62,128"]

# #######################################
parser = argparse.ArgumentParser()
parser.add_argument('-f', "--file", help="Input file with PICMIO calibration")
args = parser.parse_args()


if ( str(args.file)=='None') :
    print("----------------------- >>>>>>>>>>>>>>>> Input file mandatory   <<<<<<<<<<<<<<<<<<<-------------------------")
    print('Script not executed')    
    exit()



myfile = str(args.file)
##split_myfile = myfile.split('.')
##print('---- myfile name ', myfile.split('.'))

#if () 

td = date.today().strftime("%d%b%Y")
#td = myfile.split('_')[2]
##print(myfile.split('_'))

##outfile = "all_calib_"+str(myfile.split('_')[-3])+str(myfile.split('_')[-2])+"_"+td+".txt"
##outfile = "all_calib_"+str(myfile.split('_')[-4])+str(myfile.split('_')[-3])+"_"+str(myfile.split('_')[-2])+"_" +td+".txt"
outfile = 'calib_'+td+'.txt'
##outfile = myfile #split_myfile[0]+"_calib_"+str(myfile.split('_')[-4])+str(myfile.split('_')[-3])+"_"+td+".txt"
##outfile = "all_calib_"+str(myfile.split('_')[-3])+str(myfile.split('_')[-2])+"_"+td+"_45Yexcluded.txt"
##print(args.list)

##print(outfile)




##exit()

# #######################################


##filename= "GenConfFiles/I2C_config_blue-213_calib_bar.txt";
##filename= "GenConfFiles/I2C_config_blue-213_calib.txt";
##filename= "GenConfFiles/I2C_config_all_calib_astar.txt";
##filename= "GenConfFiles/"+outfile
filename= "generated_files/"+outfile
##f0 = open("pixelSequence.txt", "r")
f2 = open(filename,"w")
f2.write(f0.read())
f0.close()

##with open('../env_conda/processedDataSAMPIC/calibratoin_reduced_file.csv') as file_obj:
##with open('../env_conda/processedDataSAMPIC/calibration_18Jan2024_all_astar.csv') as file_obj:
with open(myfile) as file_obj:
    heading = next(file_obj) 
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:

        
        f2.write("62,"+str(int(row[1]))+"\n")
        f2.write("61,"+str(int(row[0]))+"\n")
        f2.write("63,"+str(int(row[2]))+"\n")

        #for val in mylist:
        ##    for idx, j in enumerate() :
        #    if ( int(row[0])==int(val[0]) and int(row[1])==int(val[1]) ) :
        #        print('Masked  --> R'+str(row[0])+'-C'+str(row[1])) 
        #        f2.write("63,"+str(int(64))+"\n")
        #    else :
        #        f2.write("63,"+str(int(row[2]))+"\n")

    for out in outro :
        f2.write(out+"\n")

    f2.close()


exit()
