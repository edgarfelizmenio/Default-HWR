import config

from database import Base, db_session

Provider = Base.classes.Provider
ProviderAttribute = Base.classes.ProviderAttribute
ProviderAttributeType = Base.classes.ProviderAttributeType

def get_provider(provider_id):
    result = db_session.query(Provider).get(provider_id)
    if result is None:
        return None

    providerObject = {
        'provider_id': result.provider_id,
        'person_id': result.person_id,
        'name': result.name,
        'identifier': result.identifier,
    }
    attributes = []
    attr_result = db_session.query(ProviderAttribute,
                                   ProviderAttributeType).join(
                                       ProviderAttributeType
                                   ).filter(
                                       ProviderAttribute.provider_id == providerObject['provider_id']
                                       ).all()
    for provider_attribute, provider_attribute_type in attr_result:
        attributes.append({
            "value": provider_attribute.value_reference,
            "name": provider_attribute_type.name,
            "description": provider_attribute_type.description,
            "datatype": provider_attribute_type.datatype,
            "min_occurs": provider_attribute_type.min_occurs,
            "max_occurs": provider_attribute_type.max_occurs
        })
    providerObject['attributes'] = attributes
    return providerObject

def get_providers():
    providers = db_session.query(Provider).all()
    return [provider.provider_id for provider in providers]