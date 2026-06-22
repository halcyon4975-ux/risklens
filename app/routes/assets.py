from flask import Blueprint, request, jsonify
from ipaddress import ip_address as validate_ip

from app import db
from app.models.asset import Asset

assets_bp = Blueprint("assets", __name__)


@assets_bp.route("/assets", methods=["POST"])
def create_asset():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body must contain JSON"
        }), 400

    name = data.get("name")
    ip_address = data.get("ip_address")
    description = data.get("description", "")

    if not name:
        return jsonify({
            "error": "Asset name is required"
        }), 400

    if not ip_address:
        return jsonify({
            "error": "IP address is required"
        }), 400

    try:
        validate_ip(ip_address)
    except ValueError:
        return jsonify({
            "error": "Invalid IP address"
        }), 400

    existing_asset = Asset.query.filter_by(
        ip_address=ip_address
    ).first()

    if existing_asset:
        return jsonify({
            "error": "Asset with this IP address already exists"
        }), 409

    asset = Asset(
        name=name,
        ip_address=ip_address,
        description=description
    )

    db.session.add(asset)
    db.session.commit()

    return jsonify({
        "message": "Asset created successfully",
        "asset": {
            "id": asset.id,
            "name": asset.name,
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
            "ip_address": asset.ip_address,
            "description": asset.description,
            "created_at": asset.created_at.isoformat()
        })

    return jsonify(results), 200