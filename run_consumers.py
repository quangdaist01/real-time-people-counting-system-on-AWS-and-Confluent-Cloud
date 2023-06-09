#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore")
from src.params import *
from src.prediction_producer import ConsumeFrames

# Running logs for latency comparison, change the path as per your use case.
log_path = os.path.join(MAIN_PATH, LOG_DIR)

if not os.path.isdir(log_path):
    os.makedirs(log_path)

CONSUME_FRAMES = [ConsumeFrames(frame_topic=FRAME_TOPIC,
                                processed_frame_topic=PROCESSED_FRAME_TOPIC,
                                topic_partitions=SET_PARTITIONS,
                                scale=1,
                                rr_distribute=ROUND_ROBIN) for _ in
                  range(HM_PROCESSESS)]

if __name__ == "__main__":
    for c in CONSUME_FRAMES:
        c.start()

    for c in CONSUME_FRAMES:
        c.join()
