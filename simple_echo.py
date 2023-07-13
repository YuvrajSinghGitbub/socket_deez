import asyncio
from websockets.server import serve, WebSocketServerProtocol


async def hello(websocket: WebSocketServerProtocol) -> None:
    # anything that returns `Coroutine` needs to be awaited

    name = await websocket.recv()  # await for the message to be recieved
    print(f"<<< {name}")

    greetings = f"hello {name}"
    await websocket.send(greetings)  # send the message as a greeting
    print(f">>> {greetings}")


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


async def main() -> None:
    # create a connection handler to serve

    async with serve(hello_many, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
