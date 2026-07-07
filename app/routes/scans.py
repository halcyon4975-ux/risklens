from flask import Blueprint, jsonify

from app.models.scan import Scan

from app.models.asset import Asset
from app.services.scan_service import create_scan
from app.services.scanner_service import run_scan


scans_bp = Blueprint("scans", __name__)


@scans_bp.route("/scans", methods=["GET"])
def list_scans():

    scans = Scan.query.order_by(Scan.started_at.desc()).all()

    results = []

    for scan in scans:
        asset = Asset.query.get(scan.asset_id)
        results.append({
            "scan_id": scan.id,
            "uuid": scan.uuid,
            "asset_id": scan.asset_id,
            "asset_name": asset.name if asset else "Unknown asset",
            "status": scan.status,
            "started_at": scan.started_at.isoformat() if scan.started_at else None,
            "completed_at": scan.completed_at.isoformat() if scan.completed_at else None,
            "total_ports_scanned": scan.total_ports_scanned,
            "open_ports_count": scan.open_ports_count,
        })

    return jsonify(results), 200


@scans_bp.route("/assets/<int:asset_id>/scan", methods=["POST"])
def start_scan(asset_id):

    asset = Asset.query.get(asset_id)

    if not asset:
        return jsonify({
            "error": "Asset not found"
        }), 404


    scan = create_scan(asset_id)


    run_scan(
        scan.id,
        asset.ip_address
    )


    return jsonify({
        "message": "Scan completed",
        "scan_id": scan.id,
        "status": "COMPLETED"
    }), 201


@scans_bp.route("/scans/<int:scan_id>", methods=["GET"])
def get_scan(scan_id):

    scan = Scan.query.get(scan_id)

    if not scan:
        return jsonify({
            "error": "Scan not found"
        }), 404


    results = []

    for result in scan.results:
        results.append({
            "port": result.port,
            "service": result.service,
            "protocol": result.protocol,
            "state": result.state,
            "severity": result.severity,
            "recommendation": result.recommendation
        })


    return jsonify({
        "scan_id": scan.id,
        "uuid": scan.uuid,
        "asset_id": scan.asset_id,
        "status": scan.status,
        "total_ports_scanned": scan.total_ports_scanned,
        "open_ports_count": scan.open_ports_count,
        "results": results
    }), 200