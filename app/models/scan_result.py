from app import db


class ScanResult(db.Model):
    __tablename__ = "scan_results"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    scan_id = db.Column(
        db.Integer,
        db.ForeignKey("scans.id"),
        nullable=False
    )

    port = db.Column(
        db.Integer,
        nullable=False
    )

    service = db.Column(
        db.String(50),
        nullable=False
    )

    protocol = db.Column(
        db.String(10),
        nullable=False,
        default="TCP"
    )

    state = db.Column(
        db.String(20),
        nullable=False
    )

    severity = db.Column(
        db.String(20),
        nullable=False
    )

    recommendation = db.Column(
        db.Text,
        nullable=True
    )