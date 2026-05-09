import asyncio
import logging
from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mission_control")

class MissionController:
    def __init__(self, connection_url="udp://:14540"):
        self.connection_url = connection_url
        self.drone = System()

    async def connect(self):
        logger.info("Connecting to drone...")
        await self.drone.connect(system_address=self.connection_url)

        async for state in self.drone.core.connection_state():
            if state.is_connected:
                logger.info("Drone connected")
                break

    async def upload_mission(self):
        mission_items = [
            MissionItem(
                47.397750, 8.545594, 10,
                10,
                True,
                float('nan'),
                float('nan'),
                MissionItem.CameraAction.NONE,
                float('nan'),
                float('nan'),
                float('nan'),
                float('nan'),
                float('nan')
            ),
            MissionItem(
                47.397850, 8.545694, 10,
                10,
                True,
                float('nan'),
                float('nan'),
                MissionItem.CameraAction.NONE,
                float('nan'),
                float('nan'),
                float('nan'),
                float('nan'),
                float('nan')
            )
        ]

        mission_plan = MissionPlan(mission_items)

        logger.info("Uploading mission")
        await self.drone.mission.upload_mission(mission_plan)

    async def start_mission(self):
        logger.info("Arming drone")
        await self.drone.action.arm()

        logger.info("Starting mission")
        await self.drone.mission.start_mission()

        async for progress in self.drone.mission.mission_progress():
            logger.info(
                f"Mission progress: {progress.current}/{progress.total}"
            )

            if progress.current == progress.total:
                logger.info("Mission completed")
                break

async def main():
    controller = MissionController()

    await controller.connect()
    await controller.upload_mission()
    await controller.start_mission()

if __name__ == '__main__':
    asyncio.run(main())
