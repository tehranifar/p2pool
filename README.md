Requirements:
-------------------------
Generic:
* Zcoin >=0.13.6.8
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

You can also use

    pip install -r requirements.txt

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6
* sudo apt-get install build-essential

Windows:
* Install [Python 2.7](http://www.python.org/getit/)
* Install [Twisted](http://twistedmatrix.com/trac/wiki/Downloads)
* Install [Zope.Interface](http://pypi.python.org/pypi/zope.interface/3.8.0)
* Install [python win32 api](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/)
* Install [python win32 api wmi wrapper](https://pypi.python.org/pypi/WMI/#downloads)
* Unzip the files into C:\Python27\Lib\site-packages

Compiling Lyra2Z Module:
-------------------------
In order to run P2Pool with the zcoin network, you would need to build and install the
Lyra2Z module that includes the lyra2z proof of work code that zcoin uses for hashes.

Linux:

    cd Lyra2Z
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd Lyra2Z
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (Microsoft Visual C++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd Lyra2Z
    C:\Python27\python.exe setup.py build --compile=mingw32 install

If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local zcoind. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net zcoin

Then run your miner program, connecting to 127.0.0.1 on port 9327 with any
username and password.

If you are behind a NAT or firewall, you should enable TCP port forwarding and access
 on your router. Forward port 9327 and 9338 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Donations towards further development:
-------------------------
    a6dc8DfVeMdDxz1VzvuHyafkArW5fJ2d7B

Alternate web frontend:
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd

Sponsors:
-------------------------

Thanks to:
* Zcoin Team
* The original [P2Pool](https://github.com/p2pool/p2pool/)
 
License:
-------------------------

[Available here](COPYING)


