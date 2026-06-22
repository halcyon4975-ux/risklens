from app.scanner.scanner import scan_ports


results = scan_ports(
    "127.0.0.1",
    [80, 5000, 8080]
)


print(results)