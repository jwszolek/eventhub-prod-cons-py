from azure.eventhub import EventHubProducerClient, EventData

# Event Hub connection parameters
CONNECTION_STR = "Endpoint=sb://bda2023.servicebus.windows.net/;SharedAccessKeyName=jwszol-user;SharedAccessKey=vQSz4FlZvyx5jPZsbjsv95ElXkM0VFbOW+AEhHGgPkw="
EVENTHUB_NAME = "jwszol"

# Create an Event Hubs producer client
producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME)


    # event_data_batch.add(EventData('Single message'))
    # producer.send_batch(event_data_batch)

# Create an EventData


# Send the EventData
with producer:
    for i in range(5):
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData("Hello, Azure Event Hubs! -- "+str(i)))
        producer.send_batch(event_data_batch)
        print("msg no = " + str(i))