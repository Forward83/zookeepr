from sqlalchemy import mapper, relation, backref

from tables import *
from domain import *
from zookeepr.model.core import Person
from zookeepr.model.registration import Registration

mapper(InvoiceItem, invoice_item)

mapper(Payment, payment)

mapper(PaymentReceived, payment_received,
       properties = {
            'payment': relation(Payment,
                                backref='payment_sent'
                       ),
            },
      )

mapper(Invoice, invoice,
       properties = {
    'person': relation(Person,
                       lazy=True,
                       backref=backref('invoices', cascade="all, delete-orphan"),
                       ),
#    'registration': relation(Registration,
#                             backref='invoice'),
    'items': relation(InvoiceItem,
                      backref='invoice',
                      cascade="all, delete-orphan",
                      ),
    'payment': relation(PaymentReceived, 
                        backref='payment_received'
                        ),
    },
       )
