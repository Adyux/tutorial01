import pytest

from mixer.backend.django import mixer
from ..models import Podcast

pytestmark = pytest.mark.django_db

class TestModels(object):

    def test_podcast_model(self, **kwargs):
        test_model = mixer.blend(Podcast, host=None, name='test')
        assert Podcast.objects.filter(id=test_model.id).count() == 1
