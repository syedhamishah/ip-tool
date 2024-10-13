#!/usr/bin/env python3
import requests
import argparse
import json
import socket

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "No reverse DNS entry found."

def main():
    parser = argparse.ArgumentParser(description='Ultimate IP Info Extractor Tool')
    parser.add_argument('ip', type=str, help='IP address to lookup')
    args = parser.parse_args()

    ip_info = get_ip_info(args.ip)

    if ip_info['status'] == 'fail':
        print(f"Error: {ip_info['message']}")
        return

    # Reverse DNS Lookup
    rdns = reverse_dns(args.ip)

    # Displaying comprehensive output
    output = {
        "IP Address": ip_info['query'],
        "Country": ip_info['country'],
        "Region": ip_info['regionName'],
        "City": ip_info['city'],
        "ZIP": ip_info['zip'],
        "Latitude": ip_info['lat'],
        "Longitude": ip_info['lon'],
        "ISP": ip_info['isp'],
        "Organization": ip_info['org'],
        "AS Number": ip_info['as'],
        "Timezone": ip_info['timezone'],
        "Reverse DNS": rdns
    }

    print(json.dumps(output, indent=4))

if __name__ == '__main__':
    main()
