
from django.conf.urls import url
from .views import LoginView, EmployeeView

urlpatterns = [
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^yeps/$', EmployeeView.as_view(),name='employee-view'),

	# url(r'^logout/$','django.contrib.auth.views.logout',name='logout'),
	# url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login'),
 #    url(r'^admin/', admin.site.urls),
]