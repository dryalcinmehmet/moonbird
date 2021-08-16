from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)

from .models import (
    Osos
)

osos_index = Index('osos')

osos_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@osos_index.doc_type
class OsosDocument(Document):

    deviceId = fields.TextField(
        attr='deviceId',
        fields={
            'suggest': fields.Completion(),
        }
    )

    deviceDatetime = fields.TextField(
        attr='deviceDatetime',
        fields={
            'suggest': fields.Completion(),
        }
    )

    meterSerial = fields.TextField(
        attr='meterSerial',
        fields={
            'suggest': fields.Completion(),
        }
    )

    meterDate = fields.TextField(
        attr='meterDate',
        fields={
            'suggest': fields.Completion(),
        }
    )

    meterTime = fields.TextField(
        attr='meterTime',
        fields={
            'suggest': fields.Completion(),
        }
    )

    meterId = fields.TextField(
        attr='meterId',
        fields={
            'suggest': fields.Completion(),
        }
    )

    bpResetCnt = fields.TextField(
        attr='bpResetCnt',
        fields={
            'suggest': fields.Completion(),
        }
    )

    posActiveEnergy = fields.TextField(
        attr='posActiveEnergy',
        fields={
            'suggest': fields.Completion(),
        }
    )

    posActiveEnergyT1 = fields.TextField(
        attr='posActiveEnergyT1',
        fields={
            'suggest': fields.Completion(),
        }
    )

    posActiveEnergyT2 = fields.TextField(
        attr='posActiveEnergyT2',
        fields={
            'suggest': fields.Completion(),
        }
    )

    posActiveEnergyT3 = fields.TextField(
        attr='posActiveEnergyT3',
        fields={
            'suggest': fields.Completion(),
        }
    )

    posActiveEnergyT4 = fields.TextField(
        attr='posActiveEnergyT4',
        fields={
            'suggest': fields.Completion(),
        }
    )

    negActiveEnergy = fields.TextField(
        attr='negActiveEnergy',
        fields={
            'suggest': fields.Completion(),
        }
    )

    negActiveEnergyT1 = fields.TextField(
        attr='negActiveEnergyT1',
        fields={
            'suggest': fields.Completion(),
        }
    )

    negActiveEnergyT2 = fields.TextField(
        attr='negActiveEnergyT2',
        fields={
            'suggest': fields.Completion(),
        }
    )

    negActiveEnergyT3 = fields.TextField(
        attr='negActiveEnergyT3',
        fields={
            'suggest': fields.Completion(),
        }
    )

    negActiveEnergyT4 = fields.TextField(
        attr='negActiveEnergyT4',
        fields={
            'suggest': fields.Completion(),
        }
    )

    curP1 = fields.TextField(
        attr='curP1',
        fields={
            'suggest': fields.Completion(),
        }
    )

    voltP1 = fields.TextField(
        attr='voltP1',
        fields={
            'suggest': fields.Completion(),
        }
    )

    powFactorP1 = fields.TextField(
        attr='powFactorP1',
        fields={
            'suggest': fields.Completion(),
        }
    )

    curP2 = fields.TextField(
        attr='curP2',
        fields={
            'suggest': fields.Completion(),
        }
    )

    voltP2 = fields.TextField(
        attr='voltP2',
        fields={
            'suggest': fields.Completion(),
        }
    )

    powFactorP2 = fields.TextField(
        attr='powFactorP2',
        fields={
            'suggest': fields.Completion(),
        }
    )

    curP3 = fields.TextField(
        attr='curP3',
        fields={
            'suggest': fields.Completion(),
        }
    )

    voltP3 = fields.TextField(
        attr='voltP3',
        fields={
            'suggest': fields.Completion(),
        }
    )

    powFactorP3 = fields.TextField(
        attr='powFactorP3',
        fields={
            'suggest': fields.Completion(),
        }
    )

    importedInductiveReactiveEnergy = fields.TextField(
        attr='importedInductiveReactiveEnergy',
        fields={
            'suggest': fields.Completion(),
        }
    )

    exportedInductiveReactiveEnergy = fields.TextField(
        attr='exportedInductiveReactiveEnergy',
        fields={
            'suggest': fields.Completion(),
        }
    )

    def prepare_points(self, instance):
        if instance.color == 'silver':
            return 2
        return 1

    class Django:
        model = Osos

