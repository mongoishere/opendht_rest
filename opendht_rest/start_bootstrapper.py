import opendht, threading, time

node = opendht.DhtRunner()
node.run()
node.bootstrap("localhost", "4222")
time.sleep(1)

print("Putting in value...")
node.put(opendht.InfoHash.get("93DDCFD45CF466F58DE7C1C0E6664551"), opendht.Value(b'Hentai 1'))
print("Done")

results = node.get(opendht.InfoHash.get("93DDCFD45CF466F58DE7C1C0E6664551"))

import pdb; pdb.set_trace()