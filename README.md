# PortScannerV1

A simple TCP port scanner written in Python using the built-in `socket` and `argparse` libraries.

## Features

* Scans common ports by default
* Allows you to specify custom ports
* Uses TCP connections to check whether ports are open or closed
* Simple command-line interface

## Usage

### Scan default ports

```bash
python port_scanner.py --ip 127.0.0.1
```

### Scan specific ports

```bash
python port_scanner.py --ip 127.0.0.1 --port 22 80 443
```

### Example

```text
[+] Port 22 is Open
[-] Port 80 is Closed
[-] Port 443 is Closed
```

## Requirements

* Python 3.x
* No external libraries required

## Disclaimer

This project was created for educational purposes and authorized security testing.

Only scan computers, networks, and systems that you own or have explicit permission to test.

