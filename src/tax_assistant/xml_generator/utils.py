from lxml import etree
from io import StringIO


def validate(xml: str, xsd: str, silent=True) -> bool:
    doc = etree.parse(StringIO(xml))
    schema_doc = etree.parse(StringIO(xsd))
    schema = etree.XMLSchema(schema_doc)
    if silent:
        return schema.validate(doc)
    else:
        return schema.assertValid(doc)
