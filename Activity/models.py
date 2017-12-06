from __future__ import unicode_literals

from django.db import models


class StandaloneTestBedSetup(models.Model):
    engineer = models.CharField(max_length=10)
    release = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    cimc_ip = models.CharField(max_length=50)
    server_type = models.CharField(max_length=50)
    cimc_bios_version = models.CharField(max_length=90)
    firmware_upgrade_prs = models.CharField(max_length=250)
    adapter_name = models.CharField(max_length=999)
    adapter_slot = models.CharField(max_length=70)
    adapter_fw = models.CharField(max_length=50)
    target_type = models.CharField(max_length=99)
    bios_bootcode = models.CharField(max_length=50)
    effort = models.CharField(max_length=10)

    def __str__(self):
        return self.engineer + '_' + self.cimc_ip


class StandaloneTestBedSetupFinal(models.Model):
    event = models.DateTimeField(auto_now_add=True, editable=True)
    engineer = models.CharField(max_length=10)
    release = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    cimc_ip = models.CharField(max_length=50)
    server_type = models.CharField(max_length=50)
    cimc_bios_version = models.CharField(max_length=90)
    firmware_upgrade_prs = models.CharField(max_length=250)
    adapter_name = models.CharField(max_length=999)
    adapter_slot = models.CharField(max_length=70)
    adapter_fw = models.CharField(max_length=50)
    target_type = models.CharField(max_length=99)
    bios_bootcode = models.CharField(max_length=50)
    effort = models.CharField(max_length=10)

    def __str__(self):
        return self.engineer + '_' + self.cimc_ip


class UcsmTestBedSetup(models.Model):
    engineer = models.CharField(max_length=10)
    release = models.CharField(max_length=50)
    fi_ip = models.CharField(max_length=50)
    fi_firmware = models.CharField(max_length=50)
    server_type = models.CharField(max_length=50)
    server_number = models.CharField(max_length=10)
    cimc_version = models.CharField(max_length=50)
    cimc_bios_version = models.CharField(max_length=50)
    discovery_methods = models.CharField(max_length=250)
    adapter_name = models.CharField(max_length=20)
    adapter_slot = models.CharField(max_length=10)
    adapter_fw = models.CharField(max_length=50)
    target_type = models.CharField(max_length=10)
    bios_bootcode = models.CharField(max_length=50)
    effort = models.CharField(max_length=10, default='N')

    def __str__(self):
        return self.engineer + '_' + self.fi_ip + '_server-' + self.server_number


class UcsmTestBedSetupFinal(models.Model):
    event = models.DateTimeField(auto_now_add=True, editable=True)
    # event = models.DateTimeField(editable=False)
    engineer = models.CharField(max_length=10)
    release = models.CharField(max_length=50)
    fi_ip = models.CharField(max_length=50)
    fi_firmware = models.CharField(max_length=50)
    server_type = models.CharField(max_length=50)
    server_number = models.CharField(max_length=10)
    cimc_version = models.CharField(max_length=50)
    cimc_bios_version = models.CharField(max_length=80)
    discovery_methods = models.CharField(max_length=250)
    adapter_name = models.CharField(max_length=999)
    adapter_slot = models.CharField(max_length=10)
    adapter_fw = models.CharField(max_length=50)
    target_type = models.CharField(max_length=99)
    bios_bootcode = models.CharField(max_length=50)
    effort = models.CharField(max_length=10, default='N', blank=True)

    def __str__(self):
        return self.engineer + '_' + self.fi_ip + '_server-' + self.server_number


class TestExecution(models.Model):
    event = models.DateTimeField(auto_now_add=True, editable=True)
    testbed_stand = models.ForeignKey(StandaloneTestBedSetupFinal, null=True, blank=True)
    testbed_ucsm = models.ForeignKey(UcsmTestBedSetupFinal, null=True, blank=True)
    setup = models.CharField(max_length=100)
    os = models.CharField(max_length=50, default='NA')
    os_bootM = models.CharField(max_length=20)
    os_bootT = models.CharField(max_length=20)
    config = models.CharField(max_length=200)
    pxe_adap = models.CharField(max_length=20)
    cdets = models.CharField(max_length=20)
    auto_logs = models.CharField(max_length=100)
    auto_usage = models.CharField(max_length=10)
    driver_version = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    comments = models.CharField(max_length=500)
    effort = models.CharField(max_length=10)

    def __str__(self):
        return self.setup


class Troubleshooting(models.Model):
    setup = models.CharField(max_length=50)
    comments = models.CharField(max_length=1000)
    testbed_stand = models.ForeignKey(StandaloneTestBedSetupFinal, null=True)
    testbed_ucsm = models.ForeignKey(UcsmTestBedSetupFinal, null=True)


class UcsmAddAcivity(models.Model):
    engineer = models.CharField(max_length=500)
    server = models.CharField(max_length=200)
    Config = models.CharField(max_length=999)
    fiDetails = models.CharField(max_length=50)
    fiFirmware = models.CharField(max_length=50)
    ucsmBuild = models.CharField(max_length=50)
    cimc = models.CharField(max_length=50)
    bios = models.CharField(max_length=50)
    adapters = models.CharField(max_length=500)
    slot = models.CharField(max_length=50)
    adapterFirmware = models.CharField(max_length=250)
    boot = models.CharField(max_length=50)
    adapterBios = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    driver = models.CharField(max_length=999)
    automationUsage = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    bigzillaId = models.CharField(max_length=200)
    link = models.CharField(max_length=2000)
    remarks = models.CharField(max_length=2000)

    def __str__(self):
        return self.server + '-' + self.os
