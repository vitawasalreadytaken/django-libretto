# Python library imports.
#

# Django imports.
from django.db import models

# Project/app imports.
#


def extendManager(mixinClass):
	class MixinManager(models.Manager, mixinClass):
		class MixinQuerySet(models.query.QuerySet, mixinClass):
			pass
		def get_query_set(self):
			return self.MixinQuerySet(self.model, using = self._db)

	return MixinManager()
