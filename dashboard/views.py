from django.shortcuts import render
from django.views.generic import View


class DashboardView(View):

    template_name = 'dashboard/dashboard.html'

    def get(self, request,  *args, **kwargs):
        """get context"""


        return render(request, self.template_name)
