import logging
from io import StringIO

log_stream = StringIO()
handler = logging.StreamHandler(log_stream)
handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

logger = logging.getLogger("stream_test")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

logger.info("ทดสอบ log ลงใน stream1")
logger.info("ทดสอบ log ลงใน stream2")

import pdb;pdb.set_trace()

log_contents = log_stream.getvalue()
print("เนื้อหา log:", log_contents.strip())
