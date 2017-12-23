from flask_restful import Resource

import models

class Provider(Resource):
    
    def get(self, provider_id):
        providerObject = models.get_provider(provider_id)
        if providerObject is None:
            return {'status': 404, 'message': 'Provider with id={} not found.'.format(provider_id)}
        return providerObject, 200

class Providers(Resource):

    def get(self):
        providers = models.get_providers()
        return providers, 200
