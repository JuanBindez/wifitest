# cli.py
from wifitest import WifiTest
import argparse

def main():
    parser = argparse.ArgumentParser(description="Wifitest CLI")
    parser.add_argument("operation", choices=["scan", "bruteforce", "events"], help="Operation to perform: scan, bruteforce, or events")
    parser.add_argument("--ssid", help="SSID of the target Wi-Fi network (required for bruteforce operation)")
    parser.add_argument("--wordlist", help="Path to the wordlist file (required for bruteforce operation)")

    args = parser.parse_args()

    wifi_test = WifiTest()

    if args.operation == "scan":
        wifi_test.scan()
    elif args.operation == "bruteforce":
        if not args.ssid or not args.wordlist:
            parser.error("--ssid and --wordlist are required for bruteforce operation")
        wifi_test.bruteforce(args.ssid, args.wordlist)
    elif args.operation == "events":
        wifi_test.events()

if __name__ == "__main__":
    main()