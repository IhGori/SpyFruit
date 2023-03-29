from django.db import models

import uuid
from django.utils import timezone
import json
from datetime import datetime


class TemperatureData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)

    # Converte a string JSON em um dicionário usando 'json.loads' e então percorre os feeds retornados pelo things, criando objetos TemperatureData
    @classmethod
    def save_from_json(cls, json_data):
        data = json.loads(json_data)
        for feed in data['feeds']:
            obj = cls(
                timestamp=feed['created_at'],
                temperature=feed['field1']
            )
            obj.save()
