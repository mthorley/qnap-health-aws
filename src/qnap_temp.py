from qnapstats import QNAPStats
from pprint import pprint
import sys
import os
import json

class Config:
  pass

# Cloudwatch logstream 
def _log(config):
    qnap = QNAPStats(config.base_url, 8080, config.username, config.pwd)

    pprint(qnap.get_system_stats())
    pprint(qnap.get_system_health())
    pprint(qnap.get_smart_disk_health())
    pprint(qnap.get_volumes())
    pprint(qnap.get_bandwidth())
    
def main(argv):
    print("main")
    # get config from args
    config = Config()
    config.username = sys.argv[1]   # auditor
    config.pwd = sys.argv[2]        # pwd
    config.base_url = sys.argv[3]   # 192.168.1.18 (qnap259.local)

    _log(config)

def lambda_handler(event, context):
    print("lambda")
    # get config from env
    config = Config()
    config.username = os.environ['username']
    config.pwd = os.environ['pwd']
    config.base_url = os.environ['base_url']

    _log(config)

    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }

if __name__== "__main__":
    main(sys.argv[1:])
