from app import db

from app.models.scan import Scan
from app.models.scan_result import ScanResult

from app.scanner.scanner import scan_ports
from app.risk_engine.rules import get_risk_info


def run_scan(scan_id, ip):

    scan = Scan.query.get(scan_id)

    if not scan:
        return None


    scan.status = "RUNNING"
    db.session.commit()


    ports = [
        21,
        22,
        23,
        25,
        53,
        80,
        443,
        3306,
        3389,
        5000
    ]

    
    results = scan_ports(ip, ports)

    scan.total_ports_scanned = len(ports)
    scan.open_ports_count = len(results)


    for result in results:

        risk = get_risk_info(
            result["port"]
        )


        scan_result = ScanResult(
            scan_id=scan.id,
            port=result["port"],
            service=risk["service"],
            protocol="TCP",
            state=result["state"],
            severity=risk["severity"],
            recommendation=risk["recommendation"]
        )


        db.session.add(scan_result)


    scan.status = "COMPLETED"

    db.session.commit()


    return scan