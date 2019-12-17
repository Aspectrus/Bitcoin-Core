from bitcoin.rpc import RawProxy

p = RawProxy()

txid = raw_input()

raw_tx = p.getrawtransaction(txid)

decoded_tx = p.decoderawtransaction(raw_tx)

i = 0
spent = 0
recieved = 0



for out in decoded_tx['vout']:
   recieved = recieved + out['value']

txids = []
vouts = []
for inputs in decoded_tx['vin']:
    txids.append(inputs['txid'])
    vouts.append(inputs['vout'])




for tx in txids:
    raw_tx = p.getrawtransaction(tx)
    decoded_tx = p.decoderawtransaction(raw_tx)

    for out in decoded_tx['vout']:
        if out['n'] == vouts[i]:
            spent = spent + out['value']
    i = i + 1



print ("spent : "+str(spent))
print ("recieved : "+str(recieved))
print ("fee is : "+str(spent-recieved))
