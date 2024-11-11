from flask import request, jsonify
from marshmallow import ValidationError
from app.blueprints.service_tickets import service_tickets_bp
from app.models import ServiceTicket
from .schemas import service_ticket_schema, service_tickets_schema, input_service_ticket_schema
from datetime import date, datetime, timedelta
from app.models import db
from sqlalchemy import select


@service_tickets_bp.route("/", methods=["POST"])
def create_service_ticket():
    try:
        service_ticket_data = input_service_ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_service_ticket = ServiceTicket(service_ticket_data=datetime.now(), service_date= datetime.now() + timedelta(days = 7), customer_id= service_ticket_data['customer_id'])
    db.session.add(new_service_ticket)
    db.session.commit()

    return service_ticket_schema.jsonify(new_service_ticket), 201

@service_tickets_bp.route("/", methods = ['GET'])
def get_service_ticket():
    query = select(ServiceTicket)
    service_ticket = db.session.execute(query).scalars().all()

    return service_ticket_schema(service_ticket)

