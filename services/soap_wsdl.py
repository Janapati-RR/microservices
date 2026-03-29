from .soap_utils import SERVICE_NS, WSDL_NS


def build_wsdl(service_url):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions
    name="MicroservicesSoapService"
    targetNamespace="{WSDL_NS}"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:tns="{WSDL_NS}"
    xmlns:ser="{SERVICE_NS}">
  <wsdl:types>
    <xsd:schema targetNamespace="{SERVICE_NS}" elementFormDefault="qualified">
      <xsd:element name="SumRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="num1" type="xsd:double"/>
            <xsd:element name="num2" type="xsd:double"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="SumResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="result" type="xsd:double"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="RegisterRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="name" type="xsd:string"/>
            <xsd:element name="age" type="xsd:string"/>
            <xsd:element name="phone" type="xsd:string"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="RegisterResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="message" type="xsd:string"/>
            <xsd:element name="id" type="xsd:string"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="UploadRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="fileName" type="xsd:string"/>
            <xsd:element name="fileContent" type="xsd:base64Binary"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="UploadResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="message" type="xsd:string"/>
            <xsd:element name="document_name" type="xsd:string"/>
            <xsd:element name="document_url" type="xsd:string"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
    </xsd:schema>
  </wsdl:types>

  <wsdl:message name="SumInput"><wsdl:part name="parameters" element="ser:SumRequest"/></wsdl:message>
  <wsdl:message name="SumOutput"><wsdl:part name="parameters" element="ser:SumResponse"/></wsdl:message>
  <wsdl:message name="RegisterInput"><wsdl:part name="parameters" element="ser:RegisterRequest"/></wsdl:message>
  <wsdl:message name="RegisterOutput"><wsdl:part name="parameters" element="ser:RegisterResponse"/></wsdl:message>
  <wsdl:message name="UploadInput"><wsdl:part name="parameters" element="ser:UploadRequest"/></wsdl:message>
  <wsdl:message name="UploadOutput"><wsdl:part name="parameters" element="ser:UploadResponse"/></wsdl:message>

  <wsdl:portType name="MicroservicesSoapPortType">
    <wsdl:operation name="Sum">
      <wsdl:input message="tns:SumInput"/>
      <wsdl:output message="tns:SumOutput"/>
    </wsdl:operation>
    <wsdl:operation name="Register">
      <wsdl:input message="tns:RegisterInput"/>
      <wsdl:output message="tns:RegisterOutput"/>
    </wsdl:operation>
    <wsdl:operation name="Upload">
      <wsdl:input message="tns:UploadInput"/>
      <wsdl:output message="tns:UploadOutput"/>
    </wsdl:operation>
  </wsdl:portType>

  <wsdl:binding name="MicroservicesSoapBinding" type="tns:MicroservicesSoapPortType">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    <wsdl:operation name="Sum">
      <soap:operation soapAction="Sum"/>
      <wsdl:input><soap:body use="literal"/></wsdl:input>
      <wsdl:output><soap:body use="literal"/></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="Register">
      <soap:operation soapAction="Register"/>
      <wsdl:input><soap:body use="literal"/></wsdl:input>
      <wsdl:output><soap:body use="literal"/></wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="Upload">
      <soap:operation soapAction="Upload"/>
      <wsdl:input><soap:body use="literal"/></wsdl:input>
      <wsdl:output><soap:body use="literal"/></wsdl:output>
    </wsdl:operation>
  </wsdl:binding>

  <wsdl:service name="MicroservicesSoapService">
    <wsdl:port name="MicroservicesSoapPort" binding="tns:MicroservicesSoapBinding">
      <soap:address location="{service_url}"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
"""
