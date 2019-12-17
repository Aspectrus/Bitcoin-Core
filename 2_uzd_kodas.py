
import hashlib
from bitcoin.rpc import RawProxy
from binascii import unhexlify



def Endian(string):
        a = []
        for j in range(0, len(str(string)), 2):
            a.append(str(string[j:j+2]))
        a.reverse()
        return "".join(a)


p = RawProxy()

blockheight = int(input())
blockhash = p.getblockhash(blockheight)
block = p.getblockheader(blockhash)

version = Endian(block['versionHex'])
previousHash = Endian(block['previousblockhash'])
merkleRoot = Endian(block['merkleroot'])
time = Endian(hex(block['time'])[2:])
difficultyBits = Endian(block['bits'])
nonce = Endian(hex(block['nonce'])[2:])

header_bin = str(version + previousHash + merkleRoot + time + difficultyBits + nonce)

a = header_bin.decode('hex')


hash =  hashlib.sha256(hashlib.sha256(a).digest()).hexdigest()

result = Endian(hash)

print "Original hash: ", blockhash
print "Calculated hash: ", result
