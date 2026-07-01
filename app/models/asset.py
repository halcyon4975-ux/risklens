from datetime import datetime

from app import db


class Asset(db.Model):
    __tablename__ = "assets"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )   
    
    target = db.Column(
    db.String(255),
    nullable=False
    )

    ip_address = db.Column(
        db.String(45),
        nullable=False,
        unique=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Asset {self.name}>"
    

    scans = db.relationship(
    "Scan",
    backref="asset",
    lazy=True,
    cascade="all, delete-orphan"
)