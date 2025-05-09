import asyncio
from bleak import BleakClient, BleakScanner

async def find_fridge():
    devices = await BleakScanner.discover()
    for d in devices:
        if "Vevor" in str(d.name):
            return d.address
    return None

async def connect_to_fridge():
    address = await find_fridge()
    if not address:
        print("Ingen Vevor kylbox hittades")
        return
    
    async with BleakClient(address) as client:
        print(f"Ansluten till kylbox på adress {address}")
        
        # Här kommer mer kod för att styra kylboxen
        # Detta är bara en grundstruktur

async def main():
    await connect_to_fridge()

if __name__ == "__main__":
    asyncio.run(main())