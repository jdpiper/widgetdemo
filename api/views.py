#  Copyright 2021 Justin Piper
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from api.serializers import UserSerializer, GroupSerializer, WidgetSerializer
from api.models import Widget


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for User objects"""

    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint for Group objects"""

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class WidgetViewSet(viewsets.ModelViewSet):
    """API endpoint for Widget objects"""

    queryset = Widget.objects.all().order_by('name')
    serializer_class = WidgetSerializer
    permission_classes = [permissions.IsAuthenticated]
