import asyncio
from mavsdk import System
from mavsdk.offboard import VelocityBodyYawspeed

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Connected to drone")
            break

    await drone.action.arm()
    await drone.action.takeoff()

    await asyncio.sleep(5)

    print("Starting offboard mode")
    await drone.offboard.set_velocity_body(
        VelocityBodyYawspeed(1.0, 0.0, 0.0, 0.0)
    )

    await drone.offboard.start()

    await asyncio.sleep(10)

    await drone.offboard.stop()

    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())
