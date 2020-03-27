from django.http import HttpResponse
from django.conf.urls import url
from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks
from wagtail.core.models import UserPagePermissionsProxy
from .views import LatestChangesView

@hooks.register('register_admin_urls')
def urlconf_time():
    return [
      url(r'^latest_changes/$', LatestChangesView.as_view(), name='latest_changes'),
    ]


class LatestChangesPagesMenuItem(MenuItem):
    def is_shown(self, request):
        return UserPagePermissionsProxy(request.user).can_remove_locks()


@hooks.register("register_reports_menu_item")
def register_latest_changes_menu_item():
    return LatestChangesPagesMenuItem(
        "Latest changes", reverse("latest_changes"), classnames="icon icon-date", order=100,
    )
