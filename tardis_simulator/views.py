from django.shortcuts import render

from graphos.renderers import gchart
from graphos.sources.simple import SimpleDataSource

from .tardis import run_default


def home(request):
	return render(request, 'tardis_simulator/home.html')

def default_chart(request):
	g_chart = gchart.LineChart(SimpleDataSource(data=run_default()))		
	return render(request,'tardis_simulator/demo.html',{
			'chart': gchart
		})
