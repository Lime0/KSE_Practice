import usb.core
import usb.util
import usb.backend.libusb1
import usb1
import sub_module
import binascii
#KSE-----------------------------------------------------------------------------------
KSE_TRUE = 1
KSE_FALSE = 0
NOT_USED = 0

LC_MANUFACTURED = 0xFF
LC_ISSUED = 0x00
LC_TERMINATED = 0xEE

gbVcType = 0
VC_DISABLED = 0xFF
VC_TYPE_0 = 0x00
VC_TYPE_1 = 0x01
VC_TYPE_2 = 0x02
VC_TYPE_3 = 0x03
VC_TYPE_4 = 0x04
VC_INFINITE = 0x00

CLEAR_ALL = 0x00
CLEAR_ISSUE_DATA_ONLY = 0x01


#Parameter for Power-------------------------------------------------------------------
KSE_POWER_OFF = 0
KSE_POWER_ON = 1
gusKsePower = KSE_POWER_OFF

CLEAR_ALL = 0x00
CLEAR_ISSUE_DATA_ONLY = 0x01

#ERRORCODE-----------------------------------------------------------------------------
ICC_SUCCESS = 0x0000
ICC_FAIL = -0x8000                         # 0x8000
ICC_FAIL_WRONG_INPUT = -0x0100             # 0xFF00
ICC_FAIL_NOT_SUPPORTED = -0x0101           # 0xFEFF
ICC_FAIL_NOT_POWERED_ON = -0x0102          # 0xFEFE
ICC_FAIL_ALREADY_POWERED_ON = -0x0103      # 0xFEFD
ICC_FAIL_ATR = -0x0104                     # 0xFEFC
ICC_FAIL_PPS = -0x0105                     # 0xFEFB
ICC_FAIL_TX = -0x0106                      # 0xFEFA
ICC_FAIL_RX = -0x0107                      # 0xFEF9
ICC_FAIL_CHAINING = -0x0108                # 0xFEF8
ICC_FAIL_APDU_FORMAT = -0x0109             # 0xFEF7
ICC_FAIL_UNKNOWN_CMD = -0x010A             # 0xFEF6
ICC_FAIL_STATE = -0x010B                   # 0xFEF5
ICC_FAIL_CODE_VERIFY = -0x010C             # 0xFEF4
ICC_FAIL_CRYPTO_VERIFY = -0x010D           # 0xFEF3
ICC_FAIL_CERT_VERIFY = -0x010E             # 0xFEF2
ICC_FAIL_FLASH = -0x010F                   # 0xFEF1

KSE_SUCCESS = 0x0000
KSE_FAIL = -0x8000                         # 0x8000
        
KSE_FAIL_WRONG_INPUT = -0x0200             # 0xFE00
KSE_FAIL_NOT_SUPPORTED = -0x0201           # 0xFDFF
KSE_FAIL_NOT_POWERED_ON = -0x0202          # 0xFDFE
KSE_FAIL_ALREADY_POWERED_ON = -0x0203      # 0xFDFD
KSE_FAIL_ATR = -0x0204                     # 0xFDFC
KSE_FAIL_PPS = -0x0205                     # 0xFDFB
KSE_FAIL_TX = -0x0206                      # 0xFDFA
KSE_FAIL_RX = -0x0207                      # 0xFDF9
KSE_FAIL_CHAINING = -0x0208                # 0xFDF8
KSE_FAIL_APDU_FORMAT = -0x0209             # 0xFDF7
KSE_FAIL_UNKNOWN_CMD = -0x020A             # 0xFDF6
KSE_FAIL_STATE = -0x020B                   # 0xFDF5
KSE_FAIL_CODE_VERIFY = -0x020C             # 0xFDF4
KSE_FAIL_CRYPTO_VERIFY = -0x020D           # 0xFDF3
KSE_FAIL_CERT_VERIFY = -0x020E             # 0xFDF2
KSE_FAIL_FLASH = -0x020F                   # 0xFDF1

KSE_FAIL_USB_INIT = -0x0300                # 0xFD00
KSE_FAIL_USB_NO_DEVICES = -0x0301          # 0xFCFF
KSE_FAIL_USB_DEVICE_OPEN = -0x0302         # 0xFCFE
KSE_FAIL_USB_DETACH_KERNEL_DRIVER = -0x0303# 0xFCFD
KSE_FAIL_USB_CLAIM_INTERFACE = -0x0304     # 0xFCFC
KSE_FAIL_USB_SEND_REPORT = -0x0305         # 0xFCFB
KSE_FAIL_USB_RECV_REPORT = -0x0306         # 0xFCFA
KSE_FAIL_NOT_FOUND = -0x0307               # 0xFCF9
KSE_FAIL_UNEXPECTED_RESP = -0x0308         # 0xFCF8
KSE_FAIL_UNEXPECTED_RESP_LEN = -0x0309     # 0xFCF7
KSE_FAIL_RECV_BUF_OVERFLOW = -0x030A       # 0xFCF6

KSETLS_FRAGMENT_RECORD = 0x0004
        # Fragment record.
KSETLS_HELLO_VERIFY_REQUEST = 0x0003
        # Hello verify requested.
KSETLS_HANDSHAKE_IN_PROGRESS = 0x0002
        # Handshake is not completed yet.
KSETLS_HANDSHAKE_DONE = 0x0001
        # Handshake done.

KSETLS_SUCCESS = 0x0000
        # Success.
KSETLS_FAIL = -0x0001
        # Fail.

KSETLS_ERR_NET_CONFIG = -0x0040
        # Failed to get ip address! Please check your
        # network configuration.
KSETLS_ERR_NET_SOCKET_FAILED = -0x0042
        # Failed to open a socket.
KSETLS_ERR_NET_CONNECT_FAILED = -0x0044
        # The connection to the given server:port failed.
KSETLS_ERR_NET_BIND_FAILED = -0x0046
        # Binding of the socket failed.
KSETLS_ERR_NET_LISTEN_FAILED = -0x0048
        # Could not listen on the socket.
KSETLS_ERR_NET_ACCEPT_FAILED = -0x004A
        # Could not accept the incoming connection.
KSETLS_ERR_NET_RECV_FAILED = -0x004C
        # Reading information from the socket failed.
KSETLS_ERR_NET_SEND_FAILED = -0x004E
        # Sending information through the socket failed.
KSETLS_ERR_NET_CONN_RESET = -0x0050
        # Connection was reset by peer.
KSETLS_ERR_NET_UNKNOWN_HOST = -0x0052
        # Failed to get an IP address for the given
        # hostname.
KSETLS_ERR_NET_BUFFER_TOO_SMALL = -0x0043
        # Buffer is too small to hold the data.
