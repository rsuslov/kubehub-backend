from django.db import models
from subprocess import check_output

from ..models.vm_group import VMGroup


class KubernetesCluster(models.Model):
    name_max = int(check_output("getconf NAME_MAX /", shell=True))
    name = models.CharField(max_length=name_max)
    k8s_version = models.CharField(max_length=name_max)
    vm_group = models.OneToOneField(
        VMGroup,
        on_delete=models.CASCADE
    )

    readonly_fields = 'k8s_version'

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, k8s_version: {self.k8s_version}, ' \
               f'vm_group: {self.vm_group}'

