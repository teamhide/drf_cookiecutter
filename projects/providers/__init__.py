from __future__ import absolute_import

import inject

from projects.providers.app_service_provider import AppServiceProvider


def create():
    inject.clear_and_configure(AppServiceProvider().inject)
