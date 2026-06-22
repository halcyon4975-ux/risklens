from datetime import datetime
import uuid

from app import db




class Scan(db.Model):
    __tablename__ = "scans"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    uuid = db.Column(
        db.String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )

    asset_id = db.Column(
        db.Integer,
        db.ForeignKey("assets.id"),
        nullable=False
    )

    started_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    completed_at = db.Column(
        db.DateTime,
        nullable=True
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="PENDING"
    )

    total_ports_scanned = db.Column(
        db.Integer,
        default=0
    )

    open_ports_count = db.Column(
        db.Integer,
        default=0
    )

    error_message = db.Column(
        db.Text,
        nullable=True
    )


    results = db.relationship(
    "ScanResult",
    backref="scan",
    lazy=True,
    cascade="all, delete-orphan"
    )