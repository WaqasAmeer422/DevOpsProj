import pika
import time

# Use the container name 'rabbit-srv' as the host
try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbit-srv')
    )
    channel = connection.channel()

    # The queue 'rfid_scans' is already created by your JSON!
    channel.basic_publish(
        exchange='',
        routing_key='TestQueue',
        body='{"vehicle_id": "ICT-2026", "timestamp": "17:15"}'
    )

    print(" [x] RFID Scan Sent to RabbitMQ!")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")