KSETLS_ERR_NET_INVALID_CONTEXT = -0x0045
        # The context is invalid, eg because it was
        # free()ed.
KSETLS_ERR_NET_POLL_FAILED = -0x0047
        # Polling the net context failed.
KSETLS_ERR_NET_BAD_INPUT_DATA = -0x0049
        # Input invalid.

KSETLS_ERR_TLS_FEATURE_UNAVAILABLE = -0x7080
        # The requested feature is not available.
KSETLS_ERR_TLS_BAD_INPUT_DATA = -0x7100
        # Bad input parameters to function.
KSETLS_ERR_TLS_INVALID_MAC = -0x7180
        # Verification of the message MAC failed.
KSETLS_ERR_TLS_INVALID_RECORD = -0x7200
        # An invalid SSL record was received.
KSETLS_ERR_TLS_CONN_EOF = -0x7280
        # The connection indicated an EOF.
KSETLS_ERR_TLS_UNKNOWN_CIPHER = -0x7300
        # An unknown cipher was received.
KSETLS_ERR_TLS_NO_CIPHER_CHOSEN = -0x7380
        # The server has no ciphersuites in common with the
        # client.
KSETLS_ERR_TLS_NO_RNG = -0x7400
        # No RNG was provided to the SSL module.
KSETLS_ERR_TLS_NO_CLIENT_CERTIFICATE = -0x7480
        # No client certification received from the client,
        # but required by the authentication mode.
KSETLS_ERR_TLS_CERTIFICATE_TOO_LARGE = -0x7500
        # Our own certificate(s) is/are too large to send in
        # an SSL message.
KSETLS_ERR_TLS_CERTIFICATE_REQUIRED = -0x7580
        # The own certificate is not set, but needed by the
        # server.
KSETLS_ERR_TLS_PRIVATE_KEY_REQUIRED = -0x7600
        # The own private key or pre-shared key is not set,
        # but needed.
KSETLS_ERR_TLS_CA_CHAIN_REQUIRED = -0x7680
        # No CA Chain is set, but required to operate.
KSETLS_ERR_TLS_UNEXPECTED_MESSAGE = -0x7700
        # An unexpected message was received from our peer.
KSETLS_ERR_TLS_FATAL_ALERT_MESSAGE = -0x7780
        # A fatal alert message was received from our peer.
KSETLS_ERR_TLS_PEER_VERIFY_FAILED = -0x7800
        # Verification of our peer failed.
KSETLS_ERR_TLS_PEER_CLOSE_NOTIFY = -0x7880
        # The peer notified us that the connection is going
        # to be closed.
KSETLS_ERR_TLS_BAD_HS_CLIENT_HELLO = -0x7900
        # Processing of the ClientHello handshake message
        # failed.
KSETLS_ERR_TLS_BAD_HS_SERVER_HELLO = -0x7980
        # Processing of the ServerHello handshake message
        # failed.
KSETLS_ERR_TLS_BAD_HS_CERTIFICATE = -0x7A00
        # Processing of the Certificate handshake message
        # failed.
KSETLS_ERR_TLS_BAD_HS_CERTIFICATE_REQUEST = -0x7A80
        # Processing of the CertificateRequest handshake
        # message failed.
KSETLS_ERR_TLS_BAD_HS_SERVER_KEY_EXCHANGE = -0x7B00
        # Processing of the ServerKeyExchange handshake
        # message failed.
KSETLS_ERR_TLS_BAD_HS_SERVER_HELLO_DONE = -0x7B80
        # Processing of the ServerHelloDone handshake
        # message failed.
KSETLS_ERR_TLS_BAD_HS_CLIENT_KEY_EXCHANGE = -0x7C00
        # Processing of the ClientKeyExchange handshake
        # message failed.
KSETLS_ERR_TLS_BAD_HS_CLIENT_KEY_EXCHANGE_RP = -0x7C80
        # Processing of the ClientKeyExchange handshake
        # message failed in DHM / ECDH Read Public.
KSETLS_ERR_TLS_BAD_HS_CLIENT_KEY_EXCHANGE_CS = -0x7D00
        # Processing of the ClientKeyExchange handshake
        # message failed in DHM / ECDH Calculate Secret.
KSETLS_ERR_TLS_BAD_HS_CERTIFICATE_VERIFY = -0x7D80
        # Processing of the CertificateVerify handshake
        # message failed.
KSETLS_ERR_TLS_BAD_HS_CHANGE_CIPHER_SPEC = -0x7E00
        # Processing of the ChangeCipherSpec handshake
        # message failed.
KSETLS_ERR_TLS_BAD_HS_FINISHED = -0x7E80
        # Processing of the Finished handshake message
        # failed.
KSETLS_ERR_TLS_ALLOC_FAILED = -0x7F00
        # Memory allocation failed.
KSETLS_ERR_TLS_HW_ACCEL_FAILED = -0x7F80
        # Hardware acceleration function returned with
        # error.
KSETLS_ERR_TLS_HW_ACCEL_FALLTHROUGH = -0x6F80
        # Hardware acceleration function skipped / left
        # alone data.
KSETLS_ERR_TLS_COMPRESSION_FAILED = -0x6F00
        # Processing of the compression / decompression
        # failed.
KSETLS_ERR_TLS_BAD_HS_PROTOCOL_VERSION = -0x6E80
        # Handshake protocol not within min/max boundaries.
KSETLS_ERR_TLS_BAD_HS_NEW_SESSION_TICKET = -0x6E00
        # Processing of the NewSessionTicket handshake
        # message failed.
KSETLS_ERR_TLS_SESSION_TICKET_EXPIRED = -0x6D80
        # Session ticket has expired.
KSETLS_ERR_TLS_PK_TYPE_MISMATCH = -0x6D00
        # Public key type mismatch (eg, asked for RSA key
        # exchange and presented EC key).
KSETLS_ERR_TLS_UNKNOWN_IDENTITY = -0x6C80
        # Unknown identity received (eg, PSK identity).
KSETLS_ERR_TLS_INTERNAL_ERROR = -0x6C00
        # Internal error (eg, unexpected failure in
        # lower-level module).
KSETLS_ERR_TLS_COUNTER_WRAPPING = -0x6B80
        # A counter would wrap (eg, too many messages
        # exchanged).
KSETLS_ERR_TLS_WAITING_SERVER_HELLO_RENEGO = -0x6B00
        # Unexpected message at ServerHello in
        # renegotiation.
KSETLS_ERR_TLS_HELLO_VERIFY_REQUIRED = -0x6A80
        # DTLS client must retry for hello verification.
KSETLS_ERR_TLS_BUFFER_TOO_SMALL = -0x6A00
        # A buffer is too small to receive or write a
        # message.
