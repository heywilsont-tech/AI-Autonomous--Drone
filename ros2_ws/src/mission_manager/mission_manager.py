import asyncio
import logging
from mavsdk import System
from mavsdk.offboard import PositionNedYaw

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mission_manager")

class MissionManager:
    def __init__(self):
        self.drone = System()
        self.waypoints = [
            (0, 0, -3, 0),
            (5, 0, -3, 0),
            (5, 5, -3, 90),
            (0, 5, -3, 180)
        ]

    async def connect(self):
        logger.info("Connecting to drone...")
        await self.drone.connect(system_address="udp://:14540")

        async for state in self.drone.core.connection_state():
            if state.is_connected:
                logger.info("Drone connected")
                break

    async def execute_mission(self):
        logger.info("Arming drone")
        await self.drone.action.arm()

        logger.info("Taking off")
        await self.drone.action.takeoff()

        await asyncio.sleep(8)

        await self.drone.offboard.set_position_ned(
            PositionNedYaw(0, 0, -3, 0)
        )

        await self.drone.offboard.start()

        for idx, waypoint in enumerate(self.waypoints):
            north, east, down, yaw = waypoint

            logger.info(f"Moving to waypoint {idx + 1}")

            await self.drone.offboard.set_position_ned(
                PositionNedYaw(north, east, down, yaw)
            )

            await asyncio.sleep(5)

        logger.info("Stopping offboard mode")
        await self.drone.offboard.stop()

        logger.info("Landing drone")
        await self.drone.action.land()

async def main():
    manager = MissionManager()

    await manager.connect()
    await manager.execute_mission()

if __name__ == '__main__':
    asyncio.run(main())
