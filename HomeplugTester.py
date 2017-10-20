import HelperMac
import HelperHomeplug
import HelperDiagram
import RawPacketGenerator
import sys

mMac = HelperMac.get()
aMac = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]

mPacketGenerator = RawPacketGenerator.PacketGenerator(HelperHomeplug.get_eth_type_int(), sys.argv[1])

mPacketGenerator.psend(mMac, aMac, HelperHomeplug.get_eth_type_list(), HelperHomeplug.getCCoReq())

mPacketGenerator.srecv()

# mPacketGenerator.psend(mMac, aMac, HelperHomeplug.get_eth_type_list(), HelperHomeplug.getDevAttrReq())
# mPacketGenerator.psend(mMac, aMac, HelperHomeplug.get_eth_type_list(), HelperHomeplug.getDevVerReq())
# mPacketGenerator.psend(mMac, aMac, HelperHomeplug.get_eth_type_list(), HelperHomeplug.getNwInfReq())
# mPacketGenerator.psend(mMac, aMac, HelperHomeplug.get_eth_type_list(), HelperHomeplug.getEthSetReq())

mNetworkInformations = []
mBridgeInformations = []

for aMac in mPacketGenerator.m_stations:
    mPacketGenerator.psend(mMac, list(aMac), HelperHomeplug.get_eth_type_list(), HelperHomeplug.getNwInfReq())
    mNetworkInformations.append(HelperHomeplug.NetworkInformation(mPacketGenerator.precv(), aMac))
    mPacketGenerator.psend(mMac, list(aMac), HelperHomeplug.get_eth_type_list(), HelperHomeplug.getBrInfReq())
    mBridgeInformations.append(HelperHomeplug.BridgeInformation(mPacketGenerator.precv()))


myD = HelperDiagram.NodeDiagram()

for i in range(0, len(mNetworkInformations)):
    # print(mNetworkInformations[i].get())
    myD.addNode(["#" + str(mNetworkInformations[i].getRaw()[0]) +
                 ": " + HelperMac.getVendorMac(mNetworkInformations[i].getRaw()[3]),
                 mBridgeInformations[i].get()[3]
                 ])

myD.drawDiagram()

# Ethernet
# DST Byte 0:5
# SRC Byte 6:11
# ETHTYPE Byte 12:13
# Homeplug-AV
# VERS Byte 14
# TYPE Byte 15
# ROLE Byte 16
# FRAG Byte 17:18
# STC Byte 19