KSETLS_ERR_TLS_NO_USABLE_CIPHERSUITE = -0x6980
        # None of the common ciphersuites is usable (eg, no
        # suitable certificate, see debug messages).
KSETLS_ERR_TLS_WANT_READ = -0x6900
        # No data of requested type currently available on
        # underlying transport.
KSETLS_ERR_TLS_WANT_WRITE = -0x6880
        # Connection requires a write call.
KSETLS_ERR_TLS_TIMEOUT = -0x6800
        # The operation timed out.
KSETLS_ERR_TLS_CLIENT_RECONNECT = -0x6780
        # The client initiated a reconnect from the same
        # port.
KSETLS_ERR_TLS_UNEXPECTED_RECORD = -0x6700
        # Record header looks valid but is not expected.
KSETLS_ERR_TLS_NON_FATAL = -0x6680
        # The alert message received indicates a non-fatal
        # error.
KSETLS_ERR_TLS_INVALID_VERIFY_HASH = -0x6600
        # Couldn't set the hash for verifying
        # CertificateVerify.
KSETLS_ERR_TLS_CONTINUE_PROCESSING = -0x6580
        # Internal-only message signaling that further
        # message-processing should be done.
KSETLS_ERR_TLS_ASYNC_IN_PROGRESS = -0x6500
        # The asynchronous operation is not completed yet.
KSETLS_ERR_TLS_EARLY_MESSAGE = -0x6480
        # Internal-only message signaling that a message
        # arrived early.
KSETLS_ERR_TLS_CRYPTO_IN_PROGRESS = -0x7000
        # A cryptographic operation failure in progress.
#Debug---------------------------------------------------------------------------------
gfEnableDebugPrint = False
strKseErr = 0

#Parameter for USB Communication-------------------------------------------------------
gsKseLastErrorCode = 0
gsTransceiveLastErrorCode = 0
backend = usb.backend.libusb1.get_backend(find_library=lambda x : "/usr/lib/libsub.so")
hDevice = 0 #Close hadle for device
dev = 0
VALID_CONNECT = 0

#USB Communication in Data send&Recv---------------------------------------------------
REP_ONE_BLOCK = 0xA5
REP_FIRST_BLOCK = 0xA1
REP_MIDDLE_BLOCK =0x11
REP_LAST_BLOCK = 0x15
OUT_ENDPOINT = 0x01 #end point for bulk write
IN_ENDPOINT = 0x81 #end point for bulk read
TIMEOUT_MS = 5000

#KSE100U
MAX_KCMVP_KEY_COUNT = 8
MAX_CERT_KEY_COUNT = 96
MAX_IO_DATA_SIZE = 2944
MAX_INFO_FILE_SIZE = 8192

MAX_CTRL_DATA_SIZE = 128
MAX_TRANSCEIVE_SIZE = MAX_IO_DATA_SIZE + MAX_CTRL_DATA_SIZE

#KCMVP----------------------------------------------------------------------------------

KCMVP_DES_KEY = 0x20
KCMVP_TDES_KEY = 0x30
KCMVP_AES128_KEY = 0x40
KCMVP_AES192_KEY = 0x41
KCMVP_AES256_KEY = 0x42
KCMVP_ARIA128_KEY = 0x50
KCMVP_ARIA192_KEY = 0x51
KCMVP_ARIA256_KEY = 0x52
KCMVP_HMAC_KEY = 0x70
KCMVP_ECDSA_KEYPAIR = 0x80
KCMVP_ECDSA_PRI_KEY = 0x81
KCMVP_ECDSA_PUB_KEY = 0x82
KCMVP_ECDH_KEYPAIR = 0x90
KCMVP_ECDH_PRI_KEY = 0x91
KCMVP_ECDH_PUB_KEY = 0x92

KCMVP_DES = 0x20
KCMVP_TDES = 0x30
KCMVP_AES = 0x40
KCMVP_ARIA = 0x50
KCMVP_FAST_ARIA = 0x58
KCMVP_SHA = 0x60
KCMVP_HMAC_GEN = 0x70
KCMVP_HMAC_VERI = 0x78
KCMVP_ECDSA_SIGN = 0x80
KCMVP_ECDSA_VERI = 0x88
KCMVP_ECDH = 0x90

ENCRYPT = 0
DECRYPT = 1

########################################################################################
## Methods #############################################################################
########################################################################################

def find_kse():
    global dev
    dev=usb.core.find(idVendor=0x25f8,idProduct=0x9001)
    return dev


def Transceive(abSendData):
    global gsTransceiveLastErrorCode
    global dev
    
    abRecvData = bytearray()
    
    if(VALID_CONNECT != 0):
        gsTransceiveLastErrorCode = KSE_FAIL_NOT_FOUND
        return None
    
    usSendLen = len(abSendData)
    usLen = 0
    usOffset = 0
    abOutReport = bytearray(64)
    abInReport = bytearray(64)
    
    while usSendLen > 0:
        if (abOutReport[0] == 0x00)and(usSendLen <= 60):
            abOutReport[0] = REP_ONE_BLOCK
        elif (abOutReport[0] == 0x00)and(usSendLen > 60):
            abOutReport[0] = REP_FIRST_BLOCK
        elif (abOutReport[0]!= 0x00)and(usSendLen > 60):
            abOutReport[0] = REP_MIDDLE_BLOCK
        else:
            abOutReport[0] = REP_LAST_BLOCK
        
        if usSendLen > 60:
            usLen = 60
        else:
            usLen = usSendLen
        
        abOutReport[1] = 0x05
        abOutReport[2] = usOffset 
        abOutReport[3] = usLen

        abOutReport[4:4+usLen] = abSendData[usOffset*60:usOffset*60+usLen]
        usOffset += 1
        usSendLen -= usLen

        #Transceive report for process between send&receive data packet
        try:
            dev.write(OUT_ENDPOINT,abOutReport,TIMEOUT_MS)
        except:
            gsTransceiveLastErrorCode = KSE_FAIL_USB_SEND_REPORT
            return None
        try :    
            tmp = dev.read(IN_ENDPOINT,len(abOutReport),TIMEOUT_MS)
            abInReport = bytearray(tmp) 
        except:
            gsTransceiveLastErrorCode = KSE_FAIL_USB_RECV_REPORT
            return None
 
        if (((abOutReport[0] == REP_ONE_BLOCK) or (abOutReport[0] == REP_LAST_BLOCK)) and \
           ((abInReport[1] != 0x06) or (abInReport[2] != 0x00))) or \
           (((abOutReport[0] == REP_FIRST_BLOCK) or (abOutReport[0] == REP_MIDDLE_BLOCK)) and \
           ((abInReport[0] != abOutReport[0]) or (abInReport[1] != 0xFE) \
            or (abInReport[2] != abOutReport[2]) or (abInReport[3] != abOutReport[3]))):
            gsTransceiveLastErrorCode = KSE_FAIL_UNEXPECTED_RESP
            return None
       
    #receive ack packet from USB
    usOffset = 0
    usRecvLen = abInReport[3]
    if usRecvLen > MAX_TRANSCEIVE_SIZE:
        gsTransceiveLastErrorCode = KSE_FAIL_RECV_BUF_OVERFLOW
        return None
    abIoBuffer = bytearray(MAX_TRANSCEIVE_SIZE)
    abIoBuffer[0:usRecvLen] = abInReport[4:4+usRecvLen]
    if abInReport[0] == REP_FIRST_BLOCK:
        while True:
            abOutReport[0:4] = abInReport[0:4]
            abOutReport[1] = 0xFE
            
            try:
                dev.write(OUT_ENDPOINT,abOutReport,TIMEOUT_MS)
            except:
                gsTransceiveLastErrorCode = KSE_FAIL_USB_SEND_REPORT
                return None
            try :    
                tmp = dev.read(IN_ENDPOINT,len(abOutReport),TIMEOUT_MS)
                abInReport = bytearray(tmp) 
            except:
                gsTransceiveLastErrorCode = KSE_FAIL_USB_RECV_REPORT
                return None
            usOffset = abInReport[2]
            usLen = abInReport[3]
            usRecvLen += usLen
            if usRecvLen > MAX_TRANSCEIVE_SIZE:
                gsTransceiveLastErrorCode = KSE_FAIL_UNEXPECTED_RESP
                return None
            abIoBuffer[60*usOffset:60*usOffset+usLen] = abInReport[4:usLen+4]
            if not abInReport[0] == REP_MIDDLE_BLOCK:
                break
    abRecvData = bytearray(usRecvLen)
    abRecvData[0:usRecvLen] = abIoBuffer[0:usRecvLen]
    Str_abRecvData = (binascii.hexlify(abRecvData)).decode("ascii")
    #print(Str_abRecvData)
    return abRecvData
        
