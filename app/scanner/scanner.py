import socket


def scan_port(ip, port):
    """
    Checks if a port is open on a target IP.
    """

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.settimeout(1)

    try:
        result = sock.connect_ex((ip, port))

        if result == 0:
            return True

        return False

    except socket.error:
        return False

    finally:
        sock.close()



def scan_ports(ip, ports):
    """
    Scan multiple ports on a target.
    """

    results = []

    for port in ports:

        is_open = scan_port(ip, port)

        if is_open:
            results.append({
                "port": port,
                "state": "OPEN"
            })

    return results