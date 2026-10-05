import argparse
import socket

parse = argparse.ArgumentParser()

parse.add_argument("--ip", type=str, required=True, help="Ip to Scan for Open ports (Required)")
parse.add_argument("--port", type=int, required=False, nargs="+",  help="Custom Ports to Scan (Optional)")

args = parse.parse_args()

default_ports = [20,21,22,23,25,53,67,69,80,110,111,123,135,137,138,139,143,161,162,443,445,500,514,520,631,993]

def main(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    response = sock.connect_ex((ip, port))

    if response == 0:
        print(f"[+] Port {port} is Open")
    else:
        print(f"[-] Port {port} is Closed")

    sock.close()


def default():

    if args.port is None:
      for port in default_ports:
        main(args.ip, port)

    else:
       for port in args.port:
          main(args.ip, port)
        
if __name__ == "__main__":
 
 default()