#MethodName : PowerOn
def Connect():
#Code for connecting & error detecting on finding kse100u
    global gsKseLastErrorCode
    global VALID_CONNECT
    global hDevice
    global dev
    
    if gusKsePower != KSE_POWER_OFF:
        gsKseLastErrorCode = KSE_FAIL_ALREADY_POWERED_ON
        return KSE_FAIL
    
    busses = usb.busses()
    for bus in busses:
        devices = bus.devices
    if len(devices)<0:
        gsKseLastErrorCode = KSE_FAIL_USB_INIT
        print("KSE_FAIL_USB_INIT")
        return KSE_FAIL
    elif len(devices) == 0:
        gsKseLastErrorCode = KSE_FAIL_USB_NO_DEVICES
        #profilelist.close()
        print("KSE_FAIL_USB_NO_DEVICE")
        return KSE_FAIL 
    else:
        dev=find_kse()
        
        if dev is None:
            gsKseLastErrorCode = KSE_FAIL_NOT_FOUND
            #profilelist.close()
            print("KSE_FAIL_NOT_FOUND")
            return KSE_FAIL
        with usb1.USBContext() as context:
            hDevice = context.openByVendorIDAndProductID(0x25f8,0x9001,)
        if dev.is_kernel_driver_active(0):
            try:
                dev.detach_kernel_driver(0)
            except:
                gsKseLastErrorCode = KSE_FAIL_USB_DEVICE_OPEN
                dev.reset()
                return KSE_FAIL
        else:
            dev.set_configuration()
            cfg = dev.get_active_configuration
            if cfg is None:
                gsKseLastErrorCode = KSE_FAIL_USB_CLAIM_INTERFACE
                dev.reset()
                return KSE_FAIL             
            else:
                try:
                    usb.util.claim_interface(dev,0)
                    VALID_CONNECT = KSE_SUCCESS
                    dev.reset()
                    return KSE_SUCCESS
                except:
                    gsKseLastErrorCode = KSE_FAIL_USB_CLAIM_INTERFACE
                    dev.reset()
                    return KSE_FAIL

def PowerOn(): 
    global gsTransceiveLastErrorCode
    global gsKseLastErrorCode
    global gusKsePower
        
    if Connect() == KSE_FAIL:
        return KSE_FAIL
    abTxData = bytes([0x00, 0x00])
    abRxData = Transceive(abTxData)
    if abRxData == None:
        dev.reset()
        gsKseLastErrorCode = gsTransceiveLastErrorCode
        return KSE_FAIL
    usLen = len(abRxData)
    if usLen < 2: 
        dev.reset()
        gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
        return KSE_FAIL#
    sRv = ((abRxData[0]<<8) | abRxData[1])
    if ((sRv == KSE_SUCCESS) and (usLen !=39)) or ((sRv != KSE_SUCCESS) and (usLen != 2)):
        dev.reset()
        gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
    valid_result = sub_module.slicing_for_valid(abRxData)

    gusKsePower = KSE_POWER_ON

    return [sRv, valid_result]

def PowerOff():
    global gusKsePower
    gsKseLastErrorCode = KSE_SUCCESS
    if gusKsePower != KSE_POWER_ON:
        gsKseLastErrorCode = KSE_FAIL_NOT_POWERED_ON
        return KSE_FAIL
    
    abTxData = bytearray([0x00, 0x01])
    abRxData = Transceive(abTxData)
    if abRxData == None:
        dev.reset()
        hDevice = None
        gsKseLastErrorCode = gsTransceiveLastErrorCode
        return KSE_FAIL
    usLen = len(abRxData)
    if usLen != 2:
        dev.reset()
        hDevice = None
        gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
        return KSE_FAIL
    sRv = (abRxData[0] << 8) | abRxData[1]
    if sRv != KSE_SUCCESS:
        dev.reset()
        hDevice = None
        gsKseLastErrorCode = sRv
        return KSE_FAIL
    dev.reset()
    hDevice = None
    
    gusKsePower = KSE_POWER_OFF
    return sRv
    

def Clear(bOpt):
    global gsKseLastErrorCode
    gsKseLastErrorCode = KSE_SUCCESS
    if gusKsePower != KSE_POWER_ON:
        gsKseLastErrorCode = KSE_FAIL_NOT_POWERED_ON
        return KSE_FAIL
    abTxData = bytearray(3)
    abTxData[1] = 0xFC
    abTxData[2] = bOpt
    abRxData = Transceive(abTxData)
    if abRxData == None:
        gsKseLastErrorCode = gsTransceiveLastErrorCode
        return KSE_FAIL
    usLen = len(abRxData)
    if(usLen != 2):
        gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
        return KSE_FAIL
    sRv = (abRxData[0] <<8 | abRxData[1])
    if sRv != KSE_SUCCESS:
        gsKseLastErrorCode = sRv
        return KSE_FAIL
    return KSE_SUCCESS

