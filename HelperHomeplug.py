import HelperMac

def get_eth_type_list():
    return [0x88, 0xe1]

def get_eth_type_int():
    return 0x88e1

def getVendorOUI():
    return [0x00, 0xb0, 0x52]

def getCCoReq():
    return [0x01, 0x14]

def getDevAttrReq():
    return [0x00, 0x68, 0xa0] + getVendorOUI()

def getDevVerReq():
    return [0x00, 0x00, 0xa0] + getVendorOUI()

def getNwInfReq():
    return [0x01, 0x38, 0xa0, 0x00, 0x00] + getVendorOUI()

def getBrInfReq():
    return [0x01, 0x20, 0x60, 0x00, 0x00]

def getEthSetReq():
    return [0x00, 0x6c, 0xa0] + getVendorOUI()

class NetworkInformation:
    cco = []

    def __init__(self, data, mMac):
        self.m_identifier = data[38]
        self.m_numofsta = data[54]
        self.m_sta = []
        self.m_sta_ven = []
        self.m_mac = mMac
        self.cco = data[44:50]
        for i in range(0, self.m_numofsta):
            start = 60 + (i * 24)
            self.m_sta.append(data[start:start + 6])
            self.m_sta_ven.append(
                HelperMac.checkVendor(self.m_sta[i]) + "_" + HelperMac.rawMacToString(self.m_sta[i][3:6])
            )

    def get(self):
        return ["I am #" + str(self.m_identifier) + " and i am connected to " + str(self.m_numofsta) + " Stations.",
                "My CCo is " + (HelperMac.checkVendor(self.cco) + "_" + HelperMac.rawMacToString(self.cco[3:6])) + ".",
                "My MAC is " + (HelperMac.checkVendor(self.m_mac) + "_" + HelperMac.rawMacToString(self.m_mac[3:6])) + ".",
                self.m_sta_ven
                ]

    def getRaw(self):
        return [self.m_identifier, self.m_numofsta, self.cco, self.m_mac, self.m_sta, self.m_sta_ven]

class BridgeInformation:
    def __init__(self, data):
        self.m_identifier = data[20]
        self.m_numofdev = data[21]
        self.m_sta = []
        self.m_sta_ven = []
        for i in range(0, self.m_numofdev):
            start = 22 + (i * 6)
            self.m_sta.append(data[start:start + 6])
            self.m_sta_ven.append(
                HelperMac.checkVendor(self.m_sta[i]) + "_" + HelperMac.rawMacToString(self.m_sta[i][3:6])
            )

    def get(self):
        return [self.m_identifier, self.m_numofdev, self.m_sta, self.m_sta_ven]

# Homeplug-AV
# VERS Byte 14
# TYPE Byte 15
# ROLE Byte 16
# FRAG Byte 17:18
# STC Byte 19
