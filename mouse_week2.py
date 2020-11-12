
#importing PyUSB for using [usb.core & usb.util] 
#importing usb.backend.libusb1 for solving problem of "Backend error"
#import sys #for exception errror

import usb.core 
import usb.util
import usb.backend.libusb1 

#binding library for exception error
backend = usb.backend.libusb1.get_backend(find_library=lambda x:"/usr/lib/libusb.so") 

#idVender & idProduct can be detected in windows(just enter to control properties) and Linux(lsusb)
dev = usb.core.find(idVendor=0x046d,idProduct=0xc077, backend=backend)

#setting HID's interface
interface=0                     

# [configuration][interface,alternative interface][endpoint]
endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(interface) is True:
    dev.detach_kernel_driver(interface)
    usb.util.claim_interface(dev, interface)

    try:
        while True:
            try:
                receive = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize,0) 
                #bEndpointAddress: final destination to access
                #wMaxPacketSize: sender's packet size 
                print(receive)
 
            except usb.core.USBError as e:
                receive = None
                if e.args == ("Operate time out",):
                    continue

    except KeyboardInterrupt:
        pass
    usb.util.release_interface(dev, interface)
    dev.attach_kernel_driver(interface)