from django.db import models
from django.utils.translation import ugettext_lazy as _


class Osos(models.Model):

    class Meta:
        verbose_name = _('Osos')
        verbose_name_plural = _('OsosData')

    deviceId = models.CharField(
        _('deviceId'),
        max_length=100,
    )
    deviceDatetime = models.CharField(
        _('deviceDatetime'),
        max_length=30,
    )
    meterSerial = models.CharField(
        _('meterSerial'),
        max_length=30,
    )
    meterDate = models.CharField(
        _('meterDate'),
        max_length=30,
    )
    
    meterTime = models.CharField(
        _('meterTime'),
        max_length=30,
    )

    meterId = models.CharField(
        _('meterId'),
        max_length=30,
    )

    bpResetCnt = models.CharField(
        _('bpResetCnt'),
        max_length=30,
    )

    posActiveEnergy = models.CharField(
        _('posActiveEnergy'),
        max_length=30,
    )

    posActiveEnergyT1 = models.CharField(
        _('posActiveEnergyT1'),
        max_length=30,
    )

    posActiveEnergyT2 = models.CharField(
        _('posActiveEnergyT2'),
        max_length=30,
    )

    posActiveEnergyT3 = models.CharField(
        _('posActiveEnergyT3'),
        max_length=30,
    )

    posActiveEnergyT4 = models.CharField(
        _('posActiveEnergyT4'),
        max_length=30,
    )

    negActiveEnergy = models.CharField(
        _('negActiveEnergy'),
        max_length=30,
    )

    negActiveEnergyT1 = models.CharField(
        _('negActiveEnergyT1'),
        max_length=30,
    )

    negActiveEnergyT2 = models.CharField(
        _('negActiveEnergyT2'),
        max_length=30,
    )

    negActiveEnergyT3 = models.CharField(
        _('negActiveEnergyT3'),
        max_length=30,
    )

    negActiveEnergyT4 = models.CharField(
        _('negActiveEnergyT4'),
        max_length=30,
    )

    curP1 = models.CharField(
        _('curP1'),
        max_length=30,
    )

    voltP1 = models.CharField(
        _('voltP1'),
        max_length=30,
    )

    powFactorP1 = models.CharField(
        _('powFactorP1'),
        max_length=30,
    )

    curP2 = models.CharField(
        _('curP2'),
        max_length=30,
    )

    voltP2 = models.CharField(
        _('voltP2'),
        max_length=30,
    )

    powFactorP2 = models.CharField(
        _('powFactorP2'),
        max_length=30,
    )

    curP3 = models.CharField(
        _('curP3'),
        max_length=30,
    )

    voltP3 = models.CharField(
        _('voltP3'),
        max_length=30,
    )

    powFactorP3 = models.CharField(
        _('powFactorP3'),
        max_length=30,
    )

    importedInductiveReactiveEnergy = models.CharField(
        _('importedInductiveReactiveEnergy'),
        max_length=30,
    )

    exportedInductiveReactiveEnergy = models.CharField(
        _('exportedInductiveReactiveEnergy'),
        max_length=30,
    )

    def __str__(self):
        return self.deviceId
