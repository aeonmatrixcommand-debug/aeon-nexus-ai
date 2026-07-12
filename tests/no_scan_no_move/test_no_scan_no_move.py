from services.guardian.no_scan_no_move.runtime import NoScanNoMoveControl


def test_scan_control():
    assert NoScanNoMoveControl().validate(
        {"scanned": True}
    )["allowed"]

    assert not NoScanNoMoveControl().validate(
        {"scanned": False}
    )["allowed"]
