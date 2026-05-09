import asyncio
import logging
from mavsdk import System
from mavsdk.offboard import PositionNedYaw

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("autonomous_patrol")

WAYPOINTS = [
    (0.0, 0.0, -3.0, 0.0),
    (5.0, 0.0, -3.0, 0.0),
    (5.0, 5.0, -3.0, 90.0),
    (0.0, 5.0, -3.0, 180.0),
]

async def wait_for_connection(drone: System):
    async for state in drone.core.connection_state():
        if state.is_connected:
            logger.info("Drone connected")
            return

async def wait_for_global_position(drone: System):
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            logger.info("Global position estimate acquired")
            return

async def run_patrol():
    drone = System()

    logger.info("Connecting to PX4 SITL...")
    await drone.connect(system_address="udp://:14540")

    await wait_for_connection(drone)
    await wait_for_global_position(drone)

    logger.info("Arming drone")
    await drone.action.arm()

    logger.info("Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(8)

    logger.info("Initializing offboard control")

    await drone.offboard.set_position_ned(
        PositionNedYaw(0.0, 0.0, -3.0, 0.0)
    )

    await drone.offboard.start()

    for index, waypoint in enumerate(WAYPOINTS):
        north, east, down, yaw = waypoint

        logger.info(
            f"Navigating to waypoint {index + 1}: "
            f"N={north}, E={east}, D={down}, Yaw={yaw}"
        )

        await drone.offboard.set_position_ned(
            PositionNedYaw(north, east, down, yaw)
        )

        await asyncio.sleep(6)

    logger.info("Mission complete")

    await drone.offboard.stop()

    logger.info("Landing")
    await drone.action.land()

    await asyncio.sleep(10)

if __name__ == "__main__":
    try:
        asyncio.run(run_patrol())
    except Exception as error:
        logger.error(f"Mission failed: {error}")
