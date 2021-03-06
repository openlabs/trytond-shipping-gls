# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from shipment import Package, ShipmentOut, GenerateShippingLabel, ShippingGLS, \
    Address
from carrier import Carrier
from sale import Sale


def register():
    Pool.register(
        Carrier,
        Sale,
        Package,
        ShipmentOut,
        ShippingGLS,
        Address,
        module='shipping_gls', type_='model'
    )

    Pool.register(
        GenerateShippingLabel,
        module='shipping_gls', type_='wizard'
    )
