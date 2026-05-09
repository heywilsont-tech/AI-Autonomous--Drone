import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('AI_Autonomous_UAV')

if __name__ == '__main__':
    logger.info('Logger initialized successfully')
