"""Deliberately incomplete input for a completion evaluation."""


def export_rows(rows):
    lines = []
    for row in rows:
        lines.append(",".join(row))
    if not lines:
        return ""
    return "\n".join(lines) + "\n"
