import asyncio
from websockets.client import connect


async def main() -> None:
    uri = "ws://localhost:8765"
    async with connect(uri) as ws_connection:
        while True:
            msg = input("- msg ->>> ")
            if msg == ":quit":
                break

            await ws_connection.send(msg)

            recieved_msg = await ws_connection.recv()
            print(f">>> {recieved_msg}")


if __name__ == "__main__":
    asyncio.run(main())
