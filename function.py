import json
import ipaddress

"""

    Lambda expects IP address passed in the API's header:

    ip:192.168.1.1

"""

def lambda_handler(event, context):

    # Parse event to get the ip
    ip = event["headers"]
    ip = (ip['ip']).strip()
    
    try:
        value = ipaddress.ip_address(ip).is_private
    except:
        value = False
    
    sendback = {
      "isBase64Encoded": False,
      "statusCode": 200,
      "headers": { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
      "body": value
      }
      
    return sendback
