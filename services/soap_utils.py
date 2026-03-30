import xml.etree.ElementTree as ET
from flask import Response

SOAP_NS = "http://schemas.xmlsoap.org/soap/envelope/"
SERVICE_NS = "http://microservices.example.com/soap"
WSDL_NS = "http://microservices.example.com/soap/wsdl"


def qname(ns, tag):
    return f"{{{ns}}}{tag}"


def first_text(parent, tag):
    element = parent.find(tag)
    return (element.text or "").strip() if element is not None else ""


def soap_response(operation_name, body_values, status_code=200):
    envelope = ET.Element(qname(SOAP_NS, "Envelope"))
    body = ET.SubElement(envelope, qname(SOAP_NS, "Body"))
    response_el = ET.SubElement(body, qname(SERVICE_NS, operation_name))

    for key, value in body_values.items():
        child = ET.SubElement(response_el, qname(SERVICE_NS, key))
        child.text = str(value)

    xml_body = ET.tostring(envelope, encoding="utf-8", xml_declaration=True)
    return Response(xml_body, status=status_code, mimetype="text/xml")


def soap_fault(message, status_code=400):
    envelope = ET.Element(qname(SOAP_NS, "Envelope"))
    body = ET.SubElement(envelope, qname(SOAP_NS, "Body"))
    fault = ET.SubElement(body, qname(SOAP_NS, "Fault"))

    fault_code = ET.SubElement(fault, "faultcode")
    fault_code.text = "soap:Client"
    fault_string = ET.SubElement(fault, "faultstring")
    fault_string.text = message

    xml_body = ET.tostring(envelope, encoding="utf-8", xml_declaration=True)
    return Response(xml_body, status=status_code, mimetype="text/xml")
