import asyncio
from mavsdk import System
from mavsdk.offboard import PositionNedYaw

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for connection...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Connected")
            break

    await drone.action.arm()
    await drone.action.takeoff()

    await asyncio.sleep(5)

    await drone.offboard.set_position_ned(
        PositionNedYaw(5.0, 0.0, -3.0, 0.0)
    )

    await drone.offboard.start()

    await asyncio.sleep(10)

    await drone.offboard.stop()

    await drone.action.land()

if __name__ == '__main__':
    asyncio.run(run())
