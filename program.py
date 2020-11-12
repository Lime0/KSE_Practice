import kse100u
import sub_module

cabDsSystemTitle = bytes([0x4B, 0x53, 0x45, 0x00, 0x00, 0x00, 0x00, 0x01])

AES_PLAIN = bytearray([0x4c, 0x6f, 0x72, 0x65, 0x6d, 0x20, 0x69, 0x70, 0x73, 0x75, 0x6d, 0x20, 0x64, 0x6f, 0x6c, 0x6f, 0x72, 0x20, 0x73,\
               0x69, 0x74, 0x20, 0x61, 0x6d, 0x65, 0x74, 0x2c, 0x20, 0x63, 0x6f, 0x6e, 0x73, 0x65, 0x63, 0x74, 0x65, 0x74, 0x75,\
               0x72, 0x20, 0x61, 0x64, 0x69, 0x70, 0x69, 0x73, 0x63, 0x69, 0x6e, 0x67, 0x20, 0x65, 0x6c, 0x69, 0x74, 0x2e, 0x20,\
               0x41, 0x6c, 0x69, 0x71, 0x75, 0x61, 0x6d, 0x20, 0x6c, 0x69, 0x67, 0x75, 0x6c, 0x61, 0x20, 0x73, 0x61, 0x70, 0x69,\
               0x65, 0x6e, 0x2c, 0x20, 0x72, 0x75, 0x74, 0x72, 0x75, 0x6d, 0x20, 0x73, 0x65, 0x64, 0x20, 0x76, 0x65, 0x73, 0x74,\
               0x69, 0x62, 0x75, 0x6c, 0x75, 0x6d, 0x20, 0x65, 0x67, 0x65, 0x74, 0x2c, 0x20, 0x72, 0x68, 0x6f, 0x6e, 0x63, 0x75,\
               0x73, 0x20, 0x61, 0x63, 0x20, 0x65, 0x72, 0x61, 0x74, 0x2e, 0x20, 0x41, 0x6c, 0x69, 0x71, 0x75, 0x61, 0x6d, 0x20,\
               0x65, 0x72, 0x61, 0x74, 0x20, 0x76, 0x6f, 0x6c, 0x75, 0x74, 0x70, 0x61, 0x74, 0x2e, 0x20, 0x53, 0x65, 0x64, 0x20,\
               0x63, 0x6f, 0x6e, 0x76, 0x61, 0x6c, 0x6c, 0x69])

def CheckFailure(strFunc, sRv):
    if sRv != kse100u.KSE_SUCCESS:
        kse100u.DebugPrintErrStr(strFunc)
        raise Exception()

