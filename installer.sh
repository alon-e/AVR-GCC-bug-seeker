#!/bin/sh
############################################
#   Arduino compile & upload Flow
#   Requires root permissions & physical COM
#   
#   *writes checksum to file
############################################


###################
base=$PWD
src_dir=$1
echo "Installing in - $base"
echo "Creating directories"
#create folders
	#Work area:
	dir=./workFolder
	mkdir $dir
		mkdir $dir/flow
		mkdir $dir/debug
		mkdir $dir/arduino
	#Sources:
	dir=./src
	mkdir $dir
		mkdir $dir/runtime
	#Utilities:
	dir=./utils
	mkdir $dir
	#results:
	dir=./results
	mkdir $dir
		mkdir $dir/failedCFiles
		mkdir $dir/failedCFiles/cfiles2Debug
		mkdir $dir/lineMarked
		#TODO change name ^
		

#copy src files
	#src_dir="/home/student/avr/public/avrTest/src"
	cp -Rf $src_dir $base/
	#TODO: make sure the files are already present

#Install Utilities:
###################
echo "Installing Utilities..."
	dir=$base/utils
	cd $dir
	mkdir $dir/temp
	#csmith
	echo "	Installing csmith..."
		url="https://embed.cs.utah.edu/csmith/csmith-2.2.0.tar.gz"
		package="$dir/temp/csmith.tar.gz"
		appDir="$dir/csmith/"
		#download
		wget $url -O $package
		#un-pack
		mkdir $appDir
		tar -C $appDir -xvf $package
		
		#install
			#dependencies
			apt-get install -y m4
			apt-get install -y g++

		cd $appDir/csmith-2.2.0
		./configure
		make
		#test
		#TODO
	cd $dir

	echo "	Installing avr-gcc..."
		#package found in base
		# - local file
		avr_pkg="$dir/../avr8-toolchain-linux.tar.gz"
		package="$dir/temp/avr-toolchain.tar.gz"
		appDir="$dir/avr-gcc/"
		#download
		#wget $url -O $package
		cp $avr_pkg $package
		#un-pack
		mkdir $appDir
		tar -C $appDir -xvf $package
		
		#install
			#NOTHING TO DO...
		#test
		#TODO
	cd $dir

	#simulavr
	echo "	Installing simulavr..."
		url="http://download.savannah.nongnu.org/releases/simulavr/simulavr-1.0.0-binary-linux32.tar.gz"
		package="$dir/temp/simulavr.tar.gz"
		appDir="$dir/simulavr/"
		#download
		wget $url -O $package
		#un-pack
		mkdir $appDir
		tar -C $appDir -xvf $package
		
		#install
                        #dependencies
                        sudo apt-get install -y zlib1g:i386
			#NOTHING TO DO...
		#test
		#TODO
	cd $dir

	#pycparser
	echo "	Installing pycparser..."
		url="https://github.com/eliben/pycparser/archive/master.zip"
		package="$dir/temp/pycparser.zip"
		appDir="$dir/pycparser/"
		#download
		wget $url -O $package
		#un-pack
		mkdir $appDir
		unzip $package -d $appDir
		
		#install
		cd $appDir/pycparser-master
		python setup.py install
		#test
		#TODO
	cd $dir
	rm -Rf $dir/temp
cd $base

#update config file
	#change 'home = ' to pwd
	settings_path=$base/src/settings.py
	echo "home = \"$base/\"" > $settings_path.temp
	cat $settings_path >> $settings_path.temp
	cp $settings_path.temp $settings_path
	rm $settings_path.temp

echo "Finished instalation."

echo "Opening console.."
#start console
$base/src/console.py