def IssueInit(abSystemTitle):
    gsKseLastErrorCode = KSE_SUCCESS
    if gusKsePower != KSE_POWER_ON:
        gsKseLastErrorCode - KSE_FAIL_NOT_POWERED_ON
        return KSE_FAIL
    
    if (abSystemTitle == None) or (len(abSystemTitle) != 8):
        gsKseLastErrorCode = KSE_FAIL_WRONG_INPUT
        return KSE_FAIL
    
    abTxData = bytearray(10)
    abTxData[1] = 0xFE
    abTxData[2:10] = abSystemTitle
    abRxData = Transceive(abTxData)
    if abRxData == None:
        gsKseLastErrorCode = gsTransceiveLastErrorCode
        return KSE_FAIL
    usLen = len(abRxData)
    if usLen != 2:
        gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
        return KSE_FAIL
    sRv = (abRxData[0] << 8) | abRxData[1]
    if sRv != KSE_SUCCESS:
        gsKseLastErrorCode = sRv
        return KSE_FAIL
    return KSE_SUCCESS

def IssueFinal():
    gsKseLastErrorCode = KSE_SUCCESS
    if gusKsePower != KSE_POWER_ON:
        gsKseLastErrorCode = KSE_FAIL_NOT_POWERED_ON
        return KSE_FAIL
    
    abTxData = ([0x00, 0xFF])
    abRxData = Transceive(abTxData)
    if abRxData == None:
        gsKseLastErrorCode = gsTransceiveLastErrorCode
        return KSE_FAIL
    usLen = len(abRxData)
    if usLen != 2:
        gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
        return KSE_FAIL
    sRv = (abRxData[0] << 8) | abRxData[1]
    if sRv != KSE_SUCCESS:
        gsKseLastErrorCode = sRv
        return KSE_FAIL
    return KSE_SUCCESS

def VerifyCode(bVcType, abCode, abDs):
    ulCodeSize = 0
    sRv = 0
    usLen = 0
    abRxData = 0
    abTxData = bytearray()
    abRxData = bytearray()
    gsKseLastErrorCode = KSE_SUCCESS
    if gusKsePower != KSE_POWER_ON:
        gsKseLastErrorCode = KSE_FAIL_NOT_POWERED_ON
        return KSE_FAIL
    if ((bVcType > VC_TYPE_4) or\
       ((bVcType == VC_TYPE_0) and\
        ((abCode == None) or (len(abCode) != 32)))) or\
        (((bVcType == VC_TYPE_2) or (bVcType == VC_TYPE_4)) and\
         ((abDs == None) or (len(abDs) != 64))):
        gsKseLastErrorCode = KSE_FAIL_WRONG_INPUT
        return KSE_FAIL
    if abCode == None:
        ulCodeSize = 0
    else:
        ulCodeSize = len(abCode)
    if ulCodeSize == VC_TYPE_0:
        abTxData = bytearray(35)
        abTxData[0] = 0x00
        abTxData[1] = 0x14
        abTxData[2] = bVcType
        abTxData[3:35] =abCode[0:32]
    else:
        abTxData = bytearray(MAX_IO_DATA_SIZE + 5)
        abTxData[0] = 0x00
        abTxData[1] = 0x15
        abTxData[2] = bVcType
        abTxData[3] = MAX_IO_DATA_SIZE >> 8
        abTxData[4] = MAX_IO_DATA_SIZE & 0xFF
        abTxData[5:MAX_IO_DATA_SIZE] = abCode[0:MAX_IO_DATA_SIZE]
        abRxData = Transceive(abTxData)
        
        if abRxData == None:
            gsKseLastErrorCode = gsTransceiveLastErrorCode
            return KSE_FAIL
        usLen = len(abRxData)
        
        if usLen != 2:
            gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
            return KSE_FAIL
        sRv = ((abRxData[0] << 8) | abRxData[1])
        
        if sRv != KSE_SUCCESS:
            gsKseLastErrorCode = sRv
            return KSE_FAIL
        
        ulCodeOffset = MAX_IO_DATA_SIZE
        ulCodeSize -= MAX_IO_DATA_SIZE
        
        while ulCodeSize > MAX_IO_DATA_SIZE:
            abTxData = bytearray(MAX_IO_DATA_SIZE + 4)
            abTxData[0] = 0x00
            abTxData[1] = 0x16
            abTxData[2] = MAX_IO_DATA_SIZE >> 8
            abTxData[3] = MAX_IO_DATA_SIZE & 0xFF
            abTxData[4:4+MAX_IO_DATA_SIZE] = abCode[ulCodeOffset:ulCodeOffset+MAX_IO_DATA_SIZE]

            abRxData = Transceive(abTxData)
            if abRxData == None:
                gsKseLastErrorCode = gsTransceiveLastErrorCode
                return KSE_FAIL
            
            usLen = len(abRxData)
            if usLen != 2:
                gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
                return KSE_FAIL
            
            sRv = ((abRxData[0] << 8) | abRxData[1])
            if sRv != KSE_SUCCESS:
                gsKseLastErrorCode = sRv
                return KSE_FAIL
            
            ulCodeOffset += MAX_IO_DATA_SIZE
            ulCodeSize -= MAX_IO_DATA_SIZE
            
            if (bVcType == VC_TYPE_1) or (bVcType == VC_TYPE_3):
                abTxData = bytearray(ulCodeSize + 4)
            else:
                abTxData = bytearray(ulCodeSize + 68)
            abTxData[0] = 0x00
            abTxData[1] = 0x17
            abTxData[2] = ulCodeSize >> 8
            abTxData[3] = ulCodeSize
            abTxData[4:4+ulCodeSize] = abCode[0:ulCodeSize]

            if (bVcType == VC_TYPE_2) or (bVcType == VC_TYPE_4):
                abTxData[ulCodeSize+4:ulCodeSize+68] = abDs[0:64]
            abRxData = Transceive(abTxData)
        
        if abRxData == None:
            gsKseLastErrorCode = gsTransceiveLastErrorCode
            return KSE_FAIL
        
        usLen = len(abRxData)
        if usLen != 2:
            gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
            return KSE_FAIL
        
        sRv = (abRxData[0] << 8) | abRxData[1]
        if (sRv != KSE_SUCCESS):
            gsKseLastErrorCode = sRv
            return KSE_FAIL
        
        gbVcType = VC_DISABLED

        return KSE_SUCCESS
        
                
        
