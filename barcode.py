import serial
import serial.tools.list_ports

# initialization
ports = serial.tools.list_ports.comports(include_links=False)

print('Device list:')
# iterate to find the most recent device
for port in ports:
    print(f'{port.device}\t found.')

ser = serial.Serial(port.device)
#
if ser.is_open:
    ser.close()
# use the most recent device
ser = serial.Serial(port.device)

# display info
print(f'Using {ser.name} :')
print(ser)

# main program
try:
    result_line = ''
    print('start scanning barcodes:')
    while ser.is_open:
        result = ser.read()
        if (result == b'\r'):
            print(result_line)
            result_line = ''
            ser.reset_output_buffer()
        result_line += result.decode('utf-8')
except KeyboardInterrupt:
    ser.close()
    print("keyboard Interrupt.")
