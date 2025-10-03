import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

class KafkaClient:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = None
        self.consumer = None

    async def start_producer(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        await self.producer.start()

    async def send(self, topic, value):
        await self.producer.send_and_wait(topic, value)

    async def start_consumer(self, topic):
        self.consumer = AIOKafkaConsumer(topic, bootstrap_servers=self.bootstrap_servers)
        await self.consumer.start()

    async def consume(self):
        async for message in self.consumer:
            print(f"Consumed: {message.value}")

    async def shutdown(self):
        await self.producer.stop()
        await self.consumer.stop()