def ErrStr():
    global strKseErr

    if gsKseLastErrorCode == KSE_SUCCESS:
        strKseErr = "Success"
    elif gsKseLastErrorCode == KSE_FAIL:
        strKseErr = "Fail"

    elif gsKseLastErrorCode == ICC_FAIL_WRONG_INPUT:
        strKseErr = "ICC wrong input"
    elif gsKseLastErrorCode == ICC_FAIL_NOT_SUPPORTED:
        strKseErr = "ICC not supported"
    elif gsKseLastErrorCode == ICC_FAIL_NOT_POWERED_ON:
        strKseErr = "ICC not powered on"
    elif gsKseLastErrorCode == ICC_FAIL_ALREADY_POWERED_ON:
        strKseErr = "ICC already powered on"
    elif gsKseLastErrorCode == ICC_FAIL_ATR:
        strKseErr = "ICC ATR error"
    elif gsKseLastErrorCode == ICC_FAIL_PPS:
        strKseErr = "ICC PPS error"
    elif gsKseLastErrorCode == ICC_FAIL_TX:
        strKseErr = "ICC Tx error"
    elif gsKseLastErrorCode == ICC_FAIL_RX:
        strKseErr = "ICC Rx error"
    elif gsKseLastErrorCode == ICC_FAIL_CHAINING:
        strKseErr = "ICC chaining error"
    elif gsKseLastErrorCode == ICC_FAIL_APDU_FORMAT:
        strKseErr = "ICC wrong APDU format"
    elif gsKseLastErrorCode == ICC_FAIL_UNKNOWN_CMD:
        strKseErr = "ICC unknown command"
    elif gsKseLastErrorCode == ICC_FAIL_STATE:
        strKseErr = "ICC state error"
    elif gsKseLastErrorCode == ICC_FAIL_CODE_VERIFY:
        strKseErr = "ICC code verification error"
    elif gsKseLastErrorCode == ICC_FAIL_CRYPTO_VERIFY:
        strKseErr = "ICC crypto verification error"
    elif gsKseLastErrorCode == ICC_FAIL_CERT_VERIFY:
        strKseErr = "ICC certificate verification error"
    elif gsKseLastErrorCode == ICC_FAIL_FLASH:
        strKseErr = "ICC flash memory error"

    elif gsKseLastErrorCode == KSE_FAIL_WRONG_INPUT:
        strKseErr = "KSE wrong input"
    elif gsKseLastErrorCode == KSE_FAIL_NOT_SUPPORTED:
        strKseErr = "KSE not supported"
    elif gsKseLastErrorCode == KSE_FAIL_NOT_POWERED_ON:
        strKseErr = "KSE not powered on"
    elif gsKseLastErrorCode == KSE_FAIL_ALREADY_POWERED_ON:
        strKseErr = "KSE already powered on"
    elif gsKseLastErrorCode == KSE_FAIL_ATR:
        strKseErr = "KSE ATR error"
    elif gsKseLastErrorCode == KSE_FAIL_PPS:
        strKseErr = "KSE PPS error"
    elif gsKseLastErrorCode == KSE_FAIL_TX:
        strKseErr = "KSE Tx error"
    elif gsKseLastErrorCode == KSE_FAIL_RX:
        strKseErr = "KSE Rx error"
    elif gsKseLastErrorCode == KSE_FAIL_CHAINING:
        strKseErr = "KSE chaining error"
    elif gsKseLastErrorCode == KSE_FAIL_APDU_FORMAT:
        strKseErr = "KSE wrong APDU format"
    elif gsKseLastErrorCode == KSE_FAIL_UNKNOWN_CMD:
        strKseErr = "KSE unknown command"
    elif gsKseLastErrorCode == KSE_FAIL_STATE:
        strKseErr = "KSE state error"
    elif gsKseLastErrorCode == KSE_FAIL_CODE_VERIFY:
        strKseErr = "KSE code verification error"
    elif gsKseLastErrorCode == KSE_FAIL_CRYPTO_VERIFY:
        strKseErr = "KSE crypto verification error"
    elif gsKseLastErrorCode == KSE_FAIL_CERT_VERIFY:
        strKseErr = "KSE certificate verification error"
    elif gsKseLastErrorCode == KSE_FAIL_FLASH:
        strKseErr = "KSE flash memory error"
    elif (gsKseLastErrorCode & 0xFF00) == 0x6F00:
        strKseErr = "0x"+ str(hex(gsKseLastErrorCode))[0:4] + " CLIB error." 

    elif (gsKseLastErrorCode == KSE_FAIL_USB_INIT):
        strKseErr = "USB initialization error"
    elif (gsKseLastErrorCode == KSE_FAIL_USB_NO_DEVICES):
        strKseErr = "No USB devices"
    elif (gsKseLastErrorCode == KSE_FAIL_USB_DEVICE_OPEN):
        strKseErr = "USB device open error"
    elif (gsKseLastErrorCode == KSE_FAIL_USB_DETACH_KERNEL_DRIVER):
        strKseErr = "USB detach kernel driver error"
    elif (gsKseLastErrorCode == KSE_FAIL_USB_CLAIM_INTERFACE):
        strKseErr = "USB claim interface driver error"
    elif (gsKseLastErrorCode == KSE_FAIL_USB_SEND_REPORT):
        strKseErr = "USB send report error"
    elif (gsKseLastErrorCode == KSE_FAIL_USB_RECV_REPORT):
        strKseErr = "USB receive report error"
    elif (gsKseLastErrorCode == KSE_FAIL_NOT_FOUND):
        strKseErr = "KSE not found"
    elif (gsKseLastErrorCode == KSE_FAIL_UNEXPECTED_RESP):
        strKseErr = "KSE unexpected response"
    elif (gsKseLastErrorCode == KSE_FAIL_UNEXPECTED_RESP_LEN):
        strKseErr = "KSE unexpected response length"
    elif (gsKseLastErrorCode == KSE_FAIL_RECV_BUF_OVERFLOW):
        strKseErr = "USB receive buffer overflow"

    elif (gsKseLastErrorCode == KSETLS_FRAGMENT_RECORD):
        strKseErr = "Fragment record"
    elif (gsKseLastErrorCode == KSETLS_HELLO_VERIFY_REQUEST):
        strKseErr = "Hello verify requested"
    elif (gsKseLastErrorCode == KSETLS_HANDSHAKE_IN_PROGRESS):
        strKseErr = "Handshake is not completed yet"
    elif (gsKseLastErrorCode == KSETLS_HANDSHAKE_DONE):
        strKseErr = "Handshake done"

    elif (gsKseLastErrorCode == KSETLS_ERR_NET_CONFIG):
        strKseErr = "Failed to get ip address! Please check your " + "network configuration"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_SOCKET_FAILED):
        strKseErr = "Failed to open a socket"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_CONNECT_FAILED):
        strKseErr = "The connection to the given server:port failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_BIND_FAILED):
        strKseErr = "Binding of the socket failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_LISTEN_FAILED):
        strKseErr = "Could not listen on the socket"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_ACCEPT_FAILED):
        strKseErr = "Could not accept the incoming connection"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_RECV_FAILED):
        strKseErr = "Reading information from the socket failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_SEND_FAILED):
        strKseErr = "Sending information through the socket failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_CONN_RESET):
        strKseErr = "Connection was reset by peer"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_UNKNOWN_HOST):
        strKseErr = "Failed to get an IP address for the given " + "hostname"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_BUFFER_TOO_SMALL):
        strKseErr = "Buffer is too small to hold the data"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_INVALID_CONTEXT):
        strKseErr = "The context is invalid, eg because it was " + "free()ed"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_POLL_FAILED):
        strKseErr = "Polling the net context failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_NET_BAD_INPUT_DATA):
        strKseErr = "Input invalid"

    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_FEATURE_UNAVAILABLE):
        strKseErr = "The requested feature is not available"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_INPUT_DATA):
        strKseErr = "Bad input parameters to function"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_INVALID_MAC):
        strKseErr = "Verification of the message MAC failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_INVALID_RECORD):
        strKseErr = "An invalid SSL record was received"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_CONN_EOF):
        strKseErr = "The connection indicated an EOF"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_UNKNOWN_CIPHER):
        strKseErr = "An unknown cipher was received"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_NO_CIPHER_CHOSEN):
        strKseErr = "The server has no ciphersuites in common with " + "the client"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_NO_RNG):
        strKseErr = "No RNG was provided to the SSL module"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_NO_CLIENT_CERTIFICATE):
        strKseErr = "No client certification received from the " + "client, but required by the authentication mode"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_CERTIFICATE_TOO_LARGE):
        strKseErr = "Our own certificate(s) is/are too large to send " + "in an SSL message"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_CERTIFICATE_REQUIRED):
        strKseErr = "The own certificate is not set, but needed by " + "the server"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_PRIVATE_KEY_REQUIRED):
        strKseErr = "The own private key or pre-shared key is not " + "set, but needed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_CA_CHAIN_REQUIRED):
        strKseErr = "No CA Chain is set, but required to operate"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_UNEXPECTED_MESSAGE):
        strKseErr = "An unexpected message was received from our peer"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_FATAL_ALERT_MESSAGE):
        strKseErr = "A fatal alert message was received from our peer"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_PEER_VERIFY_FAILED):
        strKseErr = "Verification of our peer failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_PEER_CLOSE_NOTIFY):
        strKseErr = "The peer notified us that the connection is " + "going to be closed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_CLIENT_HELLO):
        strKseErr = "Processing of the ClientHello handshake message " + "failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_SERVER_HELLO):
        strKseErr = "Processing of the ServerHello handshake message " + "failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_CERTIFICATE):
        strKseErr = "Processing of the Certificate handshake message " + "failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_CERTIFICATE_REQUEST):
        strKseErr = "Processing of the CertificateRequest handshake " + "message failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_SERVER_KEY_EXCHANGE):
        strKseErr = "Processing of the ServerKeyExchange handshake " + "message failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_SERVER_HELLO_DONE):
        strKseErr = "Processing of the ServerHelloDone handshake " + "message failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_CLIENT_KEY_EXCHANGE):
        strKseErr = "Processing of the ClientKeyExchange handshake " + "message failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_CLIENT_KEY_EXCHANGE_RP):
        strKseErr = "Processing of the ClientKeyExchange handshake " + "message failed in DHM / ECDH Read Public"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_CLIENT_KEY_EXCHANGE_CS):
        strKseErr = "Processing of the ClientKeyExchange handshake " + "message failed in DHM / ECDH Calculate Secret"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_CERTIFICATE_VERIFY):
        strKseErr = "Processing of the CertificateVerify handshake " +"message failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_CHANGE_CIPHER_SPEC):
        strKseErr = "Processing of the ChangeCipherSpec handshake " +"message failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BAD_HS_FINISHED):
        strKseErr = "Processing of the Finished handshake message " + "failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_ALLOC_FAILED):
        strKseErr = "Memory allocation failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_HW_ACCEL_FAILED):
        strKseErr = "Hardware acceleration function returned with " + "error"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_HW_ACCEL_FALLTHROUGH):
        strKseErr = "Hardware acceleration function skipped / left " + "alone data"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_COMPRESSION_FAILED):
        strKseErr = "Processing of the compression / decompression " + "failed"
    elif (gsKseLastErrorCode ==KSETLS_ERR_TLS_BAD_HS_PROTOCOL_VERSION):
        strKseErr = "Handshake protocol not within min/max boundaries"
    elif (gsKseLastErrorCode ==KSETLS_ERR_TLS_BAD_HS_NEW_SESSION_TICKET):
        strKseErr = "Processing of the NewSessionTicket handshake " +"message failed"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_SESSION_TICKET_EXPIRED):
        strKseErr = "Session ticket has expired"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_PK_TYPE_MISMATCH):
        strKseErr = "Public key type mismatch (eg, asked for RSA key " +"exchange and presented EC key)"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_UNKNOWN_IDENTITY):
        strKseErr = "Unknown identity received (eg, PSK identity)"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_INTERNAL_ERROR):
        strKseErr = "Internal error (eg, unexpected failure in " +"lower-level module)"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_COUNTER_WRAPPING):
        strKseErr = "A counter would wrap (eg, too many messages " +"exchanged)"
    elif (gsKseLastErrorCode ==KSETLS_ERR_TLS_WAITING_SERVER_HELLO_RENEGO):
        strKseErr = "Unexpected message at ServerHello in " +"renegotiation"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_HELLO_VERIFY_REQUIRED):
        strKseErr = "DTLS client must retry for hello verification"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_BUFFER_TOO_SMALL):
        strKseErr = "A buffer is too small to receive or write a " +"message"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_NO_USABLE_CIPHERSUITE):
        strKseErr = "None of the common ciphersuites is usable (eg, " +"no suitable certificate, see debug messages)"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_WANT_READ):
        strKseErr = "No data of requested type currently available " +"on underlying transport"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_WANT_WRITE):
        strKseErr = "Connection requires a write call"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_TIMEOUT):
        strKseErr = "The operation timed out"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_CLIENT_RECONNECT):
        strKseErr = "The client initiated a reconnect from the same " +"port"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_UNEXPECTED_RECORD):
        strKseErr = "Record header looks valid but is not expected"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_NON_FATAL):
        strKseErr = "The alert message received indicates a " +"non-fatal error"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_INVALID_VERIFY_HASH):
        strKseErr = "Couldn't set the hash for verifying " +"CertificateVerify"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_CONTINUE_PROCESSING):
        strKseErr = "Internal-only message signaling that further " +"message-processing should be done"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_ASYNC_IN_PROGRESS):
        strKseErr = "The asynchronous operation is not completed yet"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_EARLY_MESSAGE):
        strKseErr = "Internal-only message signaling that a message " +"arrived early"
    elif (gsKseLastErrorCode == KSETLS_ERR_TLS_CRYPTO_IN_PROGRESS):
        strKseErr = "A cryptographic operation failure in progress."

    else:
        strKseErr = "0x"+ str(hex(-gsKseLastErrorCode))[0:4] + " KSE unknown error."

    return strKseErr
    

