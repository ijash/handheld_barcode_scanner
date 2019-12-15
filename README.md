# Handheld single directional laser Barcode Scanner

python3 implementation for handheld barcode scanner using COM port/ serial.
tested on ubuntu 18.04 / linux mint tina
## requirements:
### OS
most linux distribution. But, it should be working fine with mac or windows.
### Software
- [python3](https://www.python.org/)
- [git](https://git-scm.com/)
- [pyserial](https://pypi.org/project/pyserial/)
### Hardware
  Any generic, cheap chinese single directional laser barcode scanner (they're usually the same) with COM or serial communication over USB. 
  It is dentified by a very _"direct"_ user manual such as this:
  ![alt text](maunal_preview.jpg "manual preview")
  
## Installation:
This code is using [pyserial](https://pypi.org/project/pyserial/) module, so install it first before using it. It is recommended using [virtual environment](https://docs.python.org/3/tutorial/venv.html).  
1. Enter in terminal:
    ```bash
    git clone https://github.com/ijash/handheld_barcode_scanner.git
    cd handheld_barcode_scanner
    pip3 install pyserial
    ```
    _note:pip3 command is interchangeable with pipenv if installed_  
  
2. Then, connect the USB to computer and make sure the barcode scanner is using serial communication (COM).
3. Run it in terminal
    ```bash
     python3 barcode.py
    ```

## Contributing
feel free to create a pull request.
