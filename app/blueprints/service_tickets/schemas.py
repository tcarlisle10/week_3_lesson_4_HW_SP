from app.extensions import ma
from app.models import ServiceTicket
from marshmallow import fields

class ServiceTicketSchema(ma.Schema):
    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    service_ticket = fields.Integer(required=True)
    finish_date = fields.Integer(required=True)

    class Meta:
        fields = ('customer_id', 'service_date', 'service_desc', 'id')

service_ticket_schema = ServiceTicketSchema()
input_service_ticket_schema = ServiceTicketSchema(exclude=['service_date', 'service_desc'])
service_tickets_schema = ServiceTicketSchema(many=True)