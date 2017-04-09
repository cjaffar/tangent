from django.conf.urls import url
from django.views.generic import TemplateView

from .views import LoginView, EmployeeView


urlpatterns = [
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^employee-form/$', EmployeeView.as_view(),name='employee-view'),
	url(r'^success/$', TemplateView.as_view(template_name='hr/success.html'),name='leave-success'),

	# url(r'^logout/$','django.contrib.auth.views.logout',name='logout'),
	# url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login'),
 #    url(r'^admin/', admin.site.urls),
]