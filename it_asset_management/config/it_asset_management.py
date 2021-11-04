def get_data():
    return [
        {
            "label": _("IT Asset Management"),
            "icon": "octicon octicon-book",
            "items": [
                {
                    "type": "doctype",
                    "name": "Laptop",
                    "label": _("Laptop"),
                    "description": _("Manage Laptop"),
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Peminjaman Laptop",
                    "label": _("Peminjaman Laptop"),
                    "description": _("Manage Peminjaman"),
                    # Not displayed on dropdown list action but on page after click on module
                    "onboard": 0,
                }
            ]
        }
    ]