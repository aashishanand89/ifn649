import paho.mqtt.publish as publish
publish.single("ifn649", "hello world", hostname="18.142.96.176")
print("Done")
