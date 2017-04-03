
from django.conf.urls import url
from .views import LoginView

urlpatterns = [
	url(r'^login/$', LoginView.as_view(), name='login'),
	# url(r'^login/$', 'django.contrib.auth.views.login',name='login'),

	# url(r'^logout/$','django.contrib.auth.views.logout',name='logout'),
	# url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login'),
 #    url(r'^admin/', admin.site.urls),
]