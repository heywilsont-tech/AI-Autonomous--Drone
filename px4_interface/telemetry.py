import asyncio
from mavsdk import System

async def print_telemetry():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone connection...")

    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Connected to drone")
            break

    async for position in drone.telemetry.position():
        print(
            f"Latitude: {position.latitude_deg}, "
            f"Longitude: {position.longitude_deg}, "
            f"Altitude: {position.relative_altitude_m}"
        )

if __name__ == '__main__':
    asyncio.run(print_telemetry())