def main():
    print("\n")
    print("=== Main 1 =================")
    print("============================")
    val = kse100u.PowerOn()
    kse100u.gfEnableDebugPrint = True
    sRv = val[0]
    _valid_result = val[1]
    
    CheckFailure("PowerOn()", sRv) # no timer
    if (_valid_result[0][2] & 0x80) == 0x80:
        sRv = kse100u.Clear(kse100u.CLEAR_ALL)
        CheckFailure("Clear(CLEAR_ALL)",sRv)
        sRv = kse100u.IssueInit(cabDsSystemTitle)
        CheckFailure("IssueInit()",sRv)
        sRv = kse100u.IssueFinal()
        CheckFailure("IssueFinal()", sRv)
        print("Sample Chip is reissued")
        print("\n")
        sRv = kse100u.PowerOff()
        CheckFailure("PowerOff()", sRv)
        
        val = kse100u.PowerOn()
        sRv = val[0]
        CheckFailure("PowerOn()", sRv)
    print("PowerOn() : Success...\n")
    tmp_str = 0
    tmp_str = sub_module.byte_in_hex(_valid_result[0])#_valid_result[0]=outabVer
    print("  * Version          : {0}.{1}.{2}\n".format(tmp_str[0],tmp_str[1],tmp_str[2]))
    if _valid_result[1] == kse100u.LC_MANUFACTURED:
        print("  * Life Cycle       : MANUFACTURED\n")
    elif _valid_result[1] == kse100u.LC_ISSUED:
        print("  * Life Cycle       : ISSUED\n")
    elif _valid_result[1] == kse100u.LC_TERMINATED:    
        print("  * Life Cycle       : TERMINATED\n")
    else:
        print("  * Life Cycle       : Unknown\n")
    tmp_str = sub_module.byte_in_hex(_valid_result[9])#_valid_result[9]=outabChipSerial
    print("  * Chip Serial      : {0}{1}{2}{3}{4}{5}{6}{7}\n".format(tmp_str[0],tmp_str[1],tmp_str[2],tmp_str[3],\
                                                                   tmp_str[4],tmp_str[5],tmp_str[6],tmp_str[7]))
    tmp_str = sub_module.byte_in_hex(_valid_result[2])#_valid_result[2]=outabSystemTitle
    abManufacturer = bytearray(3)
    abManufacturer = (_valid_result[2][0:3]).decode("ascii")
    print("  * System Title     : {0}{1}{2}{3}{4}{5}{6}{7} {8}".format(tmp_str[0],tmp_str[1],tmp_str[2],tmp_str[3],\
                                                                     tmp_str[4],tmp_str[5],tmp_str[6],tmp_str[7], \
                                                                    abManufacturer + ''.join(tmp_str[4:8])))
    if _valid_result[3] == kse100u.VC_DISABLED:#_valid_result[3]=outbVcType
        print("\n  * Verify code type : Disabled\n")
    elif _valid_result[3] <= kse100u.VC_TYPE_4:
        print("  * Verify code type : {0}\n".format(_valid_result[3][0]))
    else:
        print("  * Verify code type : Unknown\n")
    print("  * MaxVcRetryCount  : {0}\n".format(_valid_result[4]))#_valid_result[4]=outbMaxVcRetryCount
    print("  * MaxKcmvpKeyCount : {0}\n".format(_valid_result[5]))#_valid_result[5]=outusMaxKcmvpKeyCount
    print("  * MaxCertCount     : {0}\n".format(_valid_result[6]))#_valid_result[6]=outusMaxCertCount
    print("  * MaxIoDataSize    : {0}\n".format(_valid_result[7]))#_valid_result[7]=outusMaxIoDataSize
    print("  * FileSize         : {0}\n".format(_valid_result[8]))#_valid_result[8]=outusInfoFileSize
    print("\n")
    print("=== KCMVP Crypto Algorithms Test =================\n")
    print("==============================")
    print("\n\n")
    print("# DRBG -------------------------------------------\n")
    print("------------------------------\n")
    
    print("#AES ECB TEST-------------------------------------\n")
    kse100u.KcmvpGenerateKey(0x40, 2, 0)
    AES_ENCODE = kse100u.KcmvpEcb(AES_PLAIN,0x40,2,0,0x40)
    AES_DECODE = kse100u.KcmvpEcb(AES_ENCODE,0x40,2,1,0x40)
    print("Plain Txt : {0}\n".format(AES_PLAIN))
    print("\n")
    print("Encoded Txt : {0}\n".format(AES_ENCODE))
    print("\n")
    print("Decoded Txt : {0}\n".format(AES_DECODE))
    
    
    
  
    #_valid_result[0]=outabVer
    #_valid_result[1]=outbLifeCycle
    #_valid_result[2]=outabSystemTitle
    #_valid_result[3]=outbVcType
    #_valid_result[4]=outbMaxVcRetryCount
    #_valid_result[5]=outusMaxKcmvpKeyCount
    #_valid_result[6]=outusMaxCertCount
    #_valid_result[7]=outusMaxIoDataSize
    #_valid_result[8]=outusInfoFileSize
    #_valid_result[9]=outabChipSerial
    #def
    
main()