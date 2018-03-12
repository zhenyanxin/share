#-*-coding:utf-8-*-

from django.views.generic.base import View
from Things.models import Equipment


class EquipmentsListView(View):
    def get(self,request):
        '''

        :param request:
        :return:
        '''
        json_list=[]
        equipments=Equipment.objects.all()
        from django.forms.models import model_to_dict
        for equipment in equipments:
            json_dict = model_to_dict(equipment)
            json_list.append(json_dict)


        import json
        from django.core import serializers
        from django.http import HttpResponse,JsonResponse
        json_data=serializers.serialize("json",equipments)
        json_data=json.loads(json_data)
        return JsonResponse(json_data,safe=False)