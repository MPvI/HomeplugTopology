
from socket import *

class PacketGenerator:

    def __init__(self, m_type, eth='eno1'):
        self.mSocket = socket(AF_PACKET, SOCK_RAW)
        self.mSocket.bind((eth, m_type))
        self.m_stations = []

    # Hexlist to bytearray and fill up to 60 bytes
    @staticmethod
    def pack(hexlist):
        m_packet = bytearray()
        for h in hexlist:
            m_packet.append(int(h))
        for i in range(len(m_packet), 60):
            m_packet.append(0)
        return m_packet

    # Send packed packet on own socket
    def psend(self, src, dst, eth_type, payload):
        return self.mSocket.send(self.pack(dst + src + eth_type + payload))

    # Receive handler for testing
    def srecv(self):
        m_resp = [self.mSocket.recv(256)]
        self.m_stations.append(m_resp[0][6:12])
        if m_resp[0][15] == int(0x0015):
            for i in range(1, m_resp[0][19] + 1):
                m_resp.append(self.mSocket.recv(60))
                self.m_stations.append(m_resp[i][6:12])
        return m_resp

    def precv(self):
        return self.mSocket.recv(256)
