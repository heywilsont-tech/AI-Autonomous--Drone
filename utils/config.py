CONFIG = {
    'drone': {
        'connection_url': 'udp://:14540',
        'takeoff_altitude': 3.0,
        'safe_distance': 2.0
    },
    'camera': {
        'source': 0,
        'resolution': [640, 480]
    },
    'ai_model': {
        'yolo_model': 'yolov8n.pt'
    },
    'simulation': {
        'world': 'gz_x500'
    }
}