def DebugPrintErrStr(strErrFunc):

    if gfEnableDebugPrint != True:
        return
    
    print(strErrFunc + " : " + ErrStr())

def KcmvpGenerateKey(bKeyType, usKeyIndex,usHmacKeySize):
    gsKseLastErrorCode = KSE_SUCCESS
    if gusKsePower != KSE_POWER_ON:
        gusKseLastErrorCode = KSE_FAIL_NOT_POWERED_ON
        return KSE_FAIL
    
    if(((bKeyType!=KCMVP_DES_KEY)and(bKeyType!=KCMVP_TDES_KEY)and\
    (bKeyType!=KCMVP_AES128_KEY)and(bKeyType!=KCMVP_AES192_KEY)and\
    (bKeyType!=KCMVP_AES256_KEY)and(bKeyType!=KCMVP_ARIA128_KEY)and\
    (bKeyType!=KCMVP_ARIA192_KEY)and(bKeyType!=KCMVP_ARIA256_KEY)and\
    (bKeyType!=KCMVP_HMAC_KEY)and(bKeyType!=KCMVP_ECDSA_KEYPAIR)and\
    (bKeyType!=KCMVP_ECDH_KEYPAIR))or(usKeyIndex>=MAX_KCMVP_KEY_COUNT)\
   or((bKeyType==KCMVP_HMAC_KEY)and(usHmacKeySize>255))):
         gsKseLastErrorCode = KSE_FAIL_WRONG_INPUT
         return KSE_FAIL
        
    abTxData = bytearray()
    if bKeyType != KCMVP_HMAC_KEY:
        abTxData = bytearray(5)
    else:
        abTxData = bytearray(7)
    abTxData[0] = 0x02
    abTxData[2] = bKeyType
    abTxData[3] = usKeyIndex >> 8
    abTxData[4] = usKeyIndex
    
    abRxData = Transceive(abTxData)
    if abRxData == None:
        gsKseLastErrorCode = gsTransceiveLastErrorCode
        return KSE_FAIL
    usLen = len(abRxData)
    if usLen != 2:
        gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
        return KSE_FAIL
    sRv =(abRxData[0] << 8) | abRxData[1]
    if (sRv != KSE_SUCCESS):
        gsKseLastErrorCode = sRv
        return KSE_FAIL
    return KSE_SUCCESS

