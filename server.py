import asyncio
from websockets.server import serve, WebSocketServerProtocol
from datetime import datetime


async def hello_many(wsserver: WebSocketServerProtocol) -> None:
    # for every incomming data stream from the same ws connection
    # await for it, then just echo the data back
    client_id = wsserver.id
    print(f"connection made with: {client_id}")

    async for message in wsserver:
        print(f"<< {message}")

        await wsserver.send(message)
        print(f">> {message}")

    print(f"connection closed with: {client_id}.")
    print("waiting for other connection")


async def tell_time(ws: WebSocketServerProtocol) -> None:
    while True:
        now = datetime.now().time().isoformat()
        print(f"current time: {now}")
        await ws.send(now)

        await asyncio.sleep(2)


async def main() -> None:
    # create a connection handler to serve

    async with serve(tell_time, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
