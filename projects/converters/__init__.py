class Converter:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Converter, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def _remove_id_from_entity(entity):
        if 'id' in entity:
            entity.pop('id')
        return entity

    @staticmethod
    def _remove_none_from_dict(obj) -> dict:
        return dict(filter(lambda x: x[1], obj.items()))

    def _model_to_entity(self, model, entity):
        model_dict = self._remove_id_from_entity(model._data)
        return entity(**model_dict)

    def _entity_to_model(self, entity, model):
        entity_dict = self._remove_none_from_dict(obj=entity.__dict__)
        return model(**entity_dict)
