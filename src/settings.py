home = "/home/alon/code/ArduinoAnalyzer/new/"
# *****************************************************************
# **                                                             **
# **  ======***=== AVR-GCC bug seeker ===***======               **
# **                                                             **
# **  an interactive tool for testing avr C tools                **
# **                   settings.py:                              **
# ** the parameters file for all other files.                     **
# ***************************************************************** 


debug =0
#Folders:

csmith = home + "utils/csmith/csmith-2.2.0/"

lineChooser_srcFolder = home + "results/failedCFiles/cfiles2Debug/"
lineChooser_workFolder = home + "debug/"
lineChooser_outFolder = home + "debug/lineMarked/"
flow_srcFolder = home + "workFolder/"
flow_workFolder = home + "workFolder/"

FailedCFiles = home + "results/failedCFiles/"
cfiles2debug = FailedCFiles + "cfiles2Debug/"

#Applications:
#TODO use package like in flow
insertPrints = home + "src/addprints.py"
avrgcc = home + "utils/avr-gcc/avr8-toolchain-linux/bin/avr-gcc"
simulavr = home + "utils/simulavr/usr/bin/simulavr";
ardgcc = "sudo bash " + home + "src/arduino_compile.cmd"
arddude = "sudo bash " + home + "src/arduino_dude.cmd"
RunSafely = csmith + "/scripts/RunSafely.sh 2 1 /dev/null "

# TODO: standerize
ard_home = "/home/student/avr/arduino-1.6.5/"
flow_run = home + "src/flow.py"
#File names:
tracestring = "trace.txt"
srcFileName = "avrtest.c"
compileOut = "compileout.txt"
wp = "wp.c"

lineChooser_srcFilePath = lineChooser_workFolder + wp
lineChooser_gccout = "gccPrintsout.txt"
lineChooser_gccbin = "gccWprints.o"
lineChooser_avroutsuff = "avrPrintsout.txt"
lineChooser_avrbinsuff = "Wprints.elf"

flow_gccout = "gccout.txt"
flow_gccbin = "gccbin.o"
flow_avroutsuff = "optout.txt"
flow_avrbinsuff = "optBin.elf"
flow_srcFilePath = flow_srcFolder + srcFileName




#Device parameters:
dev = "atmega328"
devArd = "atmega328p"
com = "/dev/ttyUSB0"

#Compiler parameters:
#opts = ["O0", "O1", "O2", "O3", "Os"]
opts = ["Os", "O3", "O2", "O1", "O0"]
#runtimeAvr = "-I" + csmith + "runtime_avr/";
#runtimeGcc = "-I" + csmith + "runtime_gcc/"

runtimeAvr = "-I" + home + "src/runtime/runtime_avr/"
runtimeGcc = "-I" + home + "src/runtime/runtime_gcc/"

# TODO: standertize
#runtime_ard = "/home/student/avr/avrTest/alon_dev/runtime_arduino/"
runtime_ard = "-I" + home + "src/runtime/runtime_ard/"

#C-smith parameters:
csmithOptions = " --no-safe-math --no-math64 --no-bitfields --no-consts --no-float --no-divs "
csmithOptions = csmithOptions + " --max-array-dim 2 --max-array-len-per-dim 8 "
csmithOptions = csmithOptions + " --max-block-depth 2 --max-block-size 2 --max-expr-complexity 2 "
csmithOptions = csmithOptions + " --max-funcs 4 --max-struct-fields 2 --max-union-fields 2 "
csmithOptions = csmithOptions + "  --no-volatiles --no-volatile-pointers --no-pointers --no-unions --no-safe-math";

#misc.
traceDump = 0
dude = 0
csgen = 1











#####################################################
#######             Originals                ########
#####################################################


# #from lineChooser:
# home = "/home/student/publicWorkTest/avrTest/"

# avrgcc = home + "Utils/avr8-gnu-toolchain-linux_x86/bin/avr-gcc";
# simulavr = home + "Utils/Simulator/usr/bin/simulavr";
# csmith = home + "Utils/csmith-2.2.0/"

# dev = "atmega328"

# runtimeAvr = "-I" + csmith + "runtime_avr/";

# insertPrints = home + "pycparser/addprints.py"
# runtimeGcc = "-I" + csmith + "runtime_gcc/"
# srcFolder = home + "FailedCFiles/cfiles2Debug/"
# workFolder = home + "DebugFolder/"
# srcFilePath = workFolder + "wp.c"
# outFolder = home + "DebugFolder/lineMarked/"
# gccout = "gccPrintsOut.txt"
# gccbin = "gccWprints.o"
# avroutsuff = "avrPrintsOut.txt"
# avrbinsuff = "Wprints.elf"
# tracestring = "trace.txt"
# traceDump = 0
# RunSafely = csmith + "/scripts/RunSafely.sh 2 1 /dev/null "
# opts = ["O0", "O1", "O2", "O3", "Os"]
# dude = 0

# devArd = "atmega328p"
# com = "/dev/ttyUSB0"
# ardgcc = "sudo bash /home/student/avr/avrTest/alon_dev/arduino_compile.cmd"
# arddude = "sudo bash /home/student/avr/avrTest/alon_dev/arduino_dude.cmd"




# #from flow:
# home = "/home/student/publicWorkTest/avrTest/"
# runtimeGcc = "Utils/csmith-2.2.0/runtime_gcc/"
# srcFolder = home + "WorkFolder/"
# workFolder = home + "WorkFolder/"
# FailedCFiles = home + "FailedCFiles/"
# outFolder = home + "DebugFolder/"
# srcFileName = "avrtest.c"
# avrgcc = home + "Utils/avr8-gnu-toolchain-linux_x86/bin/avr-gcc";
# simulavr = home + "Utils/Simulator/usr/bin/simulavr";
# csmith = home + "Utils/csmith-2.2.0/"
# compileOut = "compileOut.txt"
# dev = "atmega328"

# runtimeAvr = "-I" + csmith + "runtime_avr";

# runtimeGcc = "-I" + csmith + "runtime_gcc/"
# gccout = "gccout.txt"
# gccbin = "gccbin.o"
# avroutsuff = "OptOut.txt"
# avrbinsuff = "OptBin.elf"
# tracestring = "trace.txt"
# srcFilePath = srcFolder + srcFileName
# traceDump = 1
# csgen = 1
# RunSafely = csmith + "/scripts/RunSafely.sh 2 1 /dev/null "

# opts = ["O0", "O1", "O2", "O3", "Os"]


# csmithOptions = " --no-safe-math --no-math64 --no-bitfields --no-consts --no-float --no-divs "
# csmithOptions = csmithOptions + " --max-array-dim 2 --max-array-len-per-dim 8 "
# csmithOptions = csmithOptions + " --max-block-depth 2 --max-block-size 2 --max-expr-complexity 2 "
# csmithOptions = csmithOptions + " --max-funcs 4 --max-struct-fields 2 --max-union-fields 2 "

# #Alon's aditional flags      $CSMITH_OPTIONS .= "  --no-volatiles --no-volatile-pointers --no-const-pointers --no-unions --no-safe-math";




# #from console:

# #TODO: get config file

# #TODO: add env for - ard_*
