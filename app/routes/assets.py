from flask import Blueprint, request, jsonify
from ipaddress import ip_address as validate_ip
import socket
from app import db
from app.models.asset import Asset

assets_bp = Blueprint("assets", __name__)


@assets_bp.route("/assets", methods=["POST"])
def create_asset():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must contain JSON"}), 400

    name = data.get("name")
    target = data.get("target")
   
    description = data.get("description", "")

    if not name:
        return jsonify({"error": "Asset name is required"}), 400

    if not target:
        return jsonify({"error": "Target is required"}), 400

    
    try:
    # If the target is already an IP address
       validate_ip(target)
       ip_address = target

    except ValueError:
    # Otherwise treat it as a domain name
        try:
            ip_address = socket.gethostbyname(target)
        except socket.gaierror:
            return jsonify({
            "error": "Invalid target. Enter a valid IP address or domain."
        }), 400 


    


    existing_asset = Asset.query.filter_by(
        ip_address=ip_address                  # ✅ now works correctly
    ).first()

    if existing_asset:
        return jsonify({"error": "Asset with this IP address already exists"}), 409

    asset = Asset(
        name=name,
        target=target,
        ip_address=ip_address,                 # ✅ now works correctly
        description=description
    )

    db.session.add(asset)
    db.session.commit()

    return jsonify({
        "message": "Asset created successfully",
        "asset": {
            "id": asset.id,
            "name": asset.name,
            "target": asset.target,
            "ip_address": asset.ip_address
        }
    }), 201

@assets_bp.route("/assets", methods=["GET"])
def get_assets():

    assets = Asset.query.all()

    results = []

    for asset in assets:
        results.append({
            "id": asset.id,
            "name": asset.name,
            "target": asset.target,
            "ip_address": asset.ip_address,
            "description": asset.description,
            "created_at": asset.created_at.isoformat()
        })

    return jsonify(results), 200