def KcmvpEcb(abInput, bKeyType, usKeyIndex, bEnDe, bAlg):
    global gsKseErrorCode
    abRxData = 0
    sRv = 0
    gsKseErrorCode = KSE_SUCCESS
    
    if gusKsePower != KSE_POWER_ON:
        gsKseLastErrorCode = KSE_FAIL_NOT_POWERED_ON
        return None
    #Check Input data
    if ((abInput == None) or (len(abInput) == 0) or \
       (usKeyIndex >= MAX_KCMVP_KEY_COUNT) or \
       ((bEnDe != ENCRYPT) and (bEnDe !=DECRYPT))):
        gsKseLastErrorCode = KSE_FAIL_WRONG_INPUT
        return None
    usBlockSize = 0
    ulInputSize = len(abInput)
    if (bAlg == KCMVP_DES) or (bAlg == KCMVP_TDES):
        usBlockSize = 8
    else:
        if ((bAlg & 0xF0) ^ bKeyType) > 0x02:
            gsKseLastErrorCode = KSE_FAIL_WRONG_INPUT
            return None
        usBlockSize = 16
    if (ulInputSize % usBlockSize) !=0:
        gsKseLastErrorCode = KSE_FAIL_WRONG_INPUT
        return None
    
    abOutput = bytearray(ulInputSize)
    ulOutputOffset = 0
    
    while True:
        if ulInputSize < MAX_IO_DATA_SIZE:
            usSize = ulInputSize
        else:
            usSize = MAX_IO_DATA_SIZE
        abTxData = bytearray()
        if usBlockSize == 16:
            abTxData = bytearray(usSize + 8)
        else:
            abTxData = bytearray(usSize + 7)
        abTxData[0] = 0x02
        abTxData[1] = (bAlg | 0x04)
        i = 2
        if usBlockSize == 16:
            abTxData[i] = bKeyType
            i += 1
        abTxData[i] = usKeyIndex >> 8
        i += 1
        abTxData[i] = usKeyIndex
        i += 1
        abTxData[i] = bEnDe
        i += 1
        abTxData[i] = usSize >> 8
        i += 1
        abTxData[i] = usSize
        i += 1

        abTxData[i:i+usSize] = abInput[ulOutputOffset:ulOutputOffset+usSize]
#Buffer.BlockCopy(abInput, (int)ulOutputOffset, abTxData, i, usSize)
        abRxData = Transceive(abTxData)
        if abRxData == None:
            gsKseLastErrorCode = gsTransceiveLastErrorCode
            return None
        usLen = len(abRxData)
        if (usLen < 2):
            gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
            return None
        sRv = ((abRxData[0] << 8) | abRxData[1])
        if (((sRv == KSE_SUCCESS) and (usLen != usSize + 2)) or\
            ((sRv != KSE_SUCCESS) and (usLen != 2))):
            gsKseLastErrorCode = KSE_FAIL_UNEXPECTED_RESP_LEN
            return None
        if sRv != KSE_SUCCESS:
            gsKseLastErrorCode = sRv
            return None

#Buffer.BlockCopy(abRxData, 2, abOutput, (int)ulOutputOffset,usSize)
        abOutput[ulOutputOffset:ulOutputOffset+usSize] = abRxData[2:2+usSize]
        ulOutputOffset += usSize
        ulInputSize -= usSize
        if not ulInputSize > 0:
            break
    return abOutput


