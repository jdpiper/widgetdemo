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

from typing import Dict
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Widget


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User objects"""

    class Meta:
        model = User
        fields = [
            'id', 'url', 'username', 'email', 'first_name', 'last_name', 'groups'
        ]
        read_only_fields = ['id']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Group objects"""

    class Meta:
        model = Group
        fields = ['id', 'url', 'name']
        read_only_fields = ['id']


class WidgetSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Widget objects"""

    class Meta:
        model = Widget
        fields = ['id', 'name', 'num_parts', 'created', 'modified']
        read_only_fields = ['id', 'created', 'modified']

    def create(self, data: Dict):
        """Create and return an instance of the Widget object"""
        return Widget.objects.create(**data)

    def update(self, instance: Widget, data: Dict):
        """Update and return an existing instance of a Widget object"""
        instance.name = data.get('name', instance.name)
        instance.num_parts = data.get('num_parts', instance.num_parts)
        instance.save()
        return instance
