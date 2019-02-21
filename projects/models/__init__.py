from mongoengine import *


class BaseDocument(Document):
    meta = {
        'abstract': True
    }

    # For type hinting
    @classmethod
    def query(cls, *args, **kwargs) -> QuerySet:
        return cls.objects(*args, **kwargs)

    def to_dict(self):
        """Convert MongoEngine Object to Dictionary"""
        return_data = []

        for field_name in self._fields:
            data = self._data[field_name]
            if isinstance(self._fields[field_name], DateTimeField):
                return_data.append((field_name, str(data.isoformat())))
            elif isinstance(self._fields[field_name], StringField):
                return_data.append((field_name, str(data)))
            elif isinstance(self._fields[field_name], FloatField):
                return_data.append((field_name, float(data)))
            elif isinstance(self._fields[field_name], IntField):
                return_data.append((field_name, int(data)))
            elif isinstance(self._fields[field_name], ListField):
                return_data.append((field_name, data))
            elif isinstance(self._fields[field_name], EmbeddedDocumentField):
                return_data.append((field_name, self.mongo_to_dict(data)))
            elif isinstance(self._fields[field_name], ObjectIdField):
                return_data.append((field_name, str(data)))
            elif isinstance(self._fields[field_name], BooleanField):
                return_data.append((field_name, bool(data)))
            elif isinstance(self._fields[field_name], SequenceField):
                return_data.append((field_name, int(data)))
            elif isinstance(self._fields[field_name], LongField):
                return_data.append((field_name, int(data)))
            else:
                type(self._fields[field_name])
        return_dict = dict(return_data)
        if 'id' in return_dict:
            return_dict.pop('id')

        return return_dict


class BaseEmbeddedDocument(EmbeddedDocument):
    meta = {
        'abstract': True
    }

    def to_dict(self):
        """Convert MongoEngine Object to Dictionary"""
        return_data = []

        for field_name in self._fields:
            data = self._data[field_name]
            if isinstance(self._fields[field_name], DateTimeField):
                return_data.append((field_name, str(data.isoformat())))
            elif isinstance(self._fields[field_name], StringField):
                return_data.append((field_name, str(data)))
            elif isinstance(self._fields[field_name], FloatField):
                return_data.append((field_name, float(data)))
            elif isinstance(self._fields[field_name], IntField):
                return_data.append((field_name, int(data)))
            elif isinstance(self._fields[field_name], ListField):
                return_data.append((field_name, data))
            elif isinstance(self._fields[field_name], EmbeddedDocumentField):
                return_data.append((field_name, self.mongo_to_dict(data)))
            elif isinstance(self._fields[field_name], ObjectIdField):
                return_data.append((field_name, str(data)))
            elif isinstance(self._fields[field_name], BooleanField):
                return_data.append((field_name, bool(data)))
            elif isinstance(self._fields[field_name], SequenceField):
                return_data.append((field_name, int(data)))
            elif isinstance(self._fields[field_name], LongField):
                return_data.append((field_name, int(data)))
            else:
                type(self._fields[field_name])
        return_dict = dict(return_data)
        if 'id' in return_dict:
            return_dict.pop('id')

        return return_dict
