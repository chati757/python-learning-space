'''
ยังไม่ได้สร้าง mqtt_client และเชื่อมต่อ (เป็นเพียงตัวอย่างการส่งหลังเชื่อมต่อแล้วเท่านั้น)
'''

if client.is_connected():
    info = client.publish(TOPIC, "ping", qos=1)  # ใช้ QoS 1 ขึ้นไปเพื่อให้มี ACK
    if info.rc != mqtt.MQTT_ERR_SUCCESS:
        print("❌ Failed to send publish command:", info.rc)
    else:
        info.wait_for_publish()  # รอให้ส่งจริง
        if info.is_published():
            print("✅ Message published and acknowledged")
        else:
            print("⚠️ Publish command sent, but no ACK yet (may be dropped)")
else:
    print("❗ Client not connected. Skip publish.")
