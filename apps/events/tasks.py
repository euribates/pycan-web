import base64
import os

import sendgrid
from django.conf import settings
from django.template import loader
from django.utils import timezone
from django_rq import job
from sendgrid.helpers.mail import Attachment, Content, Email, Mail

from apps.commons.filters import as_markdown
from apps.organizations.models import Organization


def create_ticket_message(ticket):
    event = ticket.article.event
    tmpl = loader.get_template("events/email/ticket_message.md")
    subject = "Entrada para {}".format(event.name)
    body = tmpl.render(
        {
            "ticket": ticket,
            "article": ticket.article,
            "category": ticket.article.category,
            "event": event,
        }
    )
    organization = Organization.load_main_organization()
    mail = Mail(
        from_email=Email(organization.email, organization.name),
        subject=subject,
        to_email=Email(ticket.customer_email),
        content=Content("text/html", as_markdown(body)),
    )

    attachment = Attachment()
    pdf_filename = ticket.as_pdf()
    with open(pdf_filename, "rb") as f:
        data = f.read()
    attachment.content = base64.b64encode(data).decode()
    attachment.type = "application/pdf"
    attachment.filename = "ticket.pdf"
    attachment.disposition = "attachment"
    mail.add_attachment(attachment)
    return mail


@job
def send_ticket(ticket, force=False):
    ticket.as_pdf(force)
    msg = create_ticket_message(ticket)
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    response = sg.client.mail.send.post(request_body=msg.get())
    if response.status_code >= 400:
        error_msg = []
        error_msg.append("STATUS CODE: {}".format(response.status_code))
        error_msg.append("RESPONSE HEADERS: {}".format(response.headers))
        error_msg.append("RESPONSE BODY: {}".format(response.body))
        raise Exception(os.linesep.join(error_msg))
    ticket.send_at = timezone.now()
    ticket.save()


# --[ Call for papers ]------------------------------------------------


def create_proposal_acknowledge(proposal):
    event = proposal.event
    tmpl = loader.get_template("events/email/proposal_acknowledge.md")
    subject = "Acuse de recibo de su propuesta para {}".format(event.name)
    body = tmpl.render(
        {
            "event": event,
            "proposal": proposal,
        }
    )
    organization = Organization.load_main_organization()
    mail = Mail(
        from_email=Email(organization.email, organization.name),
        subject=subject,
        to_email=Email(proposal.email),
        content=Content("text/html", as_markdown(body)),
    )
    return mail


@job
def send_proposal_acknowledge(proposal):
    msg = create_proposal_acknowledge(proposal)
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    response = sg.client.mail.send.post(request_body=msg.get())
    if response.status_code >= 400:
        error_msg = []
        error_msg.append("STATUS CODE: {}".format(response.status_code))
        error_msg.append("RESPONSE HEADERS: {}".format(response.headers))
        error_msg.append("RESPONSE BODY: {}".format(response.body))
        raise Exception(os.linesep.join(error_msg))
    # ticket.send_at = timezone.now()
    # ticket.save()


def create_proposal_notification(proposal):
    event = proposal.event
    tmpl = loader.get_template("events/email/proposal_notification.md")
    subject = "Nueva propuesta para {}".format(event.name)
    body = tmpl.render(
        {
            "event": event,
            "proposal": proposal,
        }
    )
    organization = Organization.load_main_organization()
    mail = Mail(
        from_email=Email(organization.email, organization.name),
        subject=subject,
        to_email=Email(organization.email),
        content=Content("text/html", as_markdown(body)),
    )
    return mail


@job
def send_proposal_notification(proposal):
    msg = create_proposal_notification(proposal)
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    response = sg.client.mail.send.post(request_body=msg.get())
    if response.status_code >= 400:
        error_msg = []
        error_msg.append("STATUS CODE: {}".format(response.status_code))
        error_msg.append("RESPONSE HEADERS: {}".format(response.headers))
        error_msg.append("RESPONSE BODY: {}".format(response.body))
        raise Exception(os.linesep.join(error_msg))
    # ticket.send_at = timezone.now()
    # ticket.save()
