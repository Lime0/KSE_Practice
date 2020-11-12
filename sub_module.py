import binascii

def slicing_for_valid(abRxData): #for validify 'receive data' from USB 
        
    valid_result = {}
    
    outabVer = bytearray(3)
    outbLifeCycle = 0
    outabChipSerial = bytearray(8)
    outabSystemTitle = bytearray(8)
    outbVcType = 0
    outbMaxVcRetryCount = 0
    outusMaxKcmvpKeyCount = 0
    outusMaxCertCount = 0
    outusMaxIoDataSize = 0
    outusInfoFileSize = 0
    
    outabVer = abRxData[9:12]
    outbLifeCycle = abRxData[12]
    outabSystemTitle = abRxData[13:21]
    outbVcType = abRxData[21]
    outbMaxVcRetryCount = abRxData[22]
    outusMaxKcmvpKeyCount = ((abRxData[23]<<8) | abRxData[24])
    outusMaxCertCount = ((abRxData[25]<<8) | abRxData[26])
    outusMaxIoDataSize = ((abRxData[27]<<8) | abRxData[28])
    outusInfoFileSize = ((abRxData[29]<<8) | abRxData[30])
    outabChipSerial = abRxData[31:39]
        
    valid_result = {0: outabVer, 1: outbLifeCycle, 2: outabSystemTitle, 3: outbVcType, \
        4: outbMaxVcRetryCount, 5: outusMaxKcmvpKeyCount, 6: outusMaxCertCount, \
        7: outusMaxIoDataSize, 8: outusInfoFileSize, 9: outabChipSerial}
    return valid_result

def byte_in_hex(binType):
    hexType = binascii.hexlify(binType)
    Str = hexType.decode("ascii")
    Str_list = [0 for _ in range(int(len(Str)/2))]
    for i in range(len(Str_list)):
        Str_list[i] = Str[2*i : 2*(i+1)]
    return Str_list
    


    