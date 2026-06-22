from app import db
from app.models.scan import Scan


def create_scan(asset_id):
    """
    Creates a new scan record and returns it.
    """

    scan = Scan(
        asset_id=asset_id,
        status="PENDING"
    )

    db.session.add(scan)
    db.session.commit()

    return scan