from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from proxmoxer import ProxmoxAPI
import json


@csrf_exempt
def nodes_list(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            proxmox = ProxmoxAPI(host=data["proxmox_ip"], user='root@pam', password=data["password"], verify_ssl=False)
            nodes = proxmox.nodes.get()
        except Exception as e:
            return JsonResponse(e.args, safe=False)
        else:
            return JsonResponse(nodes, safe=False)





